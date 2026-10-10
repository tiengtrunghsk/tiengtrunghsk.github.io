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
.pf-assemble-info .pf-info-example {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: clamp(.85rem, 1.1vw, .95rem);
    color: var(--text-2);
    font-weight: 500;
    white-space: nowrap;
    flex-shrink: 0;
    opacity: .85;
    padding: .15rem .35rem;
    border-radius: 6px;
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    transition: all .15s ease;
    border: 1.5px solid transparent;
}
.pf-assemble-info .pf-info-example:hover {
    background: var(--surface-2);
    border-color: var(--border);
    opacity: 1;
    color: var(--text);
}
.pf-assemble-info .pf-info-example:active {
    transform: scale(.97);
}
.pf-assemble-info .pf-info-example::after {
    content: '\f028';
    font-family: 'Font Awesome 6 Free', 'Font Awesome 5 Free';
    font-weight: 900;
    font-size: .75em;
    margin-left: .3rem;
    color: var(--text-3);
    opacity: 0;
    transition: opacity .15s ease;
}
.pf-assemble-info .pf-info-example:hover::after {
    opacity: 1;
    color: var(--primary);
}
[data-theme="dark"] .pf-assemble-info .pf-info-example:hover {
    background: var(--surface-2);
    color: var(--text);
}
.pf-assemble-info .pf-info-plain {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: clamp(.95rem, 1.2vw, 1.05rem);
    color: var(--text);
    font-weight: 600;
    white-space: nowrap;
    flex-shrink: 0;
    padding: .15rem .4rem;
    border-radius: 6px;
    user-select: text;
    cursor: default;
    letter-spacing: .02em;
}
[data-theme="dark"] .pf-assemble-info .pf-info-plain {
    color: #f1f5f9;
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
    border-width: 2.5px;
    background: linear-gradient(135deg,
        rgba(22, 163, 74, .06),
        rgba(34, 197, 94, .03));
    animation: pfAssembleCorrectGlow 1.2s cubic-bezier(.34, 1.4, .64, 1);
    display: flex;
    flex-wrap: wrap;
    gap: clamp(.4rem, .8vw, .6rem);
    align-items: flex-end;
    justify-content: center;
    padding: clamp(.7rem, 1.4vh, 1rem) clamp(.7rem, 1.4vw, 1rem);
}
.pf-assemble-answer.wrong {
    border-color: var(--danger);
    animation: pfAssembleWrong .4s ease;
}
@keyframes pfAssembleCorrectGlow {
    0% {
        border-color: var(--success);
        box-shadow: 0 0 0 0 rgba(22, 163, 74, 0);
        transform: scale(1);
    }
    30% {
        border-color: var(--success);
        box-shadow: 0 0 0 12px rgba(22, 163, 74, .18),
                    0 8px 32px rgba(22, 163, 74, .35);
        transform: scale(1.015);
    }
    100% {
        border-color: var(--success);
        box-shadow: 0 0 0 4px rgba(22, 163, 74, .12),
                    0 4px 16px rgba(22, 163, 74, .2);
        transform: scale(1);
    }
}
@keyframes pfAssembleWrong {
    0%,100% { transform: translateX(0); }
    25%     { transform: translateX(-4px); }
    75%     { transform: translateX(4px); }
}
@keyframes pfCorrectRipple {
    0% {
        opacity: .6;
        transform: scale(1);
    }
    100% {
        opacity: 0;
        transform: scale(2.2);
    }
}
.pf-assemble-answer.correct::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 14px;
    border: 2px solid var(--success);
    pointer-events: none;
    animation: pfCorrectRipple 1s ease-out;
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
    animation: pfWordPop .25s cubic-bezier(.34,1.56,.64,1);
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
@keyframes pfWordCorrectPop {
    0% {
        transform: scale(1);
        color: var(--text);
        background: var(--surface);
        border-color: var(--border-strong);
        box-shadow: 0 1px 3px rgba(15, 23, 42, .06);
    }
    35% {
        transform: scale(1.18) translateY(-3px);
        color: #fff;
        background: linear-gradient(135deg, #16a34a, #22c55e);
        border-color: #16a34a;
        box-shadow: 0 10px 26px rgba(22, 163, 74, .5),
                    0 0 0 5px rgba(22, 163, 74, .18);
    }
    70% {
        transform: scale(1.04) translateY(0);
        color: #fff;
        background: linear-gradient(135deg, #16a34a, #22c55e);
        border-color: #16a34a;
        box-shadow: 0 6px 16px rgba(22, 163, 74, .35);
    }
    100% {
        transform: scale(1) translateY(0);
        color: #fff;
        background: linear-gradient(135deg, #16a34a, #22c55e);
        border-color: #16a34a;
        box-shadow: 0 4px 12px rgba(22, 163, 74, .3);
        font-weight: 700;
    }
}
.pf-assemble-answer.correct .pf-word {
    animation: pfWordCorrectPop .9s cubic-bezier(.34, 1.4, .64, 1) forwards;
    animation-delay: calc(var(--word-idx, 0) * 80ms);
}
.pf-assemble-answer.correct .pf-word:hover {
    transform: scale(1.06) translateY(-2px);
    box-shadow: 0 8px 20px rgba(22, 163, 74, .5);
    border-color: #16a34a;
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: #fff;
}
.pf-assemble-answer.correct .pf-word:nth-child(odd) {
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: #fff;
    border-color: #16a34a;
}
.pf-assemble-answer.correct .pf-word:nth-child(even) {
    background: linear-gradient(135deg, #059669, #10b981);
    color: #fff;
    border-color: #059669;
}
.pf-assemble-answer.correct .pf-insert-cursor {
    display: none;
}
.pf-assemble-answer.correct .pf-insert-gap {
    width: 2px;
    pointer-events: none;
}
.pf-assemble-answer.correct .pf-insert-gap:hover::before {
    display: none;
}
@keyframes pfConfettiBurst {
    0% {
        opacity: 1;
        transform: translate(0, 0) scale(1) rotate(0deg);
    }
    100% {
        opacity: 0;
        transform: translate(var(--cx), var(--cy)) scale(.3) rotate(var(--cr));
    }
}
.pf-confetti {
    position: fixed;
    width: 8px;
    height: 12px;
    border-radius: 2px;
    pointer-events: none;
    z-index: 99999;
    animation: pfConfettiBurst 1.4s cubic-bezier(.25, .6, .35, 1) forwards;
}
.pf-confetti.c-green { background: #22c55e; }
.pf-confetti.c-emerald { background: #10b981; }
.pf-confetti.c-lime { background: #84cc16; }
.pf-confetti.c-yellow { background: #fbbf24; }
.pf-confetti.c-blue { background: #3b82f6; }
@keyframes pfNextBtnIn {
    0% {
        opacity: 0;
        transform: translateY(10px) scale(.9);
    }
    100% {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}
.pf-assemble-next-btn {
    margin-top: .75rem;
    padding: .65rem 1.3rem;
    border-radius: 50px;
    border: none;
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: #fff;
    font-size: .88rem;
    font-weight: 800;
    font-family: inherit;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    box-shadow: 0 6px 18px rgba(22, 163, 74, .45);
    transition: transform .2s, box-shadow .2s;
    animation: pfNextBtnIn .4s cubic-bezier(.34, 1.56, .64, 1);
    align-self: center;
}
.pf-assemble-next-btn:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 10px 26px rgba(22, 163, 74, .6);
}
.pf-assemble-next-btn:active {
    transform: translateY(0) scale(.97);
}
.pf-assemble-next-btn i {
    animation: pfNextBtnArrow 1s ease-in-out infinite;
}
@keyframes pfNextBtnArrow {
    0%, 100% { transform: translateX(0); }
    50% { transform: translateX(4px); }
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
body.pf-assemble-active #pfSpeakBtn { display: none !important; }
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
.pf-particle-layer {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 99999;
    overflow: hidden;
}
.pf-particle {
    position: absolute;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--primary, #2563eb);
    pointer-events: none;
    will-change: transform, opacity;
    box-shadow: 0 0 6px rgba(37,99,235,.6);
}
.pf-particle.c1 { background: #2563eb; box-shadow: 0 0 8px rgba(37,99,235,.7); }
.pf-particle.c2 { background: #3b82f6; box-shadow: 0 0 8px rgba(59,130,246,.7); }
.pf-particle.c3 { background: #60a5fa; box-shadow: 0 0 8px rgba(96,165,250,.7); }
.pf-particle.c4 { background: #1e40af; box-shadow: 0 0 8px rgba(30,64,175,.7); }
.pf-particle.small {
    width: 4px;
    height: 4px;
}
.pf-particle.large {
    width: 8px;
    height: 8px;
}
@keyframes pfParticleFly {
    0% {
        opacity: 1;
        transform: translate(0, 0) scale(1);
    }
    30% {
        opacity: .95;
    }
    70% {
        opacity: .5;
    }
    100% {
        opacity: 0;
        transform: translate(var(--tx), var(--ty)) scale(.15);
    }
}
@keyframes pfWordCrumble {
    0% {
        opacity: 1;
        transform: scale(1) rotate(0deg) translateY(0);
        filter: blur(0);
    }
    30% {
        opacity: .95;
        transform: scale(1.08) rotate(1deg) translateY(-2px);
        filter: blur(.3px);
    }
    60% {
        opacity: .5;
        transform: scale(1.15) rotate(3deg) translateY(-3px);
        filter: blur(1.5px);
    }
    100% {
        opacity: 0;
        transform: scale(.4) rotate(-6deg) translateY(0);
        filter: blur(4px);
    }
}
.pf-assemble-pool.pf-pool-crumbling .pf-word {
    animation: pfWordCrumble .85s cubic-bezier(.4, 0, .5, 1) forwards;
    pointer-events: none;
    transform-origin: center center;
}
@keyframes pfWordGather {
    0% {
        opacity: 0;
        transform: scale(.4) rotate(-6deg) translateY(8px);
        filter: blur(4px);
    }
    40% {
        opacity: .5;
        transform: scale(1.08) rotate(2deg) translateY(-2px);
        filter: blur(1px);
    }
    70% {
        opacity: .95;
        transform: scale(1.05) rotate(.5deg) translateY(0);
        filter: blur(0);
    }
    100% {
        opacity: 1;
        transform: scale(1) rotate(0deg) translateY(0);
        filter: blur(0);
    }
}
.pf-assemble-pool.pf-pool-gathering .pf-word {
    animation: pfWordGather 1.1s cubic-bezier(.34, 1.4, .64, 1) backwards;
    transform-origin: center center;
}
@keyframes pfWordJumpUp {
    0% {
        transform: scale(1) translateY(0);
        box-shadow: 0 1px 3px rgba(15,23,42,.06);
        background: var(--surface);
        border-color: var(--border-strong);
    }
    25% {
        transform: scale(1.18) translateY(-16px);
        box-shadow: 0 14px 32px rgba(37,99,235,.4),
                    0 0 0 5px rgba(37,99,235,.18);
        background: var(--primary-light, #dbeafe);
        border-color: var(--primary, #2563eb);
    }
    55% {
        transform: scale(1.05) translateY(-6px);
        box-shadow: 0 8px 20px rgba(37,99,235,.28),
                    0 0 0 2px rgba(37,99,235,.1);
        background: var(--primary-light, #dbeafe);
        border-color: var(--primary, #2563eb);
    }
    80% {
        transform: scale(1.02) translateY(-1px);
        box-shadow: 0 4px 12px rgba(37,99,235,.15);
        background: var(--surface);
        border-color: var(--border-strong);
    }
    100% {
        transform: scale(1) translateY(0);
        box-shadow: 0 1px 3px rgba(15,23,42,.06);
        background: var(--surface);
        border-color: var(--border-strong);
    }
}
.pf-assemble-answer .pf-word.pf-word-jumping {
    animation: pfWordJumpUp .85s cubic-bezier(.34,1.4,.64,1) !important;
    z-index: 100;
    position: relative;
}
@keyframes pfWordRipple {
    0% {
        box-shadow: 0 0 0 0 rgba(37,99,235,.55);
    }
    100% {
        box-shadow: 0 0 0 24px rgba(37,99,235,0);
    }
}
.pf-assemble-pool .pf-word:active {
    animation: pfWordRipple .55s cubic-bezier(.2, .8, .3, 1);
}
.pf-phrase-word {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    gap: .15rem;
    padding: .35rem .65rem .3rem;
    border-radius: 12px;
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: #fff;
    border: 1.5px solid #16a34a;
    box-shadow: 0 4px 12px rgba(22, 163, 74, .3);
    animation: pfPhraseIn .5s cubic-bezier(.34, 1.4, .64, 1) backwards;
    animation-delay: calc(var(--phrase-idx, 0) * 100ms);
    position: relative;
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    transition: transform .18s ease, box-shadow .18s ease;
    flex-shrink: 0;
}
.pf-phrase-word:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 22px rgba(22, 163, 74, .5);
}
.pf-phrase-word:active {
    transform: scale(.96);
}
.pf-phrase-word .pf-phrase-zh {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: clamp(1.2rem, 2.2vw, 1.5rem);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: .02em;
    color: #fff;
    text-shadow: 0 1px 2px rgba(0, 0, 0, .15);
}
.pf-phrase-word .pf-phrase-pinyin {
    font-family: inherit;
    font-size: clamp(.62rem, .8vw, .72rem);
    font-weight: 600;
    font-style: italic;
    line-height: 1;
    color: rgba(255, 255, 255, .92);
    letter-spacing: .01em;
    padding-bottom: .05rem;
}
.pf-phrase-word::after {
    content: '\f028';
    font-family: 'Font Awesome 6 Free', 'Font Awesome 5 Free';
    font-weight: 900;
    position: absolute;
    top: 4px;
    right: 5px;
    font-size: .55em;
    color: rgba(255, 255, 255, .55);
    opacity: 0;
    transition: opacity .18s ease;
}
.pf-phrase-word:hover::after {
    opacity: 1;
    color: rgba(255, 255, 255, .95);
}
.pf-phrase-word.playing {
    animation: pfPhraseSpeak 1s ease-in-out infinite;
}
@keyframes pfPhraseSpeak {
    0%, 100% { box-shadow: 0 4px 12px rgba(22, 163, 74, .3); }
    50%      { box-shadow: 0 4px 22px rgba(22, 163, 74, .7), 0 0 0 5px rgba(22, 163, 74, .18); }
}
@keyframes pfPhraseIn {
    0% {
        opacity: 0;
        transform: scale(.7) translateY(12px);
    }
    100% {
        opacity: 1;
        transform: scale(1) translateY(0);
    }
}
.pf-phrase-vi {
    width: 100%;
    text-align: center;
    font-size: clamp(.8rem, 1vw, .9rem);
    font-style: italic;
    color: var(--text-2);
    margin-top: .35rem;
    padding: .4rem .6rem;
    border-radius: 8px;
    background: var(--surface-2);
    border-left: 3px solid #22c55e;
    animation: pfPhraseIn .6s ease-out backwards;
    animation-delay: calc(var(--phrase-count, 0) * 100ms + 200ms);
}
[data-theme="dark"] .pf-phrase-vi {
    color: #cbd5e1;
    background: rgba(255, 255, 255, .04);
}
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
    .pf-assemble-info .pf-info-plain {
        font-size: .85rem;
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
    .pf-particle {
        width: 5px;
        height: 5px;
    }
    .pf-particle.small {
        width: 3px;
        height: 3px;
    }
    .pf-particle.large {
        width: 6px;
        height: 6px;
    }
    .pf-assemble-next-btn {
        padding: .55rem 1.1rem;
        font-size: .82rem;
    }
    .pf-assemble-answer.correct {
        gap: .3rem;
        padding: .55rem .5rem;
    }
    .pf-phrase-word {
        padding: .28rem .5rem .25rem;
        border-radius: 10px;
    }
    .pf-phrase-word .pf-phrase-zh {
        font-size: 1.05rem;
    }
    .pf-phrase-word .pf-phrase-pinyin {
        font-size: .58rem;
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
        '        <button type="button" class="pf-assemble-btn auto-shuffle" id="pfAssembleShuffleBtn" title="Xáo trộn - sau 12s sẽ tự động xáo lại">\n'
        '            <i class="fas fa-random pf-assemble-icon"></i>\n'
        '            <span class="pf-shuffle-countdown" id="pfShuffleCountdown">12</span>\n'
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
        '<button class="pf-nav-icon mini-nav assemble-toggle with-label active" '
        'id="pfAssembleToggleBtn" type="button" '
        'title="Đang ở chế độ Ghép từ - bấm để chuyển sang Gõ tự do" aria-label="Đang ở chế độ Ghép từ">'
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

    var pfAssembleMode = true;
    var pfAssembleWords = [];
    var pfAssembleAnswerIdx = [];
    var pfAssembleCorrectWords = [];
    var pfInsertPos = 0;
    var pfInfoVisible = false;

    var pfAutoShuffleTimer = null;
    var pfAutoShuffleCountdown = null;
    var pfAutoShuffleRemain = 12;
    var AUTO_SHUFFLE_SECONDS = 12;
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

    function pfCreateParticles(sourceEl, count) {
        if (!sourceEl) return;

        var pfModal = document.getElementById('practiceFullModal');
        if (!pfModal || !pfModal.classList.contains('show')) {
            return;
        }

        var rect = sourceEl.getBoundingClientRect();
        var width = rect.width;
        var height = rect.height;

        var layer = document.getElementById('pfParticleLayer');
        if (!layer) {
            layer = document.createElement('div');
            layer.id = 'pfParticleLayer';
            layer.className = 'pf-particle-layer';
            document.body.appendChild(layer);
        }

        for (var i = 0; i < count; i++) {
            var p = document.createElement('div');
            p.className = 'pf-particle';

            var r = Math.random();
            if (r < 0.4) p.classList.add('small');
            else if (r > 0.85) p.classList.add('large');

            p.classList.add('c' + (Math.floor(Math.random() * 4) + 1));

            var startX = rect.left + Math.random() * width;
            var startY = rect.top + Math.random() * height;
            p.style.left = startX + 'px';
            p.style.top = startY + 'px';

            var angle = Math.random() * Math.PI * 2;
            var distance = 50 + Math.random() * 100;
            var tx = Math.cos(angle) * distance;
            var ty = Math.sin(angle) * distance - 25;

            p.style.setProperty('--tx', tx + 'px');
            p.style.setProperty('--ty', ty + 'px');

            var delay = Math.random() * 150;
            var duration = 1200 + Math.random() * 800;
            p.style.animation = 'pfParticleFly ' + duration + 'ms '
                              + 'cubic-bezier(.25, .6, .35, 1) '
                              + delay + 'ms forwards';

            layer.appendChild(p);

            (function(el) {
                setTimeout(function() {
                    if (el.parentNode) el.parentNode.removeChild(el);
                }, 2200 + delay);
            })(p);
        }
    }

    function pfCleanupParticles() {
        var layer = document.getElementById('pfParticleLayer');
        if (layer) {
            layer.innerHTML = '';
            if (layer.parentNode) {
                layer.parentNode.removeChild(layer);
            }
        }
    }

    function pfPickWord(poolIdx) {
        if (pfAssembleAnswerIdx.indexOf(poolIdx) !== -1) return;

        var pickedWord = pfAssembleWords[poolIdx];

        pfAssembleAnswerIdx.splice(pfInsertPos, 0, poolIdx);
        var insertPos = pfInsertPos;
        pfInsertPos++;

        pfRenderAssemble();

        setTimeout(function() {
            var answerEl = document.getElementById('pfAssembleAnswer');
            if (!answerEl) return;

            var btns = answerEl.querySelectorAll('.pf-word');
            for (var i = 0; i < btns.length; i++) {
                var btn = btns[i];
                if (String(btn.dataset.pos) === String(insertPos) &&
                    btn.textContent === pickedWord) {
                    btn.classList.add('pf-word-jumping');

                    setTimeout(function() {
                        btn.classList.remove('pf-word-jumping');
                    }, 900);
                    break;
                }
            }
        }, 20);

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

        var pfModal = document.getElementById('practiceFullModal');
        if (!pfModal || !pfModal.classList.contains('show')) {
            return;
        }

        var poolEl = document.getElementById('pfAssemblePool');
        if (!poolEl) return;

        var words = poolEl.querySelectorAll('.pf-word');
        words.forEach(function(w) {
            var count = 6 + Math.floor(Math.random() * 5);
            pfCreateParticles(w, count);
        });

        poolEl.classList.add('pf-pool-crumbling');

        setTimeout(function() {
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

            setTimeout(function() {
                var poolEl2 = document.getElementById('pfAssemblePool');
                if (!poolEl2) return;

                poolEl2.classList.remove('pf-pool-crumbling');
                poolEl2.classList.add('pf-pool-gathering');

                var newWords = poolEl2.querySelectorAll('.pf-word');
                newWords.forEach(function(w, idx) {
                    w.style.animationDelay = (idx * 100) + 'ms';
                });

                setTimeout(function() {
                    poolEl2.classList.remove('pf-pool-gathering');
                    newWords.forEach(function(w) {
                        w.style.animationDelay = '';
                    });
                }, 1200 + (newWords.length * 100));
            }, 30);

        }, 880);
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

        if (currentItem.hsk) {
            html += '<span class="pf-info-tag pf-info-hsk">' +
                    escHtml(currentItem.hsk) +
                    '</span>';
        }

        if (currentItem.topic && currentItem.topic !== 'Từ vựng') {
            html += '<span class="pf-info-tag pf-info-topic">' +
                    escHtml(currentItem.topic) +
                    '</span>';
        }

        var hasExample = currentItem.vi_du_zh
                      && String(currentItem.vi_du_zh).trim() !== ''
                      && String(currentItem.vi_du_zh).trim() !== String(currentItem.zh || '').trim();

        if (hasExample) {
            if (currentItem.zh) {
                html += '<span class="pf-info-word" ' +
                        'data-mnemonic-char="' + escHtml(currentItem.zh) + '" ' +
                        'title="Bấm xem mẹo nhớ" ' +
                        'role="button" tabindex="0">' +
                        escHtml(currentItem.zh) +
                        '</span>';
            }

            if (currentItem.vi_du_zh) {
                html += '<span class="pf-info-example" ' +
                        'data-tts-text="' + escHtml(currentItem.vi_du_zh) + '" ' +
                        'title="Bấm để đọc câu" ' +
                        'role="button" tabindex="0">' +
                        escHtml(currentItem.vi_du_zh) +
                        '</span>';
            }

            if (currentItem.vi_du_pinyin) {
                html += '<span class="pf-info-pinyin">' +
                        escHtml(currentItem.vi_du_pinyin) +
                        '</span>';
            }

            if (currentItem.vi_du_vi) {
                html += '<span class="pf-info-meaning">' +
                        escHtml(currentItem.vi_du_vi) +
                        '</span>';
            }
        } else {
            if (currentItem.zh) {
                html += '<span class="pf-info-plain">' +
                        escHtml(currentItem.zh) +
                        '</span>';
            }

            if (currentItem.pinyin) {
                html += '<span class="pf-info-pinyin">' +
                        escHtml(currentItem.pinyin) +
                        '</span>';
            }
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
                    btn.style.setProperty('--word-idx', String(pos));

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
        if (status === 'correct') {
            answerEl.classList.add('correct');
            pfRenderCorrectPhrases(answerEl);
        } else if (status === 'wrong') {
            answerEl.classList.add('wrong');
        }
    }

    function pfGetViDuWords() {
        var currentItem = pfFindCurrentItem();
        if (!currentItem) return [];
        if (Array.isArray(currentItem.vi_du_words) && currentItem.vi_du_words.length > 0) {
            return currentItem.vi_du_words.slice();
        }
        return [];
    }

    function pfGetViDuPinyinMap() {
        var currentItem = pfFindCurrentItem();
        var map = {};
        if (!currentItem) return map;

        var pinyinStr = String(currentItem.vi_du_pinyin || '').trim();
        if (!pinyinStr) return map;

        var zhWords = pfGetViDuWords();
        var pinyinWords = pinyinStr.split(/\s+/).filter(function(p) { return p; });

        if (zhWords.length === pinyinWords.length) {
            for (var i = 0; i < zhWords.length; i++) {
                map[zhWords[i]] = pinyinWords[i];
            }
            return map;
        }

        var hanziCount = 0;
        for (var j = 0; j < zhWords.length; j++) {
            hanziCount += zhWords[j].replace(/[^\u4e00-\u9fff]/g, '').length;
        }
        if (hanziCount === pinyinWords.length) {
            var k = 0;
            for (var m = 0; m < zhWords.length; m++) {
                var w = zhWords[m];
                var chars = w.replace(/[^\u4e00-\u9fff]/g, '');
                var pys = [];
                for (var c = 0; c < chars.length; c++) {
                    pys.push(pinyinWords[k++] || '');
                }
                map[w] = pys.join(' ');
            }
            return map;
        }

        for (var n = 0; n < zhWords.length; n++) {
            map[zhWords[n]] = pinyinWords[n] || '';
        }
        return map;
    }

    function pfRenderCorrectPhrases(answerEl) {
        var zhWords = pfGetViDuWords();

        if (zhWords.length === 0) {
            return;
        }

        var pinyinMap = pfGetViDuPinyinMap();
        var currentItem = pfFindCurrentItem();
        var viText = currentItem ? (currentItem.vi_du_vi || '') : '';

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
        for (var i = 0; i < zhWords.length; i++) {
            var w = zhWords[i];
            var py = pinyinMap[w] || '';
            html += '<span class="pf-phrase-word" '
                 + 'style="--phrase-idx:' + i + '" '
                 + 'data-tts-text="' + escHtml(w) + '" '
                 + 'title="Bấm để đọc">'
                 + '<span class="pf-phrase-zh">' + escHtml(w) + '</span>'
                 + (py ? '<span class="pf-phrase-pinyin">' + escHtml(py) + '</span>' : '')
                 + '</span>';
        }

        if (viText) {
            html += '<div class="pf-phrase-vi" style="--phrase-count:' + zhWords.length + '">'
                 + '📖 ' + escHtml(viText)
                 + '</div>';
        }

        answerEl.innerHTML = html;

        answerEl.querySelectorAll('.pf-phrase-word').forEach(function(el) {
            el.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                var text = el.getAttribute('data-tts-text') || '';
                if (!text) return;
                pfSpeakText(text);
                el.classList.add('playing');
                setTimeout(function() { el.classList.remove('playing'); }, 1200);
            });
        });
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

    function pfFireConfetti() {
        var answerEl = document.getElementById('pfAssembleAnswer');
        if (!answerEl) return;

        var rect = answerEl.getBoundingClientRect();
        var colors = ['c-green', 'c-emerald', 'c-lime', 'c-yellow', 'c-blue'];

        for (var i = 0; i < 24; i++) {
            var c = document.createElement('div');
            c.className = 'pf-confetti ' + colors[Math.floor(Math.random() * colors.length)];
            c.style.left = (rect.left + Math.random() * rect.width) + 'px';
            c.style.top = (rect.top + rect.height / 2) + 'px';

            var angle = Math.random() * Math.PI * 2;
            var distance = 80 + Math.random() * 120;
            var cx = Math.cos(angle) * distance;
            var cy = Math.sin(angle) * distance - 80 - Math.random() * 60;
            var cr = (Math.random() * 720 - 360) + 'deg';

            c.style.setProperty('--cx', cx + 'px');
            c.style.setProperty('--cy', cy + 'px');
            c.style.setProperty('--cr', cr);

            document.body.appendChild(c);

            (function(el) {
                setTimeout(function() {
                    if (el.parentNode) el.parentNode.removeChild(el);
                }, 1600);
            })(c);
        }
    }

    function pfRemoveNextBtn() {
        var old = document.getElementById('pfAssembleNextBtn');
        if (old) old.remove();
    }

    function pfShowNextBtn() {
        if (document.getElementById('pfAssembleNextBtn')) return;

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.id = 'pfAssembleNextBtn';
        btn.className = 'pf-assemble-next-btn';
        btn.innerHTML = '<i class="fas fa-arrow-right"></i> Câu tiếp theo';
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            if (typeof window.pfNext === 'function') {
                window.pfNext();
            }
        });

        var modeEl = document.getElementById('pfAssembleMode');
        if (modeEl) {
            modeEl.appendChild(btn);
        }
    }

    function pfOnAssembleCorrect() {
        var statusEl = document.getElementById('pfStatus');
        if (statusEl) {
            statusEl.textContent = '🎉 CHÍNH XÁC!';
            statusEl.className = 'practice-full-status correct';
        }
        if (pfAutoShuffleTimer) {
            pfStopAutoShuffle();
        }

        setTimeout(function() {
            pfFireConfetti();
            pfRemoveNextBtn();
            pfShowNextBtn();
        }, 400);
    }

    function pfResetAssemble() {
        pfInfoVisible = false;
        var hintBtn = document.getElementById('pfAssembleHintBtn');
        if (hintBtn) hintBtn.classList.remove('active');
        pfRemoveNextBtn();
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
    function pfSpeakText(text) {
        if (!text) return;

        var candidates = [
            'speakText', 'speak', 'speakChinese', 'speakZh',
            'playAudio', 'playVoice', 'readText', 'read',
            'ttsSpeak', 'speakSentence'
        ];
        for (var i = 0; i < candidates.length; i++) {
            var fnName = candidates[i];
            if (typeof window[fnName] === 'function') {
                try {
                    window[fnName](text);
                    return;
                } catch(err) {
                    console.warn('[Assemble] ' + fnName + ' error:', err);
                }
            }
        }

        if ('speechSynthesis' in window) {
            try {
                window.speechSynthesis.cancel();
                var u = new SpeechSynthesisUtterance(text);
                u.lang = 'zh-CN';
                u.rate = 0.9;
                u.pitch = 1.0;
                window.speechSynthesis.speak(u);
                return;
            } catch(err) {
                console.warn('[Assemble] speechSynthesis error:', err);
            }
        }

        console.warn('[Assemble] Khong tim thay ham TTS nao');
    }

    function pfUpdateToggleBtnUI() {
        var btn = document.getElementById('pfAssembleToggleBtn');
        if (!btn) return;

        var testWords = pfGetCurrentTestWords();
        var canAssemble = (testWords.length >= 2);

        if (!canAssemble) {
            btn.style.display = 'none';
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
            pfCleanupParticles();
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
        var randomBtn = document.getElementById('pf randomState = document.getElementById('pfSettingsRandomState');
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

        document.addEventListener('click', function(e) {
            var exEl = e.target.closest
                ? e.target.closest('.pf-info-example[data-tts-text]')
                : null;
            if (!exEl) return;
            e.stopPropagation();
            e.preventDefault();
            var text = exEl.getAttribute('data-tts-text');
            if (text) pfSpeakText(text);
        });

        document.addEventListener('keydown', function(e) {
            if (e.key !== 'Enter' && e.key !== ' ') return;

            var wordEl = e.target.closest
                ? e.target.closest('.pf-info-word[data-mnemonic-char]')
                : null;
            if (wordEl) {
                e.preventDefault();
                var ch = wordEl.getAttribute('data-mnemonic-char');
                if (ch && typeof window.pfShowMnemonicForWord === 'function') {
                    window.pfShowMnemonicForWord(ch, e);
                }
                return;
            }

            var exEl = e.target.closest
                ? e.target.closest('.pf-info-example[data-tts-text]')
                : null;
            if (exEl) {
                e.preventDefault();
                var text = exEl.getAttribute('data-tts-text');
                if (text) pfSpeakText(text);
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
            var saved = localStorage.getItem('pfAssembleMode');
            if (saved === '1') {
                pfAssembleMode = true;
                document.body.classList.add('pf-assemble-active');
            } else if (saved === '0') {
                pfAssembleMode = false;
                document.body.classList.remove('pf-assemble-active');
            } else {
                pfAssembleMode = true;
                document.body.classList.add('pf-assemble-active');
                try { localStorage.setItem('pfAssembleMode', '1'); } catch(e2) {}
            }
        } catch(e) {
            pfAssembleMode = true;
            document.body.classList.add('pf-assemble-active');
        }

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
                pfRemoveNextBtn();
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

        (function hookCloseModal() {
            if (window.__assembleCloseHooked) return;
            window.__assembleCloseHooked = true;

            var origClose = window.closePracticeFull;
            if (typeof origClose === 'function') {
                window.closePracticeFull = function() {
                    if (pfAutoShuffleTimer) pfStopAutoShuffle();
                    pfCleanupParticles();
                    pfRemoveNextBtn();
                    return origClose.apply(this, arguments);
                };
                console.log('[Assemble] Da hook closePracticeFull - cleanup particles');
            } else {
                setTimeout(function() {
                    var origClose2 = window.closePracticeFull;
                    if (typeof origClose2 === 'function' && !window.__assembleCloseHooked2) {
                        window.__assembleCloseHooked2 = true;
                        window.closePracticeFull = function() {
                            if (pfAutoShuffleTimer) pfStopAutoShuffle();
                            pfCleanupParticles();
                            pfRemoveNextBtn();
                            return origClose2.apply(this, arguments);
                        };
                        console.log('[Assemble] Da hook closePracticeFull (retry)');
                    }
                }, 500);
            }
        })();

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
        showMnemonicForWord: window.pfShowMnemonicForWord,
        speakText: pfSpeakText,
        cleanupParticles: pfCleanupParticles
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
