# -*- coding: utf-8 -*-
"""Assemble module - Ghep tu mode for Practice Full."""

import re


def build_assemble_css():
    return r"""
.pf-assemble-mode {
    display: none;
    flex-direction: column;
    gap: clamp(.5rem, 1vh, .8rem);
    margin-top: .25rem;
}
body.pf-assemble-active .pf-assemble-mode {
    display: flex;
}
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
.pf-assemble-answer .pf-word.pf-word-ok {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    box-shadow: 0 4px 12px rgba(34,197,94,.4);
}
.pf-assemble-answer .pf-word.pf-word-bad {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    box-shadow: 0 4px 12px rgba(220,38,38,.5);
    animation: pfWordBadPulse 1.2s ease-in-out infinite;
}
@keyframes pfWordBadPulse {
    0%,100% { box-shadow: 0 4px 12px rgba(220,38,38,.5); }
    50%     { box-shadow: 0 4px 20px rgba(220,38,38,.85); }
}
.pf-assemble-answer .pf-word.pf-word-bad-cluster {
    border-radius: 6px;
    position: relative;
}
.pf-assemble-answer .pf-word.pf-word-bad-cluster:first-of-type,
.pf-assemble-answer .pf-word.pf-word-bad-cluster + .pf-word:not(.pf-word-bad-cluster) {
    border-top-right-radius: 10px;
}
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
.pf-assemble-btn.auto-shuffle {
    position: relative;
    border-color: #f59e0b;
    background: linear-gradient(135deg, rgba(245,158,11,.12), rgba(217,119,6,.06));
    color: #b45309;
    padding: clamp(.4rem, .8vh, .55rem) clamp(.7rem, 1.3vw, .95rem);
}
.pf-assemble-btn.auto-shuffle .pf-assemble-icon {
    display: none;
}
.pf-assemble-btn.auto-shuffle .pf-shuffle-label {
    display: none;
}
.pf-assemble-btn.auto-shuffle .pf-shuffle-countdown {
    display: inline-flex;
}
.pf-assemble-btn.auto-shuffle:hover {
    border-color: #d97706;
    color: #92400e;
    background: linear-gradient(135deg, rgba(245,158,11,.2), rgba(217,119,6,.1));
}
.pf-assemble-btn .pf-shuffle-countdown {
    display: none;
    align-items: center;
    justify-content: center;
    min-width: 24px;
    height: 24px;
    padding: 0 .35rem;
    border-radius: 50px;
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: #fff;
    font-size: .72rem;
    font-weight: 900;
    line-height: 1;
    font-variant-numeric: tabular-nums;
    animation: pfCountdownPulse 1s ease-in-out infinite;
}
@keyframes pfCountdownPulse {
    0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(220,38,38,.5); }
    50%      { transform: scale(1.1); box-shadow: 0 0 0 6px rgba(220,38,38,0); }
}
[data-theme="dark"] .pf-assemble-btn.auto-shuffle {
    color: #fcd34d;
    border-color: rgba(245,158,11,.6);
    background: linear-gradient(135deg, rgba(245,158,11,.2), rgba(217,119,6,.12));
}
[data-theme="dark"] .pf-assemble-btn.auto-shuffle:hover {
    color: #fde68a;
    border-color: #fbbf24;
    background: linear-gradient(135deg, rgba(245,158,11,.3), rgba(217,119,6,.18));
}
body.pf-assemble-active #pfInputMode { display: none !important; }
body.pf-assemble-active #pfPreview { display: none !important; }
body.pf-assemble-active .practice-full-input { display: none !important; }
body.pf-assemble-active #pfHintBtn,
body.pf-assemble-active #pfRevealBtn,
body.pf-assemble-active .reveal-actions {
    display: none !important;
}
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
.pf-assemble-answer .pf-insert-cursor.only {
    height: 2em;
}
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
    .pf-assemble-btn .pf-shuffle-countdown {
        min-width: 22px;
        height: 22px;
        font-size: .68rem;
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


def build_assemble_html():
    return (
        '<div class="pf-assemble-mode" id="pfAssembleMode">\n'
        '    <div class="pf-assemble-answer" id="pfAssembleAnswer">\n'
        '        <span class="pf-assemble-hint">Bấm từ bên dưới để ghép câu</span>\n'
        '    </div>\n'
        '    <div class="pf-assemble-pool" id="pfAssemblePool"></div>\n'
        '    <div class="pf-assemble-actions">\n'
        '        <button type="button" class="pf-assemble-btn auto-shuffle" id="pfAssembleShuffleBtn" title="Xáo trộn - sau 10s sẽ tự động xáo lại">\n'
        '            <i class="fas fa-random pf-assemble-icon"></i>\n'
        '            <span class="pf-shuffle-label">Xáo trộn</span>\n'
        '            <span class="pf-shuffle-countdown" id="pfShuffleCountdown">10</span>\n'
        '        </button>\n'
        '        <button type="button" class="pf-assemble-btn" id="pfAssembleClearBtn">\n'
        '            <i class="fas fa-undo-alt"></i> Xóa hết\n'
        '        </button>\n'
        '        <button type="button" class="pf-assemble-btn primary" id="pfAssembleHintBtn">\n'
        '            <i class="fas fa-lightbulb"></i> Gợi ý\n'
        '        </button>\n'
        '    </div>\n'
        '</div>\n'
    )


def inject_assemble_html(ui_html):
    toggle_btn = (
        '<button class="pf-nav-icon mini-nav assemble-toggle with-label" '
        'id="pfAssembleToggleBtn" type="button" '
        'title="Đang ở chế độ Gõ tự do - bấm để chuyển sang Ghép từ" aria-label="Đang ở chế độ Gõ tự do">'
        '<i class="fas fa-keyboard"></i>'
        '<span class="assemble-toggle-label">Gõ tự do</span>'
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
        print("[assemble] Da chen nut toggle vao mini-group")
    else:
        print("[assemble] CANH BAO: Khong tim thay .mini-group")

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
        print("[assemble] Da gop nut Random + Voice thanh 1 nut Settings")
    else:
        print("[assemble] CANH BAO: Khong tim thay 2 nut random+voice")

    assemble_block = build_assemble_html()

    char_preview_pattern = r'(<div class="char-preview" id="pfPreview"></div>)'
    if re.search(char_preview_pattern, ui_html):
        ui_html = re.sub(
            char_preview_pattern,
            r'\1\n' + assemble_block,
            ui_html,
            count=1,
        )
        print("[assemble] Da chen khoi ghep tu sau char-preview")
    else:
        print("[assemble] CANH BAO: Khong tim thay .char-preview")

    return ui_html


_JS_PART_1 = r"""
(function() {
    'use strict';

    var pfAssembleMode = false;
    var pfAssembleWords = [];
    var pfAssembleAnswerIdx = [];
    var pfAssembleCorrectWords = [];
    var pfInsertPos = 0;

    var pfAutoShuffleTimer = null;
    var pfAutoShuffleCountdown = null;
    var pfAutoShuffleRemain = 10;
    var AUTO_SHUFFLE_SECONDS = 10;
    var PF_AUTO_SHUFFLE_PREF_KEY = 'pfAutoShufflePref';

    function pfSplitIntoWords(zh) {
        if (!zh) return [];
        var words = [];
        for (var i = 0; i < zh.length; i++) {
            var c = zh[i];
            if (/[\u4e00-\u9fa5]/.test(c)) words.push(c);
        }
        return words;
    }

    function pfShuffleArray(arr) {
        var a = arr.slice();
        for (var i = a.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        }
        return a;
    }

    function pfGetAutoShufflePref() {
        try {
            return localStorage.getItem(PF_AUTO_SHUFFLE_PREF_KEY) === '1';
        } catch(e) {
            return false;
        }
    }

    function pfSetAutoShufflePref(val) {
        try {
            localStorage.setItem(PF_AUTO_SHUFFLE_PREF_KEY, val ? '1' : '0');
        } catch(e) {}
    }

    function pfBuildAssembleWords() {
        var answer = (typeof pfCurrentAnswer !== 'undefined') ? pfCurrentAnswer : '';
        pfAssembleCorrectWords = pfSplitIntoWords(answer);

        if (pfAssembleCorrectWords.length === 0) {
            pfAssembleWords = [];
            pfAssembleAnswerIdx = [];
            pfInsertPos = 0;
            return;
        }

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

    function pfGetWrongPositions() {
        var result = {};
        var n = pfAssembleAnswerIdx.length;
        var total = pfAssembleCorrectWords.length;
        if (n === 0) return result;

        var checkLen = Math.min(n, total);
        for (var i = 0; i < checkLen; i++) {
            var userWord = pfAssembleWords[pfAssembleAnswerIdx[i]];
            if (userWord !== pfAssembleCorrectWords[i]) {
                result[i] = true;
            }
        }
        if (n > total) {
            for (var k = total; k < n; k++) {
                result[k] = true;
            }
        }
        return result;
    }

    function pfGetWrongClusters(wrongPositions) {
        var clusters = [];
        var cluster = null;
        var sortedPos = Object.keys(wrongPositions)
                              .map(function(x){return parseInt(x,10);})
                              .sort(function(a,b){return a-b;});

        for (var i = 0; i < sortedPos.length; i++) {
            var p = sortedPos[i];
            if (cluster === null || p !== cluster.end + 1) {
                if (cluster) clusters.push(cluster);
                cluster = { start: p, end: p };
            } else {
                cluster.end = p;
            }
        }
        if (cluster) clusters.push(cluster);
        return clusters;
    }

    function pfPickWord(poolIdx) {
        if (pfAssembleAnswerIdx.indexOf(poolIdx) !== -1) return;

        pfAssembleAnswerIdx.splice(pfInsertPos, 0, poolIdx);
        pfInsertPos++;
        pfRenderAssemble();

        var status = pfCheckAssembleStatus();
        if (status === 'correct') {
            pfOnAssembleCorrect();
        } else {
            pfUpdateStatusText();
        }
    }

    function pfUnpickWord(pos) {
        if (pos < 0 || pos >= pfAssembleAnswerIdx.length) return;

        pfAssembleAnswerIdx.splice(pos, 1);

        if (pfInsertPos > pos) pfInsertPos--;
        if (pfInsertPos > pfAssembleAnswerIdx.length) {
            pfInsertPos = pfAssembleAnswerIdx.length;
        }
        if (pfInsertPos < 0) pfInsertPos = 0;

        pfRenderAssemble();
        pfUpdateStatusText();
    }

    function pfRemoveCluster(pos) {
        var wrongPos = pfGetWrongPositions();
        if (!wrongPos[pos]) return;

        var clusters = pfGetWrongClusters(wrongPos);
        var target = null;
        for (var i = 0; i < clusters.length; i++) {
            if (pos >= clusters[i].start && pos <= clusters[i].end) {
                target = clusters[i];
                break;
            }
        }
        if (!target) return;

        var removeCount = target.end - target.start + 1;
        pfAssembleAnswerIdx.splice(target.start, removeCount);

        if (pfInsertPos > target.end) pfInsertPos -= removeCount;
        else if (pfInsertPos >= target.start) pfInsertPos = target.start;

        if (pfInsertPos > pfAssembleAnswerIdx.length) {
            pfInsertPos = pfAssembleAnswerIdx.length;
        }
        if (pfInsertPos < 0) pfInsertPos = 0;

        pfRenderAssemble();
        pfUpdateStatusText();
    }

    function pfStopAutoShuffle() {
        if (pfAutoShuffleTimer) {
            clearInterval(pfAutoShuffleTimer);
            pfAutoShuffleTimer = null;
        }
        if (pfAutoShuffleCountdown) {
            clearInterval(pfAutoShuffleCountdown);
            pfAutoShuffleCountdown = null;
        }
        pfAutoShuffleRemain = AUTO_SHUFFLE_SECONDS;
        pfUpdateAutoShuffleUI();
    }

    function pfUpdateAutoShuffleUI() {
        var btn = document.getElementById('pfAssembleShuffleBtn');
        var countEl = document.getElementById('pfShuffleCountdown');
        if (!btn || !countEl) return;

        if (pfAutoShuffleTimer) {
            btn.classList.add('auto-shuffle');
            countEl.textContent = String(pfAutoShuffleRemain);
        } else {
            btn.classList.remove('auto-shuffle');
        }
    }

    function pfDoShuffle() {
        var status = pfCheckAssembleStatus();
        if (status === 'correct') return;

        pfAssembleWords = pfShuffleArray(pfAssembleWords);
        pfInsertPos = pfAssembleAnswerIdx.length;
        pfRenderAssemble();
    }

    function pfStartAutoShuffle() {
        pfStopAutoShuffle();

        pfAutoShuffleRemain = AUTO_SHUFFLE_SECONDS;
        pfUpdateAutoShuffleUI();

        pfAutoShuffleCountdown = setInterval(function() {
            pfAutoShuffleRemain--;
            if (pfAutoShuffleRemain < 0) pfAutoShuffleRemain = 0;
            pfUpdateAutoShuffleUI();
        }, 1000);

        pfAutoShuffleTimer = setInterval(function() {
            pfDoShuffle();
            pfAutoShuffleRemain = AUTO_SHUFFLE_SECONDS;
            pfUpdateAutoShuffleUI();
        }, AUTO_SHUFFLE_SECONDS * 1000);
    }

    function pfToggleAutoShuffle() {
        if (pfAutoShuffleTimer) {
            pfStopAutoShuffle();
            pfSetAutoShufflePref(false);
        } else {
            pfStartAutoShuffle();
            pfDoShuffle();
            pfSetAutoShufflePref(true);
        }
    }
"""


_JS_PART_2 = r"""
    function pfRenderAssemble() {
        var answerEl = document.getElementById('pfAssembleAnswer');
        var poolEl   = document.getElementById('pfAssemblePool');
        if (!answerEl || !poolEl) return;

        var escHtml = (typeof escapeHtml === 'function')
            ? escapeHtml
            : function(s) { return String(s); };

        answerEl.innerHTML = '';

        var status = pfCheckAssembleStatus();
        var isWrongFull = (status === 'wrong');
        var wrongPos = isWrongFull ? pfGetWrongPositions() : {};

        if (pfAssembleAnswerIdx.length === 0) {
            answerEl.innerHTML =
                '<span class="pf-insert-cursor only" data-gap="0"></span>' +
                '<span class="pf-assemble-hint" style="margin-left:.5rem">' +
                'Chọn từ bên dưới để ghép câu' +
                '</span>';
        } else {
            for (var pos = 0; pos <= pfAssembleAnswerIdx.length; pos++) {
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

                if (pos === pfInsertPos) {
                    var cursor = document.createElement('span');
                    cursor.className = 'pf-insert-cursor';
                    cursor.dataset.gap = pos;
                    answerEl.appendChild(cursor);
                }

                if (pos < pfAssembleAnswerIdx.length) {
                    var origIdx = pfAssembleAnswerIdx[pos];
                    var word = pfAssembleWords[origIdx];

                    var btn = document.createElement('button');
                    btn.type = 'button';
                    btn.className = 'pf-word';
                    btn.dataset.pos = pos;
                    btn.textContent = word;

                    if (isWrongFull && wrongPos[pos]) {
                        btn.classList.add('pf-word-bad');
                    }

                    btn.addEventListener('click', (function(p) {
                        return function(e) {
                            e.stopPropagation();
                            e.preventDefault();
                            var currentStatus = pfCheckAssembleStatus();
                            if (currentStatus === 'wrong') {
                                var wp = pfGetWrongPositions();
                                if (wp[p]) {
                                    pfRemoveCluster(p);
                                    return;
                                }
                            }
                            pfUnpickWord(p);
                        };
                    })(pos));

                    answerEl.appendChild(btn);
                }
            }
        }

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

        answerEl.classList.remove('correct', 'wrong');
        if (status === 'correct') answerEl.classList.add('correct');
        else if (status === 'wrong') answerEl.classList.add('wrong');
    }

    function pfSetCursor(pos) {
        if (pos < 0) pos = 0;
        if (pos > pfAssembleAnswerIdx.length) pos = pfAssembleAnswerIdx.length;
        pfInsertPos = pos;
        pfRenderAssemble();
    }

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
            statusEl.textContent = 'Sai vị trí - bấm từ đỏ để xoá cụm sai';
            statusEl.className = 'practice-full-status wrong';
        } else if (status === 'correct') {
            statusEl.textContent = 'ĐÚNG';
            statusEl.className = 'practice-full-status correct';
        }
    }

    function pfOnAssembleCorrect() {
        var statusEl = document.getElementById('pfStatus');
        if (statusEl) {
            statusEl.textContent = 'ĐÚNG';
            statusEl.className = 'practice-full-status correct';
        }
        if (pfAutoShuffleTimer) {
            pfStopAutoShuffle();
        }
    }

    function pfResetAssemble() {
        pfBuildAssembleWords();
        pfRenderAssemble();
        var statusEl = document.getElementById('pfStatus');
        if (statusEl) {
            statusEl.textContent = '';
            statusEl.className = 'practice-full-status';
        }
        // Neu user da tung bat auto-shuffle -> tu bat lai
        if (pfGetAutoShufflePref()
            && !pfAutoShuffleTimer
            && pfAssembleWords.length > 0) {
            pfStartAutoShuffle();
        }
    }
"""


_JS_PART_3 = r"""
    function pfUpdateToggleBtnUI() {
        var btn = document.getElementById('pfAssembleToggleBtn');
        if (!btn) return;

        btn.classList.toggle('active', pfAssembleMode);

        var icon = btn.querySelector('i');
        var label = btn.querySelector('.assemble-toggle-label');

        if (pfAssembleMode) {
            if (icon) icon.className = 'fas fa-puzzle-piece';
            if (label) label.textContent = 'Ghép từ';
            btn.title = 'Đang ở chế độ Ghép từ - bấm để chuyển sang Gõ tự do';
            btn.setAttribute('aria-label', 'Đang ở chế độ Ghép từ');
        } else {
            if (icon) icon.className = 'fas fa-keyboard';
            if (label) label.textContent = 'Gõ tự do';
            btn.title = 'Đang ở chế độ Gõ tự do - bấm để chuyển sang Ghép từ';
            btn.setAttribute('aria-label', 'Đang ở chế độ Gõ tự do');
        }
    }

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
            pfStopAutoShuffle();
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

    function patchLoadPracticeFull() {
        var orig = window.loadPracticeFull;
        if (typeof orig !== 'function' || orig.__assemblePatched) return;

        window.loadPracticeFull = function(stt) {
            var r = orig.apply(this, arguments);
            if (pfAssembleMode) pfResetAssemble();
            return r;
        };
        window.loadPracticeFull.__assemblePatched = true;
        console.log('[Assemble] Da hook loadPracticeFull');
    }
"""


_JS_PART_4 = r"""
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
                pfToggleAutoShuffle();
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
                pfInsertPos = pfAssembleAnswerIdx.length;
                pfRenderAssemble();
                pfOnAssembleCorrect();
            });
        }

        var answerEl = document.getElementById('pfAssembleAnswer');
        if (answerEl && !answerEl.__bound) {
            answerEl.__bound = true;
            answerEl.addEventListener('click', function(e) {
                if (e.target === answerEl) {
                    pfSetCursor(pfAssembleAnswerIdx.length);
                }
            });
        }

        console.log('[Assemble] Module loaded OK');
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAssembleFeature);
    } else {
        initAssembleFeature();
    }

    window.__assembleDebug = {
        getMode: function() { return pfAssembleMode; },
        getWords: function() { return pfAssembleWords.slice(); },
        getPicked: function() { return pfAssembleAnswerIdx.slice(); },
        getCursor: function() { return pfInsertPos; },
        setCursor: pfSetCursor,
        reset: pfResetAssemble,
        toggle: pfToggleAssembleMode,
        isAutoShuffle: function() { return !!pfAutoShuffleTimer; },
        toggleAutoShuffle: pfToggleAutoShuffle,
        getAutoShufflePref: pfGetAutoShufflePref
    };

})();
"""


def build_assemble_js():
    return _JS_PART_1 + _JS_PART_2 + _JS_PART_3 + _JS_PART_4


if __name__ == "__main__":
    css = build_assemble_css()
    html = build_assemble_html()
    js = build_assemble_js()

    print("CSS:  %d ky tu" % len(css))
    print("HTML: %d ky tu" % len(html))
    print("JS:   %d ky tu" % len(js))

    mock_ui = (
        '<div class="mini-group">\n'
        '    <button class="pf-nav-icon mini-nav random" id="pfRandomToggleBtn" type="button">\n'
        '        <i class="fas fa-dice"></i>\n'
        '    </button>\n'
        '    <button class="pf-nav-icon mini-nav voice" id="pfVoiceBtn" type="button">\n'
        '        <i class="fas fa-headphones"></i>\n'
        '    </button>\n'
        '</div>\n'
        '<div class="char-preview" id="pfPreview"></div>\n'
    )
    result = inject_assemble_html(mock_ui)
    assert 'pfAssembleToggleBtn' in result
    assert 'assemble-toggle-label' in result
    assert 'assemble-new-badge' in result
    assert 'pfAssembleMode' in result
    assert 'pfSettingsBtn' in result
    assert 'pfSettingsMenu' in result
    assert 'pfShuffleCountdown' in result
    assert 'pf-assemble-icon' in result
    assert 'pf-shuffle-label' in result
    print("Inject HTML OK")
    print("Module san sang dung")
