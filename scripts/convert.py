# -*- coding: utf-8 -*-
"""Build HTML tự chứa từ Excel + templates."""

import json
import os
import sys
import glob
import re
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config_loader import load_config, print_banner, CONFIG_FILE
from data_reader import read_excel
from ui_template import build_ui_css, build_ui_html, build_ui_js
from social_template import (
    build_social_css, build_social_html, build_social_js,
    build_tiktok_bar_html
)
from accounts_template import (
    build_accounts_css, build_accounts_html,
    build_accounts_js, build_all_auth,
)
from intro_template import (
    build_intro_css, build_intro_html, build_intro_js,
)
from favorites_module import (
    build_favorites_css, build_favorites_html, build_favorites_js,
)
from chat_support import (
    build_chat_css, build_chat_html, build_chat_js,
    build_quota_html, build_quota_js, build_quota_init_js,
    build_online_section_html,
    build_config_js, build_telegram_notify_js,
)
from admin_chat_manager import (
    build_admin_chat_css, build_admin_chat_html, build_admin_chat_js,
)
from draggable_fab import (
    build_draggable_fab_css, build_draggable_fab_js,
)
from patch_grade_toggle import (
    patch_html, patch_css, patch_js, patch_grading_js,
)
from assemble_module import (
    build_assemble_css,
    build_assemble_html,
    build_assemble_js,
    inject_assemble_html,
)

def _js_str(s):
    if s is None:
        return ""
    return (str(s)
            .replace('\\', '\\\\')
            .replace('"', '\\"')
            .replace("'", "\\'")
            .replace('\n', '\\n')
            .replace('\r', '\\r')
            .replace('</', '<\\/'))


def _json_blob(obj, compact=True):
    if compact:
        s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    else:
        s = json.dumps(obj, ensure_ascii=False)
    return s.replace("</", "<\\/")


CONFIG = load_config()
print_banner(CONFIG)

EXCEL_FILE = CONFIG["excel_file"]
OUTPUT_HTML = CONFIG["output_html"]
SHEET_INDEX = CONFIG["sheet_index"]
DATA_DIR = CONFIG.get("data_dir", "data")

data_tonghop = read_excel(EXCEL_FILE, SHEET_INDEX)
print(f"📚 Tổng hợp: {len(data_tonghop)} câu")

ICON_MAP = {
    "nhân sự": "fa-users",
    "hành chính": "fa-briefcase",
    "hành chính - nhân sự": "fa-briefcase",
    "hành chính nhân sự": "fa-briefcase",
    "thu mua": "fa-shopping-cart",
    "xuất nhập khẩu": "fa-ship",
    "logistics": "fa-truck",
    "vận tải": "fa-truck",
    "kho": "fa-warehouse",
    "bán hàng": "fa-store",
    "kinh doanh": "fa-chart-line",
    "marketing": "fa-bullhorn",
    "dịch vụ khách hàng": "fa-headset",
    "chăm sóc khách hàng": "fa-headset",
    "kế toán": "fa-calculator",
    "tài chính": "fa-coins",
    "hành chính kế toán": "fa-file-invoice-dollar",
    "sản xuất": "fa-industry",
    "kế hoạch sản xuất": "fa-calendar-alt",
    "kỹ thuật": "fa-tools",
    "bảo trì": "fa-tools",
    "chất lượng": "fa-award",
    "qa": "fa-award",
    "qc": "fa-award",
    "r&d": "fa-flask",
    "nghiên cứu": "fa-flask",
    "giày da": "fa-shoe-prints",
    "may mặc": "fa-tshirt",
    "dệt may": "fa-tshirt",
    "thực phẩm": "fa-utensils",
    "nông nghiệp": "fa-seedling",
    "máy tính & it": "fa-laptop-code",
    "máy tính": "fa-laptop-code",
    "công nghệ thông tin": "fa-laptop-code",
    "it": "fa-laptop-code",
}

DEFAULT_ICON_NAME = "fa-folder"
UNIFIED_COLOR = "#7c3aed"


def auto_detect_icon_color(display_name):
    key = display_name.strip().lower()
    if key in ICON_MAP:
        return (ICON_MAP[key], UNIFIED_COLOR)
    words = re.split(r'[\s&\-_/,\.]+', key)
    for k in sorted(ICON_MAP.keys(), key=len, reverse=True):
        if k in words:
            return (ICON_MAP[k], UNIFIED_COLOR)
    for k in sorted(ICON_MAP.keys(), key=len, reverse=True):
        if len(k) >= 3 and k in key:
            return (ICON_MAP[k], UNIFIED_COLOR)
    return (DEFAULT_ICON_NAME, UNIFIED_COLOR)


def slugify_dataset_id(filename):
    base = filename.rsplit(".", 1)[0]
    base = unicodedata.normalize("NFD", base)
    base = "".join(c for c in base if unicodedata.category(c) != "Mn")
    base = base.replace("đ", "d").replace("Đ", "D")
    base = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower()
    return base or "dataset"


DATASET_REGISTRY = {
    "tonghop": {
        "id": "tonghop",
        "name": f"{len(data_tonghop)} câu phản xạ tổng hợp VPCX",
        "icon": "fa-book-open",
        "color": "#4f46e5",
        "data": data_tonghop,
        "count": len(data_tonghop),
        "source": EXCEL_FILE,
    }
}

_tonghop_abs = os.path.abspath(EXCEL_FILE)
_chuyen_nganh_count = 0

if os.path.isdir(DATA_DIR):
    excel_files = []
    for ext in ("*.xlsx", "*.xls", "*.csv"):
        excel_files.extend(glob.glob(os.path.join(DATA_DIR, ext)))
    excel_files.sort()

    print(f"\n🔍 Quét '{DATA_DIR}/' — {len(excel_files)} file Excel")

    for filepath in excel_files:
        filename = os.path.basename(filepath)
        if filename.startswith("~$"):
            continue
        if os.path.abspath(filepath) == _tonghop_abs:
            print(f"⏭️  {filename} — bỏ qua (file tổng hợp)")
            continue

        try:
            sub_data = read_excel(filepath, 0)
            if not sub_data:
                print(f"⚠️  {filename}: rỗng")
                continue

            display_name = filename.rsplit(".", 1)[0].replace("_", " ").strip()
            display_name = unicodedata.normalize("NFC", display_name)
            if display_name.islower() or display_name.isupper():
                display_name = display_name.title()

            dataset_id = slugify_dataset_id(filename)
            base_id = dataset_id
            counter = 2
            while dataset_id in DATASET_REGISTRY:
                dataset_id = f"{base_id}-{counter}"
                counter += 1

            icon, color = auto_detect_icon_color(display_name)

            DATASET_REGISTRY[dataset_id] = {
                "id": dataset_id,
                "name": display_name,
                "icon": icon,
                "color": color,
                "data": sub_data,
                "count": len(sub_data),
                "source": filename,
            }
            _chuyen_nganh_count += 1
            print(f"🏭 {display_name:25s} ({filename}) — {len(sub_data)} câu")
        except Exception as e:
            print(f"❌ Lỗi đọc {filename}: {e}")
            continue

    if _chuyen_nganh_count == 0:
        print(f"ℹ️  Không có file chuyên ngành nào.")
