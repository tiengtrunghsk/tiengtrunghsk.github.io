# -*- coding: utf-8 -*-
"""
Intro Template — Banner marquee chạy chữ thông báo tính năng Trợ Lý AI Dịch Thuật & Tạo bài học từ ảnh.
Màu sắc nổi bật, tương phản cao, dễ nhận diện.

Cung cấp 3 hàm:
  - build_intro_css()   → CSS cho banner marquee + 3 nút mock
  - build_intro_html()  → HTML cho banner marquee + 3 nút mock
  - build_intro_js()    → JS điều khiển banner + highlight nút thật
"""

# ═══════════════════════════════════════════════════════════════════
#  CSS
# ═══════════════════════════════════════════════════════════════════
def build_intro_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* QUICK INTRO BANNER — Marquee nổi bật, dễ nhận diện            */
/* ═══════════════════════════════════════════════════════════ */
.quick-intro-banner {
    display: flex;
    align-items: center;
    gap: .65rem;
    padding: .65rem .9rem;
    margin-bottom: 1.05rem;
    /* ⭐ Gradient: Xanh dương -> Tím (Đồng bộ với Trợ Lý Dịch) */
    background: linear-gradient(135deg, #3b82f6 0%, #6366f1 50%, #8b5cf6 100%);
    border: 2px solid rgba(255, 255, 255, 0.2);
    border-radius: 14px;
    overflow: hidden;
    position: relative;
    animation: qibSlideDown .5s cubic-bezier(.34, 1.56, .64, 1);
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.3);
    transition: box-shadow .3s ease, transform .3s ease;
}
@keyframes qibSlideDown {
    from { opacity: 0; transform: translateY(-12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.quick-intro-banner.dismissed { display: none !important; }

/* ⭐ Ẩn banner khi ở tab Từ vựng Premium */
body[data-vocab-mode="1"] .quick-intro-banner {
    display: none !important;
}

/* Icon máy ảnh/robot: Màu Vàng kim nổi bật */
.qib-icon {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: linear-gradient(135deg, #f59e0b, #fbbf24);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
    box-shadow: 0 3px 12px rgba(245, 158, 11, 0.5);
    position: relative;
    z-index: 2;
}

.qib-marquee {
    flex: 1 1 auto;
    min-width: 0;
    height: 32px;
    overflow: hidden;
    position: relative;
    mask-image: linear-gradient(90deg, transparent 0%, #000 5%, #000 95%, transparent 100%);
    -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 5%, #000 95%, transparent 100%);
}

.qib-track {
    display: inline-flex;
    align-items: center;
    height: 100%;
    white-space: nowrap;
    animation: qibScroll 28s linear infinite;
    will-change: transform;
}
@keyframes qibScroll {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}

/* Chữ chạy: Trắng đậm, có viền đổ bóng để nổi bật */
.qib-item {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    padding: 0 1.5rem;
    font-size: 1.05rem;
    font-weight: 900;
    color: #ffffff;
    line-height: 1;
    flex-shrink: 0;
    letter-spacing: .03em;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Dấu chấm ngăn cách (·) màu vàng tươi */
.qib-item.sep::after {
    content: '·';
    margin-left: 1.5rem;
    color: #fde047;
    opacity: 1;
    font-size: 1.8em;
    font-weight: 900;
    line-height: 1;
    text-shadow: 0 0 8px rgba(253, 224, 71, 0.8);
}

/* ═══════════════════════════════════════════════════════════ */
/* NÚT MOCK BÊN PHẢI — minh hoạ nút thật trên card             */
/* ═══════════════════════════════════════════════════════════ */
.qib-mock-actions {
    display: flex;
    gap: .4rem;
    align-items: center;
    flex-shrink: 0;
    position: relative;
    z-index: 2;
    padding-left: .6rem;
    border-left: 2px dashed rgba(255, 255, 255, 0.4);
}
.qib-mock-btn {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    border: 2px solid rgba(255, 255, 255, 0.4);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: .95rem;
    cursor: pointer;
    flex-shrink: 0;
    transition: transform .2s cubic-bezier(.34,1.56,.64,1), box-shadow .2s, background .2s, border-color .2s;
    position: relative;
    font-family: inherit;
    padding: 0;
    background: rgba(255, 255, 255, 0.2);
    color: #fff;
    backdrop-filter: blur(4px);
}
.qib-mock-btn:hover {
    transform: scale(1.15) translateY(-2px);
    background: #fff;
    color: #3b82f6;
    border-color: #fff;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}
/* Hiệu ứng pulse nhấn mạnh nút dịch ảnh / tạo bài học từ ảnh */
.qib-mock-btn.img::after {
    content: '';
    position: absolute;
    inset: -4px;
    border-radius: 50%;
    border: 2px solid #fde047;
    animation: qibMockPulse 1.8s ease-in-out infinite;
    pointer-events: none;
}
@keyframes qibMockPulse {
    0%, 100% { opacity: .7; transform: scale(1); }
    50%      { opacity: .1; transform: scale(1.3); }
}

/* Nút đóng (X) */
.qib-actions {
    display: flex;
    align-items: center;
    gap: .35rem;
    flex-shrink: 0;
    position: relative;
    z-index: 2;
}

.qib-btn-ghost {
    width: 30px;
    height: 30px;
    padding: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.2);
    color: #fff;
    border: 2px solid transparent;
    border-radius: 50%;
    cursor: pointer;
    font-family: inherit;
    font-size: .85rem;
    transition: all .25s ease;
}
.qib-btn-ghost:hover {
    background: #ef4444;
    color: #fff;
    border-color: #fff;
    transform: rotate(90deg) scale(1.1);
    box-shadow: 0 0 12px rgba(239, 68, 68, 0.6);
}

.qib-marquee:hover .qib-track {
    animation-play-state: paused;
}

/* Responsive cho Mobile */
@media (max-width: 560px) {
    .quick-intro-banner {
        padding: .55rem .65rem;
        gap: .5rem;
    }
    .qib-icon {
        width: 32px;
        height: 32px;
        font-size: .9rem;
        border-radius: 9px;
    }
    .qib-marquee { height: 28px; }
    .qib-item {
        font-size: .9rem;
        padding: 0 1.15rem;
        gap: .35rem;
    }
    .qib-item.sep::after {
        margin-left: 1.15rem;
        font-size: 1.5em;
    }
    .qib-mock-actions {
        gap: .3rem;
        padding-left: .4rem;
    }
    .qib-mock-btn {
        width: 32px;
        height: 32px;
        font-size: .85rem;
    }
    .qib-btn-ghost {
        width: 28px;
        height: 28px;
    }
}
@media (max-width: 400px) {
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
<!-- QUICK INTRO BANNER — Giới thiệu Tạo bài học từ ảnh & Trợ lý Dịch thuật AI -->
<div class="quick-intro-banner" id="quickIntroBanner">
    <div class="qib-icon">
        <i class="fas fa-camera-retro"></i>
    </div>

    <div class="qib-marquee">
        <div class="qib-track">
            <span class="qib-item sep">
                📸 TÍNH NĂNG MỚI: TẠO BÀI HỌC TỪ ẢNH & TRỢ LÝ AI - Chụp ảnh văn bản, cắt vùng OCR thông minh và tự động tạo bài tập luyện tập trong 1 click!
            </span>
            <span class="qib-item sep">
                📸 TÍNH NĂNG MỚI: TẠO BÀI HỌC TỪ ẢNH & TRỢ LÝ AI - Chụp ảnh văn bản, cắt vùng OCR thông minh và tự động tạo bài tập luyện tập trong 1 click!
            </span>
        </div>
    </div>

    <div class="qib-mock-actions">
        <button type="button" class="qib-mock-btn img"
                id="qibMockImgBtn"
                title="Tạo bài học từ ảnh / Dịch ảnh">
            <i class="fas fa-camera"></i>
        </button>
        <button type="button" class="qib-mock-btn write"
                id="qibMockWriteBtn"
                title="Đổi chiều dịch Việt - Trung">
            <i class="fas fa-exchange-alt"></i>
        </button>
        <button type="button" class="qib-mock-btn full"
                id="qibMockFullBtn"
                title="Bắt đầu dịch văn bản tự do">
            <i class="fas fa-rocket"></i>
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
/* ═══════════════════════════════════════════════════════════ */
/* QUICK INTRO BANNER — Marquee + 3 nút mock + auto-hide theo tab */
/* ═══════════════════════════════════════════════════════════ */
function initQuickIntroBanner() {
    var banner = $('quickIntroBanner');
    var dismiss = $('quickIntroDismiss');
    if (!banner) return;

    /* ─── Nút đóng ─── */
    var hidden = false;
    try { hidden = localStorage.getItem('quick_intro_dismissed') === '1'; } catch(e) {}

    if (dismiss && !dismiss.__bound) {
        dismiss.__bound = true;
        dismiss.addEventListener('click', function() {
            banner.classList.add('dismissed');
            try { localStorage.setItem('quick_intro_dismissed', '1'); } catch(e) {}
        });
    }

    /* ─── Auto-tính tốc độ marquee ─── */
    var track = banner.querySelector('.qib-track');
    if (track && !track.__bound) {
        track.__bound = true;
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

    /* ─── 3 nút mock — click để làm nổi bật nút thật trên khung Trợ lý dịch ─── */
    var mockImgBtn   = $('qibMockImgBtn');
    var mockWriteBtn = $('qibMockWriteBtn');
    var mockFullBtn  = $('qibMockFullBtn');

    function highlightRealButton(selector) {
        var targetBtn = document.querySelector(selector);
        if (!targetBtn) return;

        // Cuộn đến phần tử tương ứng
        window.scrollTo({
            top: targetBtn.getBoundingClientRect().top + window.scrollY - 150,
            behavior: 'smooth'
        });

        // Hiệu ứng nhấp nháy
        var origBoxShadow = targetBtn.style.boxShadow;
        var origTransform = targetBtn.style.transform;
        var origZIndex = targetBtn.style.zIndex;
        var count = 0;
        var timer = setInterval(function() {
            count++;
            if (count % 2 === 1) {
                targetBtn.style.boxShadow = '0 0 0 6px rgba(37,99,235,.4), 0 4px 14px rgba(37,99,235,.4)';
                targetBtn.style.transform = 'scale(1.1)';
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

    if (mockImgBtn && !mockImgBtn.__bound) {
        mockImgBtn.__bound = true;
        mockImgBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            // Trỏ đến nút chụp/tải ảnh thật (cpUploadImgBtn)
            highlightRealButton('#cpUploadImgBtn');
        });
    }

    if (mockWriteBtn && !mockWriteBtn.__bound) {
        mockWriteBtn.__bound = true;
        mockWriteBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            // Trỏ đến nút chuyển đổi ngôn ngữ (cpSwitchBtn)
            highlightRealButton('#cpSwitchBtn');
        });
    }

    if (mockFullBtn && !mockFullBtn.__bound) {
        mockFullBtn.__bound = true;
        mockFullBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            // Trỏ đến nút bắt đầu dịch (cpStartBtn)
            highlightRealButton('#cpStartBtn');
        });
    }

    /* ⭐ Tự động ẩn/hiện banner theo tab hiện tại */
    if (!window.__qibTabSyncBound) {
        window.__qibTabSyncBound = true;
        var _lastDs = null;
        var syncBannerByTab = function() {
            var bannerEl = document.getElementById('quickIntroBanner');
            if (!bannerEl) return;

            var curDs = (typeof CURRENT_DATASET !== 'undefined') ? CURRENT_DATASET : 'tonghop';
            if (curDs === _lastDs) return;
            _lastDs = curDs;

            if (curDs === 'tu-vung') {
                bannerEl.style.display = 'none';
            } else {
                var dismissed = false;
                try { dismissed = localStorage.getItem('quick_intro_dismissed') === '1'; } catch(e) {}
                bannerEl.style.display = dismissed ? 'none' : '';
            }
        };
        syncBannerByTab();
        setInterval(syncBannerByTab, 300);
    }

    /* Khởi tạo lần đầu: nếu là tab vocab hoặc đã dismissed → ẩn */
    var curDsInit = (typeof CURRENT_DATASET !== 'undefined') ? CURRENT_DATASET : 'tonghop';
    if (curDsInit === 'tu-vung' || hidden) {
        banner.classList.add('dismissed');
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

    /* Nếu đang ở tab Từ vựng → chuyển về tab Tổng hợp trước */
    var curDs = (typeof CURRENT_DATASET !== 'undefined') ? CURRENT_DATASET : 'tonghop';
    if (curDs === 'tu-vung') {
        if (typeof window.switchDataset === 'function') {
            window.switchDataset('tonghop');
        } else if (typeof window.__switchRawData === 'function') {
            window.__switchRawData('tonghop');
            if (typeof applyFilter === 'function') applyFilter();
            if (typeof markCurrentDatasetActive === 'function') markCurrentDatasetActive();
        }
        setTimeout(function() {
            window.scrollTo({
                top: banner.getBoundingClientRect().top + window.scrollY - 100,
                behavior: 'smooth'
            });
        }, 200);
    } else {
        /* Scroll đến banner */
        var y = banner.getBoundingClientRect().top + window.scrollY - 100;
        window.scrollTo({ top: y, behavior: 'smooth' });
    }

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

        var _origIntApp = window.initApp;
        window.initApp = function() {
            _origIntApp.apply(this, arguments);
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
