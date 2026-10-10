# -*- coding: utf-8 -*-
r"""
patch_buttons.py - Cover CSS nút dataset trong index.html.
                    - Parse số có chữ K/M (1K+, 1.5K+...)
                    - Giữ HTML gốc cho chuyen-nganh + favorites
                    - CSS icon match cả khi thiếu class ds-btn-icon
                    - FIX ACTIVE TAB: clear tab Yêu thích khi chuyển

Cách dùng:
    python patch_buttons.py
"""
import os
import re
import sys
import unicodedata


# =================================================================
#  CONFIG — NỘI DUNG TỪNG NÚT
# =================================================================
BUTTON_CONFIG = {
    "tonghop": {
        "icon": "fa-book-open",
        "title_html": "<b>1750+</b> Câu phản xạ",
        "sub": "Văn phòng · Công xưởng",
    },
    "tu-vung": {
        "icon": "",
        "title_html": "<b>11000+</b> Từ vựng HSK",
        "sub": "Mẹo nhớ · Bộ thủ",
    },
}

DEFAULT_CONFIG = {
    "icon": "fa-comments",
    "title_template": "<b>{count}</b> {name}",
    "sub_template": "Hội thoại thực tế",   # ⭐ ĐÃ SỬA từ "Câu giao tiếp"
}


