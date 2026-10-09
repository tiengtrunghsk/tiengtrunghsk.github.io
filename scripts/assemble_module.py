# -*- coding: utf-8 -*-
"""
ASSEMBLE MODULE — Chế độ "Ghép từ" cho Practice Full.
Module độc lập, không đụng vào mã gốc.

Đặc điểm:
  - Tap pool → chèn từ vào VỊ TRÍ CON TRỎ (không phải cuối)
  - Tap vào ô đáp án → đặt con trỏ ở vị trí tap
  - Tap vào từ trong ô đáp án → đưa từ về pool
  - Tap giữa 2 từ → chèn con trỏ vào giữa
  - Khi bật mode → ẩn nút "Chấm điểm" + "Xem đáp án"
  - Nút toggle có label "Ghép từ" ↔ "Gõ tự do" + badge "MỚI"
  - Nút Random + Voice gộp vào 1 nút Settings ⚙️

Cách dùng trong convert.py:
    from assemble_module import (
        build_assemble_css,
        build_assemble_html,
        build_assemble_js,
        inject_assemble_html,
    )

    full_css += "\n/* ASSEMBLE */\n" + build_assemble_css()
    ui_html = inject_assemble_html(ui_html)
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

/* Ô "Câu trả lời" */
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
    gap: 2px;
    align-items: center;
    justify-content: center;
    transition: border-color .2s, background .2s;
    position: relative;
    cursor: text;
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

/* Ô "Từ gợi ý" */
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
    flex-shrink: 0;
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

/* Nút từ ở ô đáp án — màu khác */
.pf-assemble-answer .pf-word {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 12px rgba(99,102,241,.35);
    animation: pfWordPop .25s cubic-bezier(.34,1.56,.64,1);
}
@keyframes pfWordPop {
    0%   { transform: scale(.7); opacity: 0; }
    100% { transform: scale(1);  opacity: 1; }
}
.pf-assemble-answer .pf-word:hover {
    box-shadow: 0 6px 18px rgba(99,102,241,.5);
    border-color: transparent;
    transform: translateY(-2px) scale(1.04);
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

/* Khi bật chế độ ghép từ → ẩn input gõ tự do */
body.pf-assemble-active #pfInputMode { display: none !important; }
body.pf-assemble-active #pfPreview { display: none !important; }
body.pf-assemble-active .practice-full-input { display: none !important; }

/* Ẩn "Chấm điểm" + "Xem đáp án" khi bật ghép từ */
body.pf-assemble-active #pfHintBtn,
body.pf-assemble-active #pfRevealBtn,
body.pf-assemble-active .reveal-actions {
    display: none !important;
}

/* ═══════════════════════════════════════════════════════════ */
/* CON TRỎ INSERT — vạch dọc nhấp nháy giữa các từ             */
/* ═══════════════════════════════════════════════════════════ */
.pf-insert-cursor {
    display: inline-block;
    width: 3px;
    height: 1.6em;
    background: var(--primary);
    vertical-align: middle;
    margin: 0 2px;
    border-radius: 2px;
    animation: pfCursorBlink 1s steps(2) infinite;
    box-shadow: 0 0 8px rgba(37,99,235,.7),
                0 0 2px rgba(37,99,235,.9);
    flex-shrink: 0;
    pointer-events: none;
}
[data-theme="dark"] .pf-insert-cursor {
    box-shadow: 0 0 8px rgba(96,165,250,.9),
                0 0 2px rgba(96,165,250,1);
}
@keyframes pfCursorBlink {
    0%, 50%   { opacity: 1; }
    51%, 100% { opacity: .2; }
}

/* Vùng click giữa 2 slot để chèn con trỏ */
.pf-insert-gap {
    display: inline-block;
    width: 6px;
    height: 1.6em;
    vertical-align: middle;
    cursor: text;
    flex-shrink: 0;
    position: relative;
}
.pf-insert-gap:hover::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 10%;
    bottom: 10%;
    width: 2px;
    transform: translateX(-50%);
    background: var(--primary);
    opacity: .5;
    border-radius: 1px;
}

/* Ô đáp án khi trống + có con trỏ */
.pf-assemble-answer .pf-insert-cursor.only {
    height: 2em;
}

/* ═══════════════════════════════════════════════════════════ */
/* NÚT TOGGLE GHÉP TỪ — có text label                          */
/* ═══════════════════════════════════════════════════════════ */
.pf-nav-icon.mini-nav.assemble-toggle.with-label {
    width: auto !important;
    min-width: auto !important;
    height: clamp(38px, 4.5vw, 44px) !important;
    padding: 0 clamp(.65rem, 1.1vw, .85rem) !important;
    border-radius: 50px !important;
    gap: .35rem;
    display: inline-flex;
    align-items: center;
    position: relative;
    overflow: visible;
    background: var(--surface);
    color: var(--text-2);
    border-color: var(--border);
    opacity: .9;
    transition: transform .2s, background .2s, color .2s,
                border-color .2s, box-shadow .2s, opacity .2s;
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label:hover:not(:disabled) {
    border-color: #6366f1;
    color: #4f46e5;
    background: rgba(99,102,241,.1);
    opacity: 1;
    transform: scale(1.05);
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label i {
    font-size: clamp(.85rem, 1vw, .95rem);
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label .assemble-toggle-label {
    font-size: clamp(.7rem, .82vw, .78rem);
    font-weight: 800;
    letter-spacing: .01em;
    white-space: nowrap;
    line-height: 1;
}
[data-theme="dark"] .pf-nav-icon.mini-nav.assemble-toggle.with-label {
    background: var(--surface-2);
    color: var(--text-2);
    border-color: var(--border);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.assemble-toggle.with-label:hover:not(:disabled) {
    background: rgba(99,102,241,.25);
    color: #a5b4fc;
    border-color: rgba(165,180,252,.5);
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label.active {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 14px rgba(99,102,241,.5);
    opacity: 1;
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label.active:hover:not(:disabled) {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 6px 18px rgba(99,102,241,.65);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.assemble-toggle.with-label.active {
    background: linear-gradient(135deg, #818cf8, #a78bfa);
    color: #1e1b4b;
    box-shadow: 0 4px 14px rgba(129,140,248,.55);
}

/* Badge "MỚI" */
.pf-nav-icon.mini-nav.assemble-toggle .assemble-new-badge {
    position: absolute;
    top: -8px;
    right: -6px;
    padding: .15rem .4rem;
    border-radius: 50px;
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: #fff;
    font-size: .55rem;
    font-weight: 900;
    letter-spacing: .3px;
    line-height: 1;
    box-shadow: 0 2px 8px rgba(220,38,38,.5),
                0 0 0 2px var(--surface);
    animation: assembleNewPulse 1.8s ease-in-out infinite;
    pointer-events: none;
    z-index: 10;
    white-space: nowrap;
    text-transform: uppercase;
}
@keyframes assembleNewPulse {
    0%, 100% { transform: scale(1); }
    50%      { transform: scale(1.12); }
}
.pf-nav-icon.mini-nav.assemble-toggle.visited .assemble-new-badge {
    display: none;
}
[data-theme="dark"] .pf-nav-icon.mini-nav.assemble-toggle .assemble-new-badge {
    box-shadow: 0 2px 8px rgba(220,38,38,.7),
                0 0 0 2px var(--surface-2);
}

/* ═══════════════════════════════════════════════════════════ */
/* NÚT CÀI ĐẶT GỘP (Random + Voice)                            */
/* ═══════════════════════════════════════════════════════════ */
.pf-settings-wrap {
    position: relative;
    display: inline-flex;
}
.pf-nav-icon.mini-nav.settings-btn {
    background: var(--surface);
    color: var(--text-2);
    border-color: var(--border);
    opacity: .85;
}
.pf-nav-icon.mini-nav.settings-btn:hover:not(:disabled) {
    opacity: 1;
    transform: scale(1.08) rotate(45deg);
    border-color: #6366f1;
    color: #4f46e5;
    background: rgba(99,102,241,.1);
}
.pf-nav-icon.mini-nav.settings-btn.active {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 12px rgba(99,102,241,.5);
    opacity: 1;
    transform: rotate(45deg);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.settings-btn {
    background: var(--surface-2);
    color: var(--text-2);
    border-color: var(--border);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.settings-btn.active {
    background: linear-gradient(135deg, #818cf8, #a78bfa);
    color: #1e1b4b;
}

.pf-settings-menu {
    position: absolute;
    bottom: calc(100% + 8px);
    right: 0;
    min-width: 220px;
    padding: .4rem;
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 14px;
    box-shadow: 0 12px 32px rgba(15,23,42,.18),
                0 4px 12px rgba(15,23,42,.1);
    display: none;
    flex-direction: column;
    gap: .15rem;
    z-index: 3000;
    animation: pfSettingsIn .2s cubic-bezier(.34,1.56,.64,1);
    transform-origin: bottom right;
}
[data-theme="dark"] .pf-settings-menu {
    box-shadow: 0 12px 32px rgba(0,0,0,.5),
                0 4px 12px rgba(0,0,0,.4);
}
.pf-settings-menu.show {
    display: flex;
}
@keyframes pfSettingsIn {
    from { opacity: 0; transform: translateY(8px) scale(.92); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}

.pf-settings-item {
    display: flex;
    align-items: center;
    gap: .6rem;
    padding: .55rem .7rem;
    border-radius: 10px;
    border: none;
    background: transparent;
    color: var(--text);
    font-size: .82rem;
    font-weight: 600;
    font-family: inherit;
    cursor: pointer;
    text-align: left;
    transition: background .15s, color .15s;
    white-space: nowrap;
}
.pf-settings-item:hover {
    background: var(--surface-2);
    color: var(--primary);
}
.pf-settings-item i:first-child {
    width: 20px;
    text-align: center;
    font-size: .95rem;
    color: var(--text-3);
    flex-shrink: 0;
    transition: color .15s;
}
.pf-settings-item:hover i:first-child {
    color: var(--primary);
}
.pf-settings-item .pf-settings-label {
    flex: 1;
    min-width: 0;
}
.pf-settings-item .pf-settings-state {
    font-size: .68rem;
    font-weight: 800;
    padding: .15rem .5rem;
    border-radius: 50px;
    background: var(--surface-2);
    color: var(--text-3);
    text-transform: uppercase;
    letter-spacing: .3px;
    flex-shrink: 0;
}
.pf-settings-item.active .pf-settings-state {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #fff;
    box-shadow: 0 2px 6px rgba(245,158,11,.4);
}
.pf-settings-item.active i:first-child {
    color: #d97706;
}

.pf-settings-backdrop {
    position: fixed;
    inset: 0;
    z-index: 2999;
    display: none;
    background: transparent;
}
.pf-settings-backdrop.show {
    display: block;
}

/* ─── Responsive ─── */
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
    .pf-nav-icon.mini-nav.assemble-toggle.with-label {
        height: 38px !important;
        padding: 0 .55rem !important;
    }
    .pf-nav-icon.mini-nav.assemble-toggle.with-label i {
        font-size: .8rem;
    }
    .pf-nav-icon.mini-nav.assemble-toggle.with-label .assemble-toggle-label {
        font-size: .68rem;
    }
    .pf-nav-icon.mini-nav.assemble-toggle .assemble-new-badge {
        font-size: .5rem;
        padding: .12rem .35rem;
    }
    .pf-settings-menu {
        min-width: 200px;
    }
    .pf-insert-gap {
        width: 4px;
    }
}

@media (max-width: 400px) {
    .pf-nav-icon.mini-nav.assemble-toggle.with-label .assemble-toggle-label {
        font-size: .64rem;
    }
    .pf-nav-icon.mini-nav.assemble-toggle.with-label {
        padding: 0 .5rem !important;
        height: 36px !important;
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
# HTML injection
# ═══════════════════════════════════════════════════════════════
def inject_assemble_html(ui_html: str) -> str:
    """
    Chèn vào ui_html:
      1. Nút toggle "Ghép từ" (có text label) vào mini-group
      2. GỘP nút Random + Voice thành 1 nút Settings ⚙️
      3. Khối pf-assemble-mode sau char-preview
    """

    # ── 1. Nút toggle "Ghép từ" có text vào mini-group ──
    toggle_btn = (
        '<button class="pf-nav-icon mini-nav assemble-toggle with-label" '
        'id="pfAssembleToggleBtn" type="button" '
        'title="Chuyển sang chế độ Ghép từ" aria-label="Chế độ Ghép từ">'
        '<i class="fas fa-puzzle-piece"></i>'
        '<span class="assemble-toggle-label">Ghép từ</span>'
        '<span class="assemble-new-badge">MỚI</span>'
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
        print("✅ [assemble] Đã chèn nút toggle 'Ghép từ' vào mini-group")
    else:
        print("⚠️  [assemble] Không tìm thấy .mini-group để chèn nút toggle")

    # ── 2. Gộp nút random + voice thành 1 nút settings ──
    combined_pattern = (
        r'(<button class="pf-nav-icon mini-nav random" id="pfRandomToggleBtn"[^>]*>.*?</button>)'
        r'\s*'
        r'(<button class="pf-nav-icon mini-nav voice" id="pfVoiceBtn"[^>]*>.*?</button>)'
    )

    settings_html = (
        '<div class="pf-settings-wrap" id="pfSettingsWrap">\n'
        '        <button class="pf-nav-icon mini-nav settings-btn" id="pfSettingsBtn" type="button" title="Cài đặt" aria-label="Cài đặt">\n'
        '            <i class="fas fa-cog"></i>\n'
        '        </button>\n'
        '        <div class="pf-settings-menu" id="pfSettingsMenu">\n'
        '            <button type="button" class="pf-settings-item" id="pfSettingsRandomBtn">\n'
        '                <i class="fas fa-dice"></i>\n'
        '                <span class="pf-settings-label">Câu ngẫu nhiên</span>\n'
        '                <span class="pf-settings-state" id="pfSettingsRandomState">OFF</span>\n'
        '            </button>\n'
        '            <button type="button" class="pf-settings-item" id="pfSettingsVoiceBtn">\n'
        '                <i class="fas fa-headphones"></i>\n'
        '                <span class="pf-settings-label">Giọng đọc</span>\n'
        '                <i class="fas fa-chevron-right" style="font-size:.7rem;opacity:.5;margin-left:auto;width:auto"></i>\n'
        '            </button>\n'
        '        </div>\n'
        '    </div>\n'
        '    <div class="pf-settings-backdrop" id="pfSettingsBackdrop"></div>'
    )

    if re.search(combined_pattern, ui_html, flags=re.DOTALL):
        ui_html = re.sub(
            combined_pattern,
            settings_html,
            ui_html,
            count=1,
            flags=re.DOTALL
        )
        print("✅ [assemble] Đã gộp nút Random + Voice thành 1 nút Settings")
    else:
        print("⚠️  [assemble] Không tìm thấy 2 nút random+voice để gộp")

    # ── 3. Khối pf-assemble-mode sau char-preview ──
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
/* GHÉP TỪ (Word Assembly) — chèn từ vào vị trí bất kỳ         */
/* ═══════════════════════════════════════════════════════════ */
(function() {
    'use strict';

    var pfAssembleMode = false;
    var pfAssembleWords = [];
    var pfAssembleAnswerIdx = [];   // mảng các poolIdx đã chọn, theo thứ tự
    var pfAssembleCorrectWords = [];
    var pfInsertPos = 0;            // vị trí con trỏ (0..answerIdx.length)

    /* ─────────────────────────────────────────────────── */
    /* Tách đáp án thành TỪNG KÝ TỰ Hán                     */
    /* ─────────────────────────────────────────────────── */
    function pfSplitIntoWords(zh) {
        if (!zh) return [];
        var words = [];
        for (var i = 0; i < zh.length; i++) {
            var c = zh[i];
            if (/[\u4e00-\u9fa5]/.test(c)) words.push(c);
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
    /* Tạo bộ từ xáo trộn cho câu hiện tại                 */
    /* ─────────────────────────────────────────────────── */
    function pfBuildAssembleWords() {
        var answer = (typeof pfCurrentAnswer !== 'undefined') ? pfCurrentAnswer : '';
        pfAssembleCorrectWords = pfSplitIntoWords(answer);

        if (pfAssembleCorrectWords.length === 0) {
            pfAssembleWords = [];
            pfAssembleAnswerIdx = [];
            pfInsertPos = 0;
            return;
        }

        // Xáo trộn, đảm bảo không trùng thứ tự gốc
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
        pfInsertPos = 0;
    }

    /* ─────────────────────────────────────────────────── */
    /* Kiểm tra trạng thái ghép                            */
    /* ─────────────────────────────────────────────────── */
    function pfCheckAssembleStatus() {
        var n = pfAssembleAnswerIdx.length;
        var total = pfAssembleCorrectWords.length;
        if (n === 0) return 'empty';

        var userWords = pfAssembleAnswerIdx.map(function(i) {
            return pfAssembleWords[i];
        });

        if (n < total) {
            for (var i = 0; i < n; i++) {
                if (userWords[i] !== pfAssembleCorrectWords[i]) return 'wrong';
            }
            return 'incomplete';
        }

        if (userWords.length !== total) return 'wrong';
        for (var j = 0; j < total; j++) {
            if (userWords[j] !== pfAssembleCorrectWords[j]) return 'wrong';
        }
        return 'correct';
    }

    /* ─────────────────────────────────────────────────── */
    /* Render ô đáp án + pool                              */
    /* ─────────────────────────────────────────────────── */
    function pfRenderAssemble() {
        var answerEl = document.getElementById('pfAssembleAnswer');
        var poolEl   = document.getElementById('pfAssemblePool');
        if (!answerEl || !poolEl) return;

        var escHtml = (typeof escapeHtml === 'function')
            ? escapeHtml
            : function(s) { return String(s); };

        // ═══ Ô ĐÁP ÁN ═══
        answerEl.innerHTML = '';

        if (pfAssembleAnswerIdx.length === 0) {
            // Chưa có từ nào → hiện con trỏ đứng giữa + hint
            answerEl.innerHTML =
                '<span class="pf-insert-cursor only" data-gap="0"></span>' +
                '<span class="pf-assemble-hint" style="margin-left:.5rem">' +
                'Chọn từ bên dưới để ghép câu' +
                '</span>';
        } else {
            // Duyệt qua các vị trí: 0..n
            // Tại mỗi vị trí: nếu là vị trí con trỏ → hiện cursor
            //                 nếu < n → hiện gap + từ
            for (var pos = 0; pos <= pfAssembleAnswerIdx.length; pos++) {
                // Gap cho phép click đặt con trỏ
                var gap = document.createElement('span');
                gap.className = 'pf-insert-gap';
                gap.dataset.gap = pos;
                gap.addEventListener('click', (function(p) {
                    return function(e) {
                        e.stopPropagation();
                        e.preventDefault();
                        pfSetCursor(p);
                    };
                })(pos));
                answerEl.appendChild(gap);

                // Con trỏ tại vị trí này
                if (pos === pfInsertPos) {
                    var cursor = document.createElement('span');
                    cursor.className = 'pf-insert-cursor';
                    cursor.dataset.gap = pos;
                    answerEl.appendChild(cursor);
                }

                // Từ tại vị trí pos
                if (pos < pfAssembleAnswerIdx.length) {
                    var origIdx = pfAssembleAnswerIdx[pos];
                    var word = pfAssembleWords[origIdx];

                    var btn = document.createElement('button');
                    btn.type = 'button';
                    btn.className = 'pf-word';
                    btn.dataset.pos = pos;
                    btn.textContent = word;

                    btn.addEventListener('click', (function(p) {
                        return function(e) {
                            e.stopPropagation();
                            e.preventDefault();
                            pfUnpickWord(p);
                        };
                    })(pos));

                    answerEl.appendChild(btn);
                }
            }
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

        poolEl.querySelectorAll('.pf-word:not(.used)').forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                var idx = parseInt(this.dataset.poolIdx, 10);
                if (!isNaN(idx)) pfPickWord(idx);
            });
        });

        // ═══ Trạng thái border ═══
        answerEl.classList.remove('correct', 'wrong');
        var status = pfCheckAssembleStatus();
        if (status === 'correct') answerEl.classList.add('correct');
        else if (status === 'wrong') answerEl.classList.add('wrong');
    }

    /* ─────────────────────────────────────────────────── */
    /* Đặt con trỏ vào vị trí bất kỳ                       */
    /* ─────────────────────────────────────────────────── */
    function pfSetCursor(pos) {
        // Clamp
        if (pos < 0) pos = 0;
        if (pos > pfAssembleAnswerIdx.length) pos = pfAssembleAnswerIdx.length;
        pfInsertPos = pos;
        pfRenderAssemble();
    }

    /* ─────────────────────────────────────────────────── */
    /* Tap từ ở pool → chèn vào vị trí con trỏ             */
    /* ─────────────────────────────────────────────────── */
    function pfPickWord(poolIdx) {
        if (pfAssembleAnswerIdx.indexOf(poolIdx) !== -1) return;

        // Chèn vào vị trí con trỏ
        pfAssembleAnswerIdx.splice(pfInsertPos, 0, poolIdx);
        pfInsertPos++;   // con trỏ nhảy sau từ vừa chèn
        pfRenderAssemble();

        var status = pfCheckAssembleStatus();
        if (status === 'correct') {
            pfOnAssembleCorrect();
        } else {
            pfUpdateStatusText();
        }
    }

    /* ─────────────────────────────────────────────────── */
    /* Tap từ trong ô đáp án → đưa về pool                 */
    /* ─────────────────────────────────────────────────── */
    function pfUnpickWord(pos) {
        if (pos < 0 || pos >= pfAssembleAnswerIdx.length) return;

        pfAssembleAnswerIdx.splice(pos, 1);

        // Điều chỉnh con trỏ
        if (pfInsertPos > pos) {
            pfInsertPos--;
        } else if (pfInsertPos === pos) {
            // Con trỏ đứng ngay chỗ vừa xoá → giữ nguyên (nhảy vào vị trí đó)
        }
        if (pfInsertPos > pfAssembleAnswerIdx.length) {
            pfInsertPos = pfAssembleAnswerIdx.length;
        }
        if (pfInsertPos < 0) pfInsertPos = 0;

        pfRenderAssemble();
        pfUpdateStatusText();
    }

    /* ─────────────────────────────────────────────────── */
    /* Cập nhật text trạng thái                            */
    /* ─────────────────────────────────────────────────── */
    function pfUpdateStatusText() {
        var statusEl = document.getElementById('pfStatus');
        if (!statusEl) return;

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
        } else if (status === 'correct') {
            statusEl.textContent = 'ĐÚNG';
            statusEl.className = 'practice-full-status correct';
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
    /* Reset                                               */
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
    /* Cập nhật UI nút toggle                              */
    /* ─────────────────────────────────────────────────── */
    function pfUpdateToggleBtnUI() {
        var btn = document.getElementById('pfAssembleToggleBtn');
        if (!btn) return;

        btn.classList.toggle('active', pfAssembleMode);

        var icon = btn.querySelector('i');
        var label = btn.querySelector('.assemble-toggle-label');

        if (pfAssembleMode) {
            if (icon) icon.className = 'fas fa-keyboard';
            if (label) label.textContent = 'Gõ tự do';
            btn.title = 'Chuyển về chế độ Gõ tự do';
            btn.setAttribute('aria-label', 'Chuyển về chế độ Gõ tự do');
        } else {
            if (icon) icon.className = 'fas fa-puzzle-piece';
            if (label) label.textContent = 'Ghép từ';
            btn.title = 'Chuyển sang chế độ Ghép từ';
            btn.setAttribute('aria-label', 'Chế độ Ghép từ');
        }
    }

    /* ─────────────────────────────────────────────────── */
    /* Bật/tắt chế độ ghép từ                              */
    /* ─────────────────────────────────────────────────── */
    function pfToggleAssembleMode() {
        pfAssembleMode = !pfAssembleMode;

        pfUpdateToggleBtnUI();

        var btn = document.getElementById('pfAssembleToggleBtn');
        if (btn) {
            btn.classList.add('visited');
            try { localStorage.setItem('assembleVisited', '1'); } catch(e) {}
        }

        document.body.classList.toggle('pf-assemble-active', pfAssembleMode);

        if (pfAssembleMode) {
            pfResetAssemble();
        } else {
            var statusEl = document.getElementById('pfStatus');
            if (statusEl) {
                statusEl.textContent = '';
                statusEl.className = 'practice-full-status';
            }
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
    /* Hook loadPracticeFull để reset khi đổi câu          */
    /* ─────────────────────────────────────────────────── */
    function patchLoadPracticeFull() {
        var orig = window.loadPracticeFull;
        if (typeof orig !== 'function' || orig.__assemblePatched) return;

        window.loadPracticeFull = function(stt) {
            var r = orig.apply(this, arguments);
            if (pfAssembleMode) pfResetAssemble();
            return r;
        };
        window.loadPracticeFull.__assemblePatched = true;
        console.log('[Assemble] Đã hook loadPracticeFull');
    }

    /* ═══════════════════════════════════════════════════════════ */
    /* NÚT CÀI ĐẶT GỘP (Random + Voice)                            */
    /* ═══════════════════════════════════════════════════════════ */
    function initSettingsMenu() {
        var settingsWrap = document.getElementById('pfSettingsWrap');
        var settingsBtn = document.getElementById('pfSettingsBtn');
        var settingsMenu = document.getElementById('pfSettingsMenu');
        var backdrop = document.getElementById('pfSettingsBackdrop');
        var randomBtn = document.getElementById('pfSettingsRandomBtn');
        var randomState = document.getElementById('pfSettingsRandomState');
        var voiceBtn = document.getElementById('pfSettingsVoiceBtn');

        if (!settingsBtn || !settingsMenu) return;
        if (settingsBtn.__bound) return;
        settingsBtn.__bound = true;

        function openMenu() {
            settingsMenu.classList.add('show');
            settingsBtn.classList.add('active');
            if (backdrop) backdrop.classList.add('show');
            updateRandomStateUI();
        }
        function closeMenu() {
            settingsMenu.classList.remove('show');
            settingsBtn.classList.remove('active');
            if (backdrop) backdrop.classList.remove('show');
        }
        function toggleMenu() {
            if (settingsMenu.classList.contains('show')) closeMenu();
            else openMenu();
        }

        settingsBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            e.preventDefault();
            toggleMenu();
        });

        if (backdrop) {
            backdrop.addEventListener('click', function() {
                closeMenu();
            });
        }

        function updateRandomStateUI() {
            if (!randomState) return;
            var isOn = (typeof pfRandomMode !== 'undefined') && pfRandomMode;
            randomState.textContent = isOn ? 'ON' : 'OFF';
            if (randomBtn) randomBtn.classList.toggle('active', isOn);
        }

        if (randomBtn) {
            randomBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                if (typeof window.pfToggleRandom === 'function') {
                    window.pfToggleRandom();
                } else if (typeof pfRandomMode !== 'undefined') {
                    pfRandomMode = !pfRandomMode;
                    try {
                        localStorage.setItem('pfRandomMode', pfRandomMode ? '1' : '0');
                    } catch(e2) {}
                }
                updateRandomStateUI();
            });
        }

        if (voiceBtn) {
            voiceBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                closeMenu();
                var voiceModal = document.getElementById('voiceModal');
                if (voiceModal) {
                    if (typeof populateVoiceSelect === 'function') {
                        try { populateVoiceSelect(); } catch(e2) {}
                    }
                    if (typeof updateVoiceUI === 'function') {
                        try { updateVoiceUI(); } catch(e2) {}
                    }
                    voiceModal.classList.add('show');
                }
            });
        }

        document.addEventListener('click', function(e) {
            if (!settingsMenu.classList.contains('show')) return;
            if (settingsWrap && settingsWrap.contains(e.target)) return;
            closeMenu();
        });

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && settingsMenu.classList.contains('show')) {
                closeMenu();
            }
        });

        updateRandomStateUI();
        window.__updateRandomSettingsUI = updateRandomStateUI;
    }

    /* ─────────────────────────────────────────────────── */
    /* Init                                                */
    /* ─────────────────────────────────────────────────── */
    function initAssembleFeature() {
        patchLoadPracticeFull();
        initSettingsMenu();

        var toggleBtn = document.getElementById('pfAssembleToggleBtn');
        if (toggleBtn && !toggleBtn.__bound) {
            toggleBtn.__bound = true;
            toggleBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                pfToggleAssembleMode();
            });
        }

        try {
            var visited = localStorage.getItem('assembleVisited') === '1';
            if (visited && toggleBtn) toggleBtn.classList.add('visited');
        } catch(e) {}

        try {
            var saved = localStorage.getItem('pfAssembleMode') === '1';
            if (saved && !pfAssembleMode) {
                pfAssembleMode = true;
                document.body.classList.add('pf-assemble-active');
            }
        } catch(e) {}

        pfUpdateToggleBtnUI();

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
                pfInsertPos = 0;
                pfRenderAssemble();
                var statusEl = document.getElementById('pfStatus');
                if (statusEl) {
                    statusEl.textContent = '';
                    statusEl.className = 'practice-full-status';
                ô }
            });
        }

        đ var hintBtn = document.getElementById('pfápAssembleHintBtn');
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
                pfInsertPos = pfAssembleAnswerIdx.length;
                pfRenderAssemble();
                pfOnAssembleCorrect();
            });
        }

        // Click trực tiếp vào vùng trống của án → đặt con trỏ về cuối
        var answerEl = document.getElementById('pfAssembleAnswer');
        if (answerEl && !answerEl.__bound) {
            answerEl.__bound = true;
            answerEl.addEventListener('click', function(e) {
                // Nếu click trực tiếp vào ô (không phải vào từ / gap / cursor)
                if (e.target === answerEl) {
                    pfSetCursor(pfAssembleAnswerIdx.length);
                }
            });
        }

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
        getCursor: function() { return pfInsertPos; },
        setCursor: pfSetCursor,
        reset: pfResetAssemble,
        toggle: pfToggleAssembleMode
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

    mock_ui = '''
    <div class="mini-group">
        <button class="pf-nav-icon mini-nav random" id="pfRandomToggleBtn" type="button">
            <i class="fas fa-dice"></i>
        </button>
        <button class="pf-nav-icon mini-nav voice" id="pfVoiceBtn" type="button">
            <i class="fas fa-headphones"></i>
        </button>
    </div>
    <div class="char-preview" id="pfPreview"></div>
    '''
    result = inject_assemble_html(mock_ui)
    assert 'pfAssembleToggleBtn' in result
    assert 'assemble-toggle-label' in result
    assert 'assemble-new-badge' in result
    assert 'pfAssembleMode' in result
    assert 'pfSettingsBtn' in result
    assert 'pfSettingsMenu' in result
    print("✅ Inject HTML OK")
    print("\n🎉 Module sẵn sàng dùng!")
