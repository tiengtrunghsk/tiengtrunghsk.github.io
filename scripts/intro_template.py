# -*- coding: utf-8 -*-
"""
Intro Template — Banner marquee chạy chữ giới thiệu tính năng.

Cung cấp 3 hàm:
  - build_intro_css()   → CSS cho banner marquee + 2 nút mock
  - build_intro_html()  → HTML cho banner marquee + 2 nút mock
  - build_intro_js()    → JS điều khiển banner + highlight nút thật

Nút #introBtn trên header → scroll đến banner + nhấp nháy highlight.
"""


# ═══════════════════════════════════════════════════════════════════
#  CSS
# ═══════════════════════════════════════════════════════════════════
def build_intro_css():
    return r"""
/* ═══════════════════════════════════════════════════════════════ */
/* QUICK INTRO BANNER — Marquee chạy chữ quảng cáo              */
/* ═══════════════════════════════════════════════════════════════ */
.quick-intro-banner {
    display: flex;
    align-items: center;
    gap: .65rem;
    padding: .55rem .85rem;
    margin-bottom: 1rem;
    background: linear-gradient(135deg,
        rgba(99, 102, 241, .08) 0%,
        rgba(139, 92, 246, .08) 50%,
        rgba(217, 70, 239, .06) 100%);
    border: 1.5px solid rgba(139, 92, 246, .3);
    border-radius: 12px;
    overflow: hidden;
    position: relative;
    animation: qibSlideDown .5s cubic-bezier(.34, 1.56, .64, 1);
    box-shadow: 0 2px 10px rgba(139, 92, 246, .08);
    transition: box-shadow .3s ease, transform .3s ease;
}
@keyframes qibSlideDown {
    from { opacity: 0; transform: translateY(-12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.quick-intro-banner.dismissed { display: none !important; }

.qib-icon {
    width: 32px;
    height: 32px;
    border-radius: 9px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6 40%, #d946ef);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: .9rem;
    flex-shrink: 0;
    box-shadow: 0 3px 10px rgba(139, 92, 246, .35);
    position: relative;
    z-index: 2;
}

.qib-marquee {
    flex: 1 1 auto;
    min-width: 0;
    height: 26px;
    overflow: hidden;
    position: relative;
    mask-image: linear-gradient(90deg,
        transparent 0%,
        #000 6%,
        #000 94%,
        transparent 100%);
    -webkit-mask-image: linear-gradient(90deg,
        transparent 0%,
        #000 6%,
        #000 94%,
        transparent 100%);
}

.qib-track {
    display: inline-flex;
    align-items: center;
    height: 100%;
    white-space: nowrap;
    animation: qibScroll 30s linear infinite;
    will-change: transform;
}
@keyframes qibScroll {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}

.qib-item {
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    padding: 0 1.5rem;
    font-size: .8rem;
    font-weight: 700;
    color: var(--text);
    line-height: 1;
    flex-shrink: 0;
}
.qib-item i {
    color: #d946ef;
    font-size: .8rem;
}
.qib-item b {
    color: #dc2626;
    font-weight: 900;
    margin: 0 .1em;
}
.qib-item.sep::after {
    content: '·';
    margin-left: 1.5rem;
    color: var(--text-3);
    opacity: .5;
    font-size: 1.2em;
}

[data-theme="dark"] .qib-item {
    color: #e2e8f0;
}
[data-theme="dark"] .qib-item b {
    color: #fca5a5;
}
[data-theme="dark"] .qib-item i {
    color: #f0abfc;
}

/* ═══════════════════════════════════════════════════════════ */
/* 2 NÚT MOCK BÊN PHẢI — minh hoạ nút thật trên card            */
/* ═══════════════════════════════════════════════════════════ */
.qib-mock-actions {
    display: flex;
    gap: .35rem;
    align-items: center;
    flex-shrink: 0;
    position: relative;
    z-index: 2;
    padding-left: .5rem;
    border-left: 1.5px dashed rgba(139, 92, 246, .3);
}
.qib-mock-btn {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: none;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: .85rem;
    cursor: pointer;
    flex-shrink: 0;
    transition: transform .2s cubic-bezier(.34,1.56,.64,1),
                box-shadow .2s, background .2s, color .2s;
    position: relative;
    font-family: inherit;
    padding: 0;
}
.qib-mock-btn:hover {
    transform: scale(1.15);
}
.qib-mock-btn.write {
    background: var(--amber-light, #fef3c7);
    color: #92400e;
}
.qib-mock-btn.write:hover {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #fff;
    box-shadow: 0 4px 12px rgba(245, 158, 11, .45);
}
.qib-mock-btn.full {
    background: var(--primary-light, #dbeafe);
    color: var(--primary-dark, #1e40af);
}
.qib-mock-btn.full::after {
    content: '';
    position: absolute;
    inset: -3px;
    border-radius: 50%;
    border: 2px solid var(--primary, #2563eb);
    animation: qibMockPulse 1.8s ease-in-out infinite;
    pointer-events: none;
}
@keyframes qibMockPulse {
    0%, 100% { opacity: .5; transform: scale(1); }
    50%      { opacity: .1; transform: scale(1.3); }
}
.qib-mock-btn.full:hover {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: #fff;
    box-shadow: 0 4px 12px rgba(37, 99, 235, .45);
}
[data-theme="dark"] .qib-mock-btn.write {
    background: rgba(245,158,11,.22);
    color: #fcd34d;
}
[data-theme="dark"] .qib-mock-btn.full {
    background: rgba(59,130,246,.22);
    color: #93c5fd;
}

.qib-actions {
    display: flex;
    align-items: center;
    gap: .35rem;
    flex-shrink: 0;
    position: relative;
    z-index: 2;
}

.qib-btn-ghost {
    width: 28px;
    height: 28px;
    padding: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: var(--surface);
    color: var(--text-3);
    border: 1px solid var(--border);
    border-radius: 50px;
    cursor: pointer;
    font-family: inherit;
    font-size: .78rem;
    transition: all .2s ease;
}
.qib-btn-ghost:hover {
    background: var(--danger-light);
    color: var(--danger);
    border-color: var(--danger);
    transform: rotate(90deg);
}

.qib-marquee:hover .qib-track {
    animation-play-state: paused;
}

@media (max-width: 500px) {
    .quick-intro-banner {
        padding: .5rem .65rem;
        gap: .5rem;
    }
    .qib-icon {
        width: 28px;
        height: 28px;
        font-size: .82rem;
        border-radius: 8px;
    }
    .qib-marquee { height: 22px; }
    .qib-item  {
        font-size: .2672rem;
        padding: 0px 1.15rem;
    }
    .;
qib-item.sep::after {
        margin   -left: 1.15rem;
 }
    }
    .qib-mock-actions {
        gap: .25rem;
        padding-left: .35rem;
    }
    .qib-mock-btn {
        width: 28px;
        height: 28px;
        font-size: .75rem;
    }
    .qib-btn-ghost {
        width: 26px;
        height:}
@media (max-width: 380px) {
    .qib-mock-btn.write {
        display: none;
    }
}
"""


