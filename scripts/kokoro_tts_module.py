# -*- coding: utf-8 -*-
"""
Module tích hợp Kokoro TTS (AI) vào web - Bản Test với file âm thanh cụ thể.
- Giọng Nam: zm_009
- Giọng Nữ: zf_008
"""

def build_kokoro_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KOKORO TTS UI - BẢN TIẾNG TRUNG                             */
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
        <span><i class="fas fa-robot"></i> Giọng AI (Kokoro - Tiếng Trung)</span>
        <span class="voice-value" id="kkStatusBadge" style="background:#f1f5f9; color:#64748b; font-size:0.65rem;">Chưa tải</span>
    </div>
    
    <button class="kk-download-btn" id="kkDownloadBtn" type="button">
        <i class="fas fa-cloud-download-alt"></i> Tải giọng AI chất lượng cao (~127MB)
    </button>
    
    <div class="kk-progress-wrap" id="kkProgressWrap">
        <div class="kk-progress-text" id="kkProgressText">Đang kết nối...</div>
        <div class="kk-progress-bg"><div class="kk-progress-bar" id="kkProgressBar"></div></div>
    </div>

    <div class="kk-voice-select-wrap" id="kkVoiceSelectWrap">
        <select class="kk-voice-select" id="kkVoiceSelect">
            <option value="zm_009">Nam - Giọng 009</option>
            <option value="zf_008">Nữ - Giọng 008</option>
        </select>
    </div>
</div>
"""

def build_kokoro_js():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KOKORO TTS MODULE - TEST FILE zm_009 & zf_008               */
/* ═══════════════════════════════════════════════════════════ */
(function() {
    'use strict';
    
    var kkModel = null;
    var isDownloading = false;
    var KK_CACHE_KEY = 'kokoro_zh_model_loaded_v2'; // Đổi key để xóa cache cũ

    function checkKokoroStatus() {
        var badge = document.getElementById('kkStatusBadge');
        var btn = document.getElementById('kkDownloadBtn');
        var voiceWrap = document.getElementById('kkVoiceSelectWrap');
        
        if (!badge || !btn) return;

        if (localStorage.getItem(KK_CACHE_KEY) === 'true') {
            badge.textContent = 'Đã tải';
            badge.style.background = '#dcfce7';
            badge.style.color = '#16a34a';
            if(btn) btn.style.display = 'none';
            if(voiceWrap) voiceWrap.classList.add('show');
        }
    }

    function loadKokoroLibrary() {
        return new Promise(function(resolve, reject) {
            if (window.KokoroTTS) return resolve();
            
            var script = document.createElement('script');
            script.type = 'module';
            script.innerHTML = `
                import { KokoroTTS } from 'https://cdn.jsdelivr.net/npm/@uzen/kokoro-js@1.2.4/+esm';
                window.KokoroTTS = KokoroTTS;
                window.dispatchEvent(new Event('kokoroLoaded'));
            `;
            document.head.appendChild(script);
            
            window.addEventListener('kokoroLoaded', resolve, { once: true });
            
            setTimeout(function() {
                if (!window.KokoroTTS) reject(new Error('Timeout tải thư viện Kokoro (30s)'));
            }, 30000);
        });
    }

    async function initKokoro() {
        if (kkModel) return kkModel;
        if (isDownloading) return null;
        
        isDownloading = true;
        var progressWrap = document.getElementById('kkProgressWrap');
        var progressText = document.getElementById('kkProgressText');
        var progressBar = document.getElementById('kkProgressBar');
        
        if(progressWrap) progressWrap.classList.add('show');
        if(progressText) progressText.textContent = 'Đang tải thư viện AI...';

        try {
            await loadKokoroLibrary();
            
            if(progressText) progressText.textContent = 'Đang tải Model tiếng Trung (~127MB)...';
            if(progressBar) progressBar.style.width = '20%';

            kkModel = await window.KokoroTTS.from_pretrained("onnx-community/Kokoro-82M-v1.1-zh-ONNX", {
                dtype: "q8",
                device: "wasm",
                voicePath: "/kokoro/voices", // Thư mục chứa zm_009.bin và zf_008.bin
                progress_callback: function(progress) {
                    if (progress.status === 'progress' && progress.total) {
                        var pct = Math.round((progress.loaded / progress.total) * 100);
                        if(progressBar) progressBar.style.width = pct + '%';
                        if(progressText) progressText.textContent = 'Đang tải Model: ' + pct + '%';
                    }
                }
            });

            if(progressBar) progressBar.style.width = '100%';
            if(progressText) progressText.textContent = 'Hoàn tất!';
            
            localStorage.setItem(KK_CACHE_KEY, 'true');
            
            setTimeout(function() {
                if(progressWrap) progressWrap.classList.remove('show');
                checkKokoroStatus();
                alert("✅ Đã tải xong giọng AI! Hãy thử bấm nút loa.");
            }, 800);

            return kkModel;
        } catch (e) {
            console.error("Lỗi tải Kokoro:", e);
            alert("❌ Lỗi tải AI: " + e.message);
            if(progressText) progressText.textContent = '❌ Lỗi tải. Vui lòng thử lại.';
            if(progressBar) progressBar.style.background = '#ef4444';
            isDownloading = false;
            return null;
        }
    }

    function overrideSpeakText() {
        if (!window.__originalSpeakText) {
            window.__originalSpeakText = window.speakText;
        }
        
        window.speakText = async function(text, btn, evt) {
            if (evt && evt.stopPropagation) evt.stopPropagation();
            
            if (!kkModel || localStorage.getItem(KK_CACHE_KEY) !== 'true') {
                console.log("[Kokoro] Chưa tải model, dùng giọng mặc định.");
                if (typeof window.__originalSpeakText === 'function') {
                    return window.__originalSpeakText.call(this, text, btn, evt);
                }
                return;
            }

            console.log("[Kokoro] Đang xử lý:", text);
            if (btn) btn.classList.add('speaking');
            
            try {
                var voiceSelect = document.getElementById('kkVoiceSelect');
                // Lấy giọng từ dropdown (zm_009 hoặc zf_008)
                var selectedVoice = voiceSelect ? voiceSelect.value : 'zm_009'; 
                if (!selectedVoice) selectedVoice = 'zm_009';

                console.log("[Kokoro] Giọng chọn:", selectedVoice);

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
                console.log("[Kokoro] Đã phát xong.");
            } catch (e) {
                console.error("[Kokoro] Lỗi:", e);
                alert("Lỗi khi đọc AI: " + e.message);
                if (btn) btn.classList.remove('speaking');
                if (typeof window.__originalSpeakText === 'function') {
                    return window.__originalSpeakText.call(this, text, btn, evt);
                }
            }
        };
        window.speakText.__isKokoro = true;
    }

    function initEvents() {
        checkKokoroStatus();
        
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
        
        if (localStorage.getItem(KK_CACHE_KEY) === 'true' && !kkModel && !isDownloading) {
            console.log("[Kokoro] Tự động khôi phục model từ cache...");
            initKokoro();
        }
    }

    setInterval(function() {
        if (localStorage.getItem(KK_CACHE_KEY) === 'true') {
            if (!window.speakText || !window.speakText.__isKokoro) {
                overrideSpeakText();
            }
        } else {
            if (!window.speakText || !window.speakText.__isKokoro) {
                overrideSpeakText();
            }
        }
    }, 1000);

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initEvents);
    } else {
        setTimeout(initEvents, 1000);
    }
})();
"""
