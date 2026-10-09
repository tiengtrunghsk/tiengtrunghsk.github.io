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
.pf-assemble-info {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: .4rem .55rem;
    padding: .45rem .7rem;
    margin-bottom: .5rem;
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 10px;
    font-size: clamp(.72rem, .85vw, .82rem);
    color: var(--text-2);
    transition: opacity .2s;
    line-height: 1.2;
    min-height: 0;
}
.pf-assemble-info:empty {
    display: none;
}
.pf-assemble-info.pf-info-hidden {
    display: none;
}
.pf-assemble-info .pf-info-tag {
    display: inline-flex;
    align-items: center;
    gap: .3rem;
    padding: .2rem .55rem;
    border-radius: 50px;
    font-size: clamp(.62rem, .75vw, .72rem);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .3px;
    background: var(--surface-2);
    color: var(--text-3);
    border: 1px solid var(--border);
    flex-shrink: 0;
}
.pf-assemble-info .pf-info-tag.pf-info-hsk {
    background: var(--surface-2);
    color: var(--text);
    border-color: var(--border-strong);
    font-weight: 800;
}
.pf-assemble-info .pf-info-tag.pf-info-topic {
    font-weight: 700;
    text-transform: none;
    letter-spacing: 0;
    font-size: clamp(.68rem, .82vw, .78rem);
}