else:
    print(f"\nℹ️  Chưa có thư mục '{DATA_DIR}/'.")

DATA_OUTPUT_DIR = "data"
os.makedirs(DATA_OUTPUT_DIR, exist_ok=True)

dataset_registry_meta = {}
for _ds_id, _ds in DATASET_REGISTRY.items():
    dataset_registry_meta[_ds_id] = {
        "id": _ds["id"],
        "name": _ds["name"],
        "icon": _ds["icon"],
        "color": _ds["color"],
        "count": _ds["count"],
        "source": _ds["source"],
    }

all_datasets_data = {}
for _ds_id, _ds in DATASET_REGISTRY.items():
    all_datasets_data[_ds_id] = _ds["data"]

with open(os.path.join(DATA_OUTPUT_DIR, "all_datasets.json"), "w", encoding="utf-8") as _f:
    json.dump(all_datasets_data, _f, ensure_ascii=False, separators=(",", ":"))

with open(os.path.join(DATA_OUTPUT_DIR, "dataset_registry.json"), "w", encoding="utf-8") as _f:
    json.dump(dataset_registry_meta, _f, ensure_ascii=False, separators=(",", ":"))

print(f"💾 Ghi data/all_datasets.json ({os.path.getsize(os.path.join(DATA_OUTPUT_DIR, 'all_datasets.json'))/1024:.1f} KB)")
print(f"💾 Ghi data/dataset_registry.json")

dataset_registry_json = _json_blob(dataset_registry_meta)
json_data = "[]"
firebase_config_json = _json_blob(CONFIG["firebase_config"])
synonyms_json = _json_blob(CONFIG["synonyms"])
fillers_json = _json_blob(CONFIG["filler_words"])
onboarding_config_json = _json_blob(CONFIG.get("onboarding", {}))

telegram_bot_token = CONFIG.get("telegram_bot_token", "")
telegram_chat_id = CONFIG.get("telegram_chat_id", "")

auth_css, auth_html, auth_js = build_all_auth(CONFIG)

if '<!-- __ADMIN_ONLINE_SECTION__ -->' in auth_html:
    auth_html = auth_html.replace(
        '<!-- __ADMIN_ONLINE_SECTION__ -->',
        build_online_section_html()
    )
    print("✅ Chèn User Online section")
else:
    print("⚠️  Thiếu placeholder __ADMIN_ONLINE_SECTION__")

if '<!-- __ADMIN_QUOTA_SECTION__ -->' in auth_html:
    auth_html = auth_html.replace(
        '<!-- __ADMIN_QUOTA_SECTION__ -->',
        build_quota_html()
    )
    print("✅ Chèn Quota Dashboard")
else:
    print("⚠️  Thiếu placeholder __ADMIN_QUOTA_SECTION__")


