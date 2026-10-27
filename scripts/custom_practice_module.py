# -*- coding: utf-8 -*-
r"""
custom_practice_module.py - Tích hợp Modal Popup cảnh báo lỗi chính tả trực quan & Trợ lý dịch thuật
"""

def build_custom_practice_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KHU VỰC LUYỆN TẬP TỰ DO - MODERN GLASSMORPHIC UI           */
/* ═══════════════════════════════════════════════════════════ */
.cp-card {
    background: linear-gradient(145deg, var(--surface, #ffffff), var(--surface-2, #f8fafc));
    border: 1px solid rgba(124, 58, 237, 0.15);
    border-radius: 24px;
    padding: 1.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 16px 40px -12px rgba(124, 58, 237, 0.12), 0 0 0 1px rgba(255, 255, 255, 0.8) inset;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    position: relative;
    overflow: hidden;
}
.cp-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 5px;
    background: linear-gradient(90deg, #4f46e5, #7c3aed, #ec4899);
}
.cp-header-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
}
.cp-section-header {
    display: flex;
    align-items: center;
    gap: 12px;
}
.cp-icon-badge {
    color: #fff;
    font-size: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 14px;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    box-shadow: 0 6px 16px rgba(168, 85, 247, 0.35);
}
.cp-title-group h3 {
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text, #1e1b4b);
    margin: 0;
}
.cp-title-group p {
    font-size: 0.8rem;
    color: var(--text-3, #64748b);
    margin: 2px 0 0 0;
}

.cp-token-badge {
    display: flex; align-items: center; gap: 6px;
    background: rgba(16, 185, 129, 0.1); color: #059669;
    padding: 4px 12px; border-radius: 50px;
    font-size: 0.75rem; font-weight: 800;
    border: 1px solid rgba(16, 185, 129, 0.2);
    transition: all 0.3s;
    cursor: pointer;
}
.cp-token-badge.warn { background: rgba(245, 158, 11, 0.1); color: #d97706; border-color: rgba(245, 158, 11, 0.2); }
.cp-token-badge.danger { background: rgba(220, 38, 38, 0.1); color: #dc2626; border-color: rgba(220, 38, 38, 0.2); }

.cp-token-badge.cooldown {
    background: rgba(100, 116, 139, 0.15) !important;
    color: #64748b !important;
    border-color: rgba(100, 116, 139, 0.3) !important;
    cursor: not-allowed !important;
}

.cp-btn-reset {
    padding: 0.45rem 0.9rem;
    border-radius: 50px;
    border: 1px solid var(--border, #e2e8f0);
    background: var(--surface, #ffffff);
    color: var(--text-3, #64748b);
    font-size: 0.75rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
}
.cp-btn-reset:hover { background: #fee2e2; color: #ef4444; border-color: #fca5a5; }

.cp-switch-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--surface-2, #f1f5f9);
    padding: 6px;
    border-radius: 16px;
    border: 1px solid var(--border, #e2e8f0);
    cursor: pointer;
    user-select: none;
    width: 100%;
    max-width: 320px;
    margin: 0 auto;
}
.cp-switch-label {
    flex: 1;
    text-align: center;
    padding: 8px;
    font-weight: 700;
    font-size: 0.85rem;
    color: var(--text-3, #64748b);
    border-radius: 12px;
    transition: all 0.3s ease;
}
.cp-switch-label.active {
    background: var(--surface, #ffffff);
    color: #7c3aed;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.cp-switch-icon-box {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 6px;
    transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.cp-switch-container:hover .cp-switch-icon-box {
    transform: rotate(180deg);
}

.cp-textarea {
    width: 100%;
    padding: 1.25rem;
    border-radius: 16px;
    border: 1.5px solid var(--border, #e2e8f0);
    background: var(--surface, #ffffff);
    color: var(--text, #1e1b4b);
    font-family: var(--font-zh, inherit);
    font-size: 1.05rem;
    resize: none;
    min-height: 120px;
    max-height: 400px;
    line-height: 1.6;
    transition: all 0.25s ease;
}
.cp-textarea:focus {
    border-color: #a855f7;
    outline: none;
    box-shadow: 0 0 0 4px rgba(168, 85, 247, 0.15);
}

.cp-spell-container {
    display: none;
    flex-direction: column;
    gap: 0.5rem;
    background: rgba(245, 158, 11, 0.08);
    border: 1px solid rgba(245, 158, 11, 0.3);
    padding: 0.75rem 1rem;
    border-radius: 12px;
    font-size: 0.85rem;
    color: #92400e;
    margin-top: 6px;
    animation: fadeIn 0.3s ease;
}
.cp-spell-container.show { display: flex; }
.cp-spell-header {
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
}
.cp-spell-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}
.cp-spell-chip {
    background: #ffffff;
    border: 1px solid #f59e0b;
    color: #b45309;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 0.8rem;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.cp-modal-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(4px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    animation: fadeIn 0.2s ease;
}
.cp-modal-overlay.show { display: flex; }
.cp-modal-box {
    background: var(--surface, #ffffff);
    border: 1px solid rgba(245, 158, 11, 0.4);
    border-radius: 20px;
    padding: 1.5rem;
    width: 90%;
    max-width: 400px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    display: flex;
    flex-direction: column;
    gap: 1rem;
    text-align: center;
}
.cp-modal-icon {
    font-size: 2.5rem;
    color: #f59e0b;
}
.cp-modal-title {
    font-size: 1.1rem;
    font-weight: 800;
    color: var(--text, #1e1b4b);
    margin: 0;
}
.cp-modal-desc {
    font-size: 0.85rem;
    color: var(--text-3, #64748b);
    line-height: 1.5;
    margin: 0;
}
.cp-modal-words {
    background: rgba(245, 158, 11, 0.1);
    color: #d97706;
    padding: 8px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.95rem;
    word-break: break-all;
}
.cp-modal-actions {
    display: flex;
    gap: 10px;
    margin-top: 5px;
}
.cp-modal-btn {
    flex: 1;
    padding: 10px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 0.9rem;
    cursor: pointer;
    border: none;
    transition: all 0.2s;
}
.cp-modal-btn-cancel {
    background: var(--surface-2, #f1f5f9);
    color: var(--text-3, #64748b);
}
.cp-modal-btn-cancel:hover { background: #e2e8f0; }
.cp-modal-btn-proceed {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #fff;
    box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
}
.cp-modal-btn-proceed:hover { opacity: 0.9; }



.cp-btn-buy-token {
    width: 100%;
    height: 52px;
    border-radius: 16px;
    border: 2px dashed #f59e0b;
    background: rgba(245, 158, 11, 0.1);
    color: #d97706;
    font-weight: 800;
    font-size: 1rem;
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    transition: all 0.2s;
}
.cp-btn-buy-token:hover { background: rgba(245, 158, 11, 0.2); }

.cp-progress-wrap {
    display: none;
    flex-direction: column;
    gap: 0.6rem;
    background: var(--surface-2, #f1f5f9);
    padding: 1rem;
    border-radius: 14px;
    border: 1px solid var(--border, #e2e8f0);
}
.cp-progress-wrap.show { display: flex; animation: fadeIn 0.3s ease; }
.cp-progress-bar-bg {
    width: 100%;
    height: 10px;
    background: var(--surface, #ffffff);
    border-radius: 50px;
    overflow: hidden;
}
.cp-progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
    transition: width 0.3s ease;
}
@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }

.cp-history-item {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    transition: all 0.2s;
}
.cp-history-item:hover { border-color: #a855f7; box-shadow: 0 4px 12px rgba(168,85,247,0.1); }
.cp-history-vi { font-size: 0.9rem; color: #1e293b; font-weight: 600; }
.cp-history-zh { font-size: 1.05rem; color: #7c3aed; font-weight: 700; }
.cp-history-pinyin { font-size: 0.8rem; color: #64748b; font-style: italic; }
.cp-history-time { font-size: 0.7rem; color: #94a3b8; text-align: right; margin-top: 4px; }

@media (min-width: 768px) {
    .cp-btn-start, .cp-btn-buy-token { width: auto; min-width: 280px; align-self: flex-end; }
}

.cp-btn-reset:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    background: var(--surface-2, #f1f5f9);
    color: #94a3b8;
    border-color: #e2e8f0;
}
.cp-hidden {
    display: none !important;
}
/* ⭐ Phóng to toàn màn hình Textarea */
.cp-input-wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
}
.cp-input-wrapper.fullscreen {
    position: fixed !important;
    inset: 0 !important;
    z-index: 99999 !important;
    background: var(--surface, #ffffff) !important;
    padding: 2rem !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 0.75rem !important;
    box-sizing: border-box !important;
    box-shadow: 0 0 50px rgba(0,0,0,0.5) !important;
    overflow-y: auto !important;
}
.cp-input-wrapper.fullscreen .cp-textarea {
    flex: 1 !important;
    min-height: calc(100vh - 200px) !important;
    max-height: none !important;
    font-size: 1.15rem !important;
}
[data-theme="dark"] .cp-input-wrapper.fullscreen {
    background: var(--surface-2, #1e1b4b) !important;
}

/* ⭐ CSS Modal Cắt Ảnh (Crop) */
.cp-crop-container {
    max-width: 90% !important;
    width: 600px !important;
    text-align: left !important;
}
.cp-crop-img-wrap {
    max-height: 50vh;
    background: #0f172a;
    border-radius: 12px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}
.cp-crop-img-wrap img {
    max-width: 100%;
    display: block;
}

/* ═══════════════════════════════════════════════════════════ */
/* TỐI ƯU GIAO DIỆN HEADER & TOOLBAR                         */
/* ═══════════════════════════════════════════════════════════ */
.cp-header-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    width: 100%;
    margin-bottom: 10px;
}

.cp-header-top {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 100%;
    min-width: 0;
}

.cp-title-group {
    min-width: 0; 
    flex: 1; 
}

.cp-title-group h3 {
    font-size: 1.15rem;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.cp-title-group p {
    font-size: 0.8rem;
    margin: 2px 0 0 0;
    color: #64748b;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.cp-header-actions {
    display: flex;
    align-items: center;
    gap: 8px;
}

/* ⭐ THANH CÔNG CỤ NHẬP LIỆU (TỐI GIẢN) */
.cp-input-toolbar {
    display: flex;
    justify-content: flex-end; /* Dồn tất cả sang phải */
    align-items: center;
    margin-bottom: 6px;
    gap: 6px;
}

.cp-input-tools-right {
    display: flex;
    gap: 6px;
    align-items: center;
}

/* Nút chuyển đổi ngôn ngữ nhỏ gọn */
.cp-switch-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 30px;
    height: 30px;
    border-radius: 8px;
    border: 1px solid var(--border, #e2e8f0);
    background: var(--surface, #ffffff);
    color: var(--text-3, #64748b);
    cursor: pointer;
    transition: all 0.2s;
    padding: 0;
}
.cp-switch-btn:hover {
    background: var(--primary-light, #ede9fe);
    color: var(--primary, #7c3aed);
    border-color: var(--primary, #7c3aed);
}
.cp-switch-btn.active {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    border-color: transparent;
}

/* Ẩn cụm switch to cũ */
.cp-switch-container {
    display: none !important;
}

.cp-action-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 10px;
    border: 1px solid var(--border, #e2e8f0);
    background: var(--surface, #ffffff);
    color: var(--text-2, #475569);
    font-size: 0.8rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
}
.cp-action-btn i { font-size: 0.9rem; }
.cp-action-btn.cp-btn-primary {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    border: none;
    box-shadow: 0 2px 8px rgba(124, 58, 237, 0.3);
}
.cp-action-btn.cp-btn-primary:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
}

.cp-action-btn span {
    display: inline-block;
}

.cp-token-badge {
    padding: 4px 10px;
    font-size: 0.75rem;
    border-radius: 8px;
    background: rgba(16, 185, 129, 0.1); 
    color: #059669;
    border: 1px solid rgba(16, 185, 129, 0.2);
    white-space: nowrap;
}

@media (max-width: 600px) {
    .cp-header-container {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
    }
    .cp-header-top {
        justify-content: space-between;
        width: 100%;
    }
    .cp-header-actions {
        justify-content: space-between;
        width: 100%;
    }
    .cp-action-btn { flex: 1; }
    .cp-token-badge { flex: 1; justify-content: center; }
    .cp-action-btn { padding: 8px 10px; }
}

.cp-textarea-wrapper {
    position: relative;
    display: flex;
    width: 100%;
}

.cp-textarea-wrapper .cp-textarea {
    width: 100%;
    padding-right: 55px;
}

.cp-btn-start-icon {
    position: absolute;
    bottom: 12px;
    right: 12px;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: none;
    background: linear-gradient(135deg, #4f46e5, #7c3aed, #ec4899);
    color: #fff;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
    transition: all 0.2s ease;
    z-index: 10;
}

.cp-btn-start-icon:hover:not(:disabled) {
    transform: scale(1.08);
    box-shadow: 0 6px 16px rgba(124, 58, 237, 0.6);
}

.cp-btn-start-icon:disabled {
    background: #cbd5e1;
    cursor: not-allowed;
    box-shadow: none;
    opacity: 0.7;
}

.cp-btn-start {
    display: none !important;
}
"""

def build_custom_practice_html():
    return r"""
<div class="cp-card" id="cpSection">
    <!-- HEADER -->
    <div class="cp-header-container">
        <div class="cp-header-top">
            <div class="cp-section-header">
                <div class="cp-icon-badge" style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4);">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="cp-title-group">
                    <h3>Trợ Lý Dịch Thuật</h3>
                    <p>Dịch và tạo bài tập cá nhân hóa</p>
                </div>
            </div>
            <div class="cp-token-badge" id="cpTokenBadge" title="Bấm để cập nhật số Token mới nhất">
                <i class="fas fa-bolt"></i> <span id="cpTokenText">Đang tải...</span>
            </div>
        </div>
    </div>

    <!-- Các nút thao tác chính (Ảnh & Lịch sử) -->
    <div class="cp-header-actions" style="margin-bottom: 10px;">
        <button class="cp-action-btn cp-btn-primary" id="cpUploadImgBtn" type="button" title="Dịch từ ảnh">
            <i class="fas fa-camera"></i> <span>Dịch Ảnh</span>
        </button>
        <input type="file" id="cpImageInput" accept="image/*" style="display:none;">
        
        <button class="cp-action-btn" id="cpHistoryBtn" type="button" title="Xem lịch sử">
            <i class="fas fa-clock-rotate-left"></i> <span>Lịch sử</span>
        </button>
    </div>

    <!-- Vùng nhập văn bản -->
    <div class="cp-input-wrapper" id="cpInputWrapper">
        <!-- Thanh công cụ: Switch nhỏ + Phóng to + Xóa -->
        <div class="cp-input-toolbar">
            <div class="cp-input-tools-right">
                <button type="button" id="cpSwitchBtn" class="cp-switch-btn" title="Đảo chiều dịch">
                    <i class="fas fa-exchange-alt"></i>
                </button>
                
                <button type="button" id="cpExpandBtn" class="cp-btn-reset" style="padding: 4px 10px; font-size: 0.75rem; display: flex; align-items: center; gap: 4px; border-radius: 8px;" title="Phóng to toàn màn hình">
                    <i class="fas fa-expand" id="cpExpandIcon"></i> <span id="cpExpandText">Phóng to</span>
                </button>
                
                <button class="cp-btn-reset" id="cpResetBtn" type="button" title="Làm mới" style="padding: 4px 10px; font-size: 0.75rem; display: flex; align-items: center; gap: 4px; border-radius: 8px;">
                    <i class="fas fa-rotate-right"></i> <span>Xóa</span>
                </button>
                <button class="cp-btn-reset cp-btn-reset-mobile" id="cpResetBtnMobile" type="button" title="Làm mới" style="padding: 4px 10px; font-size: 0.75rem; display: none; align-items: center; gap: 4px; border-radius: 8px;">
                    <i class="fas fa-rotate-right"></i> <span>Xóa</span>
                </button>
            </div>
        </div>
        
        <div class="cp-textarea-wrapper">
            <textarea class="cp-textarea" id="cpInputZh" rows="4" placeholder="Nhập hoặc dán văn bản để Trợ lý dịch giúp bạn..."></textarea>
            
            <button class="cp-btn-start-icon" id="cpStartBtn" type="button" title="Bắt đầu luyện tập">
                <i class="fas fa-arrow-right"></i>
            </button>
        </div>
        
        <button class="cp-btn-buy-token" id="cpBuyTokenBtn" type="button" style="margin-top: 10px;">
            <i class="fas fa-shopping-cart"></i> Mua thêm Token
        </button>

        <div class="cp-spell-container" id="cpSpellContainer">
            <div class="cp-spell-header">
                <i class="fas fa-triangle-exclamation"></i> Phát hiện từ nghi ngờ sai chính tả / dính phím:
            </div>
            <div class="cp-spell-chips" id="cpSpellChips"></div>
        </div>
        <div class="cp-char-count" id="cpCharCount" style="text-align:right;font-size:.75rem;font-weight:600;color:#64748b;margin-top:4px;">0 / 5000</div>
    </div>

    <!-- Thanh tiến trình -->
    <div class="cp-progress-wrap" id="cpProgressWrap">
        <div class="cp-progress-text" id="cpProgressText" style="text-align:center;font-size:.8rem;font-weight:700;">Đang xử lý...</div>
        <div class="cp-progress-bar-bg"><div class="cp-progress-bar" id="cpProgressBar"></div></div>
    </div>
</div>

<!-- MODAL CẢNH BÁO CHÍNH TẢ -->
<div class="cp-modal-overlay" id="cpModalOverlay">
    <div class="cp-modal-box">
        <div class="cp-modal-icon"><i class="fas fa-triangle-exclamation"></i></div>
        <h4 class="cp-modal-title">Phát hiện từ nghi ngờ sai chính tả!</h4>
        <p class="cp-modal-desc">Hệ thống phát hiện các từ sau có dấu hiệu gõ nhầm hoặc dính phím:</p>
        <div class="cp-modal-words" id="cpModalWordsList"></div>
        <p class="cp-modal-desc" style="font-size:0.75rem;">Tiếp tục dịch có thể làm tốn Quota và kết quả không chuẩn xác.</p>
        <div class="cp-modal-actions">
            <button class="cp-modal-btn cp-modal-btn-cancel" id="cpModalFixBtn" type="button">Sửa lại văn bản</button>
            <button class="cp-modal-btn cp-modal-btn-proceed" id="cpModalProceedBtn" type="button">Vẫn tiếp tục dịch</button>
        </div>
    </div>
</div>

<!-- MODAL LỊCH SỬ DỊCH -->
<div class="cp-modal-overlay" id="cpHistoryOverlay">
    <div class="cp-modal-box" style="max-width: 600px; text-align: left;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1px solid #eee; padding-bottom: 10px;">
            <div>
                <h4 class="cp-modal-title" style="font-size: 1.1rem; color: #1e1b4b; margin:0;"><i class="fas fa-history"></i> Lịch sử dịch gần đây</h4>
                <div id="cpHistoryCounter" style="font-size: 0.75rem; color: #64748b; margin-top: 2px; font-weight: 600;">Đang tải bộ đếm...</div>
            </div>
            <div style="display:flex; gap:6px; align-items:center;">
                <button id="cpSelectAllHistoryBtn" style="background:linear-gradient(135deg,#4f46e5,#7c3aed); color:#fff; border:none; padding:5px 10px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer;" title="Chọn tất cả ra luyện tập">
                    <i class="fas fa-check-double"></i> Chọn tất cả
                </button>
                <button id="cpDeleteAllHistoryBtn" style="background:#fee2e2; color:#ef4444; border:1px solid #fca5a5; padding:5px 10px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer;" title="Xóa tất cả lịch sử">
                    <i class="fas fa-trash-alt"></i> Xóa tất cả
                </button>
                <button id="cpHistoryCloseBtn" style="background:none; border:none; font-size:1.2rem; cursor:pointer; color:#64748b;"><i class="fas fa-times"></i></button>
            </div>
        </div>
        <div id="cpHistoryList" style="max-height: 400px; overflow-y: auto; margin-top: 10px; display: flex; flex-direction: column; gap: 10px;"></div>
    </div>
</div>

<!-- MODAL CẮT ẢNH (CROPPER) -->
<div class="cp-modal-overlay" id="cpCropModalOverlay">
    <div class="cp-modal-box cp-crop-container">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1px solid var(--border, #e2e8f0); padding-bottom: 10px;">
            <h4 class="cp-modal-title" style="font-size: 1.1rem; margin:0;"><i class="fas fa-crop"></i> Cắt sát vùng văn bản</h4>
            <button type="button" id="cpCropCloseBtn" style="background:none; border:none; font-size:1.2rem; cursor:pointer; color:#64748b;"><i class="fas fa-times"></i></button>
        </div>
        <p class="cp-modal-desc" style="margin:0; font-size: 0.8rem;">Kéo các góc để chọn đúng phần chữ cần đọc (giúp tiết kiệm token và tăng độ chính xác):</p>
        <div class="cp-crop-img-wrap">
            <img id="cpImageToCrop" src="" alt="Crop Preview">
        </div>
        <div class="cp-modal-actions" style="margin-top: 5px;">
            <button class="cp-modal-btn cp-modal-btn-cancel" id="cpCropCancelBtn" type="button">Hủy bỏ</button>
            <button class="cp-modal-btn cp-modal-btn-proceed" id="cpCropConfirmBtn" type="button"><i class="fas fa-check"></i> Cắt & Đọc ảnh</button>
        </div>
    </div>
</div>
"""
def build_custom_practice_js():
    return r"""
(function() {
    'use strict';
    var MAX_CHARS = 5000;
    var currentMode = 'vi2zh';
    var SERVER_API_URL = 'https://server-vopb.onrender.com/api/translate'; 

    var selectAllHistoryBtn = document.getElementById('cpSelectAllHistoryBtn');
    var deleteAllHistoryBtn = document.getElementById('cpDeleteAllHistoryBtn');
    var historyCounter = document.getElementById('cpHistoryCounter');

    var inputArea = document.getElementById('cpInputZh');
    var charCount = document.getElementById('cpCharCount');
    var startBtn = document.getElementById('cpStartBtn');
    var buyTokenBtn = document.getElementById('cpBuyTokenBtn');
    var resetBtn = document.getElementById('cpResetBtn');
    var resetBtnMobile = document.getElementById('cpResetBtnMobile');
    var tokenBadge = document.getElementById('cpTokenBadge');
    var tokenText = document.getElementById('cpTokenText');
    
    var switchBtn = document.getElementById('cpSwitchBtn');
    
    var progressWrap = document.getElementById('cpProgressWrap');
    var progressBar = document.getElementById('cpProgressBar');
    var progressText = document.getElementById('cpProgressText');

    var spellContainer = document.getElementById('cpSpellContainer');
    var spellChips = document.getElementById('cpSpellChips');

    var modalOverlay = document.getElementById('cpModalOverlay');
    var modalWordsList = document.getElementById('cpModalWordsList');
    var modalFixBtn = document.getElementById('cpModalFixBtn');
    var modalProceedBtn = document.getElementById('cpModalProceedBtn');

    var historyBtn = document.getElementById('cpHistoryBtn');
    var historyOverlay = document.getElementById('cpHistoryOverlay');
    var historyList = document.getElementById('cpHistoryList');
    var historyCloseBtn = document.getElementById('cpHistoryCloseBtn');

    var myTokensUsed = 0;
    var myTokenQuota = 0;
    var myBonusTokens = 0;
    var currentUser = null;
    var lastDeletedText = '';
    var resolveModalAction = null;
    var cachedHistoryData = [];
    var currentTodayCount = 0;
    var isUserAdmin = false;
    var currentReadRemain = 250;
    
    var TOKEN_REFRESH_COOLDOWN = 60000;
    var lastTokenRefreshTime = 0;
    var isTokenRefreshing = false;
    var cooldownTimerInterval = null;
    
    try {
        var savedTime = parseInt(localStorage.getItem('cp_last_token_refresh') || '0');
        if (savedTime > 0) lastTokenRefreshTime = savedTime;
    } catch(e) {}

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadPinyinPro);
    } else {
        loadPinyinPro();
    }

    var expandBtn = document.getElementById('cpExpandBtn');
    var inputWrapper = document.getElementById('cpInputWrapper');
    var expandIcon = document.getElementById('cpExpandIcon');
    var expandText = document.getElementById('cpExpandText');

    if (expandBtn && inputWrapper) {
        expandBtn.addEventListener('click', function() {
            var isFullscreen = inputWrapper.classList.toggle('fullscreen');
            if (isFullscreen) {
                expandIcon.className = 'fas fa-compress';
                expandText.textContent = 'Thu nhỏ';
                expandBtn.title = 'Thu nhỏ lại';
            } else {
                expandIcon.className = 'fas fa-expand';
                expandText.textContent = 'Phóng to';
                expandBtn.title = 'Phóng to toàn màn hình';
            }
            autoResizeTextarea();
        });
    }

    function checkIsExpired() {
        if (window.APP_TIER === 'expired' || window.APP_TIER === 'expire') return true;
        if (window.isUserExpired === true) return true;
        if (typeof window.isExpired === 'boolean' && window.isExpired) return true;
        
        var expiryBanner = document.getElementById('vocabWarningBanner') || document.querySelector('.vocab-warning-banner.tier-expired');
        if (expiryBanner) return true;

        if (currentUser) {
            if (currentUser.isExpiredOnly === true || currentUser.tier === 'expired' || currentUser.appTier === 'expired' || currentUser.tier === 'expire' || currentUser.appTier === 'expire') return true;
            if (currentUser.expiryDate) {
                var expTime = new Date(currentUser.expiryDate).getTime();
                if (!isNaN(expTime) && expTime < Date.now()) return true;
            }
        }
        return false;
    }

    function updateCooldownUI() {
        if (!tokenText || !tokenBadge) return;
        var now = Date.now();
        var timeSinceLastRefresh = now - lastTokenRefreshTime;
        
        if (lastTokenRefreshTime === 0 || timeSinceLastRefresh >= TOKEN_REFRESH_COOLDOWN) {
            tokenBadge.classList.remove('cooldown');
            tokenBadge.style.cursor = 'pointer';
            if (cooldownTimerInterval) {
                clearInterval(cooldownTimerInterval);
                cooldownTimerInterval = null;
            }
            return;
        }
        
        tokenBadge.classList.add('cooldown');
        tokenBadge.style.cursor = 'not-allowed';
    }

    function startCooldownTimer() {
        if (cooldownTimerInterval) clearInterval(cooldownTimerInterval);
        updateCooldownUI();
        cooldownTimerInterval = setInterval(updateCooldownUI, 1000);
    }

    function initTokenState() {
        var user = null;
        try {
            for (var i = 0; i < localStorage.length; i++) {
                var key = localStorage.key(i);
                if (key && key.indexOf('user_cache_') === 0) {
                    var cached = JSON.parse(localStorage.getItem(key) || 'null');
                    if (cached && cached.data && cached.data.email) {
                        user = cached.data;
                        break;
                    }
                }
            }
        } catch(e) {}

        currentUser = user;
        if (!user) {
            tokenText.textContent = 'Chưa đăng nhập';
            tokenBadge.className = 'cp-token-badge warn';
            startBtn.disabled = true;
            return;
        }

        if (user.role === 'super_admin' || user.isPermanent) {
            tokenText.textContent = 'Không giới hạn';
            tokenBadge.className = 'cp-token-badge';
            return;
        } else {
            var defaultQuota = (user.role === 'admin') ? 20000 : 10000;
            myTokenQuota = user.tokenQuota || defaultQuota;
        }

        myBonusTokens = user.bonusTokens || 0;
        myTokensUsed = user.tokensUsed || 0;

        var isExpired = checkIsExpired();
        renderTokenUI(isExpired);

        try {
            var savedRefreshTime = parseInt(localStorage.getItem('cp_last_token_refresh') || '0');
            if (savedRefreshTime > 0) {
                lastTokenRefreshTime = savedRefreshTime;
                var timePassed = Date.now() - savedRefreshTime;
                if (timePassed < TOKEN_REFRESH_COOLDOWN) {
                    startCooldownTimer();
                } else {
                    lastTokenRefreshTime = 0;
                    try { localStorage.removeItem('cp_last_token_refresh'); } catch(e) {}
                }
            }
        } catch(e) {}
    }

    async function refreshTokenFromFirestore() {
        if (!currentUser || !currentUser.email) return false;
        
        try {
            var res = await fetch(SERVER_API_URL.replace('/translate', '/user/check-token'), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: currentUser.email })
            });
            var json = await res.json();
            
            if (!json.ok) return false;
            
            myTokenQuota = json.quota;
            myBonusTokens = json.bonus;
            myTokensUsed = json.used;
            currentUser.role = json.role;
            
            try {
                var cacheKey = 'user_cache_' + currentUser.email;
                var cached = JSON.parse(localStorage.getItem(cacheKey) || 'null');
                if (cached && cached.data) {
                    cached.data.tokenQuota = json.quota;
                    cached.data.bonusTokens = json.bonus;
                    cached.data.tokensUsed = json.used;
                    cached.data.role = json.role;
                    if (json.lastTokenResetDate) cached.data.lastTokenResetDate = json.lastTokenResetDate;
                    if (json.lastTokenResetMonth) cached.data.lastTokenResetMonth = json.lastTokenResetMonth;
                    localStorage.setItem(cacheKey, JSON.stringify(cached));
                    currentUser = cached.data;
                }
            } catch(e) {}
            
            var isExpired = checkIsExpired();
            renderTokenUI(isExpired);
            return true;
        } catch(e) {
            console.error('Lỗi gọi API check-token:', e);
            return false;
        }
    }

    function renderTokenUI(isExpired) {
        if (!currentUser) {
            tokenText.textContent = 'Chưa đăng nhập';
            tokenBadge.className = 'cp-token-badge warn';
            tokenBadge.style.pointerEvents = 'none'; 
            tokenBadge.style.opacity = '1';
            tokenBadge.title = 'Vui lòng đăng nhập';
            
            startBtn.classList.add('cp-hidden');
            buyTokenBtn.classList.remove('cp-hidden');
            buyTokenBtn.innerHTML = '<i class="fas fa-sign-in-alt"></i> Đăng nhập để sử dụng';
            
            inputArea.disabled = true;
            inputArea.placeholder = 'Vui lòng đăng nhập để sử dụng Trợ lý dịch thuật.';
            
            var historyBtnEl = document.getElementById('cpHistoryBtn');
            if (historyBtnEl) {
                historyBtnEl.disabled = true;
                historyBtnEl.style.opacity = '0.4';
                historyBtnEl.style.cursor = 'not-allowed';
                historyBtnEl.title = 'Vui lòng đăng nhập';
                historyBtnEl.innerHTML = '<i class="fas fa-lock"></i>';
            }
            return;
        }

        if (currentUser.role === 'super_admin' || currentUser.isPermanent) {
            tokenText.textContent = 'Không giới hạn';
            tokenBadge.className = 'cp-token-badge';
            tokenBadge.style.pointerEvents = 'auto';
            tokenBadge.style.opacity = '1';
            tokenBadge.title = 'Bấm để cập nhật số Token mới nhất';
            
            startBtn.classList.remove('cp-hidden');
            buyTokenBtn.classList.add('cp-hidden');
            inputArea.disabled = false;
            return;
        }

        var totalAvailable = myTokenQuota + myBonusTokens;
        var remain = totalAvailable - myTokensUsed;
        if (remain < 0) remain = 0;

        tokenText.textContent = remain.toLocaleString('vi-VN') + ' token';
        tokenBadge.classList.remove('warn', 'danger');
        
        var historyBtnEl = document.getElementById('cpHistoryBtn');
        if (historyBtnEl) {
            if (isExpired) {
                historyBtnEl.disabled = true;
                historyBtnEl.style.opacity = '0.4';
                historyBtnEl.style.cursor = 'not-allowed';
                historyBtnEl.title = 'Tài khoản đã hết hạn - Không thể xem lịch sử';
                historyBtnEl.innerHTML = '<i class="fas fa-lock"></i>';
            } else {
                historyBtnEl.disabled = false;
                historyBtnEl.style.opacity = '1';
                historyBtnEl.style.cursor = 'pointer';
                historyBtnEl.title = 'Xem lịch sử';
                historyBtnEl.innerHTML = '<i class="fas fa-clock-rotate-left"></i>';
            }
        }

        if (isExpired) {
            tokenBadge.classList.add('danger');
            tokenBadge.style.pointerEvents = 'none';
            tokenBadge.style.opacity = '0.6';
            tokenBadge.title = 'Tài khoản đã hết hạn - Không thể làm mới Token';
            
            startBtn.classList.add('cp-hidden');
            buyTokenBtn.classList.remove('cp-hidden');
            buyTokenBtn.innerHTML = '<i class="fas fa-crown"></i> Gia hạn ngay (Giữ nguyên Token)';
            
            inputArea.disabled = true;
            inputArea.placeholder = 'Tài khoản đã hết hạn. Vui lòng gia hạn để tiếp tục sử dụng Luyện tập tự do.';
            return; 
        }

        tokenBadge.style.pointerEvents = 'auto';
        tokenBadge.style.opacity = '1';
        tokenBadge.title = 'Bấm để cập nhật số Token mới nhất';

        if (remain <= 2000) tokenBadge.classList.add('danger');
        else if (remain <= 5000) tokenBadge.classList.add('warn');

        if (remain <= 0) {
            startBtn.classList.add('cp-hidden');
            buyTokenBtn.classList.remove('cp-hidden');
            buyTokenBtn.innerHTML = '<i class="fas fa-shopping-cart"></i> Mua thêm Token';
            
            inputArea.disabled = true;
            inputArea.placeholder = 'Bạn đã hết Token. Vui lòng mua thêm để tiếp tục.';
        } else {
            startBtn.classList.remove('cp-hidden');
            buyTokenBtn.classList.add('cp-hidden');
            
            inputArea.disabled = false;
            inputArea.placeholder = currentMode === 'vi2zh' ? 'Nhập văn bản tiếng Việt vào đây...' : 'Dán văn bản tiếng Trung vào đây...';
        }
    }

    buyTokenBtn.addEventListener('click', async function() {
        if (!currentUser) {
            if (typeof openLoginModal === 'function') openLoginModal();
            else alert('Vui lòng đăng nhập để sử dụng tính năng này!');
            return;
        }

        if (currentUser.role === 'admin') {
            var amountStr = prompt("Nhập số lượng Token bạn muốn nạp (Ví dụ: 5000):", "5000");
            if (amountStr === null) return;
            
            var amount = parseInt(amountStr, 10);
            if (isNaN(amount) || amount <= 0) {
                alert("Số lượng token không hợp lệ!");
                return;
            }

            var password = prompt("Nhập MẬT KHẨU DUYỆT để xác nhận nạp " + amount + " token:");
            if (password === null) return;

            if (!password.trim()) {
                alert("Vui lòng nhập mật khẩu!");
                return;
            }

            var originalText = buyTokenBtn.innerHTML;
            buyTokenBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Đang duyệt...';
            buyTokenBtn.disabled = true;

            try {
                var apiUrl = SERVER_API_URL.replace('/translate', '/admin/approve-token');
                var res = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        admin_email: currentUser.email,
                        target_email: currentUser.email,
                        amount: amount,
                        password: password
                    })
                });

                var json = await res.json();

                if (!res.ok) {
                    alert("❌ Lỗi: " + (json.error || "Không thể duyệt token"));
                } else {
                    if (typeof showUserChangedToast === 'function') {
                        showUserChangedToast("✅ " + json.message, 'success');
                    } else {
                        alert("✅ " + json.message);
                    }
                    await refreshTokenFromFirestore();
                }
            } catch (e) {
                alert("Lỗi kết nối Server: " + e.message);
            } finally {
                buyTokenBtn.innerHTML = originalText;
                buyTokenBtn.disabled = false;
            }
            return;
        }

        if (typeof openRenewalModal === 'function') openRenewalModal();
        else alert('Vui lòng liên hệ Admin để gia hạn tài khoản!');
    });

    function autoResizeTextarea() {
        inputArea.style.height = 'auto';
        var newHeight = inputArea.scrollHeight;
        var maxHeight = 400;
        if (newHeight > maxHeight) {
            inputArea.style.height = maxHeight + 'px';
            inputArea.style.overflowY = 'auto';
        } else {
            inputArea.style.height = newHeight + 'px';
            inputArea.style.overflowY = 'hidden';
        }
    }

    function findSuspiciousWords() {
        if (currentMode !== 'vi2zh') return [];
        var text = inputArea.value;
        
        if (/[\u4e00-\u9fa5]/.test(text)) return [];

        var rawWords = text.split(/\s+/);
        var suspicious = [];
        var whitelist = ['tr', 'và', 'của', 'cho', 'với', 'để', 'là', 'có', 'không', 'những', 'các', 'được'];

        for (var i = 0; i < rawWords.length; i++) {
            var w = rawWords[i].replace(/^[.,!?;:"'()\[\]{}]+|[.,!?;:"'()\[\]{}]+$/g, '');
            if (!w || w.length < 3) continue;
            if (whitelist.includes(w.toLowerCase())) continue;

            var wLower = w.toLowerCase();
            var hasTripleChar = /(.)\1{2,}/.test(wLower);
            var vowelsRegex = /[aeiouyàáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừừứửữựỳýỷỹỵ]/i;
            var hasVowel = vowelsRegex.test(wLower);

            if (hasTripleChar || (!hasVowel && w.length >= 4)) {
                if (suspicious.indexOf(w) === -1) suspicious.push(w);
            }
        }
        return suspicious;
    }

    function checkSpellingSuggestions() {
        var suspiciousWords = findSuspiciousWords();
        if (suspiciousWords.length > 0) {
            spellChips.innerHTML = '';
            suspiciousWords.forEach(function(word) {
                var chip = document.createElement('div');
                chip.className = 'cp-spell-chip';
                chip.innerHTML = '<i class="fas fa-triangle-exclamation"></i> ' + word;
                spellChips.appendChild(chip);
            });
            spellContainer.classList.add('show');
        } else {
            spellContainer.classList.remove('show');
        }
    }

    function updateCharCount() {
        var len = inputArea.value.length;
        charCount.textContent = len + ' / ' + MAX_CHARS;
        if (len > MAX_CHARS) {
            charCount.classList.add('over');
            inputArea.value = inputArea.value.substring(0, MAX_CHARS);
            charCount.textContent = MAX_CHARS + ' / ' + MAX_CHARS + ' (Đã cắt)';
        } else {
            charCount.classList.remove('over');
        }
        autoResizeTextarea();
        checkSpellingSuggestions();
    }

    function autoDetectAndSwitchLanguage() {
        var text = inputArea.value;
        if (!text || text.trim() === '') return;

        var hasChinese = /[\u4e00-\u9fa5]/.test(text);

        if (hasChinese && currentMode !== 'zh2vi') {
            currentMode = 'zh2vi';
            spellContainer.classList.remove('show');
            if (!inputArea.disabled) {
                inputArea.placeholder = '输入或粘贴中文文本，让翻译助手帮您搞定...';
            }
        } else if (!hasChinese && currentMode !== 'vi2zh') {
            var hasLatin = /[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪỬỮỰỲỴÝỶỸ]/.test(text);
            if (hasLatin) {
                currentMode = 'vi2zh';
                if (!inputArea.disabled) {
                    inputArea.placeholder = 'Nhập hoặc dán văn bản để Trợ lý dịch giúp bạn...';
                }
            }
        }
    }

    inputArea.addEventListener('input', function() {
        autoDetectAndSwitchLanguage();
        updateCharCount();
        if (lastDeletedText !== '') {
            lastDeletedText = '';
            resetBtn.innerHTML = '<i class="fas fa-rotate-right"></i>';
            resetBtn.title = 'Làm mới';
            resetBtn.style.color = '';
            resetBtn.style.borderColor = '';
        }
    });

    setTimeout(updateCharCount, 200);

    switchBtn.addEventListener('click', function() {
        if (currentMode === 'vi2zh') {
            currentMode = 'zh2vi';
            spellContainer.classList.remove('show');
            if (!inputArea.disabled) inputArea.placeholder = '输入或粘贴中文文本，让翻译助手帮您搞定...';
        } else {
            currentMode = 'vi2zh';
            if (!inputArea.disabled) inputArea.placeholder = 'Nhập hoặc dán văn bản để Trợ lý dịch giúp bạn...';
        }
        
        updateCharCount();
    });

    var handleResetClick = async function() {
        var currentText = inputArea.value;

        if (currentText.trim() !== '') {
            lastDeletedText = currentText; 
            inputArea.value = ''; 
            
            [resetBtn, resetBtnMobile].forEach(function(btn) {
                if (!btn) return;
                btn.innerHTML = '<i class="fas fa-undo"></i>';
                btn.title = 'Bấm lần nữa để khôi phục văn bản';
                btn.style.color = '#16a34a'; 
                btn.style.borderColor = '#16a34a';
            });
            
            spellContainer.classList.remove('show');
            updateCharCount();
            progressWrap.classList.remove('show');
            startBtn.disabled = false;
            startBtn.innerHTML = '<i class="fas fa-arrow-right"></i>';
            setTimeout(autoResizeTextarea, 50);
        } 
        else if (lastDeletedText !== '') {
            inputArea.value = lastDeletedText; 
            lastDeletedText = ''; 
            
            [resetBtn, resetBtnMobile].forEach(function(btn) {
                if (!btn) return;
                btn.innerHTML = '<i class="fas fa-rotate-right"></i>';
                btn.title = 'Làm mới';
                btn.style.color = '';
                btn.style.borderColor = '';
            });
            
            updateCharCount();
            setTimeout(autoResizeTextarea, 50);
        } 
        else {
            if (!currentUser || !currentUser.email) {
                alert('Vui lòng đăng nhập để kiểm tra Token!');
                return;
            }
            if (currentUser.role === 'super_admin' || currentUser.isPermanent) {
                alert('Tài khoản của bạn không giới hạn Token!');
                return;
            }

            var now = Date.now();
            var timeSinceLastRefresh = now - lastTokenRefreshTime;
            if (timeSinceLastRefresh < TOKEN_REFRESH_COOLDOWN) {
                var waitSec = Math.ceil((TOKEN_REFRESH_COOLDOWN - timeSinceLastRefresh) / 1000);
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('⏳ Vui lòng đợi ' + waitSec + ' giây nữa mới kiểm tra lại', 'warn');
                } else {
                    alert('⏳ Vui lòng đợi ' + waitSec + ' giây nữa mới kiểm tra lại');
                }
                return;
            }

            var originalHTML = resetBtn ? resetBtn.innerHTML : '<i class="fas fa-rotate-right"></i>';
            
            [resetBtn, resetBtnMobile].forEach(function(btn) {
                if (!btn) return;
                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            });
            
            tokenText.textContent = 'Đang kiểm tra...';

            var ok = await refreshTokenFromFirestore();
            
            [resetBtn, resetBtnMobile].forEach(function(btn) {
                if (!btn) return;
                btn.innerHTML = originalHTML;
                btn.disabled = false;
            });

            if (ok) {
                lastTokenRefreshTime = Date.now();
                try { localStorage.setItem('cp_last_token_refresh', String(lastTokenRefreshTime)); } catch(e) {}
                startCooldownTimer();

                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('✅ Đã cập nhật số dư Token mới nhất', 'success');
                }
            } else {
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('⚠️ Không thể kết nối Server', 'warn');
                }
                tokenText.textContent = 'Lỗi mạng';
            }
        }
    };

    if (resetBtn) resetBtn.addEventListener('click', handleResetClick);
    if (resetBtnMobile) resetBtnMobile.addEventListener('click', handleResetClick);

    function showSpellModal(words) {
        return new Promise(function(resolve) {
            modalWordsList.textContent = words.join(', ');
            modalOverlay.classList.add('show');
            resolveModalAction = resolve;
        });
    }

    modalFixBtn.addEventListener('click', function() {
        modalOverlay.classList.remove('show');
        if (resolveModalAction) resolveModalAction(false);
    });

    modalProceedBtn.addEventListener('click', function() {
        modalOverlay.classList.remove('show');
        if (resolveModalAction) resolveModalAction(true);
    });

    function smartSplit(text, mode) {
        var protectedText = text.replace(/(\d)\.(\d)/g, '$1__DOT__$2');
        var rawParts = protectedText.split(/(?<=[.!?。！？\n])/g);
        var result = [];
        for (var i = 0; i < rawParts.length; i++) {
            var s = rawParts[i].replace(/__DOT__/g, '.').trim();
            if (s.length === 0) continue;
            if (mode === 'zh2vi') {
                if (!/[\u4e00-\u9fa5]/.test(s)) continue; 
            } else {
                if (!/[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪỬỮỰỲỴÝỶỸửữựỳỵỷỹ]/.test(s)) continue;
            }
            result.push(s);
        }
        return result;
    }

    function getAccuratePracticeItems(zhText, serverItems) {
        if (serverItems && serverItems.length > 0) {
            return serverItems;
        }
        if (zhText && typeof Intl !== 'undefined' && Intl.Segmenter) {
            var segmenter = new Intl.Segmenter('zh', { granularity: 'word' });
            var result = [];
            for (var seg of segmenter.segment(zhText)) {
                var w = seg.segment;
                if (!w.trim()) continue;
                var py = '';
                if (window.pinyinPro && /[\u4e00-\u9fa5]/.test(w)) {
                    py = window.pinyinPro.pinyin(w, { toneType: 'symbol', separator: '' });
                } else {
                    py = w;
                }
                result.push({
                    text: w,
                    pinyin: py,
                    type: /[\u4e00-\u9fa5]/.test(w) ? 'phrase' : 'symbol'
                });
            }
            if (result.length > 0) return result;
        }
        return [{ text: zhText, pinyin: '', type: 'phrase' }];
    }

    startBtn.addEventListener('click', async function() {
        if (!currentUser) { alert('Vui lòng đăng nhập!'); return; }

        var isExpired = checkIsExpired();
        if (isExpired) {
            alert('Tài khoản của bạn đã hết hạn. Vui lòng gia hạn để tiếp tục sử dụng tính năng Luyện tập tự do.\n(Số dư Token của bạn vẫn được bảo lưu an toàn).');
            if (typeof openRenewalModal === 'function') openRenewalModal();
            return;
        }

        if (!currentUser.isPermanent && currentUser.role !== 'super_admin' && (myTokenQuota + myBonusTokens - myTokensUsed <= 0)) { 
            alert('Bạn đã hết token! Vui lòng mua thêm hoặc quay lại vào ngày mai (đối với Admin).'); 
            return; 
        }

        var rawText = inputArea.value.trim();
        if (!rawText) { alert('Vui lòng nhập văn bản!'); return; }

        var suspiciousWords = findSuspiciousWords();
        if (suspiciousWords.length > 0) {
            var proceed = await showSpellModal(suspiciousWords);
            if (!proceed) return;
        }

        startBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        startBtn.disabled = true;
        switchBtn.style.pointerEvents = 'none';
        progressWrap.classList.add('show');
        progressBar.style.width = '0%';

        var sentences = smartSplit(rawText, currentMode);
        if (sentences.length === 0) {
            alert('Không tìm thấy câu hợp lệ!');
            finishProcess();
            return;
        }

        await loadPinyinPro();

        var total = sentences.length;
        var customData = [];
        var totalTokensThisSession = 0;
        var CHUNK_SIZE = 10;
        var processedCount = 0;
        var groupId = Date.now();

        try {
            for (var i = 0; i < total; i += CHUNK_SIZE) {
                var chunk = sentences.slice(i, i + CHUNK_SIZE);
                var combinedText = chunk.join('\n[---]\n');
                
                var data = await fetchTranslate(combinedText, currentMode);
                if (data.tokensUsed > 0) {
                    totalTokensThisSession += data.tokensUsed;
                }

                var translatedChunk = data.translated.split(/\n?\[\s*---\s*\]\n?/);

                var allItems = data.items || [];
                var sentenceItemsList = [];
                var currentGroup = [];
                for (var k = 0; k < allItems.length; k++) {
                    var itm = allItems[k];
                    if (itm.text && itm.text.indexOf('---') !== -1) {
                        sentenceItemsList.push(currentGroup);
                        currentGroup = [];
                    } else {
                        currentGroup.push(itm);
                    }
                }
                sentenceItemsList.push(currentGroup);

                for (var j = 0; j < chunk.length; j++) {
                    var originalSentence = chunk[j];
                    var transSentence = translatedChunk[j] ? translatedChunk[j].trim() : originalSentence;

                    var zhText = currentMode === 'vi2zh' ? transSentence : originalSentence;
                    var viText = currentMode === 'vi2zh' ? originalSentence : transSentence;

                    var sItems = sentenceItemsList[j] || null;
                    var accurateItems = getAccuratePracticeItems(zhText, sItems);

                    var pinyinStr = '';
                    if (accurateItems && accurateItems.length > 0) {
                        pinyinStr = accurateItems.map(function(it) { return it.pinyin || it.text; }).filter(Boolean).join(' ');
                    }
                    if (!pinyinStr) {
                        pinyinStr = getSmartPinyin(zhText);
                    }

                    customData.push({
                        stt: String(i + j + 1),
                        groupId: groupId,
                        zh: zhText,
                        vi: viText,
                        pinyin: pinyinStr,
                        items: accurateItems,
                        hsk: 'HSK1',
                        topic: 'Văn bản tự do',
                        subject: 'Custom'
                    });

                    processedCount++;
                    var pct = Math.round((processedCount / total) * 100);
                    progressBar.style.width = pct + '%';
                    progressText.textContent = 'Đang xử lý: ' + processedCount + ' / ' + total + ' câu (' + pct + '%)';
                }
            }

            customData.sort(function(a, b) { return parseInt(a.stt) - parseInt(b.stt); });

            if (currentUser && currentUser.email && customData.length > 0) {
                fetch(SERVER_API_URL.replace('/translate', '/history'), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        email: currentUser.email,
                        items: customData
                    })
                }).catch(function(e) {});
            }

            if (totalTokensThisSession > 0) {
                myTokensUsed += totalTokensThisSession;
                renderTokenUI(checkIsExpired());
                try {
                    var cacheKey = 'user_cache_' + currentUser.email;
                    var cached = JSON.parse(localStorage.getItem(cacheKey) || 'null');
                    if (cached && cached.data) { 
                        cached.data.tokensUsed = myTokensUsed; 
                        localStorage.setItem(cacheKey, JSON.stringify(cached)); 
                    }
                } catch(e) {}
            }

            loadDataToPracticeScreen(customData);
        } catch(e) {
            alert('Có lỗi xảy ra: ' + e.message);
        } finally {
            finishProcess();
        }
    });

    function loadDataToPracticeScreen(customData) {
        if (typeof window.activateCustomPracticeMode === 'function') {
            window.activateCustomPracticeMode(customData);
        } else {
            if (typeof RAW_DATA !== 'undefined') RAW_DATA = customData;
            if (typeof filtered !== 'undefined') filtered = customData;
            if (typeof buildFilters === 'function') buildFilters();
            if (typeof applyFilter === 'function') applyFilter();
            if (typeof updateResultCount === 'function') updateResultCount();
            if (typeof render === 'function') render(true);
        }
    }

    function finishProcess() {
        startBtn.innerHTML = '<i class="fas fa-arrow-right"></i>';
        startBtn.disabled = false;
        switchBtn.style.pointerEvents = 'auto';
        setTimeout(function() { progressWrap.classList.remove('show'); }, 1200);
        
        if (currentUser) {
            renderTokenUI(checkIsExpired());
        }
    }

    function loadPinyinPro() {
        if (window.pinyinPro) return Promise.resolve();
        return new Promise(function(resolve) {
            var script = document.createElement('script');
            script.src = 'https://unpkg.com/pinyin-pro@3.18.2/dist/index.js';
            script.onload = function() {
                if (!window.pinyinPro && window.pinyin) window.pinyinPro = window.pinyin;
                resolve();
            };
            script.onerror = function() {
                var script2 = document.createElement('script');
                script2.src = 'https://cdn.jsdelivr.net/npm/pinyin-pro@3.18.2/dist/index.min.js';
                script2.onload = resolve;
                script2.onerror = resolve;
                document.head.appendChild(script2);
            };
            document.head.appendChild(script);
        });
    }

    function getSmartPinyin(text) {
        if (!text) return '';
        if (!window.pinyinPro) return text;

        try {
            var rawPinyin = '';
            if (typeof Intl !== 'undefined' && Intl.Segmenter) {
                var segmenter = new Intl.Segmenter('zh', { granularity: 'word' });
                var parts = [];
                for (var seg of segmenter.segment(text)) {
                    var word = seg.segment;
                    if (/[\u4e00-\u9fa5]/.test(word)) {
                        parts.push(window.pinyinPro.pinyin(word, { toneType: 'symbol', separator: '' }));
                    } else if (/[\s\n\r\t]+/.test(word)) {
                        parts.push(' ');
                    } else {
                        parts.push(word);
                    }
                }
                rawPinyin = parts.join('');
            } else {
                rawPinyin = window.pinyinPro.pinyin(text, { toneType: 'symbol', separator: ' ' });
            }

            return rawPinyin
                .replace(/\s+([,,.,!！?？;；:：])/g, '$1')
                .replace(/([,,.,!！?？;；:：])([^\s])/g, '$1 $2')
                .replace(/\s+/g, ' ')
                .trim();

        } catch (e) {
            var fallbackPinyin = window.pinyinPro.pinyin(text, { toneType: 'symbol', separator: ' ' });
            return fallbackPinyin
                .replace(/\s+([,,.,!！?？;；:：])/g, '$1')
                .replace(/([,,.,!！?？;；:：])([^\s])/g, '$1 $2')
                .replace(/\s+/g, ' ')
                .trim();
        }
    }

    async function fetchTranslate(text, mode) {
        var translated = '';
        var pinyinRes = '';
        var itemsRes = null;
        var tokensUsed = 0;

        try {
            var source = mode === 'zh2vi' ? 'zh-CN' : 'vi';
            var target = mode === 'zh2vi' ? 'vi' : 'zh-CN';
            
            var res = await fetch(SERVER_API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    text: text, 
                    source: source, 
                    target: target,
                    email: currentUser ? currentUser.email : ''
                })
            });
            
            if (!res.ok) throw new Error('HTTP ' + res.status);
            var json = await res.json();
            if (json.error) throw new Error(json.error);
            
            translated = json.translated;
            pinyinRes = json.pinyin || '';
            itemsRes = json.items || null;
            tokensUsed = json.tokensUsed || 0;
        } catch(e) {
            translated = text; 
        }
        
        return { 
            translated: translated, 
            pinyin: pinyinRes, 
            items: itemsRes, 
            tokensUsed: tokensUsed 
        };
    }

    function updateCounterUI() {
        if (!historyCounter) return;
        if (isUserAdmin) {
            historyCounter.innerHTML = '<span style="color:#059669; font-weight:700;"><i class="fas fa-shield-halved"></i> Admin: Không giới hạn Read/Save</span>';
        } else {
            var saveRemain = 150 - currentTodayCount; 
            if (saveRemain < 0) saveRemain = 0;
            var readRemainText = (typeof currentReadRemain !== 'undefined') ? currentReadRemain : 250; 
            historyCounter.innerHTML = '📖 Lượt xem hôm nay: <b style="color:' + (readRemainText > 0 ? '#4f46e5' : '#dc2626') + ';">' + readRemainText + '</b>/250 | ⏳ Đã lưu: <b>' + currentTodayCount + '</b>/150';
        }
    }

    function renderHistoryUI() {
        updateCounterUI();
        if (cachedHistoryData.length === 0) {
            historyList.innerHTML = '<div style="text-align:center; color:#64748b; font-size:0.9rem;">Chưa có lịch sử dịch nào.</div>';
            return;
        }
        
        var html = '';
        cachedHistoryData.forEach(function(item, idx) {
            var timeDisplay = item.createdAt || '';
            if (timeDisplay) {
                try {
                    var d = new Date(timeDisplay.replace(' ', 'T') + 'Z'); 
                    if (!isNaN(d.getTime())) {
                        var yyyy = d.getFullYear();
                        var mm = String(d.getMonth() + 1).padStart(2, '0');
                        var dd = String(d.getDate()).padStart(2, '0');
                        var hh = String(d.getHours()).padStart(2, '0');
                        var min = String(d.getMinutes()).padStart(2, '0');
                        var ss = String(d.getSeconds()).padStart(2, '0');
                        timeDisplay = yyyy + '-' + mm + '-' + dd + ' ' + hh + ':' + min + ':' + ss;
                    }
                } catch(e) {}
            }

            var sttNumber = item.stt || (idx + 1);

            html += '<div class="cp-history-item cp-history-card" style="position:relative; display:flex; align-items:flex-start; gap:8px; cursor:pointer;" data-index="' + idx + '" id="cp-hist-' + (item.id || idx) + '">' +
                '<div style="display:flex; align-items:center; justify-content:center; min-width:26px; height:26px; border-radius:50%; background:linear-gradient(135deg,#4f46e5,#7c3aed); color:#fff; font-size:0.75rem; font-weight:800; flex-shrink:0; margin-top:2px; box-shadow:0 2px 6px rgba(79,70,229,.3);">' + sttNumber + '</div>' +
                '<div style="flex:1; min-width:0;">' +
                    '<div class="cp-history-vi">' + (item.text_vi || '') + '</div>' +
                    '<div class="cp-history-zh">' + (item.text_zh || '') + '</div>' +
                    (item.pinyin ? '<div class="cp-history-pinyin">' + item.pinyin + '</div>' : '') +
                    '<div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">' +
                        '<div class="cp-history-time">' + timeDisplay + '</div>' +
                        '<div style="display:flex; gap:6px;">' +
                            '<button class="cp-delete-single-history" data-id="' + (item.id || '') + '" data-index="' + idx + '" style="background:#fee2e2; color:#ef4444; border:none; padding:5px 10px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer;" title="Xóa câu này">' +
                                '<i class="fas fa-trash-alt"></i> Xóa' +
                            '</button>' +
                            '<button class="cp-load-single-history" data-index="' + idx + '" style="background:linear-gradient(135deg,#6366f1,#a855f7); color:#fff; border:none; padding:5px 12px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer;" type="button">' +
                                '<i class="fas fa-play"></i> Luyện tập' +
                            '</button>' +
                        '</div>' +
                    '</div>' +
                '</div>' +
            '</div>';
        });
        historyList.innerHTML = html;

        var cardItems = historyList.querySelectorAll('.cp-history-card');
        cardItems.forEach(function(card) {
            var lastTap = 0;
            var touchStartX = 0;
            var touchStartY = 0;
            var touchStartTime = 0;

            card.addEventListener('touchstart', function(e) {
                var touch = e.touches[0];
                touchStartX = touch.clientX;
                touchStartY = touch.clientY;
                touchStartTime = Date.now();
            }, { passive: true });

            card.addEventListener('touchend', function(e) {
                if (e.target.closest('button')) return;

                var touch = e.changedTouches[0];
                var touchEndX = touch.clientX;
                var touchEndY = touch.clientY;
                var touchEndTime = Date.now();

                var distance = Math.sqrt(Math.pow(touchEndX - touchStartX, 2) + Math.pow(touchEndY - touchStartY, 2));
                var duration = touchEndTime - touchStartTime;

                if (distance < 10 && duration < 300) {
                    e.preventDefault();
                    triggerPracticeFromIndex(this.getAttribute('data-index'));
                }
            });

            card.addEventListener('click', function(e) {
                if (e.target.closest('button')) return;
                if (e.pointerType === 'touch' || ('ontouchstart' in window)) return;

                var now = Date.now();
                var timesince = now - lastTap;
                
                if (timesince < 300 && timesince > 0) {
                    e.preventDefault();
                    e.stopPropagation();
                    triggerPracticeFromIndex(this.getAttribute('data-index'));
                    lastTap = 0;
                } else {
                    lastTap = now;
                }
            });
        });

        function triggerPracticeFromIndex(indexStr) {
            var idx = parseInt(indexStr);
            if (isNaN(idx) || idx < 0) return;
            
            var slicedData = cachedHistoryData.slice(idx).map(function(item, i) {
                return {
                    stt: item.stt || String(i + 1),
                    zh: item.text_zh || '',
                    vi: item.text_vi || '',
                    pinyin: item.pinyin || '',
                    items: item.items || null,
                    hsk: 'HSK1',
                    topic: 'Lịch sử dịch',
                    subject: 'History'
                };
            });

            if (slicedData.length === 0) return;
            historyOverlay.classList.remove('show');
            loadDataToPracticeScreen(slicedData);
        }

        var singleBtns = historyList.querySelectorAll('.cp-load-single-history');
        singleBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                var idx = parseInt(this.getAttribute('data-index'));
                var targetItem = cachedHistoryData[idx];
                if (!targetItem) return;

                var singleData = [{
                    stt: targetItem.stt || String(idx + 1),
                    zh: targetItem.text_zh || '',
                    vi: targetItem.text_vi || '',
                    pinyin: targetItem.pinyin || '',
                    items: targetItem.items || null,
                    hsk: 'HSK1',
                    topic: 'Lịch sử dịch',
                    subject: 'History'
                }];

                historyOverlay.classList.remove('show');
                loadDataToPracticeScreen(singleData);
            });
        });

        var deleteBtns = historyList.querySelectorAll('.cp-delete-single-history');
        deleteBtns.forEach(function(btn) {
            btn.addEventListener('click', async function() {
                var docId = this.getAttribute('data-id');
                var idx = parseInt(this.getAttribute('data-index'));
                if (!confirm('Bạn có chắc chắn muốn xóa câu này khỏi lịch sử?')) return;

                if (docId) {
                    try {
                        var res = await fetch(SERVER_API_URL.replace('/translate', '/history/delete'), {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ email: currentUser.email, id: docId })
                        });
                        var json = await res.json();
                        if (json.ok && typeof json.todayCount !== 'undefined') {
                            currentTodayCount = json.todayCount;
                        }
                    } catch(e) {}
                }

                cachedHistoryData.splice(idx, 1);
                renderHistoryUI();
            });
        });
    }

    if (historyBtn) {
        historyBtn.addEventListener('click', async function() {
            if (!currentUser || !currentUser.email) { alert('Vui lòng đăng nhập để xem lịch sử!'); return; }
            
            var isExpired = checkIsExpired();
            if (isExpired) {
                alert('Tài khoản của bạn đã hết hạn. Vui lòng gia hạn để xem lịch sử dịch.\n(Số dư Token và lịch sử của bạn vẫn được bảo lưu an toàn).');
                if (typeof openRenewalModal === 'function') openRenewalModal();
                return;
            }

            historyOverlay.classList.add('show');
            historyList.innerHTML = '<div style="text-align:center; color:#64748b; font-size:0.9rem;"><i class="fas fa-spinner fa-spin"></i> Đang tải...</div>';
            historyCounter.textContent = 'Đang tải bộ đếm...';
            
            try {
                var res = await fetch(SERVER_API_URL.replace('/translate', '/history'), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        email: currentUser.email,
                        _method: 'GET'
                    })
                });
                
                var json = await res.json();
                if (!json.ok || !json.history) throw new Error(json.error || 'Không thể tải lịch sử');
                
                cachedHistoryData = json.history;
                currentTodayCount = json.todayCount || 0;
                currentReadRemain = (typeof json.readRemain !== 'undefined') ? json.readRemain : 250;
                isUserAdmin = json.isAdmin || false;

                renderHistoryUI();
                
            } catch (e) {
                historyList.innerHTML = '<div style="text-align:center; color:#ef4444; font-size:0.9rem;">Lỗi tải lịch sử: ' + e.message + '</div>';
                historyCounter.textContent = 'Không tải được bộ đếm';
            }
        });
    }

    if (selectAllHistoryBtn) {
        selectAllHistoryBtn.addEventListener('click', function() {
            if (!cachedHistoryData || cachedHistoryData.length === 0) {
                alert('Không có lịch sử nào để chọn!');
                return;
            }

            var allPracticeData = [];
            cachedHistoryData.forEach(function(item, idx) {
                allPracticeData.push({
                    stt: item.stt || String(idx + 1),
                    zh: item.text_zh || '',
                    vi: item.text_vi || '',
                    pinyin: item.pinyin || '',
                    items: item.items || null,
                    hsk: 'HSK1',
                    topic: 'Lịch sử dịch',
                    subject: 'History'
                });
            });

            historyOverlay.classList.remove('show');
            loadDataToPracticeScreen(allPracticeData);
        });
    }

    if (deleteAllHistoryBtn) {
        deleteAllHistoryBtn.addEventListener('click', async function() {
            if (!cachedHistoryData || cachedHistoryData.length === 0) {
                alert('Không có lịch sử nào để xóa!');
                return;
            }

            var confirmDelete = confirm('⚠️ Bạn có chắc chắn muốn XÓA TẤT CẢ ' + cachedHistoryData.length + ' câu trong lịch sử dịch không?\nThao tác này không thể hoàn tác!');
            if (!confirmDelete) return;

            var originalHTML = deleteAllHistoryBtn.innerHTML;
            deleteAllHistoryBtn.disabled = true;
            deleteAllHistoryBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Đang xóa...';

            try {
                var deletePromises = cachedHistoryData.map(function(item) {
                    if (item.id) {
                        return fetch(SERVER_API_URL.replace('/translate', '/history/delete'), {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ email: currentUser.email, id: item.id })
                        });
                    }
                    return Promise.resolve();
                });

                await Promise.all(deletePromises);

                cachedHistoryData = [];
                currentTodayCount = 0;
                renderHistoryUI();

                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('🗑️ Đã xóa toàn bộ lịch sử dịch!', 'success');
                } else {
                    alert('🗑️ Đã xóa toàn bộ lịch sử dịch!');
                }
            } catch (e) {
                alert('Có lỗi xảy ra khi xóa lịch sử: ' + e.message);
            } finally {
                deleteAllHistoryBtn.disabled = false;
                deleteAllHistoryBtn.innerHTML = originalHTML;
            }
        });
    }

    if (historyCloseBtn) {
        historyCloseBtn.addEventListener('click', function() {
            historyOverlay.classList.remove('show');
        });
    }
    if (historyOverlay) {
        historyOverlay.addEventListener('click', function(e) {
            if (e.target === this) this.classList.remove('show');
        });
    }

    if (tokenBadge) {
        tokenBadge.addEventListener('click', async function() {
            var now = Date.now();
            var timeSinceLastRefresh = now - lastTokenRefreshTime;
            
            if (timeSinceLastRefresh < TOKEN_REFRESH_COOLDOWN) {
                var waitSec = Math.ceil((TOKEN_REFRESH_COOLDOWN - timeSinceLastRefresh) / 1000);
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('⏳ Vui lòng đợi ' + waitSec + ' giây nữa mới kiểm tra lại', 'warn');
                }
                return;
            }
            
            if (isTokenRefreshing || this.classList.contains('refreshing')) return;
            
            isTokenRefreshing = true;
            this.classList.add('refreshing');
            var originalText = tokenText.textContent;
            tokenText.textContent = 'Đang cập nhật...';
            
            var ok = await refreshTokenFromFirestore();
            
            this.classList.remove('refreshing');
            isTokenRefreshing = false;
            
            if (!ok) {
                tokenText.textContent = originalText;
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('⚠️ Không thể cập nhật, vui lòng thử lại', 'warn');
                }
            } else {
                lastTokenRefreshTime = Date.now();
                try { localStorage.setItem('cp_last_token_refresh', String(lastTokenRefreshTime)); } catch(e) {}
                startCooldownTimer();
                
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('✅ Đã cập nhật số dư Token mới nhất', 'success');
                }
            }
        });
    }

    function loadCropperLibrary() {
        if (window.Cropper) return Promise.resolve();
        return new Promise(function(resolve) {
            var link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = 'https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.13/cropper.min.css';
            document.head.appendChild(link);

            var script = document.createElement('script');
            script.src = 'https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.13/cropper.min.js';
            script.onload = resolve;
            script.onerror = resolve;
            document.head.appendChild(script);
        });
    }

    var uploadImgBtn = document.getElementById('cpUploadImgBtn');
    var imageInput = document.getElementById('cpImageInput');
    
    var cropperInstance = null;
    var cropModalOverlay = document.getElementById('cpCropModalOverlay');
    var imageToCrop = document.getElementById('cpImageToCrop');
    var cropConfirmBtn = document.getElementById('cpCropConfirmBtn');
    var cropCancelBtn = document.getElementById('cpCropCancelBtn');
    var cropCloseBtn = document.getElementById('cpCropCloseBtn');

    if (uploadImgBtn && imageInput) {
        uploadImgBtn.addEventListener('click', function() {
            if (!currentUser) { alert('Vui lòng đăng nhập để sử dụng!'); return; }
            
            var isExpired = checkIsExpired();
            if (isExpired) {
                alert('Tài khoản đã hết hạn. Vui lòng gia hạn để dịch ảnh!');
                return;
            }
            if (currentUser.role !== 'super_admin' && !currentUser.isPermanent && (myTokenQuota + myBonusTokens - myTokensUsed <= 0)) { 
                alert('Bạn đã hết token, vui lòng mua thêm để dịch ảnh!'); 
                return; 
            }
            imageInput.click();
        });
    }

    if (imageInput) {
        imageInput.addEventListener('change', async function(e) {
            if (!e.target.files || e.target.files.length === 0) return;
            var file = e.target.files[0];
            
            var originalHTML = uploadImgBtn.innerHTML;
            uploadImgBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            uploadImgBtn.disabled = true;

            try {
                await loadCropperLibrary();
                
                var reader = new FileReader();
                reader.onload = function(evt) {
                    imageToCrop.src = evt.target.result;
                    cropModalOverlay.classList.add('show');
                    
                    if (cropperInstance) {
                        cropperInstance.destroy();
                    }
                    
                    cropperInstance = new Cropper(imageToCrop, {
                        aspectRatio: NaN,
                        viewMode: 1,
                        autoCropArea: 0.95,
                        responsive: true,
                    });
                    
                    uploadImgBtn.innerHTML = originalHTML;
                    uploadImgBtn.disabled = false;
                };
                reader.readAsDataURL(file);
            } catch(err) {
                alert('Không thể tải công cụ cắt ảnh: ' + err.message);
                uploadImgBtn.innerHTML = originalHTML;
                uploadImgBtn.disabled = false;
                imageInput.value = '';
            }
        });
    }

    if (cropConfirmBtn) {
        cropConfirmBtn.addEventListener('click', async function() {
            if (!cropperInstance) return;
            
            cropModalOverlay.classList.remove('show');
            progressWrap.classList.add('show');
            progressBar.style.width = '30%';
            progressText.textContent = 'Đang xử lý ảnh tối ưu (Trắng đen)...';

            var canvas = cropperInstance.getCroppedCanvas({
                maxWidth: 900,
                maxHeight: 900
            });
            
            var ctx = canvas.getContext('2d');
            var imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            var data = imgData.data;
            for (var i = 0; i < data.length; i += 4) {
                var avg = (data[i] * 0.299 + data[i + 1] * 0.587 + data[i + 2] * 0.114);
                data[i] = avg;     
                data[i + 1] = avg; 
                data[i + 2] = avg; 
            }
            ctx.putImageData(imgData, 0, 0);

            canvas.toBlob(async function(blob) {
                try {
                    progressBar.style.width = '60%';
                    progressText.textContent = 'Đang nhận diện văn bản (OCR)...';

                    var formData = new FormData();
                    formData.append('image', blob, 'grayscale-cropped.jpg');
                    formData.append('email', currentUser.email);

                    var res = await fetch(SERVER_API_URL.replace('/translate', '/translate-image'), {
                        method: 'POST',
                        body: formData
                    });
                    
                    var json = await res.json();
                    if (json.error) throw new Error(json.error);
                    
                    inputArea.value = json.original_text;
                    updateCharCount();
                    
                    if (json.detected_source === 'zh' && currentMode !== 'zh2vi') {
                        currentMode = 'zh2vi';
                        if (!inputArea.disabled) inputArea.placeholder = 'Dán văn bản tiếng Trung vào đây...';
                    } else if (json.detected_source === 'vi' && currentMode !== 'vi2zh') {
                        currentMode = 'vi2zh';
                        if (!inputArea.disabled) inputArea.placeholder = 'Nhập văn bản tiếng Việt vào đây...';
                    }
                                      
                    if (json.tokensUsed > 0 && !currentUser.isPermanent) {
                        await refreshTokenFromFirestore();
                    }

                    if (typeof showUserChangedToast === 'function') {
                        showUserChangedToast('✅ Đã đọc ảnh xong (Tốn ' + json.tokensUsed + ' token). Vui lòng bấm Bắt đầu để dịch!', 'success');
                    } else {
                        alert('Đã đọc ảnh xong (Tốn ' + json.tokensUsed + ' token).');
                    }
                    
                } catch(err) {
                    alert('Lỗi đọc ảnh: ' + err.message);
                } finally {
                    imageInput.value = '';
                    progressWrap.classList.remove('show');
                    progressBar.style.width = '0%';
                    if (cropperInstance) {
                        cropperInstance.destroy();
                        cropperInstance = null;
                    }
                }
            }, 'image/jpeg', 0.75);
        });
    }

    setTimeout(initTokenState, 100);
    setTimeout(initTokenState, 1500);

})();
"""
