# -*- coding: utf-8 -*-
"""
ASSEMBLE MODULE — Chế độ "Ghép từ" cho Practice Full.
Module độc lập, không đụng vào mã gốc.

Cách dùng trong convert.py:
    from assemble_module import (
        build_assemble_css,
        build_assemble_html,
        build_assemble_js,
        inject_assemble_html,
    )

    full_css += "\n/* ASSEMBLE */\n" + build_assemble_css()
    ui_html = inject_assemble_html(ui_html)   # sau patch_html()
    full_js += "\n/* ASSEMBLE */\n" + build_assemble_js()
"""

import re


# ═══════════════════════════════════════════════════════════════
# CSS
# ═══════════════════════════════════════════════════════════════
def build_assemble_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* GHÉP TỪ (Word Assembly) — chế độ luyện dịch nâng cao        */
/* ═══════════════════════════════════════════════════════════ */
.pf-assemble-mode {
    display: none;
    flex-direction: column;
    gap: clamp(.5rem, 1vh, .8rem);
    margin-top: .25rem;
}
body.pf-assemble-active .pf-assemble-mode {
    display: flex;
}

/* Ô "Câu trả lời" — các từ đã chọn */
.pf-assemble-answer {
    min-height: clamp(56px, 8vh, 72px);
    padding: clamp(.5rem, 1vh, .75rem) clamp(.6rem, 1.2vw, .9rem);
    background: linear-gradient(135deg,
        rgba(99,102,241,.06),
        rgba(139,92,246,.04));
    border: 2px dashed rgba(139,92,246,.35);
    border-radius: 14px;
    display: flex;
    flex-wrap: wrap;
    gap: clamp(.3rem, .6vw, .5rem);
    align-items: center;
    justify-content: center;
    transition: border-color .2s, background .2s;
    position: relative;
}
[data-theme="dark"] .pf-assemble-answer {
    background: linear-gradient(135deg,
        rgba(99,102,241,.12),
        rgba(139,92,246,.08));
    border-color: rgba(165,180,252,.4);
}
.pf-assemble-answer.correct {
    border-color: var(--success);
    border-style: solid;
    background: linear-gradient(135deg,
        rgba(22,163,74,.1),
        rgba(34,197,94,.06));
    animation: pfAssembleCorrect .5s ease;
}
.pf-assemble-answer.wrong {
    border-color: var(--danger);
    animation: pfAssembleWrong .4s ease;
}
@keyframes pfAssembleCorrect {
    0%   { transform: scale(1); }
    40%  { transform: scale(1.03); box-shadow: 0 0 0 8px rgba(34,197,94,.15); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(34,197,94,0); }
}
@keyframes pfAssembleWrong {
    0%,100% { transform: translateX(0); }
    25%     { transform: translateX(-5px); }
    75%     { transform: translateX(5px); }
}

.pf-assemble-hint {
    color: var(--text-3);
    font-size: clamp(.78rem, .95vw, .88rem);
    font-style: italic;
    user-select: none;
    pointer-events: none;
}

/* Ô "Từ gợi ý" — các từ chưa chọn (bị xáo trộn) */
.pf-assemble-pool {
    min-height: clamp(56px, 8vh, 72px);
    padding: clamp(.5rem, 1vh, .75rem) clamp(.6rem, 1.2vw, .9rem);
    background: var(--surface-2);
    border: 1.5px solid var(--border);
    border-radius: 14px;
    display: flex;
    flex-wrap: wrap;
    gap: clamp(.3rem, .6vw, .5rem);
    align-items: center;
    justify-content: center;
}

/* Nút từ — dùng chung cho cả 2 ô */
.pf-word {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: clamp(1.1rem, 2vw, 1.35rem);
    font-weight: 500;
    padding: clamp(.35rem, .7vh, .5rem) clamp(.7rem, 1.2vw, 1rem);
    border-radius: 10px;
    border: 2px solid var(--border);
    background: var(--surface);
    color: var(--text);
    cursor: pointer;
    transition: transform .15s cubic-bezier(.34,1.56,.64,1),
                background .2s, border-color .2s, box-shadow .2s, opacity .2s;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    line-height: 1.4;
    letter-spacing: .02em;
    box-shadow: 0 2px 6px rgba(15,23,42,.06);
    position: relative;
}
.pf-word:hover {
    transform: translateY(-2px) scale(1.04);
    border-color: var(--primary);
    box-shadow: 0 6px 16px rgba(37,99,235,.25);
}
.pf-word:active {
    transform: scale(.96);
}
.pf-word.used {
    opacity: .25;
    pointer-events: none;
    transform: scale(.92);
}