FULLWIDTH_CSS = r"""
.page-wrap{width:100%;max-width:100%;margin:0 auto;overflow-x:hidden}
.container{width:100%!important;max-width:100%!important;margin-left:auto!important;margin-right:auto!important;padding-left:1.25rem!important;padding-right:1.25rem!important}
.sticky-top{position:relative!important;width:100%!important;max-width:100%!important}
.main,#mainContent{width:100%!important;max-width:100%!important}
.search-bar{width:100%!important;max-width:100%!important}
.search-bar input{width:100%!important;max-width:100%!important}
.filters{display:grid!important;width:100%!important;max-width:100%!important;grid-template-columns:1fr 1fr!important;gap:.75rem!important}
@media(min-width:1000px){.filters{grid-template-columns:220px 260px!important;gap:1rem!important}}
.result-count{margin-top:.5rem!important}
.mobile-view{display:grid!important;width:100%!important;max-width:100%!important;margin-left:auto!important;margin-right:auto!important;gap:1rem!important;grid-template-columns:1fr!important}
@media(min-width:769px){.mobile-view{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:1.1rem!important}}
@media(min-width:1800px){.mobile-view{grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:1.2rem!important}}
@media(min-width:2400px){.mobile-view{grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:1.3rem!important}}
.demo-banner,.expiry-banner{width:100%!important;max-width:100%!important;margin-left:auto!important;margin-right:auto!important;margin-bottom:1rem!important}
@media(min-width:1000px){.container{padding-left:1.5rem!important;padding-right:1.5rem!important}}
@media(min-width:1400px){.container{padding-left:2rem!important;padding-right:2rem!important}}
@media(min-width:1900px){.container{padding-left:2.5rem!important;padding-right:2.5rem!important}}
@media(max-width:768px){.container{padding-left:.7rem!important;padding-right:.7rem!important}.mobile-view{gap:.8rem!important}}
.practice-full-modal{position:fixed!important;inset:0!important;z-index:2500!important;display:none;flex-direction:column!important;overflow:hidden!important}
.practice-full-modal.show{display:flex!important}
.practice-full-header,.pf-filters,.practice-full-nav{flex:0 0 auto!important}
.practice-full-body{flex:1 1 auto!important;min-height:0!important;overflow-y:auto!important}
.practice-full-input{width:100%!important;text-align:center!important;font-size:clamp(1.15rem,2.2vw,1.6rem)!important}
@media(min-width:769px){.ds-main-row{grid-template-columns:1fr 1fr 1fr!important}}
@media(max-width:768px){.ds-main-row{grid-template-columns:1fr 1fr!important}}
@media(max-width:500px){.ds-main-row{grid-template-columns:1fr!important}}
.header{position:relative;padding:.25rem 0}
.header-inner{display:flex!important;align-items:center!important;justify-content:space-between!important;width:100%!important;gap:1rem!important}
.logo{flex:1 1 auto!important;min-width:0!important;display:flex!important;align-items:center!important;gap:.9rem!important}
.logo-icon{width:clamp(46px,4.5vw,58px)!important;height:clamp(46px,4.5vw,58px)!important;border-radius:clamp(12px,1.2vw,16px)!important;background:linear-gradient(135deg,#6366f1 0%,#8b5cf6 40%,#d946ef 100%)!important;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff!important;font-size:clamp(1.2rem,1.8vw,1.6rem)!important;flex-shrink:0!important;position:relative!important;overflow:hidden!important;box-shadow:0 6px 20px rgba(139,92,246,.45),0 2px 6px rgba(139,92,246,.3),inset 0 1px 0 rgba(255,255,255,.25)!important;transition:transform .35s cubic-bezier(.34,1.56,.64,1),box-shadow .35s ease!important}
.logo-icon::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.35) 50%,transparent 70%);transform:translateX(-100%) rotate(25deg);transition:transform .8s ease;pointer-events:none}
.logo-icon:hover::before{transform:translateX(100%) rotate(25deg)}
.logo-icon::after{content:'';position:absolute;inset:0;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,.4),transparent 55%);pointer-events:none}
.logo-icon:hover{transform:translateY(-2px) rotate(-4deg) scale(1.04);box-shadow:0 10px 28px rgba(139,92,246,.6),0 4px 10px rgba(139,92,246,.4),inset 0 1px 0 rgba(255,255,255,.3)!important}
.logo-text{display:flex!important;flex-direction:column!important;line-height:1.1!important;min-width:0!important;overflow:hidden!important;gap:4px!important}
.logo-text .title{font-size:clamp(1.25rem,1.9vw,1.7rem)!important;font-weight:900!important;letter-spacing:-.025em!important;line-height:1.15!important;background:linear-gradient(135deg,#1e293b 0%,#4f46e5 50%,#7c3aed 100%)!important;-webkit-background-clip:text!important;background-clip:text!important;-webkit-text-fill-color:transparent!important;color:transparent!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important;position:relative!important}
[data-theme="dark"] .logo-text .title{background:linear-gradient(135deg,#f1f5f9 0%,#a5b4fc 50%,#c4b5fd 100%)!important;-webkit-background-clip:text!important;background-clip:text!important;-webkit-text-fill-color:transparent!important}
.logo-text .subtitle{display:inline-flex!important;align-items:center!important;gap:.4rem!important;padding:.25rem .7rem!important;border-radius:999px!important;background:linear-gradient(135deg,rgba(99,102,241,.13) 0%,rgba(139,92,246,.13) 50%,rgba(217,70,239,.13) 100%)!important;border:1px solid rgba(139,92,246,.3)!important;color:#5b21b6!important;font-size:clamp(.68rem,.85vw,.78rem)!important;font-weight:700!important;letter-spacing:.02em!important;margin-top:3px!important;padding-left:.6rem!important;width:fit-content!important;max-width:100%!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important;box-shadow:0 1px 3px rgba(139,92,246,.12),inset 0 1px 0 rgba(255,255,255,.5)!important;transition:transform .3s ease,box-shadow .3s ease!important}
.logo-text .subtitle:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(139,92,246,.25),inset 0 1px 0 rgba(255,255,255,.6)!important}
.logo-text .subtitle::before{content:'✦';display:inline-flex!important;align-items:center!important;justify-content:center!important;color:#d946ef!important;font-size:.9em!important;font-weight:900!important;line-height:1!important;flex-shrink:0!important;text-shadow:0 0 6px rgba(217,70,239,.7),0 0 12px rgba(139,92,246,.5)!important;animation:sparkleSubtitle 2.5s ease-in-out infinite!important}
@keyframes sparkleSubtitle{0%,100%{opacity:.65;transform:scale(1) rotate(0deg)}50%{opacity:1;transform:scale(1.2) rotate(18deg);text-shadow:0 0 10px rgba(217,70,239,.9),0 0 18px rgba(139,92,246,.7)}}
[data-theme="dark"] .logo-text .subtitle{background:linear-gradient(135deg,rgba(99,102,241,.28) 0%,rgba(139,92,246,.28) 50%,rgba(217,70,239,.28) 100%)!important;border-color:rgba(165,180,252,.45)!important;color:#ddd6fe!important;box-shadow:0 1px 3px rgba(0,0,0,.3),inset 0 1px 0 rgba(255,255,255,.08)!important}
[data-theme="dark"] .logo-text .subtitle::before{color:#f0abfc!important;text-shadow:0 0 8px rgba(240,171,252,.9),0 0 16px rgba(165,180,252,.6)!important}
.header-actions{flex:0 0 auto!important;margin-left:auto!important;display:flex!important;gap:.5rem!important;align-items:center!important}
.header-actions .icon-btn{width:clamp(34px,3vw,40px)!important;height:clamp(34px,3vw,40px)!important;border-radius:11px!important;border:1.5px solid var(--border)!important;background:var(--surface)!important;color:var(--text-2)!important;font-size:clamp(.82rem,1vw,.95rem)!important;transition:transform .25s cubic-bezier(.34,1.56,.64,1),background .25s ease,color .25s ease,border-color .25s ease,box-shadow .25s ease!important;box-shadow:0 1px 3px rgba(15,23,42,.05)!important}
.header-actions .icon-btn:hover{background:linear-gradient(135deg,#eff6ff,#ede9fe)!important;color:#4f46e5!important;border-color:#a5b4fc!important;transform:translateY(-2px) scale(1.05)!important;box-shadow:0 6px 16px rgba(139,92,246,.25)!important}
[data-theme="dark"] .header-actions .icon-btn:hover{background:linear-gradient(135deg,rgba(59,130,246,.2),rgba(139,92,246,.25))!important;color:#a5b4fc!important;border-color:rgba(165,180,252,.5)!important}
.header-actions .trial-badge{position:relative!important;overflow:hidden!important;background:linear-gradient(135deg,#fbbf24 0%,#f59e0b 50%,#ea580c 100%)!important;color:#fff!important;font-weight:800!important;letter-spacing:.03em!important;border:none!important;box-shadow:0 3px 10px rgba(245,158,11,.4),inset 0 1px 0 rgba(255,255,255,.3)!important;text-shadow:0 1px 1px rgba(0,0,0,.15)!important}
.header-actions .trial-badge::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.5),transparent);animation:shimmerBadge 2.8s infinite;pointer-events:none}
@keyframes shimmerBadge{0%{left:-100%}60%,100%{left:200%}}
.header-actions .demo-badge{background:linear-gradient(135deg,#fef3c7,#fde68a)!important;color:#78350f!important;font-weight:800!important;letter-spacing:.04em!important;border:1.5px solid #f59e0b!important;box-shadow:0 2px 8px rgba(245,158,11,.25)!important}
@media(max-width:768px){.logo{gap:.65rem!important}.logo-icon{width:44px!important;height:44px!important;border-radius:11px!important;font-size:1.15rem!important}.logo-text{gap:3px!important}.logo-text .title{font-size:1.15rem!important}.logo-text .subtitle{font-size:.6rem!important;padding:.2rem .55rem!important;gap:.35rem!important}.header-inner{gap:.5rem!important}.header-actions{gap:.35rem!important}.header-actions .icon-btn{width:34px!important;height:34px!important;font-size:.82rem!important}}
@media(max-width:400px){.logo-text .subtitle{display:none!important}.logo-icon{width:40px!important;height:40px!important;font-size:1rem!important}.logo-text .title{font-size:1.05rem!important}}
"""

full_css = (
    patch_css(build_ui_css())
    + "\n/* SOCIAL */\n" + build_social_css()
    + "\n/* ACCOUNTS */\n" + auth_css
    + "\n/* INTRO */\n" + build_intro_css()
    + "\n/* FAVORITES */\n" + build_favorites_css()
    + "\n/* CHAT */\n" + build_chat_css()
    + "\n/* ADMIN CHAT */\n" + build_admin_chat_css()
    + "\n/* DRAGGABLE FAB */\n" + build_draggable_fab_css()
    + "\n/* ASSEMBLE */\n" + build_assemble_css()
    + "\n/* FULLWIDTH */\n" + FULLWIDTH_CSS
)
ui_html = build_ui_html()
ui_html = patch_html(ui_html)
ui_html = inject_assemble_html(ui_html)
ui_html = ui_html.replace("<!-- __TIKTOK_BAR__ -->", build_tiktok_bar_html())
ui_html = ui_html.replace("<!-- __QUICK_INTRO_BANNER__ -->", build_intro_html())

_fav_html = build_favorites_html()