# =================================================================
#  CSS — CHÈN VÀO INDEX.HTML
# =================================================================
BUTTONS_CSS = r"""
/* ═══════════════════════════════════════════════════════════ */
/* PATCH_BUTTONS: DATASET BUTTONS — 2 HÀNG GỌN                 */
/* ═══════════════════════════════════════════════════════════ */

.ds-main-row {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: .55rem;
    align-items: stretch;
}
@media (max-width: 1100px) {
    .ds-main-row { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 420px) {
    .ds-main-row { grid-template-columns: 1fr; }
}

/* ── Nút cơ bản ── */
.ds-btn {
    display: flex;
    align-items: center;
    gap: .65rem;
    padding: .65rem .8rem;
    min-height: 60px;
    height: 100%;
    border: 1.5px solid var(--border);
    border-radius: 12px;
    background: var(--surface);
    color: var(--text);
    font-family: inherit;
    text-align: left;
    cursor: pointer;
    transition: all .2s ease;
    position: relative;
    overflow: visible;
    pointer-events: auto;
    z-index: 1;
}
.ds-btn:hover {
    border-color: var(--primary);
    background: var(--surface-2);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px -6px rgba(15,23,42,.15);
}

/* ── Icon (match cả khi KHÔNG có .ds-btn-icon) ── */
.ds-btn > i:first-child,
.ds-btn > i.fas,
.ds-btn .ds-btn-icon {
    flex-shrink: 0;
    width: 36px;
    height: 36px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.05rem;
    background: linear-gradient(135deg, rgba(99,102,241,.14), rgba(139,92,246,.08));
    color: var(--primary);
    transition: all .2s;
    pointer-events: none;
}

/* ── Khối text 2 hàng ── */
.ds-btn .ds-btn-text {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: .12rem;
    pointer-events: auto;
    z-index: 2;
    position: relative;
}
.ds-btn .ds-btn-title {
    font-size: clamp(.78rem, 1vw, .9rem);
    font-weight: 700;
    color: var(--text);
    line-height: 1.2;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    letter-spacing: -.01em;
}
.ds-btn .ds-btn-title b {
    font-weight: 900;
    color: var(--text);
    margin-right: .15rem;
}
.ds-btn .ds-btn-sub {
    font-size: clamp(.62rem, .78vw, .72rem);
    font-weight: 600;
    color: var(--text-3);
    line-height: 1.25;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* ── Active ── */
.ds-btn.active {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    border-color: transparent;
    box-shadow: 0 6px 18px -4px rgba(124,58,237,.45);
    transform: translateY(-2px);
}
.ds-btn.active .ds-btn-icon,
.ds-btn.active > i:first-child,
.ds-btn.active > i.fas {
    background: rgba(255,255,255,.2);
    color: #fff;
}
.ds-btn.active .ds-btn-title,
.ds-btn.active .ds-btn-title b { color: #fff; }
.ds-btn.active .ds-btn-sub { color: rgba(255,255,255,.82); }

/* ═══ CHUYÊN NGÀNH ═══ */
.ds-btn[data-dataset-group="chuyen-nganh"] {
    padding-right: 2.2rem;
}
.ds-btn[data-dataset-group="chuyen-nganh"] .ds-arrow {
    position: absolute;
    right: .75rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: .7rem;
    color: var(--text-3);
    transition: transform .25s;
    pointer-events: none;
    z-index: 5;
}
.ds-btn[data-dataset-group="chuyen-nganh"].active .ds-arrow {
    transform: translateY(-50%) rotate(180deg);
    color: #fff;
}

/* ⭐ Badge NEW */
.ds-btn[data-dataset-group="chuyen-nganh"] .ds-new-badge {
    position: absolute;
    top: -8px;
    right: -8px;
    padding: .18rem .55rem;
    border-radius: 50px;
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: #fff;
    font-size: .58rem;
    font-weight: 900;
    letter-spacing: .5px;
    box-shadow: 0 2px 8px rgba(220,38,38,.5), 0 0 0 2px var(--surface);
    animation: dsNewPulse 1.6s ease-in-out infinite;
    z-index: 100;
    pointer-events: none;
    white-space: nowrap;
}
@keyframes dsNewPulse {
    0%,100% { transform: scale(1); }
    50%     { transform: scale(1.1); }
}

/* ═══ TỪ VỰNG PREMIUM ═══ */
.ds-btn[data-dataset="tu-vung"] {
    background: linear-gradient(135deg, #fffbeb, #fef3c7);
    border-color: rgba(245,158,11,.5);
}
.ds-btn[data-dataset="tu-vung"] .ds-btn-title,
.ds-btn[data-dataset="tu-vung"] .ds-btn-title b { color: #92400e; }
.ds-btn[data-dataset="tu-vung"] .ds-btn-sub { color: #b45309; }
.ds-btn[data-dataset="tu-vung"]:hover {
    border-color: #f59e0b;
    background: linear-gradient(135deg, #fef3c7, #fde68a);
}
.ds-btn[data-dataset="tu-vung"].active {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    border-color: transparent;
}
.ds-btn[data-dataset="tu-vung"].active .ds-btn-title,
.ds-btn[data-dataset="tu-vung"].active .ds-btn-title b { color: #fff; }
.ds-btn[data-dataset="tu-vung"].active .ds-btn-sub { color: rgba(255,255,255,.85); }

/* ⭐ Ẩn icon vương miện — MỌI LOẠI ICON */
.ds-btn[data-dataset="tu-vung"] > i,
.ds-btn[data-dataset="tu-vung"] > i.fas,
.ds-btn[data-dataset="tu-vung"] > i[class*="fa-"],
.ds-btn[data-dataset="tu-vung"] .ds-btn-icon,
.ds-btn[data-dataset="tu-vung"] .vocab-icon,
.ds-btn[data-dataset="tu-vung"] .vocab-crown {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important;
    height: 0 !important;
    opacity: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* ⭐ Badge PREMIUM */
.ds-btn[data-dataset="tu-vung"] .ds-vocab-badge,
.ds-btn[data-dataset="tu-vung"] [class*="vocab-badge"] {
    position: absolute;
    top: -8px;
    right: -8px;
    padding: .18rem .55rem;
    border-radius: 50px;
    background: linear-gradient(135deg, #7c3aed, #a855f7);
    color: #fff;
    font-size: .58rem;
    font-weight: 900;
    letter-spacing: .5px;
    text-transform: uppercase;
    box-shadow: 0 2px 8px rgba(124,58,237,.5), 0 0 0 2px var(--surface);
    pointer-events: none;
    white-space: nowrap;
    z-index: 100;
}

/* ═══ YÊU THÍCH ═══ */
.ds-btn[data-dataset-group="favorites"] {
    background: linear-gradient(135deg, #fef2f2, #fee2e2);
    border-color: rgba(239,68,68,.35);
    pointer-events: auto;
    cursor: pointer;
    z-index: 10;
}
.ds-btn[data-dataset-group="favorites"] .ds-btn-title,
.ds-btn[data-dataset-group="favorites"] .ds-btn-title b { color: #991b1b; }
.ds-btn[data-dataset-group="favorites"] .ds-btn-sub { color: #b91c1c; }
.ds-btn[data-dataset-group="favorites"].active {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    border-color: transparent;
}
.ds-btn[data-dataset-group="favorites"].active .ds-btn-title,
.ds-btn[data-dataset-group="favorites"].active .ds-btn-title b,
.ds-btn[data-dataset-group="favorites"].active .ds-btn-sub { color: #fff; }

/* ═══ DARK MODE ═══ */
[data-theme="dark"] .ds-btn .ds-btn-icon,
[data-theme="dark"] .ds-btn > i:first-child {
    background: linear-gradient(135deg, rgba(99,102,241,.28), rgba(139,92,246,.18));
}
[data-theme="dark"] .ds-btn[data-dataset="tu-vung"] {
    background: linear-gradient(135deg, rgba(245,158,11,.18), rgba(217,119,6,.12));
    border-color: rgba(245,158,11,.45);
}
[data-theme="dark"] .ds-btn[data-dataset="tu-vung"] .ds-btn-title,
[data-theme="dark"] .ds-btn[data-dataset="tu-vung"] .ds-btn-title b { color: #fcd34d; }
[data-theme="dark"] .ds-btn[data-dataset="tu-vung"] .ds-btn-sub { color: #fbbf24; }
[data-theme="dark"] .ds-btn[data-dataset-group="favorites"] {
    background: linear-gradient(135deg, rgba(239,68,68,.18), rgba(220,38,38,.1));
    border-color: rgba(239,68,68,.4);
}
[data-theme="dark"] .ds-btn[data-dataset-group="favorites"] .ds-btn-title,
[data-theme="dark"] .ds-btn[data-dataset-group="favorites"] .ds-btn-title b { color: #fca5a5; }
[data-theme="dark"] .ds-btn[data-dataset-group="favorites"] .ds-btn-sub { color: #f87171; }

/* ═══ MOBILE ═══ */
@media (max-width: 500px) {
    .ds-btn {
        min-height: 56px;
        padding: .55rem .7rem;
        gap: .5rem;
    }
    .ds-btn .ds-btn-icon,
    .ds-btn > i:first-child {
        width: 32px;
        height: 32px;
        font-size: .92rem;
        border-radius: 9px;
    }
    .ds-btn .ds-btn-title { font-size: .76rem; }
    .ds-btn .ds-btn-sub   { font-size: .6rem; }
}

/* ═══════════════════════════════════════════════════════════ */
/* ⭐ FIX CLICK — CHUYÊN NGÀNH + YÊU THÍCH BẤM ĐƯỢC            */
/* ═══════════════════════════════════════════════════════════ */

/* ── Nút CHUYÊN NGÀNH ── */
.ds-btn[data-dataset-group="chuyen-nganh"] {
    pointer-events: auto !important;
    cursor: pointer !important;
    z-index: 10 !important;
}
.ds-btn[data-dataset-group="chuyen-nganh"] > .ds-btn-text,
.ds-btn[data-dataset-group="chuyen-nganh"] > span:not(.ds-new-badge) {
    pointer-events: auto !important;
    z-index: 20 !important;
    position: relative !important;
}
.ds-btn[data-dataset-group="chuyen-nganh"] > i,
.ds-btn[data-dataset-group="chuyen-nganh"] > i.fas,
.ds-btn[data-dataset-group="chuyen-nganh"] > i.ds-btn-icon,
.ds-btn[data-dataset-group="chuyen-nganh"] > i.ds-arrow,
.ds-btn[data-dataset-group="chuyen-nganh"] > .ds-new-badge,
.ds-btn[data-dataset-group="chuyen-nganh"]::before,
.ds-btn[data-dataset-group="chuyen-nganh"]::after {
    pointer-events: none !important;
}

/* ── Nút YÊU THÍCH ── */
.ds-btn[data-dataset-group="favorites"] {
    pointer-events: auto !important;
    cursor: pointer !important;
    z-index: 10 !important;
}
.ds-btn[data-dataset-group="favorites"] > .ds-btn-text,
.ds-btn[data-dataset-group="favorites"] > span:not(.ds-fav-badge):not(.ds-fav-lock) {
    pointer-events: auto !important;
    z-index: 20 !important;
    position: relative !important;
}
.ds-btn[data-dataset-group="favorites"] > i,
.ds-btn[data-dataset-group="favorites"] > i.fas,
.ds-btn[data-dataset-group="favorites"] > i.ds-btn-icon,
.ds-btn[data-dataset-group="favorites"] > .ds-fav-badge,
.ds-btn[data-dataset-group="favorites"] > .ds-fav-lock,
.ds-btn[data-dataset-group="favorites"]::before,
.ds-btn[data-dataset-group="favorites"]::after {
    pointer-events: none !important;
}
"""