# ═══════════════════════════════════════════════════════════════════
#  HTML
# ═══════════════════════════════════════════════════════════════════
def build_intro_html():
    return r"""
<!-- QUICK INTRO BANNER — Marquee chạy chữ + 2 nút mock -->
<div class="quick-intro-banner" id="quickIntroBanner">
    <div class="qib-icon">
        <i class="fas fa-bullhorn"></i>
    </div>

    <div class="qib-marquee">
        <div class="qib-track">
            <span class="qib-item sep">
                <i class="fas fa-bolt"></i>
                <b>Chế độ luyện tập</b> Gõ tự do · Ghép chữ · HSK 1 → 9
            </span>
            <span class="qib-item sep">
                <i class="fas fa-bolt"></i>
                <b>Chế độ luyện tập</b> Gõ tự do · Ghép chữ · HSK 1 → 9
            </span>
        </div>
    </div>

    <div class="qib-mock-actions">
        <button type="button" class="qib-mock-btn write"
                id="qibMockWriteBtn"
                title="Bấm nút này trên mỗi câu để luyện viết chữ Hán">
            <i class="fas fa-pen-fancy"></i>
        </button>
        <button type="button" class="qib-mock-btn full"
                id="qibMockFullBtn"
                title="Bấm nút này trên mỗi câu để mở chế độ luyện tập toàn màn hình">
            <i class="fas fa-expand"></i>
        </button>
    </div>

    <div class="qib-actions">
        <button class="qib-btn-ghost" id="quickIntroDismiss" title="Đóng">
            <i class="fas fa-times"></i>
        </button>
    </div>
</div>
"""