ui_html = ui_html.replace(
    '<!-- __FAV_DATASET_TAB__ -->',
    _fav_html["dataset_tab"]
)
if 'data-dataset-group="favorites"' in ui_html:
    print("✅ Chèn tab Yêu thích")
else:
    print("⚠️  Chưa chèn tab Yêu thích")

_pf_buttons = _fav_html["pf_float_btn"] + '\n' + _fav_html["pf_fav_only_btn"]
ui_html = ui_html.replace(
    '<a class="pf-tiktok-float" id="pfTiktokFloat"',
    _pf_buttons + '\n<a class="pf-tiktok-float" id="pfTiktokFloat"'
)

_dd_patterns = [
    r'(<button[^>]*class="[^"]*ds-dropdown-item[^"]*"[^>]*data-dataset-group="chuyen-nganh"[^>]*>.*?</button>)',
    r'(<button[^>]*id="dsChuyenNganhDropdownItem"[^>]*>.*?</button>)',
    r'(<a[^>]*class="[^"]*ds-dropdown-item[^"]*"[^>]*data-dataset-group="chuyen-nganh"[^>]*>.*?</a>)',
]

_dd_inserted = False
for _pat in _dd_patterns:
    if _dd_inserted:
        break
    _new, _n = re.subn(
        _pat,
        r'\1\n            ' + _fav_html["dataset_dropdown_item"],
        ui_html,
        count=1,
        flags=re.DOTALL
    )
    if _n > 0:
        ui_html = _new
        _dd_inserted = True
        print("✅ Chèn 'Yêu thích' vào dropdown")

if not _dd_inserted:
    print("⚠️  Chưa chèn được 'Yêu thích' vào dropdown")

social_html = build_social_html()
ui_html = ui_html.replace(
    '<div class="writer-modal" id="writerModal">',
    social_html + '\n<div class="writer-modal" id="writerModal">'
)

full_body = (
    '<div class="page-wrap">\n'
    + ui_html
    + "\n" + auth_html
    + "\n" + build_chat_html()
    + "\n" + build_admin_chat_html()
    + '\n</div>'
)


