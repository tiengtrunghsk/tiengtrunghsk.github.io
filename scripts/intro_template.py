# -*- coding: utf-8 -*-
"""
Intro Template — Giới thiệu tính năng Luyện tập Full Modal.

Cung cấp 3 hàm:
  - build_intro_css()   → CSS cho intro modal + quick banner (marquee)
  - build_intro_html()  → HTML cho intro modal + quick banner (marquee)
  - build_intro_js()    → JS điều khiển intro modal + quick banner

Banner trên trang chủ: chữ chạy ngang như quảng cáo (marquee),
nhấn mạnh chế độ Luyện tập + HSK 1-9.
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
}
@keyframes qibSlideDown {
    from { opacity: 0; transform: translateY(-12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.quick-intro-banner.dismissed { display: none !important; }

/* Icon bên trái */
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

/* Khung marquee — overflow hidden, mask 2 đầu */
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

/* Track chạy — chứa 2 bản sao nội dung để loop mượt */
.qib-track {
    display: inline-flex;
    align-items: center;
    height: 100%;
    white-space: nowrap;
    animation: qibScroll 45s linear infinite;
    will-change: transform;
}
@keyframes qibScroll {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}

/* Từng item trong track */
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

/* Nút bên phải */
.qib-actions {
    display: flex;
    align-items: center;
    gap: .35rem;
    flex-shrink: 0;
    position: relative;
    z-index: 2;
}

.qib-btn {
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    padding: .4rem .8rem;
    border-radius: 50px;
    border: none;
    font-size: .74rem;
    font-weight: 800;
    cursor: pointer;
    font-family: inherit;
    transition: all .2s cubic-bezier(.34, 1.56, .64, 1);
    white-space: nowrap;
    line-height: 1;
}
.qib-btn-primary {
    background: linear-gradient(135deg, #4f46e5, #7c3aed 50%, #a855f7);
    color: #fff;
    box-shadow: 0 3px 10px rgba(124, 58, 237, .3);
}
.qib-btn-primary:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 6px 16px rgba(124, 58, 237, .5);
}
.qib-btn-primary i { font-size: .78rem; }

.qib-btn-ghost {
    width: 28px;
    height: 28px;
    padding: 0;
    background: var(--surface);
    color: var(--text-3);
    border: 1px solid var(--border);
    justify-content: center;
}
.qib-btn-ghost:hover {
    background: var(--danger-light);
    color: var(--danger);
    border-color: var(--danger);
    transform: rotate(90deg);
}

/* Pause khi hover */
.qib-marquee:hover .qib-track {
    animation-play-state: paused;
}

/* ─── Mobile ─── */
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
    .qib-btn-primary {
        padding: .35rem .65rem;
        font-size: .68rem;
    }
    .qib-btn-primary span { display: none; }
    .qib-btn-primary::after {
        content: 'Xem';
        margin-left: 0;
    }
    .qib-btn-ghost {
        width: 26px;
        height: 26px;
    }
}

/* ═══════════════════════════════════════════════════════════════ */
/* INTRO MODAL — 1 trang giới thiệu Luyện tập Full Modal          */
/* ═══════════════════════════════════════════════════════════════ */
.intro-modal {
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, .82);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    z-index: 6000;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    animation: introFadeIn .25s ease;
}
.intro-modal.show { display: flex; }
@keyframes introFadeIn { from { opacity: 0; } to { opacity: 1; } }

.intro-box {
    background: var(--surface);
    border-radius: 20px;
    width: 100%;
    max-width: 640px;
    max-height: min(90vh, 720px);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
    box-shadow: 0 20px 60px rgba(0, 0, 0, .4);
    animation: introSlideUp .35s cubic-bezier(.34, 1.56, .64, 1);
}
@keyframes introSlideUp {
    from { transform: translateY(30px) scale(.96); opacity: 0; }
    to   { transform: translateY(0) scale(1);      opacity: 1; }
}

.intro-close {
    position: absolute;
    top: 12px;
    right: 12px;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    border: none;
    background: rgba(241, 245, 249, .9);
    color: #475569;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: .9rem;
    z-index: 20;
    transition: .15s;
    font-family: inherit;
}
.intro-close:hover {
    background: var(--danger);
    color: #fff;
    transform: scale(1.08) rotate(90deg);
}
[data-theme="dark"] .intro-close {
    background: rgba(30, 41, 59, .9);
    color: #cbd5e1;
}

.intro-body {
    padding: 2rem 1.75rem 1.5rem;
    overflow-y: auto;
    flex: 1 1 auto;
    min-height: 0;
    -webkit-overflow-scrolling: touch;
}

/* ─── Header ─── */
.intro-header {
    text-align: center;
    margin-bottom: 1.5rem;
}
.intro-header-icon {
    width: 64px;
    height: 64px;
    margin: 0 auto .85rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed 50%, #a855f7);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
    box-shadow: 0 8px 24px rgba(124, 58, 237, .4);
}
.intro-header-title {
    font-size: 1.35rem;
    font-weight: 900;
    color: var(--text);
    letter-spacing: -.02em;
    margin-bottom: .35rem;
    line-height: 1.2;
}
.intro-header-subtitle {
    font-size: .85rem;
    color: var(--text-2);
    line-height: 1.5;
    max-width: 480px;
    margin: 0 auto;
}

/* ─── Mock preview ─── */
.intro-preview {
    margin: 1.25rem 0;
    padding: 1rem;
    background: var(--surface-2);
    border: 1.5px solid var(--border);
    border-radius: 14px;
    display: flex;
    flex-direction: column;
    gap: .75rem;
}

.intro-preview-row {
    display: flex;
    align-items: center;
    gap: .6rem;
    flex-wrap: wrap;
}

.intro-preview-label {
    font-size: .68rem;
    font-weight: 800;
    color: var(--text-3);
    text-transform: uppercase;
    letter-spacing: .4px;
    flex-shrink: 0;
    min-width: 80px;
}

.intro-preview-box {
    flex: 1;
    min-width: 0;
    padding: .55rem .75rem;
    border-radius: 10px;
    background: var(--surface);
    border: 1px dashed var(--border);
    display: flex;
    flex-wrap: wrap;
    gap: .35rem;
    align-items: center;
    justify-content: center;
    min-height: 44px;
}

.intro-chip {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: 1rem;
    font-weight: 600;
    padding: .35rem .6rem;
    border-radius: 8px;
    background: var(--surface);
    border: 1.5px solid var(--border);
    color: var(--text);
    line-height: 1;
}
.intro-chip.active {
    background: var(--primary-light, #dbeafe);
    border-color: var(--primary, #2563eb);
    color: var(--primary-dark, #1e40af);
}

.intro-chip.placeholder {
    background: transparent;
    border: 1px dashed var(--border-strong);
    color: var(--text-3);
    font-family: inherit;
    font-size: .75rem;
    font-style: italic;
    font-weight: 500;
}

.intro-chip-info {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: .9rem;
    font-weight: 900;
    padding: .35rem .6rem;
    border-radius: 8px;
    background: var(--primary-light, #dbeafe);
    border: 2px solid var(--primary, #2563eb);
    color: var(--primary-dark, #1e40af);
    display: inline-flex;
    align-items: center;
    gap: .3rem;
    line-height: 1;
}
.intro-chip-info::after {
    content: '\f0eb';
    font-family: 'Font Awesome 6 Free', 'Font Awesome 5 Free';
    font-weight: 900;
    font-size: .75em;
    color: var(--primary, #2563eb);
}

.intro-chip-example {
    font-family: var(--font-zh, 'PingFang SC', sans-serif);
    font-size: .8rem;
    font-weight: 500;
    padding: .3rem .55rem;
    border-radius: 8px;
    background: transparent;
    border: 1.5px solid transparent;
    color: var(--text-2);
    display: inline-flex;
    align-items: center;
    gap: .25rem;
    line-height: 1;
}
.intro-chip-example::after {
    content: '\f028';
    font-family: 'Font Awesome 6 Free', 'Font Awesome 5 Free';
    font-weight: 900;
    font-size: .7em;
    color: var(--text-3);
}

.intro-arrow-down {
    text-align: center;
    color: var(--text-3);
    font-size: .85rem;
    margin: -.3rem 0;
}

/* ─── Features list ─── */
.intro-features {
    display: flex;
    flex-direction: column;
    gap: .55rem;
    margin-bottom: 1.25rem;
}
.intro-feature {
    display: flex;
    align-items: flex-start;
    gap: .65rem;
    padding: .6rem .75rem;
    border-radius: 10px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    transition: all .2s ease;
}
.intro-feature:hover {
    border-color: rgba(139, 92, 246, .4);
    transform: translateX(3px);
}
.intro-feature-icon {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: .8rem;
    flex-shrink: 0;
}
.intro-feature-icon.green {
    background: linear-gradient(135deg, #10b981, #059669);
}
.intro-feature-icon.amber {
    background: linear-gradient(135deg, #f59e0b, #d97706);
}
.intro-feature-icon.pink {
    background: linear-gradient(135deg, #ec4899, #db2777);
}
.intro-feature-text {
    flex: 1;
    min-width: 0;
    font-size: .82rem;
    color: var(--text-2);
    line-height: 1.5;
}
.intro-feature-text b {
    color: var(--text);
    font-weight: 800;
}

/* ─── Footer CTA ─── */
.intro-footer-actions {
    display: flex;
    gap: .6rem;
    justify-content: flex-end;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
    flex-wrap: wrap;
}

.intro-btn {
    padding: .65rem 1.25rem;
    border-radius: 50px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text-2);
    font-size: .82rem;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    transition: all .2s ease;
    white-space: nowrap;
}
.intro-btn:hover {
    background: var(--surface-2);
    border-color: var(--border-strong);
    color: var(--text);
}

.intro-btn.primary {
    background: linear-gradient(135deg, #4f46e5, #7c3aed 50%, #a855f7);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 14px rgba(124, 58, 237, .35);
}
.intro-btn.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(124, 58, 237, .55);
}

/* ─── Mobile ─── */
@media (max-width: 500px) {
    .intro-modal { padding: .5rem; align-items: flex-end; }
    .intro-box {
        max-width: 100%;
        max-height: 92vh;
        border-radius: 20px 20px 0 0;
    }
    .intro-body { padding: 1.5rem 1.15rem 1.15rem; }
    .intro-header-icon { width: 54px; height: 54px; font-size: 1.35rem; border-radius: 15px; }
    .intro-header-title { font-size: 1.1rem; }
    .intro-header-subtitle { font-size: .78rem; }
    .intro-preview { padding: .8rem; }
    .intro-preview-label { min-width: 70px; font-size: .62rem; }
    .intro-chip { font-size: .9rem; padding: .3rem .5rem; }
    .intro-chip-info { font-size: .82rem; }
    .intro-chip-example { font-size: .72rem; }
    .intro-feature-text { font-size: .76rem; }
    .intro-footer-actions { flex-direction: column-reverse; }
    .intro-btn { width: 100%; justify-content: center; }
}
"""