/* Nút từ ở ô đáp án — màu khác để phân biệt */
.pf-assemble-answer .pf-word {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 12px rgba(99,102,241,.35);
}
.pf-assemble-answer .pf-word:hover {
    box-shadow: 0 6px 18px rgba(99,102,241,.5);
    border-color: transparent;
}

/* Nút hành động */
.pf-assemble-actions {
    display: flex;
    gap: clamp(.4rem, .8vw, .6rem);
    justify-content: center;
    flex-wrap: wrap;
}
.pf-assemble-btn {
    padding: clamp(.4rem, .8vh, .55rem) clamp(.7rem, 1.3vw, .95rem);
    border-radius: 50px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text-2);
    font-size: clamp(.72rem, .85vw, .82rem);
    font-weight: 700;
    cursor: pointer;
    font-family: inherit;
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    transition: .18s;
}
.pf-assemble-btn:hover {
    border-color: var(--primary);
    color: var(--primary);
    background: var(--primary-light);
    transform: translateY(-1px);
}
.pf-assemble-btn.primary {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 12px rgba(124,58,237,.35);
}
.pf-assemble-btn.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(124,58,237,.5);
}

/* Nút toggle trong mini-group */
.pf-nav-icon.mini-nav.assemble-toggle {
    background: var(--surface);
    color: var(--text-2);
    border-color: var(--border);
}
.pf-nav-icon.mini-nav.assemble-toggle:hover:not(:disabled) {
    border-color: #6366f1;
    color: #4f46e5;
    background: rgba(99,102,241,.1);
}
.pf-nav-icon.mini-nav.assemble-toggle.active {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 12px rgba(99,102,241,.5);
    opacity: 1;
}
[data-theme="dark"] .pf-nav-icon.mini-nav.assemble-toggle {
    background: var(--surface-2);
    color: var(--text-2);
    border-color: var(--border);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.assemble-toggle.active {
    background: linear-gradient(135deg, #818cf8, #a78bfa);
    color: #1e1b4b;
}

/* Khi bật chế độ ghép từ → ẩn textarea + char-preview */
body.pf-assemble-active #pfInputMode { display: none !important; }
body.pf-assemble-active #pfPreview { display: none !important; }
body.pf-assemble-active .practice-full-input { display: none !important; }

/* ⭐ Khi bật chế độ ghép từ → ẩn "Chấm điểm" + "Xem đáp án" */
body.pf-assemble-active #pfHintBtn,
body.pf-assemble-active #pfRevealBtn,
body.pf-assemble-active .reveal-actions {
    display: none !important;
}

@media (max-width: 500px) {
    .pf-word {
        padding: .35rem .7rem;
        font-size: 1.05rem;
        border-radius: 9px;
    }
    .pf-assemble-answer,
    .pf-assemble-pool {
        min-height: 54px;
        padding: .5rem .6rem;
    }
    .pf-assemble-btn {
        padding: .4rem .65rem;
        font-size: .7rem;
    }
}
"""


# ═══════════════════════════════════════════════════════════════
# HTML fragment
# ═══════════════════════════════════════════════════════════════
def build_assemble_html():
    return r"""<!-- ASSEMBLE MODE -->
<div class="pf-assemble-mode" id="pfAssembleMode">
    <div class="pf-assemble-answer" id="pfAssembleAnswer">
        <span class="pf-assemble-hint">Bấm từ bên dưới để ghép câu</span>
    </div>
    <div class="pf-assemble-pool" id="pfAssemblePool"></div>
    <div class="pf-assemble-actions">
        <button type="button" class="pf-assemble-btn" id="pfAssembleShuffleBtn">
            <i class="fas fa-random"></i> Xáo trộn
        </button>
        <button type="button" class="pf-assemble-btn" id="pfAssembleClearBtn">
            <i class="fas fa-undo-alt"></i> Xóa hết
        </button>
        <button type="button" class="pf-assemble-btn primary" id="pfAssembleHintBtn">
            <i class="fas fa-lightbulb"></i> Gợi ý
        </button>
    </div>
</div>
"""


# ═══════════════════════════════════════════════════════════════
# HTML injection — chèn vào ui_html gốc
# ═══════════════════════════════════════════════════════════════
def inject_assemble_html(ui_html: str) -> str:
    """
    Chèn 2 thứ vào ui_html:
      1. Nút toggle 🧩 vào mini-group trong practice-full-nav
      2. Khối pf-assemble-mode vào sau char-preview
    """

    # ── 1. Thêm nút toggle vào mini-group ──
    toggle_btn = (
        '<button class="pf-nav-icon mini-nav assemble-toggle" '
        'id="pfAssembleToggleBtn" type="button" '
        'title="Chế độ Ghép từ" aria-label="Chế độ Ghép từ">'
        '<i class="fas fa-puzzle-piece"></i>'
        '</button>'
    )

    mini_group_pattern = r'(<div class="mini-group">)'
    if re.search(mini_group_pattern, ui_html):
        ui_html = re.sub(
            mini_group_pattern,
            r'\1\n        ' + toggle_btn,
            ui_html,
            count=1,
        )
        print("✅ [assemble] Đã chèn nút toggle vào mini-group")
    else:
        print("⚠️  [assemble] Không tìm thấy .mini-group để chèn nút toggle")

    # ── 2. Thêm khối pf-assemble-mode sau .char-preview ──
    assemble_block = build_assemble_html()

    char_preview_pattern = (
        r'(<div class="char-preview" id="pfPreview"></div>)'
    )
    if re.search(char_preview_pattern, ui_html):
        ui_html = re.sub(
            char_preview_pattern,
            r'\1\n' + assemble_block,
            ui_html,
            count=1,
        )
        print("✅ [assemble] Đã chèn khối ghép từ sau char-preview")
    else:
        print("⚠️  [assemble] Không tìm thấy .char-preview để chèn khối ghép từ")

    return ui_html


# ═══════════════════════════════════════════════════════════════
# JS
# ═══════════════════════════════════════════════════════════════
def build_assemble_js():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* GHÉP TỪ (Word Assembly) — chế độ luyện dịch nâng cao        */
/* Module độc lập, tự hook vào loadPracticeFull               */
/* ═══════════════════════════════════════════════════════════ */
(function() {
    'use strict';

    var pfAssembleMode = false;
    var pfAssembleWords = [];
    var pfAssembleAnswerIdx = [];
    var pfAssembleCorrectWords = [];

    /* ─────────────────────────────────────────────────── */
    /* Tách đáp án thành TỪNG KÝ TỰ Hán (không dùng pinyin) */
    /* ─────────────────────────────────────────────────── */
    function pfSplitIntoWords(zh, pinyin) {
        if (!zh) return [];

        // ⭐ Luôn tách từng ký tự Hán riêng lẻ
        var words = [];
        for (var i = 0; i < zh.length; i++) {
            var c = zh[i];
            if (/[\u4e00-\u9fa5]/.test(c)) {
                words.push(c);
            }
        }
        return words;
    }

    /* ─────────────────────────────────────────────────── */
    /* Shuffle (Fisher-Yates)                              */
    /* ─────────────────────────────────────────────────── */
    function pfShuffleArray(arr) {
        var a = arr.slice();
        for (var i = a.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        }
        return a;
    }

    /* ─────────────────────────────────────────────────── */
    /* Tạo/xáo trộn bộ từ cho câu hiện tại                 */
    /* ─────────────────────────────────────────────────── */
    function pfBuildAssembleWords() {
        var answer = (typeof pfCurrentAnswer !== 'undefined') ? pfCurrentAnswer : '';
        var pinyin = (typeof pfCurrentPinyin !== 'undefined') ? pfCurrentPinyin : '';

        pfAssembleCorrectWords = pfSplitIntoWords(answer, pinyin);

        if (pfAssembleCorrectWords.length === 0) {
            pfAssembleWords = [];
            return;
        }

        // Xáo trộn, đảm bảo không trùng với thứ tự gốc
        var shuffled = pfShuffleArray(pfAssembleCorrectWords);
        var tries = 0;
        while (tries < 15
               && shuffled.join('|') === pfAssembleCorrectWords.join('|')
               && pfAssembleCorrectWords.length > 1) {
            shuffled = pfShuffleArray(pfAssembleCorrectWords);
            tries++;
        }

        pfAssembleWords = shuffled;
        pfAssembleAnswerIdx = [];
    }

    /* ─────────────────────────────────────────────────── */
    /* Kiểm tra trạng thái ghép hiện tại                   */
    /* ─────────────────────────────────────────────────── */
    function pfCheckAssembleStatus() {
        var n = pfAssembleAnswerIdx.length;
        var total = pfAssembleCorrectWords.length;

        if (n === 0) return 'empty';

        var userWords = pfAssembleAnswerIdx.map(function(i) {
            return pfAssembleWords[i];
        });

        if (n < total) {
            // Chưa đủ từ → chỉ cần prefix đúng
            for (var i = 0; i < n; i++) {
                if (userWords[i] !== pfAssembleCorrectWords[i]) {
                    return 'wrong';
                }
            }
            return 'incomplete';
        }

        // Đã đủ từ → so khớp toàn bộ
        if (userWords.length !== total) return 'wrong';
        for (var j = 0; j < total; j++) {
            if (userWords[j] !== pfAssembleCorrectWords[j]) {
                return 'wrong';
            }
        }
        return 'correct';
    }

    /* ─────────────────────────────────────────────────── */
    /* Render 2 ô: đáp án + pool                           */
    /* ─────────────────────────────────────────────────── */
    function pfRenderAssemble() {
        var answerEl = document.getElementById('pfAssembleAnswer');
        var poolEl   = document.getElementById('pfAssemblePool');
        if (!answerEl || !poolEl) return;

        var escHtml = (typeof escapeHtml === 'function')
            ? escapeHtml
            : function(s) { return String(s); };

        // ═══ Ô ĐÁP ÁN ═══
        if (pfAssembleAnswerIdx.length === 0) {
            answerEl.innerHTML = '<span class="pf-assemble-hint">Bấm từ bên dưới để ghép câu</span>';
        } else {
            var html = '';
            pfAssembleAnswerIdx.forEach(function(origIdx, pos) {
                var word = pfAssembleWords[origIdx];
                html += '<button type="button" class="pf-word" ' +
                        'data-pool-idx="' + origIdx + '" ' +
                        'data-pos="' + pos + '">' +
                        escHtml(word) +
                        '</button>';
            });
            answerEl.innerHTML = html;

            // Bind click bằng JS (tránh inline onclick phải truyền global)
            answerEl.querySelectorAll('.pf-word').forEach(function(btn) {
                btn.addEventListener('click', function(e) {
                    e.stopPropagation();
                    e.preventDefault();
                    var pos = parseInt(this.dataset.pos, 10);
                    if (!isNaN(pos)) pfUnpickWord(pos);
                });
            });
        }

        // ═══ Ô POOL ═══
        var poolHtml = '';
        pfAssembleWords.forEach(function(word, idx) {
            var isUsed = pfAssembleAnswerIdx.indexOf(idx) !== -1;
            poolHtml += '<button type="button" class="pf-word' +
                        (isUsed ? ' used' : '') + '" ' +
                        'data-pool-idx="' + idx + '">' +
                        escHtml(word) +
                        '</button>';
        });
        poolEl.innerHTML = poolHtml;

        // Bind click cho pool (chỉ những từ chưa dùng)
        poolEl.querySelectorAll('.pf-word:not(.used)').forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                var idx = parseInt(this.dataset.poolIdx, 10);
                if (!isNaN(idx)) pfPickWord(idx);
            });
        });

        // ═══ Cập nhật class trạng thái ═══
        answerEl.classList.remove('correct', 'wrong');
        var status = pfCheckAssembleStatus();
        if (status === 'correct') {
            answerEl.classList.add('correct');
        } else if (status === 'wrong') {
            answerEl.classList.add('wrong');
        }
    }

    /* ─────────────────────────────────────────────────── */
    /* User tap từ ở pool → đẩy vào ô đáp án               */
    /* ─────────────────────────────────────────────────── */
    function pfPickWord(poolIdx) {
        if (pfAssembleAnswerIdx.indexOf(poolIdx) !== -1) return;

        pfAssembleAnswerIdx.push(poolIdx);
        pfRenderAssemble();

        var status = pfCheckAssembleStatus();
        if (status === 'correct') {
            pfOnAssembleCorrect();
        } else if (status === 'wrong') {
            // Không báo lỗi ngay — chỉ hiển thị đỏ nhẹ
            var statusEl = document.getElementById('pfStatus');
            if (statusEl) {
                statusEl.textContent = 'Sai vị trí';
                statusEl.className = 'practice-full-status wrong';
            }
        } else if (status === 'incomplete') {
            var statusEl2 = document.getElementById('pfStatus');
            if (statusEl2) {
                var n = pfAssembleAnswerIdx.length;
                var total = pfAssembleCorrectWords.length;
                statusEl2.textContent = 'Đang ghép... (' + n + '/' + total + ')';
                statusEl2.className = 'practice-full-status';
            }
        }
    }

    /* ─────────────────────────────────────────────────── */
    /* User tap từ ở ô đáp án → trả về pool                */
    /* ─────────────────────────────────────────────────── */
    function pfUnpickWord(pos) {
        if (pos < 0 || pos >= pfAssembleAnswerIdx.length) return;

        pfAssembleAnswerIdx.splice(pos, 1);
        pfRenderAssemble();

        var statusEl = document.getElementById('pfStatus');
        if (statusEl) {
            var status = pfCheckAssembleStatus();
            if (status === 'empty') {
                statusEl.textContent = '';
                statusEl.className = 'practice-full-status';
            } else if (status === 'incomplete') {
                var n = pfAssembleAnswerIdx.length;
                var total = pfAssembleCorrectWords.length;
                statusEl.textContent = 'Đang ghép... (' + n + '/' + total + ')';
                statusEl.className = 'practice-full-status';
            } else if (status === 'wrong') {
                statusEl.textContent = 'Sai vị trí';
                statusEl.className = 'practice-full-status wrong';
            }
        }
    }

    /* ─────────────────────────────────────────────────── */
    /* Callback khi ghép đúng                              */
    /* ─────────────────────────────────────────────────── */
    function pfOnAssembleCorrect() {
        var statusEl = document.getElementById('pfStatus');
        if (statusEl) {
            statusEl.textContent = 'ĐÚNG';
            statusEl.className = 'practice-full-status correct';
        }

        // Tự đọc câu (không đụng vào quickSpeakFull — dùng utterance riêng)
        var answer = (typeof pfCurrentAnswer !== 'undefined') ? pfCurrentAnswer : '';
        if (answer && 'speechSynthesis' in window) {
            setTimeout(function() {
                try { speechSynthesis.cancel(); } catch(e) {}
                var u = new SpeechSynthesisUtterance(answer);
                u.lang = 'zh-CN';
                if (typeof applyVoiceSettings === 'function') {
                    try { applyVoiceSettings(u); } catch(e) {}
                }
                setTimeout(function() {
                    try { speechSynthesis.speak(u); } catch(e) {}
                }, 100);
            }, 200);
        }
    }

    /* ─────────────────────────────────────────────────── */
    /* Reset trạng thái ghép                                */
    /* ─────────────────────────────────────────────────── */
    function pfResetAssemble() {
        pfBuildAssembleWords();
        pfRenderAssemble();
        var statusEl = document.getElementById('pfStatus');
        if (statusEl) {
            statusEl.textContent = '';
            statusEl.className = 'practice-full-status';
        }
    }

    /* ─────────────────────────────────────────────────── */
    /* Bật/tắt chế độ ghép từ                              */
    /* ─────────────────────────────────────────────────── */
    function pfToggleAssembleMode() {
        pfAssembleMode = !pfAssembleMode;

        var btn = document.getElementById('pfAssembleToggleBtn');
        if (btn) btn.classList.toggle('active', pfAssembleMode);

        document.body.classList.toggle('pf-assemble-active', pfAssembleMode);

        if (pfAssembleMode) {
            pfResetAssemble();
        } else {
            var statusEl = document.getElementById('pfStatus');
            if (statusEl) {
                statusEl.textContent = '';
                statusEl.className = 'practice-full-status';
            }
            // Focus lại textarea
            setTimeout(function() {
                var inp = document.getElementById('pfInput');
                if (inp) inp.focus();
            }, 100);
        }

        try {
            localStorage.setItem('pfAssembleMode', pfAssembleMode ? '1' : '0');
        } catch(e) {}
    }

    /* ─────────────────────────────────────────────────── */
    /* Hook vào loadPracticeFull để tự reset khi đổi câu   */
    /* ─────────────────────────────────────────────────── */
    function patchLoadPracticeFull() {
        var orig = window.loadPracticeFull;
        if (typeof orig !== 'function' || orig.__assemblePatched) return;

        window.loadPracticeFull = function(stt) {
            var r = orig.apply(this, arguments);
            if (pfAssembleMode) {
                pfResetAssemble();
            }
            return r;
        };
        window.loadPracticeFull.__assemblePatched = true;
        console.log('[Assemble] Đã hook loadPracticeFull');
    }

    /* ─────────────────────────────────────────────────── */
    /* Init                                                */
    /* ─────────────────────────────────────────────────── */
    function initAssembleFeature() {
        patchLoadPracticeFull();

        var toggleBtn = document.getElementById('pfAssembleToggleBtn');
        if (toggleBtn && !toggleBtn.__bound) {
            toggleBtn.__bound = true;
            toggleBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                pfToggleAssembleMode();
            });
        }

        var shuffleBtn = document.getElementById('pfAssembleShuffleBtn');
        if (shuffleBtn && !shuffleBtn.__bound) {
            shuffleBtn.__bound = true;
            shuffleBtn.addEventListener('click', function(e) {
                e.preventDefault();
                pfResetAssemble();
            });
        }

        var clearBtn = document.getElementById('pfAssembleClearBtn');
        if (clearBtn && !clearBtn.__bound) {
            clearBtn.__bound = true;
            clearBtn.addEventListener('click', function(e) {
                e.preventDefault();
                pfAssembleAnswerIdx = [];
                pfRenderAssemble();
                var statusEl = document.getElementById('pfStatus');
                if (statusEl) {
                    statusEl.textContent = '';
                    statusEl.className = 'practice-full-status';
                }
            });
        }

        var hintBtn = document.getElementById('pfAssembleHintBtn');
        if (hintBtn && !hintBtn.__bound) {
            hintBtn.__bound = true;
            hintBtn.addEventListener('click', function(e) {
                e.preventDefault();
                pfAssembleAnswerIdx = [];
                var used = {};
                pfAssembleCorrectWords.forEach(function(correctWord) {
                    for (var i = 0; i < pfAssembleWords.length; i++) {
                        if (used[i]) continue;
                        if (pfAssembleWords[i] === correctWord) {
                            pfAssembleAnswerIdx.push(i);
                            used[i] = true;
                            break;
                        }
                    }
                });
                pfRenderAssemble();
                pfOnAssembleCorrect();
            });
        }

        // Đọc lại trạng thái từ localStorage (nhưng không auto-bật
        // — chỉ bật nếu user đã bật lần trước)
        try {
            var saved = localStorage.getItem('pfAssembleMode') === '1';
            if (saved && !pfAssembleMode) {
                // Gọi trực tiếp không qua toggle để tránh double-toggle
                pfAssembleMode = true;
                var btn2 = document.getElementById('pfAssembleToggleBtn');
                if (btn2) btn2.classList.add('active');
                document.body.classList.add('pf-assemble-active');
            }
        } catch(e) {}

        console.log('[Assemble] Module loaded OK');
    }

    // Chờ DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAssembleFeature);
    } else {
        initAssembleFeature();
    }

    // Expose để debug
    window.__assembleDebug = {
        getMode: function() { return pfAssembleMode; },
        getWords: function() { return pfAssembleWords.slice(); },
        getPicked: function() { return pfAssembleAnswerIdx.slice(); },
        reset: pfResetAssemble
    };

})();
"""


# ═══════════════════════════════════════════════════════════════
# Self-test
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    css = build_assemble_css()
    html = build_assemble_html()
    js = build_assemble_js()

    print(f"✅ CSS:  {len(css):>7} ký tự")
    print(f"✅ HTML: {len(html):>6} ký tự")
    print(f"✅ JS:   {len(js):>7} ký tự")

    # Test inject vào HTML giả
    mock_ui = '''
    <div class="mini-group">
        <button class="pf-nav-icon mini-nav random" id="pfRandomToggleBtn"></button>
    </div>
    <div class="char-preview" id="pfPreview"></div>
    '''
    result = inject_assemble_html(mock_ui)
    assert 'pfAssembleToggleBtn' in result, "Thiếu nút toggle"
    assert 'pfAssembleMode' in result, "Thiếu khối assemble"
    print("✅ Inject HTML OK")
    print("\n🎉 Module sẵn sàng dùng!")