def _build_grading_js():
    js = r"""
var GRADING_API_URL = 'https://chinese-grading.onrender.com/check';

var _GRADING_FALLBACK_MESSAGES = {
    'correct': 'Đúng hoàn toàn',
    'partial': 'Gần đúng',
    'wrong':   'Sai'
};

var _VIETNAMESE_DIACRITICS_REGEX = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i;

var _PUNCT_CLEAN_REGEX = /[\s。，！？、；：""''「」『』（）《》〈〉【】〔〕?!.,;:'"()\[\]{}\-~`@#$%^&*+=|\\/<>]/g;

function _cleanForCompare(str) {
    if (!str) return '';
    return String(str).replace(_PUNCT_CLEAN_REGEX, '');
}

function _normalizeGradingMessage(result) {
    if (!result) return 'Sai';
    var serverMsg = (result.message || '').trim();
    var status = result.status || 'wrong';
    var fallback = _GRADING_FALLBACK_MESSAGES[status] || 'Sai';
    if (!serverMsg) return fallback;
    if (_VIETNAMESE_DIACRITICS_REGEX.test(serverMsg)) return serverMsg;
    return fallback;
}

function _formatGradingErrors(errors) {
    if (!errors || !errors.length) return '';

    var HANZI = function(ch, idx) {
        return '<span class="err-hanzi" data-error-idx="' + idx + '">' +
               escapeHtml(ch) + '</span>';
    };
    var PINYIN = function(py) {
        return py ? '<span class="err-pinyin">' + escapeHtml(py) + '</span>' : '';
    };
    var INFO = function(ch) {
        if (!ch) return '';
        return '<button class="err-info-btn" type="button" ' +
               'data-char="' + escapeHtml(ch) + '" ' +
               'onclick="showMnemonic(event, this)" ' +
               'title="Xem mẹo nhớ cho ' + escapeHtml(ch) + '">' +
               '<i class="fas fa-lightbulb"></i> Xem' +
               '</button>';
    };
    var ARROW = '<span class="err-arrow">→</span>';

    return errors.map(function(e, idx) {
        if (!e) return '';

        var targetIdx = (typeof e.input_position === 'number')
                        ? e.input_position
                        : idx;

        var inner = '';

        if (e.type === 'wrong') {
            inner = HANZI(e.user || '', targetIdx) + PINYIN(e.user_pinyin) +
                    INFO(e.user) +
                    ARROW +
                    HANZI(e.correct || '', targetIdx) + PINYIN(e.correct_pinyin) +
                    INFO(e.correct);
        } else if (e.type === 'missing') {
            inner = '<span class="err-label">Thiếu</span> ' +
                    HANZI(e.correct || '', targetIdx) + PINYIN(e.correct_pinyin) +
                    INFO(e.correct);
        } else if (e.type === 'extra') {
            inner = '<span class="err-label">Thừa</span> ' +
                    HANZI(e.user || '', targetIdx) + PINYIN(e.user_pinyin) +
                    INFO(e.user);
        } else {
            return '';
        }

        return '<span class="err-item">' + inner + '</span>';
    }).filter(Boolean).join('');
}

async function gradeWithAPI(userAnswer, correctAnswer) {
    try {
        var controller = new AbortController();
        var timeoutId = setTimeout(function() { controller.abort(); }, 15000);
        var res = await fetch(GRADING_API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                user_answer: userAnswer,
                correct_answer: correctAnswer
            }),
            signal: controller.signal
        });
        clearTimeout(timeoutId);
        if (!res.ok) return null;
        return await res.json();
    } catch(e) {
        console.warn('[Grading] API error:', e);
        return null;
    }
}
window.gradeWithAPI = gradeWithAPI;

(function() {
    var _origCheckInput = window.checkInput;
    window.checkInput = async function(input) {
        var answer = input.dataset.answer;
        var val = input.value.trim();
        if (typeof updateInlinePreview === 'function') updateInlinePreview(input, answer);
        var wrap = input.closest('.card-practice');
        var btn = wrap ? wrap.querySelector('.toggle-check-btn') : null;
        var isVisible = btn && btn.dataset.visible === '1';
        if (!isVisible) return;
        if (!val) {
            var stt0 = input.dataset.stt;
            document.querySelectorAll('[data-check-stt="' + stt0 + '"]').forEach(function(c) { c.innerHTML = ''; });
            return;
        }

        var cleanUser = _cleanForCompare(val);
        var cleanAnswer = _cleanForCompare(answer);
        var answerLen = cleanAnswer.length;
        var userLen = cleanUser.length;
        if (answerLen > 0 && userLen < answerLen) {
            if (cleanAnswer.substring(0, userLen) === cleanUser) {
                var stt0b = input.dataset.stt;
                document.querySelectorAll('[data-check-stt="' + stt0b + '"]')
                    .forEach(function(c) {
                        c.innerHTML = '<span class="ai-reason">Đang gõ... (' +
                                      userLen + '/' + answerLen + ')</span>';
                    });
                return;
            }
        }

        var stt = input.dataset.stt;
        var cells = document.querySelectorAll('[data-check-stt="' + stt + '"]');
        cells.forEach(function(c) { c.innerHTML = '<span class="ai-reason">Đang chấm...</span>'; });
        var result = await gradeWithAPI(val, answer);
        if (!result) {
            if (typeof _origCheckInput === 'function') return _origCheckInput.call(this, input);
            return;
        }
        var msg = _normalizeGradingMessage(result);
        var html = '';
        if (result.status === 'correct') {
            html = '<span class="ai-correct">' + msg + '</span>';
        } else if (result.status === 'partial') {
            var pct = result.score ? ' (' + result.score + '%)' : '';
            html = '<span class="ai-partial">' + msg + pct + '</span>';
        } else {
            html = '<span class="ai-wrong">' + msg + '</span>';
        }
        var detail = _formatGradingErrors(result.errors);
        if (detail) html += '<span class="ai-reason">' + detail + '</span>';
        var answerHtml = '<div class="answer-inline-display">' +
            '<span class="answer-inline-label"><i class="fas fa-check-circle"></i> Đáp án:</span>' +
            '<span class="answer-inline-text">' + escapeHtml(answer) + '</span>' +
            '</div>';
        cells.forEach(function(c) { c.innerHTML = html + answerHtml; });
    };
    console.log('[Grading] checkInput override OK');
})();

(function() {
    var _origCheckFullAnswer = window.checkFullAnswer;
    var _pfGradeToken = 0;
    var _pfDebounceTimer = null;

    window.checkFullAnswer = function() {
        clearTimeout(_pfDebounceTimer);
        _pfDebounceTimer = setTimeout(function() { _doCheckFullAnswer(); }, 400);
    };

    async function _doCheckFullAnswer() {
        if (typeof pfGradeEnabled !== 'undefined' && !pfGradeEnabled) {
            return;
        }

        var input = document.getElementById('pfInput');
        var statusEl = document.getElementById('pfStatus');
        if (!input || !statusEl) return;

        var val = input.value.trim();

        if (!val) {
            statusEl.innerHTML = '';
            statusEl.className = 'practice-full-status';
            return;
        }

        var answer = (typeof pfCurrentAnswer !== 'undefined') ? pfCurrentAnswer : '';
        if (!answer) return;

        var cleanUser = _cleanForCompare(val);
        var cleanAnswer = _cleanForCompare(answer);
        var answerLen = cleanAnswer.length;
        var userLen = cleanUser.length;

        if (userLen < answerLen) {
            var isPrefixCorrect = cleanAnswer.substring(0, userLen) === cleanUser;
            if (isPrefixCorrect) {
                statusEl.innerHTML = '<span class="ai-reason">Đang gõ... (' +
                                     userLen + '/' + answerLen + ')</span>';
                statusEl.className = 'practice-full-status';
                return;
            }
        }

        var myToken = ++_pfGradeToken;

        statusEl.innerHTML = '<span class="ai-reason">Đang chấm...</span>';
        statusEl.className = 'practice-full-status';

        var result = await gradeWithAPI(val, answer);

        if (myToken !== _pfGradeToken) return;
        if (input.value.trim() !== val) return;

        if (!result) {
            if (typeof _origCheckFullAnswer === 'function') {
                return _origCheckFullAnswer.apply(this, arguments);
            }
            return;
        }

        var msg = _normalizeGradingMessage(result);
        var html = '';

        if (result.status === 'correct') {
            html = '<span class="ai-correct">' + msg + '</span>';
            statusEl.className = 'practice-full-status correct';
        } else if (result.status === 'partial') {
            var pct = result.score ? ' (' + result.score + '%)' : '';
            html = '<span class="ai-partial">' + msg + pct + '</span>';
            statusEl.className = 'practice-full-status partial';
        } else {
            html = '<span class="ai-wrong">' + msg + '</span>';
            statusEl.className = 'practice-full-status wrong';
        }

        var detail = _formatGradingErrors(result.errors);
        if (detail) html += '<span class="ai-reason">' + detail + '</span>';

        statusEl.innerHTML = html;
    }

    console.log('[Grading] checkFullAnswer override OK');
})();

(function() {
    var _origFixCharAt = window.fixCharAt;

    window.highlightGradingErrorByIdx = function(idx) {
        var statusEl = document.getElementById('pfStatus');
        if (!statusEl) return;

        statusEl.querySelectorAll('.err-item.highlight').forEach(function(el) {
            el.classList.remove('highlight');
        });

        var targets = statusEl.querySelectorAll('.err-hanzi[data-error-idx="' + idx + '"]');
        if (!targets.length) return;

        var itemsToHighlight = new Set();
        targets.forEach(function(t) {
            var item = t.closest('.err-item');
            if (item) itemsToHighlight.add(item);
        });

        if (itemsToHighlight.size === 0) return;

        itemsToHighlight.forEach(function(item) {
            item.classList.add('highlight');
        });

        var firstItem = itemsToHighlight.values().next().value;
        try {
            firstItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } catch(e) {}

        setTimeout(function() {
            statusEl.querySelectorAll('.err-item.highlight').forEach(function(el) {
                el.classList.remove('highlight');
            });
        }, 2000);
    };

    window.fixCharAt = function(idx, el) {
        if (typeof _origFixCharAt === 'function') {
            _origFixCharAt.call(this, idx, el);
        }
        if (typeof window.highlightGradingErrorByIdx === 'function') {
            window.highlightGradingErrorByIdx(idx);
        }
    };

    console.log('[Grading] fixCharAt override OK');
})();

var VOCAB_API_URL = 'https://chinese-vocab-api.onrender.com';
var _mnemonicCache = {};

function _loadMnemonicCache() {
    try {
        var cached = localStorage.getItem('mnemonic_cache_v1');
        if (cached) {
            _mnemonicCache = JSON.parse(cached) || {};
        }
    } catch(e) {
        _mnemonicCache = {};
    }
}

function _saveMnemonicCache() {
    try {
        localStorage.setItem('mnemonic_cache_v1', JSON.stringify(_mnemonicCache));
    } catch(e) {}
}

async function fetchMnemonic(char) {
    if (!char) return null;

    if (_mnemonicCache[char]) {
        return _mnemonicCache[char];
    }

    var controller = new AbortController();
    var timeoutId = setTimeout(function() { controller.abort(); }, 12000);

    try {
        var res = await fetch(VOCAB_API_URL + '/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ char: char }),
            signal: controller.signal
        });
        clearTimeout(timeoutId);

        if (!res.ok) throw new Error('HTTP ' + res.status);

        var json = await res.json();
        if (!json.ok || !json.data) throw new Error('Invalid response');

        _mnemonicCache[char] = json.data;
        _saveMnemonicCache();

        return json.data;
    } catch(e) {
        clearTimeout(timeoutId);
        console.warn('[Mnemonic] Fetch error for "' + char + '":', e);
        return null;
    }
}

function _lookupMeaning(char) {
    if (!char) return { meaning: '', pinyin: '' };

    try {
        if (window.FIXPY_DATASETS) {
            var vocabList = null;
            var keys = Object.keys(window.FIXPY_DATASETS);

            for (var i = 0; i < keys.length; i++) {
                var ds = window.FIXPY_DATASETS[keys[i]];
                if (ds && ds.data && Array.isArray(ds.data) && ds.data.length >= 1000) {
                    vocabList = ds.data;
                    break;
                }
            }

            if (!vocabList && keys.length > 0) {
                var ds0 = window.FIXPY_DATASETS[keys[0]];
                if (ds0 && ds0.data) vocabList = ds0.data;
            }

            if (vocabList) {
                for (var j = 0; j < vocabList.length; j++) {
                    if (vocabList[j].zh === char) {
                        return {
                            meaning: vocabList[j].vi || '',
                            pinyin: vocabList[j].pinyin || ''
                        };
                    }
                }
                for (var k = 0; k < vocabList.length; k++) {
                    if (vocabList[k].zh && vocabList[k].zh.indexOf(char) !== -1) {
                        return {
                            meaning: vocabList[k].vi || '',
                            pinyin: vocabList[k].pinyin || ''
                        };
                    }
                }
            }
        }
    } catch(e) {}

    try {
        if (typeof RAW_DATA !== 'undefined' && RAW_DATA && RAW_DATA.length > 0) {
            for (var m = 0; m < RAW_DATA.length; m++) {
                if (RAW_DATA[m].zh === char) {
                    return {
                        meaning: RAW_DATA[m].vi || '',
                        pinyin: RAW_DATA[m].pinyin || ''
                    };
                }
            }
            for (var n = 0; n < RAW_DATA.length; n++) {
                if (RAW_DATA[n].zh && RAW_DATA[n].zh.indexOf(char) !== -1) {
                    return {
                        meaning: RAW_DATA[n].vi || '',
                        pinyin: RAW_DATA[n].pinyin || ''
                    };
                }
            }
        }
    } catch(e) {}

    try {
        if (typeof DATASET_REGISTRY !== 'undefined' && DATASET_REGISTRY) {
            var dsKeys = Object.keys(DATASET_REGISTRY);
            for (var p = 0; p < dsKeys.length; p++) {
                var ds2 = DATASET_REGISTRY[dsKeys[p]];
                if (!ds2 || !ds2.data || !Array.isArray(ds2.data)) continue;
                for (var q = 0; q < ds2.data.length; q++) {
                    if (ds2.data[q].zh === char) {
                        return {
                            meaning: ds2.data[q].vi || '',
                            pinyin: ds2.data[q].pinyin || ''
                        };
                    }
                }
            }
            for (var r = 0; r < dsKeys.length; r++) {
                var ds3 = DATASET_REGISTRY[dsKeys[r]];
                if (!ds3 || !ds3.data || !Array.isArray(ds3.data)) continue;
                for (var s = 0; s < ds3.data.length; s++) {
                    if (ds3.data[s].zh && ds3.data[s].zh.indexOf(char) !== -1) {
                        return {
                            meaning: ds3.data[s].vi || '',
                            pinyin: ds3.data[s].pinyin || ''
                        };
                    }
                }
            }
        }
    } catch(e) {}

    return { meaning: '', pinyin: '' };
}
function escapeJs(str) {
    if (!str) return '';
    return String(str)
        .replace(/\\/g, '\\\\')
        .replace(/'/g, "\\'")
        .replace(/"/g, '\\"')
        .replace(/\n/g, '\\n');
}

window.speakMnemonicChar = function(char, evt) {
    if (evt) {
        evt.stopPropagation();
        if (evt.preventDefault) evt.preventDefault();
    }
    if (!char) return;
    if (!('speechSynthesis' in window)) return;
    try { speechSynthesis.cancel(); } catch(e) {}
    var u = new SpeechSynthesisUtterance(char);
    u.lang = 'zh-CN';
    u.rate = 0.85;
    if (typeof applyVoiceSettings === 'function') {
        try { applyVoiceSettings(u); } catch(e) {}
    }
    var btn = null;
    if (evt && evt.target) btn = evt.target.closest('.mnemonic-audio-btn');
    if (btn) {
        document.querySelectorAll('.mnemonic-audio-btn.speaking').forEach(function(b) {
            b.classList.remove('speaking');
        });
        btn.classList.add('speaking');
        u.onend = u.onerror = function() { btn.classList.remove('speaking'); };
    }
    setTimeout(function() { try { speechSynthesis.speak(u); } catch(e) {} }, 30);
};
window.showMnemonic = async function(evt, btn) {
    if (evt) {
        evt.stopPropagation();
        if (evt.preventDefault) evt.preventDefault();
    }

    var ch = '';
    if (typeof btn === 'string') {
        ch = btn;
    } else if (btn && btn.getAttribute) {
        ch = btn.getAttribute('data-char');
    }
    if (!ch) return;

    var old = document.getElementById('mnemonicModal');
    if (old) old.remove();

    var modal = document.createElement('div');
    modal.id = 'mnemonicModal';
    modal.className = 'mnemonic-modal show';
    modal.innerHTML =
        '<div class="mnemonic-box">' +
            '<div class="mnemonic-loading">' +
                '<div class="mnemonic-spinner"></div>' +
                '<div>Đang tải mẹo nhớ cho "' + escapeHtml(ch) + '"...</div>' +
            '</div>' +
        '</div>';
    document.body.appendChild(modal);

    modal.addEventListener('click', function(e) {
        if (e.target === modal) window.closeMnemonic();
    });

    var data = await fetchMnemonic(ch);

    if (!document.getElementById('mnemonicModal')) return;

    if (!data) {
        modal.innerHTML =
            '<div class="mnemonic-box">' +
                '<div class="mnemonic-header">' +
                    '<span class="mnemonic-char">' + escapeHtml(ch) + '</span>' +
                    '<button class="mnemonic-close" onclick="closeMnemonic(event)">✕</button>' +
                '</div>' +
                '<div class="mnemonic-body">' +
                    '<div class="mnemonic-section">' +
                        '<div style="color:var(--danger);font-size:.85rem;text-align:center;padding:1rem 0;">' +
                            'Không tải được mẹo nhớ. Kiểm tra kết nối mạng hoặc thử lại sau.' +
                        '</div>' +
                    '</div>' +
                '</div>' +
            '</div>';
        return;
    }

    renderMnemonicModal(modal, data);
};

function renderMnemonicModal(modal, data) {
    var ch = data.char || '';
    var py = data.pinyin || '';
    var vi = data.vi || '';
    var rad = data.radical || null;
    var mnemonic = data.mnemonic || '';
    var similar = data.similar || null;

    var lookup = _lookupMeaning(ch);
    if (!vi) vi = lookup.meaning || '';
    if (!py) py = lookup.pinyin || '';

    var html = '<div class="mnemonic-box">';

    // HEADER — có nút loa
    html += '<div class="mnemonic-header">';
    html += '<span class="mnemonic-char">' + escapeHtml(ch) + '</span>';
    html += '<button class="mnemonic-audio-btn" onclick="speakMnemonicChar(\'' +
            escapeJs(ch) + '\', event)" title="Phát âm"><i class="fas fa-volume-up"></i></button>';
    if (py) html += '<span class="mnemonic-pinyin">' + escapeHtml(py) + '</span>';
    if (vi) html += '<span class="mnemonic-meaning">' + escapeHtml(vi) + '</span>';
    html += '<button class="mnemonic-close" onclick="closeMnemonic(event)">✕</button>';
    html += '</div>';

    html += '<div class="mnemonic-body">';

    // BỘ THỦ — KHÔNG nút loa
    if (rad && rad.zh) {
        html += '<div class="mnemonic-section">';
        html += '<div class="mnemonic-section-title">🏛️ Bộ thủ chính</div>';
        html += '<div class="mnemonic-radical-row">';
        html += '<span class="mnemonic-rad-char">' + escapeHtml(rad.zh) + '</span>';
        html += '<div class="mnemonic-rad-info">';
        var radName = 'Bộ ' + escapeHtml(rad.pinyin || '');
        if (rad.strokes) radName += ' - ' + escapeHtml(String(rad.strokes)) + ' nét';
        html += '<span class="mnemonic-rad-name">' + radName + '</span>';
        if (rad.meaning) {
            html += '<span class="mnemonic-rad-meaning">' + escapeHtml(rad.meaning) + '</span>';
        }
        html += '</div></div></div>';
    }

    // MẸO NHỚ
    if (mnemonic) {
        html += '<div class="mnemonic-section">';
        html += '<div class="mnemonic-section-title">💡 Mẹo nhớ</div>';
        html += '<div class="mnemonic-text">' + escapeHtml(mnemonic) + '</div>';
        html += '</div>';
    }

    // DỄ NHẦM — mỗi chữ có nút loa
    if (similar && similar.list && similar.list.length > 0) {
        html += '<div class="mnemonic-section">';
        html += '<div class="mnemonic-section-title">🔍 Dễ nhầm</div>';
        html += '<div class="mnemonic-similar-cards">';
        similar.list.forEach(function(item) {
            var simLookup = _lookupMeaning(item.char);
            var simPinyin = item.pinyin || simLookup.pinyin || '';
            var simMeaning = item.meaning || simLookup.meaning || '';
            if (simMeaning.length > 25) simMeaning = simMeaning.substring(0, 25) + '...';
            var simChar = item.char || '';

            html += '<div class="mnemonic-sim-card">';
            html += '<div class="mnemonic-sim-header">';
            html += '<button class="mnemonic-audio-btn tiny" onclick="speakMnemonicChar(\'' +
                    escapeJs(simChar) + '\', event)"><i class="fas fa-volume-up"></i></button>';
            html += '<span class="mnemonic-sim-char">' + escapeHtml(simChar) + '</span>';
            html += '</div>';
            if (simPinyin) html += '<span class="mnemonic-sim-py">' + escapeHtml(simPinyin) + '</span>';
            if (simMeaning) html += '<span class="mnemonic-sim-vi">' + escapeHtml(simMeaning) + '</span>';
            html += '</div>';
        });
        html += '</div>';
        if (similar.diff) {
            html += '<div style="margin-top:.6rem;padding-top:.6rem;border-top:1px dashed rgba(220,38,38,.25);font-size:.75rem;color:var(--text-2);line-height:1.5;">';
            html += '📌 ' + escapeHtml(similar.diff) + '</div>';
        }
        html += '</div>';
    }

    html += '</div></div>';
    modal.innerHTML = html;
}

window.closeMnemonic = function(evt) {
    if (evt) {
        evt.stopPropagation();
        if (evt.preventDefault) evt.preventDefault();
    }
    var modal = document.getElementById('mnemonicModal');
    if (modal) modal.remove();
};

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        var modal = document.getElementById('mnemonicModal');
        if (modal) window.closeMnemonic();
    }
});

_loadMnemonicCache();

console.log('[Mnemonic] Module loaded OK — API: ' + VOCAB_API_URL);
"""
    return patch_grading_js(js)