# =================================================================
#  HTML GENERATOR
# =================================================================
def build_button_html(config_key, extra=None):
    cfg = BUTTON_CONFIG.get(config_key)
    if cfg is None:
        cfg = dict(DEFAULT_CONFIG)
    else:
        cfg = dict(cfg)

    if extra:
        if "title_html" in extra:
            cfg["title_html"] = extra["title_html"]
        if "sub" in extra:
            cfg["sub"] = extra["sub"]
        if "icon" in extra:
            cfg["icon"] = extra["icon"]
        if "dataset_id" in extra:
            cfg["dataset_id"] = extra["dataset_id"]

    title = cfg.get("title_html")
    if not title and "title_template" in cfg:
        title = cfg["title_template"].format(
            count=(extra or {}).get("count", ""),
            name=(extra or {}).get("name", "")
        )
    if not title:
        title = config_key

    sub = cfg.get("sub")
    if not sub and "sub_template" in cfg:
        sub = cfg["sub_template"]
    if not sub:
        sub = ""

    icon = cfg.get("icon", "")
    extra_attrs = cfg.get("extra_attrs", "")
    extra_html = cfg.get("extra_html", "")

    if "dataset_id" in cfg:
        data_attr = 'data-dataset="' + cfg["dataset_id"] + '"'
    else:
        data_attr = 'data-dataset="' + config_key + '"'

    active_cls = " active" if config_key == "tonghop" else ""

    icon_html = ''
    if icon:
        icon_html = '            <i class="fas ' + icon + ' ds-btn-icon"></i>\n'

    return (
        '<button class="ds-btn ds-btn-primary' + active_cls + '" '
        + data_attr + ' ' + extra_attrs + '>\n'
        + icon_html +
        '            <span class="ds-btn-text">\n'
        '                <span class="ds-btn-title">' + title + '</span>\n'
        '                <span class="ds-btn-sub">' + sub + '</span>\n'
        '            </span>\n'
        '            ' + extra_html + '\n'
        '        </button>'
    )


