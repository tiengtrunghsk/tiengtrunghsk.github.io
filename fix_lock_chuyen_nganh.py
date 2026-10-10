# -*- coding: utf-8 -*-
r"""
fix_lock_chuyen_nganh.py
========================
Sửa bug: Nhấn nút Chuyên ngành trước khi data load xong → nút bị kẹt.

Khớp chính xác với scripts/ui_template.py hiện tại của bạn.

Chạy:
    python fix_lock_chuyen_nganh.py
"""

import os
import sys
import shutil
from datetime import datetime


TARGET = "scripts/ui_template.py"
BACKUP_SUFFIX = ".bak_lock_" + datetime.now().strftime("%Y%m%d_%H%M%S")


def log(msg, icon="•"):
    print(f"  {icon} {msg}")


def section(title):
    print("")
    print("=" * 66)
    print(f"  {title}")
    print("=" * 66)


def main():
    section("LOCK NÚT CHUYÊN NGÀNH KHI DATA CHƯA LOAD")

    if not os.path.isfile(TARGET):
        log(f"Không tìm thấy {TARGET}", "❌")
        sys.exit(1)

    # ═══════════════════════════════════════════════════════════
    # Backup
    # ═══════════════════════════════════════════════════════════
    bak = TARGET + BACKUP_SUFFIX
    shutil.copy2(TARGET, bak)
    log(f"Backup: {TARGET} → {os.path.basename(bak)}", "💾")

    with open(TARGET, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    total = 0

    # ═══════════════════════════════════════════════════════════
    # FIX 1 — Thêm CSS vào cuối build_ui_css()
    # ═══════════════════════════════════════════════════════════
    section("FIX 1 — CSS .locked-loading")

    CSS_ANCHOR = '''@media (min-width: 1200px) {
    .ds-btn[data-dataset="tonghop"] > span {
        font-size: clamp(0.68rem, 30.85rem);
    }
}
"""

def build_ui_html():'''

    CSS_FIXED = '''@media (min-width: 1200px) {
    .ds-btn[data-dataset="tonghop"] > span {
        font-size: clamp(0.68rem, 30.85rem);
    }
}

/* ═══════════════════════════════════════════════════════════ */
/* ⭐ LOCK: Khoá nút dataset khi data chưa load xong             */
/* ═══════════════════════════════════════════════════════════ */
.ds-btn.locked-loading {
    opacity: 0.5 !important;
    cursor: not-allowed !important;
    pointer-events: none !important;
    filter: grayscale(0.4);
    position: relative;
}
.ds-btn.locked-loading::after {
    content: '';
    position: absolute;
    top: 50%;
    right: 14px;
    width: 16px;
    height: 16px;
    margin-top: -8px;
    border: 2px solid rgba(148, 163, 184, 0.3);
    border-top-color: #94a3b8;
    border-radius: 50%;
    animation: dsLockSpin 0.9s linear infinite;
    pointer-events: none;
    z-index: 5;
}
@keyframes dsLockSpin {
    to { transform: rotate(360deg); }
}
.ds-sub-wrap.loading .ds-sub-btn {
    opacity: 0.4 !important;
    pointer-events: none !important;
    filter: grayscale(0.5);
}
.ds-sub-wrap.loading::before {
    content: 'Đang tải dữ liệu...';
    display: block;
    text-align: center;
    padding: 1rem;
    font-size: 0.85rem;
    color: #94a3b8;
    font-weight: 600;
    font-style: italic;
}
"""

def build_ui_html():'''

    if CSS_ANCHOR in content:
        content = content.replace(CSS_ANCHOR, CSS_FIXED, 1)
        log("Đã chèn CSS .locked-loading", "✅")
        total += 1
    else:
        log("Không tìm thấy anchor CSS", "⚠️")

    # ═══════════════════════════════════════════════════════════
    # FIX 2 — Sửa initDatasetSelector: nhánh chuyenNganhKeys rỗng
    # ═══════════════════════════════════════════════════════════
    section("FIX 2 — Khoá nút khi data chưa load + auto-retry")

    JS_ANCHOR_1 = '''    var cnBtn = $('dsChuyenNganhBtn');
    if (chuyenNganhKeys.length === 0) {
        if (cnBtn) cnBtn.style.display = 'none';
        return;
    }'''

    JS_FIXED_1 = '''    var cnBtn = $('dsChuyenNganhBtn');
    if (chuyenNganhKeys.length === 0) {
        /* ⭐ FIX: Data chưa load → KHOÁ nút, KHÔNG ẩn */
        if (cnBtn) {
            cnBtn.classList.add('locked-loading');
            cnBtn.style.display = '';
            cnBtn.title = 'Đang tải dữ liệu chuyên ngành...';

            /* Auto-retry khi data load xong */
            if (!window.__dataLoaded && window.__dataLoadPromise) {
                window.__dataLoadPromise.then(function() {
                    /* Chờ DOM sẵn sàng rồi rebuild */
                    setTimeout(function() {
                        if (typeof initDatasetSelector === 'function') {
                            initDatasetSelector();
                        }
                    }, 150);
                }).catch(function() {
                    /* Data load fail → mở khoá để user dùng được gì thì dùng */
                    if (cnBtn) {
                        cnBtn.classList.remove('locked-loading');
                        cnBtn.title = 'Không tải được dữ liệu chuyên ngành';
                    }
                });
            } else {
                /* Fallback: chờ event dataLoaded */
                window.addEventListener('dataLoaded', function() {
                    setTimeout(function() {
                        if (typeof initDatasetSelector === 'function') {
                            initDatasetSelector();
                        }
                    }, 150);
                }, { once: true });
            }
        }
        return;
    }

    /* ⭐ Data đã có → MỞ KHOÁ nút */
    if (cnBtn) {
        cnBtn.classList.remove('locked-loading');
        cnBtn.title = 'Chọn chuyên ngành';
    }'''

    if JS_ANCHOR_1 in content:
        content = content.replace(JS_ANCHOR_1, JS_FIXED_1, 1)
        log("Đã patch nhánh chuyenNganhKeys rỗng", "✅")
        total += 1
    else:
        log("Không tìm thấy anchor JS 1", "⚠️")

    # ═══════════════════════════════════════════════════════════
    # FIX 3 — Chặn click khi data chưa load trong handler cnBtn
    # ═══════════════════════════════════════════════════════════
    section("FIX 3 — Chặn click khi data chưa load")

    JS_ANCHOR_2 = '''    if (cnBtn && !cnBtn.__boundToggle) {
        cnBtn.__boundToggle = true;
        cnBtn.addEventListener('click', function() {
            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';'''

    JS_FIXED_2 = '''    if (cnBtn && !cnBtn.__boundToggle) {
        cnBtn.__boundToggle = true;
        cnBtn.addEventListener('click', function() {
            /* ⭐ FIX: Chặn click nếu data chưa load */
            if (!window.__dataLoaded) {
                if (typeof showTagToast === 'function') {
                    showTagToast('Đang tải dữ liệu, vui lòng đợi...');
                }
                return;
            }

            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';'''

    if JS_ANCHOR_2 in content:
        content = content.replace(JS_ANCHOR_2, JS_FIXED_2, 1)
        log("Đã chặn click khi data chưa load", "✅")
        total += 1
    else:
        log("Không tìm thấy anchor JS 2", "⚠️")

    # ═══════════════════════════════════════════════════════════
    # FIX 4 — Chặn click trong sub-btn khi data chưa load
    # ═══════════════════════════════════════════════════════════
    section("FIX 4 — Chặn click sub-btn khi data chưa load")

    JS_ANCHOR_3 = '''        btn.addEventListener('click', function(e) {
            if (this.dataset.locked === '1') {
                e.preventDefault();
                e.stopPropagation();
                showChuyenNganhLockMessage();
                return;
            }'''

    JS_FIXED_3 = '''        btn.addEventListener('click', function(e) {
            /* ⭐ FIX: Chặn nếu data chưa load */
            if (!window.__dataLoaded) {
                e.preventDefault();
                e.stopPropagation();
                if (typeof showTagToast === 'function') {
                    showTagToast('Đang tải dữ liệu, vui lòng đợi...');
                }
                return;
            }

            if (this.dataset.locked === '1') {
                e.preventDefault();
                e.stopPropagation();
                showChuyenNganhLockMessage();
                return;
            }'''

    if JS_ANCHOR_3 in content:
        content = content.replace(JS_ANCHOR_3, JS_FIXED_3, 1)
        log("Đã chặn click sub-btn khi data chưa load", "✅")
        total += 1
    else:
        log("Không tìm thấy anchor JS 3", "⚠️")

    # ═══════════════════════════════════════════════════════════
    # FIX 5 — markCurrentDatasetActive không reset CN khi dropdown mở
    # ═══════════════════════════════════════════════════════════
    section("FIX 5 — markCurrentDatasetActive skip CN khi mở")

    JS_ANCHOR_4 = '''    document.querySelectorAll('.ds-btn, .ds-sub-btn').forEach(function(b) {
        b.classList.remove('active');
    });'''

    JS_FIXED_4 = '''    document.querySelectorAll('.ds-btn, .ds-sub-btn').forEach(function(b) {
        /* ⭐ FIX: Không reset nút Chuyên ngành nếu dropdown đang mở */
        if (b.getAttribute('data-dataset-group') === 'chuyen-nganh') {
            var _sw = document.getElementById('dsSubWrap');
            if (_sw && _sw.style.display !== 'none') return;
        }
        b.classList.remove('active');
    });'''

    # Chỉ thay lần đầu tiên (trong markCurrentDatasetActive)
    if JS_ANCHOR_4 in content:
        content = content.replace(JS_ANCHOR_4, JS_FIXED_4, 1)
        log("Đã patch markCurrentDatasetActive", "✅")
        total += 1
    else:
        log("Không tìm thấy anchor JS 4", "⚠️")

    # ═══════════════════════════════════════════════════════════
    # Verify syntax Python
    # ═══════════════════════════════════════════════════════════
    section("VERIFY — Syntax check")
    try:
        import ast
        ast.parse(content)
        log("Python syntax OK", "✅")
    except SyntaxError as e:
        log(f"Syntax ERROR: {e}", "❌")
        log("Rollback...", "↩️")
        shutil.copy2(bak, TARGET)
        sys.exit(1)

    # ═══════════════════════════════════════════════════════════
    # Save
    # ═══════════════════════════════════════════════════════════
    if content != original:
        with open(TARGET, "w", encoding="utf-8") as f:
            f.write(content)
        section("HOÀN TẤT")
        log(f"Đã patch {total}/5 chỗ trong {TARGET}", "🎉")
        print("")
        print("  👉 Bước tiếp theo:")
        print("     1. python fix.py")
        print("     2. python patch_buttons.py")
        print("     3. Mở index.html → Ctrl+Shift+R")
        print("")
        print("  🧪 Test race condition:")
        print("     • DevTools → Network → Slow 3G")
        print("     • Hard refresh (Ctrl+Shift+R)")
        print("     • Bấm nút Chuyên ngành NGAY khi vừa load page")
        print("     • Phải thấy: nút mờ + spinner + toast 'Đang tải...'")
        print("     • Sau ~5s: nút sáng, bấm mở dropdown bình thường")
    else:
        log("Không có thay đổi (đã patch rồi?)", "ℹ️")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Hủy")
        sys.exit(1)
    except Exception as e:
        print(f"\n[❌] {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