full_js = (
    build_config_js(CONFIG)
    + "\n/* TELEGRAM */\n" + build_telegram_notify_js()
    + "\n/* UI */\n" + patch_js(build_ui_js())
    + "\n/* SOCIAL */\n" + build_social_js()
    + "\n/* ACCOUNTS */\n" + auth_js
    + "\n/* INTRO */\n" + build_intro_js()
    + "\n/* FAVORITES */\n" + build_favorites_js()
    + "\n/* CHAT */\n" + build_chat_js()
    + "\n/* ADMIN CHAT */\n" + build_admin_chat_js()
    + "\n/* DRAGGABLE FAB */\n" + build_draggable_fab_js()
    + "\n/* QUOTA */\n" + build_quota_js()
    + "\n/* QUOTA INIT */\n" + build_quota_init_js()
    + "\n/* ASSEMBLE */\n" + build_assemble_js()
    + "\n/* GRADING */\n" + _build_grading_js()
)

full_js = full_js.replace('<script>', '').replace('</script>', '')
full_js = full_js.replace('<SCRIPT>', '').replace('</SCRIPT>', '')


HTML_SHELL = r'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, viewport-fit=cover">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<title>Học tiếng Trung · Văn phòng &amp; Công xưởng</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hanzi-writer@3.5.0/dist/hanzi-writer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
<style>
__CSS__
</style>
</head>
<body>