# =================================================================
#  PATCH CSS
# =================================================================
def patch_css(html):
    """Chèn CSS mới — LUÔN XÓA CSS CŨ TRƯỚC."""
    pat_old = re.compile(
        r'/\* ═+ \*/\s*/\* PATCH_BUTTONS: DATASET BUTTONS.*?(?=</style>)',
        re.DOTALL
    )
    html, n_removed = pat_old.subn('', html)
    if n_removed > 0:
        print("   [clean] Da xoa " + str(n_removed) + " block CSS cu")

    pat = re.compile(r'(\s*)(</style>)', re.MULTILINE)
    html, n = pat.subn(
        lambda m: m.group(1) + BUTTONS_CSS + m.group(1) + m.group(2),
        html, count=1
    )
    if n == 0:
        print("   [!] Khong tim thay </style>")
    else:
        print("   [OK CSS] Da chen CSS 2 hang gon + fix click")
    return html


# =================================================================
#  PATCH BUTTONS
# =================================================================
def patch_button_tonghop(html):
    pat = re.compile(
        r'<button[^>]*class="[^"]*ds-btn[^"]*"[^>]*data-dataset="tonghop"[^>]*>.*?</button>',
        re.MULTILINE | re.DOTALL
    )
    new_html = build_button_html("tonghop")
    html, n = pat.subn(new_html, html, count=1)
    if n:
        print("   [OK] Patch nut Tong hop")
    else:
        print("   [!] Khong tim thay nut Tong hop")
    return html


