# -*- coding: utf-8 -*-
"""
ASSEMBLE MODULE - Che do Ghep tu cho Practice Full.
Module doc lap, khong dung vao ma goc.

Cach dung trong convert.py:
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


def build_assemble_css():
    return r"""
/* GHEP TU - che do luyen dich nang cao */
.pf-assemble-mode {
    display: none;
    flex-direction: column;
    gap: clamp(.5rem, 1vh, .8rem);
    margin-top: .25rem;
}
body.pf-assemble-active .pf-assemble-mode {
    display: flex;
}

/* O cau tra loi */
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

/* O tu goi y */
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

/* Nut tu */
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

/* Nut hanh dong */
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

body.pf-assemble-active #pfInputMode { display: none !important; }
body.pf-assemble-active #pfPreview { display: none !important; }
body.pf-assemble-active .practice-full-input { display: none !important; }

body.pf-assemble-active #pfHintBtn,
body.pf-assemble-active #pfRevealBtn,
body.pf-assemble-active .reveal-actions {
    display: none !important;
}

/* Con tro insert */
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

/* Nut toggle ghep tu */
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

/* Badge MOI */
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

/* Nut cai dat gop */
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
        '        <button type="button" class="pf-assemble-btn" id="pfAssembleShuffleBtn">\n'
        '            <i class="fas fa-random"></i> Xáo trộn\n'
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
        print("[assemble] Da chen nut toggle Ghep tu vao mini-group")
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


def build_assemble_js():
    return r"""
/* GHEP TU - chen tu vao vi tri bat ky */
(function() {
    'use strict';

    var pfAssembleMode = false;
    var pfAssembleWords = [];
    var pfAssembleAnswerIdx = [];
    var pfAssembleCorrectWords = [];
    var pfInsertPos = 0;

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