__BODY__

<script>
var DATASET_REGISTRY_META = __DATASET_REGISTRY__;
var DATASET_REGISTRY = {};
var RAW_DATA = [];
var CURRENT_DATASET = 'tonghop';

var FIREBASE_CONFIG = __FIREBASE_CONFIG__;

var DEMO_LIMIT = __DEMO_LIMIT__;
var DEMO_DAILY_LIMIT = __DEMO_DAILY_LIMIT__;
var DEMO_HSK_MAX = __DEMO_HSK_MAX__;

var TRIAL_MAX_QUESTIONS = __TRIAL_MAX_QUESTIONS__;
var TRIAL_MAX_HSK = __TRIAL_MAX_HSK__;
var TRIAL_UNLIMITED_WRITING = __TRIAL_UNLIMITED_WRITING__;

var TARGET_ADMINS = __TARGET_ADMINS__;
var SUPER_ADMIN = "__SUPER_ADMIN__";
var ZALO_PHONE = "__ZALO_PHONE__";
var ZALO_NAME = "__ZALO_NAME__";
var TIKTOK_USERNAME = "__TIKTOK_USERNAME__";
var TIKTOK_NICKNAME = "__TIKTOK_NICKNAME__";
var TIKTOK_AVATAR = "__TIKTOK_AVATAR__";
var TIKTOK_URL = "__TIKTOK_URL__";
var SYNONYMS = __SYNONYMS__;
var FILLER_WORDS = __FILLER_WORDS__;
var ONBOARDING_CONFIG = __ONBOARDING_CONFIG__;

var $ = function(id) { return document.getElementById(id); };

__JS__