def patch_button_tu_vung(html):
    pat = re.compile(
        r'<button[^>]*class="[^"]*ds-btn[^"]*"[^>]*data-dataset="tu-vung"[^>]*>.*?</button>',
        re.MULTILINE | re.DOTALL
    )
    if not pat.search(html):
        print("   [skip] Khong co nut Tu vung")
        return html
    new_html = build_button_html("tu-vung")
    html, n = pat.subn(new_html, html, count=1)
    if n:
        print("   [OK] Patch nut Tu vung")
    return html


def patch_other_buttons(html):
    """
    Patch các nút data-dataset khác (giao tiếp...).
    Parse số có chữ K/M — VD: "1K+", "1.5K+", "10M+".
    SKIP chuyen-nganh + favorites để giữ event listener.
    """
    pat_all = re.compile(
        r'<button[^>]*class="[^"]*ds-btn[^"]*"[^>]*data-dataset="([^"]+)"[^>]*>(.*?)</button>',
        re.MULTILINE | re.DOTALL
    )

    SKIP_IDS = {"tonghop", "tu-vung", "chuyen-nganh", "favorites"}

    def replacer(match):
        ds_id = match.group(1)
        if ds_id in SKIP_IDS:
            return match.group(0)

        inner = match.group(2)
        text = re.sub(r'<[^>]+>', ' ', inner)
        text = re.sub(r'\s+', ' ', text).strip()

        # Regex hỗ trợ "1K+", "1.5K+", "1000+", "10M+", "500"
        m = re.match(r'^([\d\.]+[KkMm]?\+?)\s+(.+)$', text)
        if m:
            count = m.group(1)
            name = m.group(2)
        else:
            count = ""
            name = text

        if '<br' in inner.lower():
            parts = re.split(r'<br\s*/?>', inner)
            if len(parts) >= 2:
                first = re.sub(r'<[^>]+>', ' ', parts[0]).strip()
                rest = ' '.join(
                    re.sub(r'<[^>]+>', ' ', p).strip()
                    for p in parts[1:]
                )
                m2 = re.match(r'^([\d\.]+[KkMm]?\+?)\s+(.+)$', first)
                if m2:
                    count = m2.group(1)
                    name = m2.group(2)
                sub = re.sub(r'\s+', ' ', rest).strip()
            else:
                sub = DEFAULT_CONFIG["sub_template"]
        else:
            sub = DEFAULT_CONFIG["sub_template"]

        title_html = "<b>" + count + "</b> " + name if count else name

        return build_button_html(
            "giao-tiep",
            extra={
                "dataset_id": ds_id,
                "title_html": title_html,
                "sub": sub,
                "icon": "fa-comments",
            }
        )

    html, n = pat_all.subn(replacer, html)
    if n:
        print("   [OK] Patch " + str(n) + " nut khac (giao tiep...)")
    return html


