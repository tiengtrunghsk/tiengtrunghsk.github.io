# -*- coding: utf-8 -*-
"""
Module tích hợp Kokoro TTS (AI) vào web.
- Chạy 100% trên trình duyệt (không cần server).
- Tự động lưu model vào Cache của trình duyệt (chỉ tải 1 lần).
- Hỗ trợ giọng Nam tiếng Trung chất lượng cao.
"""

def build_kokoro_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KOKORO TTS UI                                               */
/* ═══════════════════════════════════════════════════════════ */
.kk-download-btn {
    display: flex; align-items: center; justify-content: center; gap: 8px;
    width: 100%; padding: 12px; margin-top: 10px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff; font-weight: 700; font-size: 0.9rem;
    border: none; border-radius: 12px; cursor: pointer;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.3);
    transition: all 0.2s;
}
.kk-download-btn:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(124, 58, 237, 0.5); }
.kk-download-btn:disabled { opacity: 0.7; cursor: not-allowed; }

.kk-progress-wrap {
    display: none; flex-direction: column; gap: 6px;
    width: 100%; margin-top: 8px; padding: 10px;
    background: var(--surface-2, #f1f5f9); border-radius: 10px;
}
.kk-progress-wrap.show { display: flex; }
.kk-progress-text { font-size: 0.75rem; font-weight: 600; color: var(--text-2, #475569); text-align: center; }
.kk-progress-bg { width: 100%; height: 8px; background: var(--border, #e2e8f0); border-radius: 50px; overflow: hidden; }
.kk-progress-bar { height: 100%; width: 0%; background: linear-gradient(90deg, #4f46e5, #ec4899); transition: width 0.3s; }

.kk-voice-select-wrap {
    display: none; flex-direction: column; gap: 6px; margin-top: 10px;
}
.kk-voice-select-wrap.show { display: flex; }
.kk-voice-select {
    padding: 8px 12px; border-radius: 10px; border: 1.5px solid var(--border, #e2e8f0);
    background: var(--surface, #fff); color: var(--text, #1e293b);
    font-size: 0.85rem; font-family: inherit; outline: none; cursor: pointer;
}
"""

def build_kokoro_html():
    return r"""
<!-- KOKORO TTS SETTINGS (Chèn vào trong modal voice-body) -->
<div class="voice-group" style="border-top: 1px dashed var(--border); padding-top: 1rem; margin-top: 0.5rem;">
    <div class="voice-group-label">
        <span><i class="fas fa-robot"></i> Giọng AI (Kokoro)</span>
        <span class="voice-value" id="kkStatusBadge" style="background:#f1f5f9; color:#64748b; font-size:0.65rem;">Chưa tải</span>
    </div>
    
    <button class="kk-download-btn" id="kkDownloadBtn" type="button">
        <i class="fas fa-cloud-download-alt"></i> Tải giọng AI chất lượng cao (~90MB)
    </button>
    
    <div class="kk-progress-wrap" id="kkProgressWrap">
        <div class="kk-progress-text" id="kkProgressText">Đang kết nối...</div>
        <div class="kk-progress-bg"><div class="kk-progress-bar" id="kkProgressBar"></div></div>
    </div>

    <div class="kk-voice-select-wrap" id="kkVoiceSelectWrap">
        <select class="kk-voice-select" id="kkVoiceSelect">
            <option value="zm_yunxi">Nam - Vân Hy (Ấm áp)</option>
            <option value="zm_yunjian">Nam - Vân Kiện (Trầm)</option>
            <option value="zm_yunyang">Nam - Vân Dương (Trẻ)</option>
            <option value="zf_xiaoxiao">Nữ - Tiểu Tiểu (Trong trẻo)</option>
            <option value="zf_xiaoyi">Nữ - Tiểu Nghệ (Dịu dàng)</option>
        </select>
    </div>
</div>
"""

def build_kokoro_js():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KOKORO TTS MODULE (Chạy 100% Client-side)                   */
/* ═══════════════════════════════════════════════════════════ */
(function() {
    'use strict';
    
    var kkModel = null;
    var isDownloading = false;
    var KK_CACHE_KEY = 'kokoro_model_loaded';

    // 1. Tự động kiểm tra xem đã tải model chưa (lưu trong localStorage)
    function checkKokoroStatus() {
        var badge = document.getElementById('kkStatusBadge');
        var btn = document.getElementById('kkDownloadBtn');
        var voiceWrap = document.getElementById('kkVoiceSelectWrap');
        
        if (!badge || !btn) return;

        if (localStorage.getItem(KK_CACHE_KEY) === 'true') {
            badge.textContent = 'Đã tải';
            badge.style.background = '#dcfce7';
            badge.style.color = '#16a34a';
            btn.style.display = 'none';
            voiceWrap.classList.add('show');
        }
    }

    // 2. Hàm tải thư viện Kokoro-JS từ CDN
    function loadKokoroLibrary() {
        return new Promise(function(resolve, reject) {
            if (window.KokoroTTS) return resolve();
            
            var script = document.createElement('script');
            script.type = 'module';
            script.innerHTML = `
                import { KokoroTTS } from 'https://cdn.jsdelivr.net/npm/kokoro-js@1.2.0/+esm';
                window.KokoroTTS = KokoroTTS;
                window.dispatchEvent(new Event('kokoroLoaded'));
            `;
            document.head.appendChild(script);
            
            window.addEventListener('kokoroLoaded', resolve, { once: true });
            
            // Timeout phòng trường hợp mạng lỗi
            setTimeout(function() {
                if (!window.KokoroTTS) reject(new Error('Timeout tải thư viện Kokoro'));
            }, 30000);
        });
    }

    // 3. Hàm khởi tạo Model (Tải 1 lần, sau đó trình duyệt tự cache)
    async function initKokoro() {
        if (kkModel) return kkModel;
        if (isDownloading) return null;
        
        isDownloading = true;
        var progressWrap = document.getElementById('kkProgressWrap');
        var progressText = document.getElementById('kkProgressText');
        var progressBar = document.getElementById('kkProgressBar');
        
        progressWrap.classList.add('show');
        progressText.textContent = 'Đang tải thư viện AI...';

        try {
            await loadKokoroLibrary();
            
            progressText.textContent = 'Đang tải Model (khoảng 90MB)...';
            progressBar.style.width = '20%';

            // ⭐ Tải model Q8 (~90MB) để nhẹ nhất
            kkModel = await window.KokoroTTS.from_pretrained("onnx-community/Kokoro-82M-v1.0-ONNX", {
                dtype: "q8",
                device: "wasm", // Hoặc "webgpu" nếu muốn nhanh hơn
                progress_callback: function(progress) {
                    if (progress.status === 'progress' && progress.total) {
                        var pct = Math.round((progress.loaded / progress.total) * 100);
                        progressBar.style.width = pct + '%';
                        progressText.textContent = 'Đang tải Model: ' + pct + '%';
                    }
                }
            });

            progressBar.style.width = '100%';
            progressText.textContent = 'Hoàn tất!';
            
            // Lưu trạng thái vào localStorage
            localStorage.setItem(KK_CACHE_KEY, 'true');
            
            setTimeout(function() {
                progressWrap.classList.remove('show');
                checkKokoroStatus();
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('✅ Đã tải xong giọng AI!', 'success');
                }
            }, 800);

            return kkModel;
        } catch (e) {
            console.error("Lỗi tải Kokoro:", e);
            progressText.textContent = '❌ Lỗi tải. Vui lòng thử lại.';
            progressBar.style.background = '#ef4444';
            isDownloading = false;
            return null;
        }
    }

    // 4. Ghi đè hàm speakText hiện tại của bạn
    // 4. Ghi đè hàm speakText hiện tại của bạn
    function overrideSpeakText() {
        // Lưu lại hàm gốc
        if (!window.__originalSpeakText) {
            window.__originalSpeakText = window.speakText;
        }
        
        // Tạo hàm mới
        window.speakText = async function(text, btn, evt) {
            if (evt) evt.stopPropagation();
            
            // Nếu chưa tải Model, dùng giọng mặc định
            if (!kkModel || localStorage.getItem(KK_CACHE_KEY) !== 'true') {
                if (typeof window.__originalSpeakText === 'function') {
                    return window.__originalSpeakText.call(this, text, btn, evt);
                }
                return;
            }

            // Nếu đã có Model, dùng Kokoro
            if (btn) btn.classList.add('speaking');
            
            try {
                // ⭐ LẤY GIỌNG TỪ DROPDOWN ĐÃ CHỌN
                var voiceSelect = document.getElementById('kkVoiceSelect');
                var selectedVoice = voiceSelect ? voiceSelect.value : 'zm_yunxi'; 
                // Nếu value rỗng thì mặc định là Vân Hy
                if (!selectedVoice) selectedVoice = 'zm_yunxi';

                console.log("[Kokoro] Đang đọc với giọng:", selectedVoice);

                var audio = await kkModel.generate(text, { 
                    voice: selectedVoice,
                    speed: (typeof voiceState !== 'undefined' && voiceState.rate) ? voiceState.rate : 1.0
                });
                
                var blob = audio.toBlob();
                var url = URL.createObjectURL(blob);
                var audioEl = new Audio(url);
                
                audioEl.onended = function() {
                    if (btn) btn.classList.remove('speaking');
                    URL.revokeObjectURL(url);
                };
                
                await audioEl.play();
            } catch (e) {
                console.error("Lỗi Kokoro generate:", e);
                if (btn) btn.classList.remove('speaking');
                // Fallback
                if (typeof window.__originalSpeakText === 'function') {
                    return window.__originalSpeakText.call(this, text, btn, evt);
                }
            }
        };
    }

    // ⭐ Thêm hàm bảo vệ để chống bị module khác ghi đè
    setInterval(function() {
        if (localStorage.getItem(KK_CACHE_KEY) === 'true' && kkModel) {
            // Nếu phát hiện hàm speakText đã bị module khác đổi mất
            if (!window.speakText.__isKokoro) {
                overrideSpeakText();
                window.speakText.__isKokoro = true; // Đánh dấu
            }
        }
    }, 2000);
    // 5. Khởi tạo các sự kiện
    function initEvents() {
        checkKokoroStatus();
        overrideSpeakText();

        var btn = document.getElementById('kkDownloadBtn');
        if (btn && !btn.__bound) {
            btn.__bound = true;
            btn.addEventListener('click', function() {
                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Đang tải...';
                initKokoro().then(function() {
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-check"></i> Đã tải xong';
                });
            });
        }
    }

    // Chạy khi DOM sẵn sàng
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initEvents);
    } else {
        setTimeout(initEvents, 1000); // Đợi các module khác load xong
    }
})();
"""