# ═══════════════════════════════════════════════════════════════════
#  HTML
# ═══════════════════════════════════════════════════════════════════
def build_intro_html():
    return r"""
<!-- ═══════════════════════════════════════════════════════════ -->
<!-- QUICK INTRO BANNER — Marquee chạy chữ quảng cáo              -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="quick-intro-banner" id="quickIntroBanner">
    <div class="qib-icon">
        <i class="fas fa-bullhorn"></i>
    </div>

    <div class="qib-marquee">
        <div class="qib-track">
            <!-- BẢN 1 -->
            <span class="qib-item sep">
                <i class="fas fa-bolt"></i>
                <b>LUYỆN TẬP</b> toàn màn hình · tập trung tối đa
            </span>
            <span class="qib-item sep">
                <i class="fas fa-check-double"></i>
                Chấm điểm tự động <b>từng ký tự</b> · sai đâu sửa đó
            </span>
            <span class="qib-item sep">
                <i class="fas fa-graduation-cap"></i>
                Đầy đủ <b>HSK 1 → HSK 9</b> · phân loại theo chủ đề
            </span>
            <span class="qib-item sep">
                <i class="fas fa-puzzle-piece"></i>
                Ghép từ thông minh · tự xáo trộn sau <b>12 giây</b>
            </span>
            <span class="qib-item sep">
                <i class="fas fa-lightbulb"></i>
                Gợi ý từ vựng · pinyin · câu ví dụ
            </span>
            <span class="qib-item sep">
                <i class="fas fa-pen-fancy"></i>
                Luyện viết chữ Hán theo từng nét
            </span>
            <span class="qib-item sep">
                <i class="fas fa-headphones"></i>
                Giọng đọc chuẩn · tốc độ tùy chỉnh
            </span>
            <span class="qib-item sep">
                <i class="fas fa-star"></i>
                Đánh dấu câu yêu thích · ôn lại dễ dàng
            </span>

            <!-- BẢN 2 — copy y nguyên bản 1 để loop liền mạch -->
            <span class="qib-item sep">
                <i class="fas fa-bolt"></i>
                <b>LUYỆN TẬP</b> toàn màn hình · tập trung tối đa
            </span>
            <span class="qib-item sep">
                <i class="fas fa-check-double"></i>
                Chấm điểm tự động <b>từng ký tự</b> · sai đâu sửa đó
            </span>
            <span class="qib-item sep">
                <i class="fas fa-graduation-cap"></i>
                Đầy đủ <b>HSK 1 → HSK 9</b> · phân loại theo chủ đề
            </span>
            <span class="qib-item sep">
                <i class="fas fa-puzzle-piece"></i>
                Ghép từ thông minh · tự xáo trộn sau <b>12 giây</b>
            </span>
            <span class="qib-item sep">
                <i class="fas fa-lightbulb"></i>
                Gợi ý từ vựng · pinyin · câu ví dụ
            </span>
            <span class="qib-item sep">
                <i class="fas fa-pen-fancy"></i>
                Luyện viết chữ Hán theo từng nét
            </span>
            <span class="qib-item sep">
                <i class="fas fa-headphones"></i>
                Giọng đọc chuẩn · tốc độ tùy chỉnh
            </span>
            <span class="qib-item sep">
                <i class="fas fa-star"></i>
                Đánh dấu câu yêu thích · ôn lại dễ dàng
            </span>
        </div>
    </div>

    <div class="qib-actions">
        <button class="qib-btn qib-btn-primary" onclick="openIntroModal()">
            <i class="fas fa-info-circle"></i> <span>Chi tiết</span>
        </button>
        <button class="qib-btn qib-btn-ghost" id="quickIntroDismiss" title="Đóng">
            <i class="fas fa-times"></i>
        </button>
    </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- INTRO MODAL — 1 trang duy nhất                                -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="intro-modal" id="introModal">
    <div class="intro-box">
        <button class="intro-close" id="introClose" aria-label="Đóng">
            <i class="fas fa-times"></i>
        </button>

        <div class="intro-body">
            <!-- ═══ HEADER ═══ -->
            <div class="intro-header">
                <div class="intro-header-icon">
                    <i class="fas fa-expand"></i>
                </div>
                <h2 class="intro-header-title">Luyện tập Full Modal</h2>
                <p class="intro-header-subtitle">
                    Chế độ luyện tập toàn màn hình — tập trung tối đa, chấm điểm tự động từng ký tự.
                </p>
            </div>

            <!-- ═══ MOCK PREVIEW ═══ -->
            <div class="intro-preview">
                <div class="intro-preview-row">
                    <span class="intro-preview-label">Câu hỏi</span>
                    <div class="intro-preview-box" style="justify-content:flex-start;">
                        <span class="intro-chip placeholder">Tôi biết lái xe.</span>
                    </div>
                </div>

                <div class="intro-arrow-down"><i class="fas fa-arrow-down"></i></div>

                <div class="intro-preview-row">
                    <span class="intro-preview-label">Gợi ý</span>
                    <div class="intro-preview-box">
                        <span class="intro-chip-info">会</span>
                        <span class="intro-chip-example">我会开车。</span>
                    </div>
                </div>

                <div class="intro-arrow-down"><i class="fas fa-arrow-down"></i></div>

                <div class="intro-preview-row">
                    <span class="intro-preview-label">Ghép câu</span>
                    <div class="intro-preview-box">
                        <span class="intro-chip active">我</span>
                        <span class="intro-chip active">会</span>
                        <span class="intro-chip active">开</span>
                        <span class="intro-chip active">车</span>
                    </div>
                </div>
            </div>

            <!-- ═══ FEATURES ═══ -->
            <div class="intro-features">
                <div class="intro-feature">
                    <div class="intro-feature-icon"><i class="fas fa-check-double"></i></div>
                    <div class="intro-feature-text">
                        <b>Chấm điểm tự động</b> — gõ câu tiếng Trung, hệ thống so khớp từng ký tự.
                    </div>
                </div>
                <div class="intro-feature">
                    <div class="intro-feature-icon green"><i class="fas fa-lightbulb"></i></div>
                    <div class="intro-feature-text">
                        <b>Gợi ý thông minh</b> — bấm 💡 để xem từ vựng, pinyin, câu ví dụ.
                    </div>
                </div>
                <div class="intro-feature">
                    <div class="intro-feature-icon amber"><i class="fas fa-puzzle-piece"></i></div>
                    <div class="intro-feature-text">
                        <b>Chế độ Ghép từ</b> — bấm từng từ để ghép câu, tự động xáo trộn sau 12 giây.
                    </div>
                </div>
                <div class="intro-feature">
                    <div class="intro-feature-icon pink"><i class="fas fa-pen-fancy"></i></div>
                    <div class="intro-feature-text">
                        <b>Luyện viết chữ Hán</b> — xem nét viết hoặc tự viết theo hướng dẫn.
                    </div>
                </div>
            </div>

            <!-- ═══ FOOTER ═══ -->
            <div class="intro-footer-actions">
                <button class="intro-btn" onclick="closeIntroModal()">
                    <i class="fas fa-times"></i> Đóng
                </button>
                <button class="intro-btn primary" onclick="handleIntroStart()">
                    <i class="fas fa-rocket"></i> Bắt đầu học
                </button>
            </div>
        </div>
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

    if (dismiss) {
        dismiss.addEventListener('click', function() {
            banner.classList.add('dismissed');
            try { localStorage.setItem('quick_intro_dismissed', '1'); } catch(e) {}
        });
    }

    /* ⭐ Auto-tính tốc độ marquee dựa trên chiều rộng track */
    var track = banner.querySelector('.qib-track');
    if (track) {
        var updateSpeed = function() {
            var w = track.scrollWidth / 2;   /* chỉ đo bản 1 */
            if (w <= 0) return;
            var pxPerSec = 60;                /* 60px/s — đổi tùy ý */
            var dur = w / pxPerSec;
            track.style.animationDuration = dur + 's';
        };
        setTimeout(updateSpeed, 100);
        setTimeout(updateSpeed, 800);   /* retry sau khi FA load xong */
        window.addEventListener('resize', updateSpeed);
    }
}

function resetQuickIntroBanner() {
    try { localStorage.removeItem('quick_intro_dismissed'); } catch(e) {}
    var banner = $('quickIntroBanner');
    if (banner) banner.classList.remove('dismissed');
}

/* ═══════════════════════════════════════════════════════════════ */
/* INTRO MODAL — 1 trang duy nhất                                  */
/* ═══════════════════════════════════════════════════════════════ */
window.openIntroModal = function() {
    var modal = $('introModal');
    if (!modal) return;
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
};

window.closeIntroModal = function() {
    var modal = $('introModal');
    if (!modal) return;
    modal.classList.remove('show');
    document.body.style.overflow = '';
};

window.handleIntroStart = function() {
    closeIntroModal();
};

function initIntroModal() {
    var btn = $('introBtn');
    var modal = $('introModal');
    var closeBtn = $('introClose');

    if (btn && !btn.__introBound) {
        btn.__introBound = true;
        btn.addEventListener('click', openIntroModal);
    }
    if (closeBtn && !closeBtn.__introBound) {
        closeBtn.__introBound = true;
        closeBtn.addEventListener('click', closeIntroModal);
    }

    if (modal && !modal.__introBound) {
        modal.__introBound = true;
        modal.addEventListener('click', function(e) {
            if (e.target === modal) closeIntroModal();
        });
    }

    if (!document.__introEscBound) {
        document.__introEscBound = true;
        document.addEventListener('keydown', function(e) {
            if (!modal || !modal.classList.contains('show')) return;
            if (e.key === 'Escape') closeIntroModal();
        });
    }
}

function maybeAutoOpenIntro() {
    try {
        var seen = localStorage.getItem('intro_seen');
        if (seen === '1') return;
        var isGuest = !(typeof currentUser !== 'undefined' && currentUser);
        if (!isGuest) return;
        setTimeout(function() {
            openIntroModal();
            try { localStorage.setItem('intro_seen', '1'); } catch(e) {}
        }, 1500);
    } catch(e) {}
}

/* Hook vào initApp */
(function() {
    function wrapInitApp() {
        if (typeof window.initApp !== 'function') return false;
        if (window.initApp.__introHooked) return true;

        var _origInitApp = window.initApp;
        window.initApp = function() {
            _origInitApp.apply(this, arguments);
            initIntroModal();
            initQuickIntroBanner();
            maybeAutoOpenIntro();
        };
        window.initApp.__introHooked = true;
        return true;
    }

    if (!wrapInitApp()) {
        /* Nếu initApp chưa được định nghĩa — retry */
        var tries = 0;
        var iv = setInterval(function() {
            tries++;
            if (wrapInitApp() || tries > 20) clearInterval(iv);
        }, 100);
    }
})();
"""
