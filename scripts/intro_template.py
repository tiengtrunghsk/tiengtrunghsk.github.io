# -*- coding: utf-8 -*-
"""
Intro Template — Banner marquee chạy chữ giới thiệu tính năng.

Cung cấp 3 hàm:
  - build_intro_css()   → CSS cho banner marquee
  - build_intro_html()  → HTML cho banner marquee
  - build_intro_js()    → JS điều khiển banner marquee

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
    .qib-item {
        font-size: .72rem;
        padding: 0 1.15rem;
    }
    .qib-item.sep::after {
        margin-left: 1.15rem;
    }
    .qib-btn-ghost {
        width: 26px;
        height: 26px;
    }
}
"""


# ═══════════════════════════════════════════════════════════════════
#  HTML
# ═══════════════════════════════════════════════════════════════════
def build_intro_html():
    return r"""
<!-- QUICK INTRO BANNER — Marquee chạy chữ -->
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
/* QUICK INTRO BANNER — Marquee                                 */
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