# =================================================================
#  ⭐ FIX ACTIVE TAB — clear tab Yêu thích khi chuyển tab khác
# =================================================================
def add_active_fix_js(html):
    """
    Thêm JS nhỏ vào cuối HTML để:
    - Khi bấm Chuyên ngành / Từ vựng / bất kỳ tab → clear active của Yêu thích
    - Khi bấm sub-ngành → clear Yêu thích + Từ vựng
    """
    MARKER = "/* PATCH_BUTTONS: FIX ACTIVE TAB */"
    if MARKER in html:
        print("   [skip JS] Da co fix active tab")
        return html

    js = """
<script>
/* PATCH_BUTTONS: FIX ACTIVE TAB */
(function() {
    'use strict';
    console.log('[patch_buttons] Fix active tab ready');

    function clearOthers(except) {
        document.querySelectorAll('.ds-btn, .ds-sub-btn').forEach(function(b) {
            if (b !== except) b.classList.remove('active');
        });
    }

    // Bấm bất kỳ nút dataset nào → clear Yêu thích ngay
    document.addEventListener('click', function(e) {
        var btn = e.target.closest('.ds-btn, .ds-sub-btn');
        if (!btn) return;

        // Nút Chuyên ngành (mở dropdown) → clear Yêu thích + Từ vựng
        if (btn.id === 'dsChuyenNganhBtn' ||
            btn.getAttribute('data-dataset-group') === 'chuyen-nganh') {

            var fav = document.querySelector('.ds-btn[data-dataset-group="favorites"]');
            if (fav) fav.classList.remove('active');
            var tv = document.querySelector('.ds-btn[data-dataset="tu-vung"]');
            if (tv) tv.classList.remove('active');
            return;
        }

        // Sub-ngành → clear Yêu thích + Từ vựng, active Chuyên ngành
        if (btn.classList.contains('ds-sub-btn')) {
            var fav2 = document.querySelector('.ds-btn[data-dataset-group="favorites"]');
            if (fav2) fav2.classList.remove('active');
            var tv2 = document.querySelector('.ds-btn[data-dataset="tu-vung"]');
            if (tv2) tv2.classList.remove('active');
            var cn = document.querySelector('.ds-btn[data-dataset-group="chuyen-nganh"]');
            if (cn) cn.classList.add('active');
            return;
        }

        // Các tab khác (Từ vựng, Tổng hợp, Giao tiếp...) → clear Yêu thích
        var favBtn = document.querySelector('.ds-btn[data-dataset-group="favorites"]');
        if (favBtn && btn !== favBtn) {
            favBtn.classList.remove('active');
        }
    }, true);
})();
</script>
"""

    pat = re.compile(r'(\s*)(</body>)', re.MULTILINE)
    html, n = pat.subn(
        lambda m: m.group(1) + js + m.group(1) + m.group(2),
        html, count=1
    )
    if n == 0:
        print("   [!] Khong tim thay </body>")
    else:
        print("   [OK JS] Da chen fix active tab")
    return html


# =================================================================
#  MAIN
# =================================================================
def patch_all_buttons(index_path="index.html"):
    print("=" * 62)
    print("[patch_buttons] Cover CSS nut + FIX ACTIVE TAB")
    print("=" * 62)

    if not os.path.isfile(index_path):
        print("[X] Khong thay " + index_path)
        return False

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    print("")
    print("[1/5] Patch CSS...")
    html = patch_css(html)

    print("")
    print("[2/5] Patch nut Tong hop...")
    html = patch_button_tonghop(html)

    print("")
    print("[3/5] Patch nut Tu vung...")
    html = patch_button_tu_vung(html)

    print("")
    print("[4/5] Patch nut khac (KHONG patch chuyen-nganh + favorites)...")
    html = patch_other_buttons(html)

    # ⭐ BƯỚC MỚI: Fix active tab
    print("")
    print("[5/5] Fix active tab khi chuyển...")
    html = add_active_fix_js(html)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)

    size_kb = os.path.getsize(index_path) / 1024
    print("")
    print("=" * 62)
    print("[patch_buttons] HOAN TAT!")
    print("[patch_buttons] File: " + index_path +
          " (" + str(round(size_kb, 1)) + " KB)")
    print("=" * 62)
    return True


if __name__ == "__main__":
    if not os.path.isfile("index.html") and os.path.isfile("../index.html"):
        os.chdir("..")
        print("[patch_buttons] Phat hien chay tu scripts/ -> chdir..")

    ok = patch_all_buttons("index.html")
    sys.exit(0 if ok else 1)