/* ⭐ TU VUNG - IN DAM, NOI BAT, CLICKABLE */
.pf-assemble-info .pf-info-word {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: clamp(1.15rem, 1.6vw, 1.35rem);
    font-weight: 900;
    color: var(--primary-dark, #1e40af);
    letter-spacing: .03em;
    line-height: 1.1;
    cursor: pointer;
    padding: .18rem .6rem;
    border-radius: 8px;
    background: var(--primary-light, #dbeafe);
    border: 2px solid var(--primary, #2563eb);
    transition: all .18s ease;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    white-space: nowrap;
    flex-shrink: 0;
    vertical-align: middle;
    box-shadow: 0 2px 6px rgba(37,99,235,.15);
}
.pf-assemble-info .pf-info-word:hover {
    background: var(--primary, #2563eb);
    color: #fff;
    border-color: var(--primary-dark, #1e40af);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(37,99,235,.3);
}
.pf-assemble-info .pf-info-word:active {
    transform: scale(.97);
}
.pf-assemble-info .pf-info-word::after {
    content: '\f0eb';
    font-family: 'Font Awesome 6 Free', 'Font Awesome 5 Free';
    font-weight: 900;
    font-size: .7em;
    color: var(--primary, #2563eb);
    transition: color .18s ease;
}
.pf-assemble-info .pf-info-word:hover::after {
    color: #fff;
}
[data-theme="dark"] .pf-assemble-info .pf-info-word {
    color: #93c5fd;
    background: rgba(96, 165, 250, .15);
    border-color: #60a5fa;
}
[data-theme="dark"] .pf-assemble-info .pf-info-word:hover {
    background: #3b82f6;
    color: #fff;
    border-color: #60a5fa;
}
[data-theme="dark"] .pf-assemble-info .pf-info-word:hover::after {
    color: #fff;
}

/* ⭐ CAU VI DU ZH - KHONG CLICKABLE, MO HON */
.pf-assemble-info .pf-info-example {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: clamp(.85rem, 1.1vw, .95rem);
    color: var(--text-2);
    font-weight: 500;
    white-space: nowrap;
    flex-shrink: 0;
    opacity: .85;
    padding: .1rem .2rem;
}

.pf-assemble-info .pf-info-pinyin {
    font-style: italic;
    color: var(--text-3);
    font-size: clamp(.7rem, .82vw, .78rem);
    white-space: nowrap;
    flex-shrink: 0;
}
.pf-assemble-info .pf-info-meaning {
    color: var(--text-2);
    font-weight: 500;
    flex: 1 1 auto;
    min-width: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.pf-assemble-answer {
    min-height: clamp(56px, 8vh, 72px);
    padding: clamp(.5rem, 1vh, .75rem) clamp(.6rem, 1.2vw, .9rem);
    background: var(--surface-2);
    border: 2px dashed var(--border);
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
    background: var(--surface-2);
    border-color: var(--border);
}
.pf-assemble-answer.correct {
    border-color: var(--success);
    border-style: solid;
    background: var(--surface-2);
    animation: pfAssembleCorrect .5s ease;
}
.pf-assemble-answer.wrong {
    border-color: var(--danger);
    animation: pfAssembleWrong .4s ease;
}
@keyframes pfAssembleCorrect {
    0%   { transform: scale(1); }
    40%  { transform: scale(1.02); }
    100% { transform: scale(1); }
}
@keyframes pfAssembleWrong {
    0%,100% { transform: translateX(0); }
    25%     { transform: translateX(-4px); }
    75%     { transform: translateX(4px); }
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
    background: var(--surface);
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
    font-size: clamp(1.15rem, 2.1vw, 1.4rem);
    font-weight: 500;
    padding: clamp(.4rem, .8vh, .55rem) clamp(.75rem, 1.3vw, 1.05rem);
    border-radius: 10px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text);
    cursor: pointer;
    transition: transform .15s cubic-bezier(.34,1.56,.64,1),
                background .15s, border-color .15s, box-shadow .15s;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    line-height: 1.4;
    letter-spacing: .02em;
    box-shadow: 0 1px 3px rgba(15,23,42,.05);
    position: relative;
    flex-shrink: 0;
}
.pf-word:hover {
    transform: translateY(-1px);
    border-color: var(--border-strong);
    box-shadow: 0 3px 10px rgba(15,23,42,.08);
}
.pf-word:active {
    transform: scale(.97);
}
.pf-word.used {
    opacity: .2;
    pointer-events: none;
    transform: scale(.94);
}
.pf-assemble-answer .pf-word {
    background: var(--surface);
    color: var(--text);
    border-color: var(--border-strong);
    box-shadow: 0 1px 3px rgba(15,23,42,.06);
    animation: pfWordPop .2s cubic-bezier(.34,1.56,.64,1);
    font-weight: 500;
}
@keyframes pfWordPop {
    0%   { transform: scale(.85); opacity: 0; }
    100% { transform: scale(1);  opacity: 1; }
}
.pf-assemble-answer .pf-word:hover {
    border-color: var(--primary);
    box-shadow: 0 3px 10px rgba(37,99,235,.15);
    transform: translateY(-1px);
}
.pf-assemble-answer .pf-word.pf-word-ok {
    background: var(--surface);
    color: var(--success);
    border-color: var(--success);
    font-weight: 600;
}
.pf-assemble-answer .pf-word.pf-word-bad {
    background: var(--surface);
    color: var(--danger);
    border-color: var(--danger);
    font-weight: 600;
    animation: pfWordBadBlink 1.5s ease-in-out infinite;
}
@keyframes pfWordBadBlink {
    0%, 100% { border-color: var(--danger); }
    50%      { border-color: rgba(220,38,38,.35); }
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
    font-weight: 600;
    cursor: pointer;
    font-family: inherit;
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    transition: .15s;
}
.pf-assemble-btn:hover {
    border-color: var(--border-strong);
    color: var(--text);
    background: var(--surface-2);
}
.pf-assemble-btn.primary {
    background: var(--surface);
    color: var(--text-2);
    border-color: var(--border);
}
.pf-assemble-btn.primary:hover {
    background: var(--surface-2);
    color: var(--text);
    border-color: var(--border-strong);
}
.pf-assemble-btn.active {
    background: var(--surface-2);
    color: var(--text);
    border-color: var(--border-strong);
    box-shadow: 0 2px 8px rgba(15,23,42,.1);
}
.pf-assemble-btn.auto-shuffle {
    width: clamp(36px, 4vw, 42px);
    height: clamp(36px, 4vw, 42px);
    padding: 0;
    justify-content: center;
    border-color: var(--border);
    background: var(--surface);
    color: var(--text-3);
    position: relative;
}
.pf-assemble-btn.auto-shuffle:hover {
    border-color: var(--border-strong);
    color: var(--text);
    background: var(--surface-2);
}
.pf-assemble-btn.auto-shuffle .pf-assemble-icon {
    font-size: clamp(.85rem, 1vw, .95rem);
}
.pf-assemble-btn.auto-shuffle.active {
    border-color: var(--border-strong);
    background: var(--surface-2);
    color: var(--text);
}
.pf-assemble-btn.auto-shuffle.active .pf-assemble-icon {
    display: none;
}
.pf-assemble-btn.auto-shuffle.active .pf-shuffle-countdown {
    display: inline-flex;
}
.pf-assemble-btn .pf-shuffle-countdown {
    display: none;
    align-items: center;
    justify-content: center;
    width: clamp(26px, 2.8vw, 30px);
    height: clamp(26px, 2.8vw, 30px);
    border-radius: 50%;
    background: var(--text-2);
    color: var(--surface);
    font-size: clamp(.68rem, .8vw, .76rem);
    font-weight: 800;
    line-height: 1;
    font-variant-numeric: tabular-nums;
    animation: pfCountdownBlink 1s ease-in-out infinite;
}
@keyframes pfCountdownBlink {
    0%, 100% { opacity: 1; }
    50%      { opacity: .65; }
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
    width: 2px;
    height: 1.6em;
    background: var(--text-2);
    vertical-align: middle;
    margin: 0 2px;
    border-radius: 1px;
    animation: pfCursorBlink 1s steps(2) infinite;
    flex-shrink: 0;
    pointer-events: none;
}
@keyframes pfCursorBlink {
    0%, 50%   { opacity: 1; }
    51%, 100% { opacity: .15; }
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
    top: 15%;
    bottom: 15%;
    width: 2px;
    transform: translateX(-50%);
    background: var(--text-3);
    opacity: .4;
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
    border-color: var(--border-strong);
    color: var(--text);
    background: var(--surface-2);
    opacity: 1;
    transform: scale(1.03);
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label i {
    font-size: clamp(.85rem, 1vw, .95rem);
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label .assemble-toggle-label {
    font-size: clamp(.7rem, .82vw, .78rem);
    font-weight: 700;
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
    background: var(--surface);
    color: var(--text);
    border-color: var(--border-strong);
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label.active {
    background: var(--surface-2);
    color: var(--text);
    border-color: var(--border-strong);
    box-shadow: 0 2px 8px rgba(15,23,42,.1);
    opacity: 1;
}
.pf-nav-icon.mini-nav.assemble-toggle.with-label.active:hover:not(:disabled) {
    background: var(--surface-2);
    color: var(--text);
    border-color: var(--border-strong);
    box-shadow: 0 2px 10px rgba(15,23,42,.15);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.assemble-toggle.with-label.active {
    background: var(--surface);
    color: var(--text);
    border-color: var(--border-strong);
}
.pf-nav-icon.mini-nav.assemble-toggle .assemble-new-badge {
    position: absolute;
    top: -8px;
    right: -6px;
    padding: .15rem .4rem;
    border-radius: 50px;
    background: var(--text-2);
    color: var(--surface);
    font-size: .55rem;
    font-weight: 800;
    letter-spacing: .3px;
    line-height: 1;
    box-shadow: 0 2px 6px rgba(15,23,42,.15),
                0 0 0 2px var(--surface);
    pointer-events: none;
    z-index: 10;
    white-space: nowrap;
    text-transform: uppercase;
}
.pf-nav-icon.mini-nav.assemble-toggle.visited .assemble-new-badge {
    display: none;
}
[data-theme="dark"] .pf-nav-icon.mini-nav.assemble-toggle .assemble-new-badge {
    box-shadow: 0 2px 6px rgba(0,0,0,.4),
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
    border-color: var(--border-strong);
    color: var(--text);
    background: var(--surface-2);
}
.pf-nav-icon.mini-nav.settings-btn.active {
    background: var(--surface-2);
    color: var(--text);
    border-color: var(--border-strong);
    box-shadow: 0 2px 8px rgba(15,23,42,.1);
    opacity: 1;
    transform: rotate(45deg);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.settings-btn {
    background: var(--surface-2);
    color: var(--text-2);
    border-color: var(--border);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.settings-btn.active {
    background: var(--surface);
    color: var(--text);
    border-color: var(--border-strong);
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
    box-shadow: 0 12px 32px rgba(15,23,42,.12),
                0 4px 12px rgba(15,23,42,.06);
    display: none;
    flex-direction: column;
    gap: .15rem;
    z-index: 3000;
    animation: pfSettingsIn .2s cubic-bezier(.34,1.56,.64,1);
    transform-origin: bottom right;
}
[data-theme="dark"] .pf-settings-menu {
    box-shadow: 0 12px 32px rgba(0,0,0,.4),
                0 4px 12px rgba(0,0,0,.3);
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
    color: var(--text);
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
    color: var(--text-2);
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
    background: var(--text-2);
    color: var(--surface);
}
.pf-settings-item.active i:first-child {
    color: var(--text-2);
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

/* ⭐ DESKTOP: info bar 1 hang, khong wrap */
@media (min-width: 501px) {
    .pf-assemble-info {
        flex-wrap: nowrap;
        overflow-x: auto;
        scrollbar-width: none;
    }
    .pf-assemble-info::-webkit-scrollbar {
        display: none;
    }
}

@media (max-width: 500px) {
    .pf-assemble-info {
        padding: .35rem .55rem;
        gap: .3rem .45rem;
        font-size: .7rem;
    }
    .pf-assemble-info .pf-info-tag {
        font-size: .58rem;
        padding: .15rem .45rem;
    }
    .pf-assemble-info .pf-info-word {
        font-size: 1.05rem;
        padding: .12rem .45rem;
        border-width: 1.5px;
    }
    .pf-assemble-info .pf-info-word::after {
        font-size: .65em;
    }
    .pf-assemble-info .pf-info-example {
        font-size: .78rem;
    }
    .pf-assemble-info .pf-info-pinyin {
        font-size: .65rem;
    }
    .pf-assemble-info .pf-info-meaning {
        font-size: .68rem;
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
        max-width: 100%;
    }
    .pf-word {
        padding: .4rem .75rem;
        font-size: 1.1rem;
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
    .pf-assemble-btn.auto-shuffle {
        width: 36px;
        height: 36px;
    }
    .pf-assemble-btn .pf-shuffle-countdown {
        width: 26px;
        height: 26px;
        font-size: .66rem;
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
        '    <div class="pf-assemble-info pf-info-hidden" id="pfAssembleInfo"></div>\n'
        '    <div class="pf-assemble-answer" id="pfAssembleAnswer">\n'
        '        <span class="pf-assemble-hint">Bấm từ bên dưới để ghép câu</span>\n'
        '    </div>\n'
        '    <div class="pf-assemble-pool" id="pfAssemblePool"></div>\n'
        '    <div class="pf-assemble-actions">\n'
        '        <button type="button" class="pf-assemble-btn auto-shuffle" id="pfAssembleShuffleBtn" title="Xáo trộn - sau 10s sẽ tự động xáo lại">\n'
        '            <i class="fas fa-random pf-assemble-icon"></i>\n'
        '            <span class="pf-shuffle-countdown" id="pfShuffleCountdown">10</span>\n'
        '        </button>\n'
        '        <button type="button" class="pf-assemble-btn" id="pfAssembleClearBtn">\n'
        '            <i class="fas fa-undo-alt"></i> Xóa hết\n'
        '        </button>\n'
        '        <button type="button" class="pf-assemble-btn" id="pfAssembleHintBtn">\n'
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
    var pfInfoVisible = false;

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

    function pfFindCurrentItem() {
        try {
            if (typeof pfCurrentStt === 'undefined' || !pfCurrentStt) return null;
            if (typeof RAW_DATA === 'undefined' || !Array.isArray(RAW_DATA)) return null;
            for (var k = 0; k < RAW_DATA.length; k++) {
                if (String(RAW_DATA[k].stt) === String(pfCurrentStt)) {
                    return RAW_DATA[k];
                }
            }
        } catch(e) {}
        return null;
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

    function pfGetAssembleSourceText() {
        var currentItem = pfFindCurrentItem();
        if (currentItem && currentItem.vi_du_zh
            && String(currentItem.vi_du_zh).trim() !== '') {
            return String(currentItem.vi_du_zh);
        }
        return (typeof pfCurrentAnswer !== 'undefined') ? pfCurrentAnswer : '';
    }

    function pfGetCurrentTestWords() {
        return pfSplitIntoWords(pfGetAssembleSourceText());
    }

    function pfBuildAssembleWords() {
        var sourceText = pfGetAssembleSourceText();
        pfAssembleCorrectWords = pfSplitIntoWords(sourceText);

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
            btn.classList.add('active');
            countEl.textContent = String(pfAutoShuffleRemain);
        } else {
            btn.classList.remove('active');
        }
    }

    function pfDoShuffle() {
        var status = pfCheckAssembleStatus();
        if (status === 'correct') return;

        if (pfAssembleAnswerIdx.length === 0) {
            pfAssembleWords = pfShuffleArray(pfAssembleWords);
        } else {
            var usedSet = {};
            pfAssembleAnswerIdx.forEach(function(i) { usedSet[i] = true; });

            var freeSlots = [];
            var freeWords = [];
            for (var i = 0; i < pfAssembleWords.length; i++) {
                if (!usedSet[i]) {
                    freeSlots.push(i);
                    freeWords.push(pfAssembleWords[i]);
                }
            }

            var shuffled = pfShuffleArray(freeWords);

            for (var k = 0; k < freeSlots.length; k++) {
                pfAssembleWords[freeSlots[k]] = shuffled[k];
            }
        }

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
    /* ⭐ RENDER INFO BAR - chi hien khi bat nut Goi y */
    function pfRenderInfo() {
        var infoEl = document.getElementById('pfAssembleInfo');
        if (!infoEl) return;

        var currentItem = pfFindCurrentItem();
        if (!currentItem) {
            infoEl.innerHTML = '';
            infoEl.classList.add('pf-info-hidden');
            return;
        }

        var escHtml = (typeof escapeHtml === 'function')
            ? escapeHtml
            : function(s) {
                return String(s)
                    .replace(/&/g, '&amp;')
                    .replace(/</g, '&lt;')
                    .replace(/>/g, '&gt;')
                    .replace(/"/g, '&quot;')
                    .replace(/'/g, '&#39;');
            };

        var html = '';

        /* 1. Tag HSK */
        if (currentItem.hsk) {
            html += '<span class="pf-info-tag pf-info-hsk">' +
                    escHtml(currentItem.hsk) +
                    '</span>';
        }

        /* 2. Tag topic - chi hien neu khac "Tu vung" */
        if (currentItem.topic && currentItem.topic !== 'Từ vựng') {
            html += '<span class="pf-info-tag pf-info-topic">' +
                    escHtml(currentItem.topic) +
                    '</span>';
        }

        /* 3. TU VUNG (zh) - IN DAM, CLICKABLE -> modal meo nho */
        if (currentItem.zh) {
            html += '<span class="pf-info-word" ' +
                    'data-mnemonic-char="' + escHtml(currentItem.zh) + '" ' +
                    'title="Bấm xem mẹo nhớ" ' +
                    'role="button" tabindex="0">' +
                    escHtml(currentItem.zh) +
                    '</span>';
        }

        /* 4. CAU VI DU ZH - KHONG clickable */
        if (currentItem.vi_du_zh) {
            html += '<span class="pf-info-example">' +
                    escHtml(currentItem.vi_du_zh) +
                    '</span>';
        }

        /* 5. Pinyin cau vi du */
        if (currentItem.vi_du_pinyin) {
            html += '<span class="pf-info-pinyin">' +
                    escHtml(currentItem.vi_du_pinyin) +
                    '</span>';
        }

        /* 6. Dich cau vi du */
        if (currentItem.vi_du_vi) {
            html += '<span class="pf-info-meaning">' +
                    escHtml(currentItem.vi_du_vi) +
                    '</span>';
        }

        infoEl.innerHTML = html;

        if (pfInfoVisible) {
            infoEl.classList.remove('pf-info-hidden');
        } else {
            infoEl.classList.add('pf-info-hidden');
        }
    }

    function pfToggleInfo() {
        pfInfoVisible = !pfInfoVisible;
        var hintBtn = document.getElementById('pfAssembleHintBtn');
        if (hintBtn) {
            hintBtn.classList.toggle('active', pfInfoVisible);
        }
        pfRenderInfo();
    }

    function pfRenderAssemble() {
        var answerEl = document.getElementById('pfAssembleAnswer');
        var poolEl   = document.getElementById('pfAssemblePool');
        if (!answerEl || !poolEl) return;

        pfRenderInfo();

        if (pfAssembleCorrectWords.length < 2) {
            answerEl.innerHTML =
                '<span class="pf-assemble-hint">' +
                'Câu này chỉ có 1 từ - chuyển sang chế độ Gõ tự do để làm' +
                '</span>';
            poolEl.innerHTML = '';
            return;
        }

        var escHtml = (typeof escapeHtml === 'function')
            ? escapeHtml
            : function(s) {
                return String(s)
                    .replace(/&/g, '&amp;')
                    .replace(/</g, '&lt;')
                    .replace(/>/g, '&gt;')
                    .replace(/"/g, '&quot;')
                    .replace(/'/g, '&#39;');
            };

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
        pfInfoVisible = false;
        var hintBtn = document.getElementById('pfAssembleHintBtn');
        if (hintBtn) hintBtn.classList.remove('active');
        pfBuildAssembleWords();
        pfRenderAssemble();
        var statusEl = document.getElementById('pfStatus');
        if (statusEl) {
            statusEl.textContent = '';
            statusEl.className = 'practice-full-status';
        }
        if (pfGetAutoShufflePref()
            && !pfAutoShuffleTimer
            && pfAssembleWords.length >= 2) {
            pfStartAutoShuffle();
        }
        pfUpdateToggleBtnUI();
    }
"""


_JS_PART_3 = r"""
    function pfUpdateToggleBtnUI() {
        var btn = document.getElementById('pfAssembleToggleBtn');
        if (!btn) return;

        var testWords = pfGetCurrentTestWords();
        var canAssemble = (testWords.length >= 2);

        if (!canAssemble) {
            btn.style.display = 'none';
            if (pfAssembleMode) {
                pfAssembleMode = false;
                document.body.classList.remove('pf-assemble-active');
                pfStopAutoShuffle();
                try { localStorage.setItem('pfAssembleMode', '0'); } catch(e) {}
            }
            return;
        } else {
            btn.style.display = '';
        }

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
        if (!pfAssembleMode) {
            var testWords = pfGetCurrentTestWords();
            if (testWords.length < 2) {
                var statusEl = document.getElementById('pfStatus');
                if (statusEl) {
                    statusEl.textContent = 'Câu này chỉ có 1 từ - không thể ghép';
                    statusEl.className = 'practice-full-status';
                    setTimeout(function() {
                        if (statusEl.textContent === 'Câu này chỉ có 1 từ - không thể ghép') {
                            statusEl.textContent = '';
                        }
                    }, 2000);
                }
                return;
            }
        }

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
            var statusEl2 = document.getElementById('pfStatus');
            if (statusEl2) {
                statusEl2.textContent = '';
                statusEl2.className = 'practice-full-status';
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
            pfUpdateToggleBtnUI();
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

    /* ⭐ BRIDGE: Goi modal meo nho */
    window.pfShowMnemonicForWord = function(char, evt) {
        if (evt) {
            evt.stopPropagation();
            if (evt.preventDefault) evt.preventDefault();
        }
        if (!char) return;

        var fakeEvt = evt || {
            stopPropagation: function() {},
            preventDefault: function() {}
        };

        if (typeof window.showMnemonic === 'function') {
            var isOldStyle = (window.showMnemonic.length <= 1);

            if (!isOldStyle) {
                try {
                    window.showMnemonic(fakeEvt, char);
                    return;
                } catch (err) {
                    console.warn('[Assemble] showMnemonic(evt, char) error:', err);
                }
            }

            var fakeBtn = document.createElement('button');
            fakeBtn.setAttribute('data-char', char);
            fakeBtn.style.display = 'none';
            document.body.appendChild(fakeBtn);
            try {
                window.showMnemonic(fakeEvt, fakeBtn);
                setTimeout(function() {
                    if (fakeBtn.parentNode) fakeBtn.remove();
                }, 3000);
                return;
            } catch (err2) {
                console.warn('[Assemble] showMnemonic(fakeEvt, btn) error:', err2);
                if (fakeBtn.parentNode) fakeBtn.remove();
            }
        }

        if (typeof showTagToast === 'function') {
            showTagToast('Chức năng mẹo nhớ đang tải, vui lòng thử lại sau');
        } else if (typeof showSearchToast === 'function') {
            showSearchToast('Chức năng mẹo nhớ đang tải...');
        } else {
            console.warn('[Assemble] showMnemonic chưa sẵn sàng cho:', char);
        }
    };

    /* ⭐ Event delegation: bam tu vung -> mo modal meo nho */
    function initMnemonicDelegation() {
        if (document.__mnemonicDelegated) return;
        document.__mnemonicDelegated = true;

        document.addEventListener('click', function(e) {
            var wordEl = e.target.closest
                ? e.target.closest('.pf-info-word[data-mnemonic-char]')
                : null;
            if (!wordEl) return;
            e.stopPropagation();
            e.preventDefault();
            var ch = wordEl.getAttribute('data-mnemonic-char');
            if (ch && typeof window.pfShowMnemonicForWord === 'function') {
                window.pfShowMnemonicForWord(ch, e);
            }
        });

        document.addEventListener('keydown', function(e) {
            if (e.key !== 'Enter' && e.key !== ' ') return;
            var wordEl = e.target.closest
                ? e.target.closest('.pf-info-word[data-mnemonic-char]')
                : null;
            if (!wordEl) return;
            e.preventDefault();
            var ch = wordEl.getAttribute('data-mnemonic-char');
            if (ch && typeof window.pfShowMnemonicForWord === 'function') {
                window.pfShowMnemonicForWord(ch, e);
            }
        });
    }

    function initAssembleFeature() {
        patchLoadPracticeFull();
        initSettingsMenu();
        initMnemonicDelegation();

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
                pfToggleInfo();
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

        setInterval(function() {
            pfUpdateToggleBtnUI();
        }, 800);

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
        getAutoShufflePref: pfGetAutoShufflePref,
        toggleInfo: pfToggleInfo,
        isInfoVisible: function() { return pfInfoVisible; },
        showMnemonicForWord: window.pfShowMnemonicForWord
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
    assert 'pfAssembleInfo' in result
    print("Inject HTML OK")
    print("Module san sang dung")