# ═══════════════════════════════════════════════════════════════════
#  JS
# ═══════════════════════════════════════════════════════════════════
def build_intro_js():
    return r"""
/* ═══════════════════════════════════════════════════════════════ */
/* QUICK INTRO BANNER — Marquee + 2 nút mock                     */
/* ═══════════════════════════════════════════════════════════════ */
function initQuickIntroBanner() {
    var banner = $('quickIntroBanner');
    var dismiss = $('quickIntroDismiss');
    if (!banner) return;

    var hidden = false;
    try { hidden = localStorage.getItem('quick_intro_dismissed') === '1'; } catch(e) {}
    if (hidden) { banner.classList.add('dismissed'); return; }

    if (dismiss && !dismiss.__bound) {
        dismiss.__bound = true;
        dismiss.addEventListener('click', function() {
            banner.classList.add('dismissed');
            try { localStorage.setItem('quick_intro_dismissed', '1'); } catch(e) {}
        });
    }

    var track = banner.querySelector('.qib-track');
    if (track) {
        var updateSpeed = function() {
            var w = track.scrollWidth / 2;
            if (w <= 0) return;
            var pxPerSec = 60;
            track.style.animationDuration = (w / pxPerSec) + 's';
        };
        setTimeout(updateSpeed, 100);
        setTimeout(updateSpeed, 800);
        window.addEventListener('resize', updateSpeed);
    }

    /* ⭐ 2 nút mock — click để làm nổi bật nút thật trên card đầu tiên */
    var mockWriteBtn = $('qibMockWriteBtn');
    var mockFullBtn  = $('qibMockFullBtn');

    function highlightRealButton(selector) {
        /* Tìm card đầu tiên đang hiện */
        var firstCard = document.querySelector('.card');
        if (!firstCard) {
            /* Fallback: scroll xuống main content */
            var main = document.getElementById('mainContent');
            if (main) {
                window.scrollTo({
                    top: main.getBoundingClientRect().top + window.scrollY - 100,
                    behavior: 'smooth'
                });
            }
            return;
        }

        /* Tìm nút trong card */
        var targetBtn = firstCard.querySelector(selector);
        if (!targetBtn) return;

        /* Scroll đến card */
        window.scrollTo({
            top: firstCard.getBoundingClientRect().top + window.scrollY - 100,
            behavior: 'smooth'
        });

        /* Highlight nhấp nháy */
        var origBoxShadow = targetBtn.style.boxShadow;
        var origTransform = targetBtn.style.transform;
        var origZIndex = targetBtn.style.zIndex;
        var count = 0;
        var timer = setInterval(function() {
            count++;
            if (count % 2 === 1) {
                targetBtn.style.boxShadow = '0 0 0 6px rgba(37,99,235,.4), 0 4px 14px rgba(37,99,235,.4)';
                targetBtn.style.transform = 'scale(1.25)';
                targetBtn.style.zIndex = '100';
            } else {
                targetBtn.style.boxShadow = origBoxShadow || '';
                targetBtn.style.transform = origTransform || '';
                targetBtn.style.zIndex = origZIndex || '';
            }
            if (count >= 6) {
                clearInterval(timer);
                targetBtn.style.boxShadow = origBoxShadow || '';
                targetBtn.style.transform = origTransform || '';
                targetBtn.style.zIndex = origZIndex || '';
            }
        }, 400);
    }

    if (mockWriteBtn && !mockWriteBtn.__bound) {
        mockWriteBtn.__bound = true;
        mockWriteBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            highlightRealButton('.write-btn');
        });
    }

    if (mockFullBtn && !mockFullBtn.__bound) {
        mockFullBtn.__bound = true;
        mockFullBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            highlightRealButton('.practice-full-btn');
        });
    }
}

function resetQuickIntroBanner() {
    try { localStorage.removeItem('quick_intro_dismissed'); } catch(e) {}
    var banner = $('quickIntroBanner');
    if (banner) banner.classList.remove('dismissed');
}

/* ⭐ Nút intro trên header → scroll xuống banner + highlight */
function handleIntroBtnClick() {
    var banner = $('quickIntroBanner');
    if (!banner) return;

    /* Nếu banner đã bị ẩn → hiện lại */
    if (banner.classList.contains('dismissed')) {
        banner.classList.remove('dismissed');
        try { localStorage.removeItem('quick_intro_dismissed'); } catch(e) {}
    }

    /* Scroll đến banner */
    var y = banner.getBoundingClientRect().top + window.scrollY - 100;
    window.scrollTo({ top: y, behavior: 'smooth' });

    /* Nhấp nháy highlight */
    banner.style.transition = 'box-shadow .3s ease, transform .3s ease';
    var blinkCount = 0;
    var blinkTimer = setInterval(function() {
        blinkCount++;
        if (blinkCount % 2 === 1) {
            banner.style.boxShadow = '0 0 0 4px rgba(139,92,246,.35), 0 8px 24px rgba(139,92,246,.35)';
            banner.style.transform = 'scale(1.01)';
        } else {
            banner.style.boxShadow = '';
            banner.style.transform = '';
        }
        if (blinkCount >= 6) {
            clearInterval(blinkTimer);
            banner.style.boxShadow = '';
            banner.style.transform = '';
        }
    }, 350);
}

/* Hook vào initApp */
(function() {
    function wrapInitApp() {
        if (typeof window.initApp !== 'function') return false;
        if (window.initApp.__introHooked) return true;

        var _origInitApp = window.initApp;
        window.initApp = function() {
            _origInitApp.apply(this, arguments);
            initQuickIntroBanner();

            /* ⭐ Bind nút intro trên header */
            var introBtn = document.getElementById('introBtn');
            if (introBtn && !introBtn.__introBound) {
                introBtn.__introBound = true;
                introBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    handleIntroBtnClick();
                });
            }
        };
        window.initApp.__introHooked = true;
        return true;
    }

    if (!wrapInitApp()) {
        var tries = 0;
        var iv = setInterval(function() {
            tries++;
            if (wrapInitApp() || tries > 20) clearInterval(iv);
        }, 100);
    }
})();
"""