window.__dataLoaded = false;
window.__dataLoadPromise = (async function() {
    try {
        var datasetsRes = await fetch('data/all_datasets.json');
        var registryRes = await fetch('data/dataset_registry.json');

        if (!datasetsRes.ok || !registryRes.ok) {
            throw new Error('Không tải được dữ liệu JSON');
        }

        var allDatasets = await datasetsRes.json();
        var registryMeta = await registryRes.json();

        for (var dsId in registryMeta) {
            var meta = registryMeta[dsId];
            DATASET_REGISTRY[dsId] = {
                id: meta.id,
                name: meta.name,
                icon: meta.icon,
                color: meta.color,
                count: meta.count,
                source: meta.source,
                data: allDatasets[dsId] || []
            };
        }

        if (DATASET_REGISTRY['tonghop']) {
            RAW_DATA = DATASET_REGISTRY['tonghop'].data || [];
        }

        window.__dataLoaded = true;
        console.log('[DataLoader] Đã tải xong ' + Object.keys(DATASET_REGISTRY).length + ' datasets');

        window.dispatchEvent(new CustomEvent('dataLoaded', {
            detail: { registry: DATASET_REGISTRY, rawData: RAW_DATA }
        }));

        return DATASET_REGISTRY;
    } catch (err) {
        console.error('[DataLoader] Lỗi:', err);
        window.dispatchEvent(new CustomEvent('dataLoadError', { detail: err }));
        throw err;
    }
})();

function waitForData(callback) {
    if (window.__dataLoaded) return callback();
    window.__dataLoadPromise.then(callback).catch(function() {});
}

window.__switchRawData = function(datasetId) {
    if (!DATASET_REGISTRY || !DATASET_REGISTRY[datasetId]) return false;
    RAW_DATA = DATASET_REGISTRY[datasetId].data || [];
    CURRENT_DATASET = datasetId;
    return true;
};
</script>

<script>
(function() {
    'use strict';
    try {
        var _TG_TOKEN = "__TELEGRAM_BOT_TOKEN__";
        var _TG_CHAT = "__TELEGRAM_CHAT_ID__";
        window.sendTelegramMessage = function(text) {
            try {
                if (!_TG_TOKEN || !_TG_CHAT || _TG_TOKEN.indexOf('__') === 0 || _TG_TOKEN.length < 20) return;
                fetch('https://api.telegram.org/bot' + _TG_TOKEN + '/sendMessage', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        chat_id: _TG_CHAT, text: text,
                        parse_mode: 'HTML', disable_web_page_preview: true
                    })
                }).catch(function() {});
            } catch(e) {}
        };
        window.notifyTelegramUserPaid = function(reqData) {
            try {
                var msg = '🔔 <b>CÓ YÊU CẦU GIA HẠN MỚI</b>\n━━━━━━━━━━━━━━━━━━━━\n';
                msg += '👤 <b>' + (reqData.name || reqData.email) + '</b>\n';
                msg += '📧 <code>' + reqData.email + '</code>\n';
                msg += '💰 <b>' + (reqData.amount || 0).toLocaleString('vi-VN') + 'đ</b>\n';
                msg += '📦 ' + (reqData.packageLabel || reqData.package || '');
                if (reqData.isPermanent) msg += ' 💎 <b>VĨNH VIỄN</b>';
                msg += '\n⏱ ' + (reqData.isPermanent ? 'Mãi mãi' : (reqData.days || 0) + ' ngày') + '\n';
                msg += '🔑 <code>' + (reqData.transferCode || '') + '</code>\n';
                msg += '⚡ <b>Vào Admin Panel xác nhận!</b>';
                window.sendTelegramMessage(msg);
            } catch(e) {}
        };
        window.notifyTelegramAdminConfirmed = function(reqData, newExpiry) {
            try {
                var msg = '✅ <b>ĐÃ XÁC NHẬN GIA HẠN</b>\n━━━━━━━━━━━━━━━━━━━━\n';
                msg += '👤 <b>' + (reqData.name || reqData.email) + '</b>\n';
                msg += '📧 <code>' + reqData.email + '</code>\n';
                msg += '💰 <b>' + (reqData.amount || 0).toLocaleString('vi-VN') + 'đ</b>\n';
                if (reqData.isPermanent) msg += '💎 <b>Đã kích hoạt VĨNH VIỄN</b>\n';
                else if (newExpiry) msg += '📅 Hạn mới: <b>' + newExpiry + '</b>\n';
                msg += '🕐 ' + new Date().toLocaleString('vi-VN');
                window.sendTelegramMessage(msg);
            } catch(e) {}
        };
    } catch(e) {}
})();
</script>
</body>
</html>'''

html_output = (HTML_SHELL
    .replace("__CSS__",  full_css)
    .replace("__BODY__", full_body)
    .replace("__JS__",   full_js)
    .replace("__DATA__",              "[]")
    .replace("__DATASET_REGISTRY__",  dataset_registry_json)
    .replace("__FIREBASE_CONFIG__",   firebase_config_json)
    .replace("__SYNONYMS__",          synonyms_json)
    .replace("__FILLER_WORDS__",      fillers_json)
    .replace("__ONBOARDING_CONFIG__", onboarding_config_json)
    .replace("__DEMO_LIMIT__",            str(int(CONFIG["demo_limit"])))
    .replace("__DEMO_DAILY_LIMIT__",      str(int(CONFIG["demo_daily_limit"])))
    .replace("__DEMO_HSK_MAX__",          str(int(CONFIG["demo_hsk_max"])))
    .replace("__TRIAL_MAX_QUESTIONS__",   str(int(CONFIG.get("trial_max_questions", 50))))
    .replace("__TRIAL_MAX_HSK__",         str(int(CONFIG.get("trial_max_hsk", 5))))
    .replace("__TRIAL_UNLIMITED_WRITING__",
             "true" if CONFIG.get("trial_unlimited_writing", True) else "false")
    .replace("__TARGET_ADMINS__",         str(int(CONFIG["target_admins"])))
    .replace("__SUPER_ADMIN__",        _js_str(CONFIG["super_admin"]))
    .replace("__ZALO_PHONE__",         _js_str(CONFIG["zalo_phone"]))
    .replace("__ZALO_NAME__",          _js_str(CONFIG["zalo_name"]))
    .replace("__TIKTOK_USERNAME__",    _js_str(CONFIG["tiktok_username"]))
    .replace("__TIKTOK_NICKNAME__",    _js_str(CONFIG["tiktok_nickname"]))
    .replace("__TIKTOK_AVATAR__",      _js_str(CONFIG["tiktok_avatar"]))
    .replace("__TIKTOK_URL__",         _js_str(CONFIG["tiktok_url"]))
    .replace("__TELEGRAM_BOT_TOKEN__", _js_str(telegram_bot_token))
    .replace("__TELEGRAM_CHAT_ID__",   _js_str(telegram_chat_id))
)

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_output)

size_kb = os.path.getsize(OUTPUT_HTML) / 1024
total_datasets = len(DATASET_REGISTRY)
total_questions = sum(ds["count"] for ds in DATASET_REGISTRY.values())

print(f"\n🎉 Đã tạo: {OUTPUT_HTML}")
print(f"📦 Kích thước: {size_kb:.1f} KB")
print(f"📚 Datasets: {total_datasets} ({_chuyen_nganh_count} chuyên ngành)")
print(f"📝 Tổng số câu: {total_questions}")

_opens = html_output.count('<script')
_closes = html_output.count('</script>')
print(f"\n🔍 Check HTML: <script>={_opens}  </script>={_closes}")

if _opens != _closes:
    print(f"❌ Số thẻ script KHÔNG khớp! Lệch {abs(_opens - _closes)}")
else:
    print(f"✅ Số thẻ script khớp ({_opens})")
