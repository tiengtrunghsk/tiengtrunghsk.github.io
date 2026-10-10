def build_ui_css():
    return r"""
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
:root{--bg:#f0f4f8;--surface:#fff;--surface-2:#f8fafc;--border:#e2e8f0;--border-strong:#cbd5e1;--text:#0f172a;--text-2:#475569;--text-3:#94a3b8;--primary:#2563eb;--primary-dark:#1d4ed8;--primary-light:#dbeafe;--success:#16a34a;--danger:#dc2626;--danger-light:#fee2e2;--amber:#f59e0b;--amber-light:#fef3c7;--shadow-sm:0 1px 2px rgba(15,23,42,.04);--shadow:0 4px 12px rgba(15,23,42,.06);--shadow-fab:0 8px 24px rgba(15,23,42,.18);--radius:14px;--radius-full:999px;--font-zh:'PingFang SC','Microsoft YaHei',sans-serif}
[data-theme="dark"]{--bg:#0f172a;--surface:#1e293b;--surface-2:#334155;--border:#334155;--border-strong:#475569;--text:#f1f5f9;--text-2:#cbd5e1;--text-3:#94a3b8;--primary:#3b82f6;--primary-dark:#2563eb;--primary-light:#1e3a8a;--danger-light:#7f1d1d;--amber-light:#78350f;--shadow-sm:0 1px 2px rgba(0,0,0,.3);--shadow:0 4px 12px rgba(0,0,0,.3);--shadow-fab:0 8px 24px rgba(0,0,0,.5)}
html,body{height:100%}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.5;font-size:15px;padding-bottom:calc(90px + env(safe-area-inset-bottom));transition:background .2s,color .2s}
.container{max-width:1100px;margin:0 auto;padding:0 1.5rem}
@media(min-width:1600px){.container{max-width:1200px}}
.loading-screen{position:fixed;inset:0;background:var(--bg);display:flex;align-items:center;justify-content:center;z-index:9998;flex-direction:column;gap:1rem;color:var(--text-2)}
.loading-screen.hidden{display:none}
.loading-screen i{font-size:2.5rem;color:var(--primary);animation:spin 1s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.sticky-top{position:relative;z-index:150;background:var(--bg);padding:clamp(.35rem,.8vh,.7rem) 0;transition:background .2s,box-shadow .2s,border-color .2s;border-bottom:1px solid transparent;overflow:visible}
.sticky-top.scrolled{background:var(--surface);border-bottom-color:var(--border);box-shadow:0 4px 16px -8px rgba(15,23,42,.15)}
[data-theme="dark"] .sticky-top.scrolled{box-shadow:0 4px 16px -8px rgba(0,0,0,.5)}
.header{background:transparent}
.header-inner{display:flex;align-items:center;gap:.75rem;margin-bottom:.4rem}
.logo{display:flex;align-items:center;gap:.85rem;flex:1;min-width:0}
.logo-icon{width:clamp(40px,5vw,56px);height:clamp(40px,5vw,56px);background:linear-gradient(135deg,#4f46e5,#7c3aed 60%,#a855f7);border-radius:clamp(10px,1.2vw,14px);display:flex;align-items:center;justify-content:center;color:#fff;font-size:clamp(1.15rem,1.8vw,1.75rem);flex-shrink:0;box-shadow:0 8px 24px rgba(124,58,237,.4);position:relative;overflow:hidden}
.logo-icon::after{content:'';position:absolute;inset:0;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,.35),transparent 60%);pointer-events:none}
.logo-text{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:flex;flex-direction:column;line-height:1.15;min-width:0}
.logo-text .title{font-size:clamp(1.1rem,2vw,1.75rem);font-weight:900;letter-spacing:-.02em;color:var(--text)}
.logo-text .subtitle{font-size:clamp(.62rem,1vw,.85rem);color:var(--text-3);font-weight:700;margin-top:2px}
.header-actions{display:flex;gap:.4rem;align-items:center;flex-shrink:0}
.icon-btn{width:clamp(30px,3vw,36px);height:clamp(30px,3vw,36px);border-radius:10px;border:1px solid var(--border);background:var(--surface);color:var(--text-3);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:clamp(.72rem,.9vw,.88rem);transition:.15s;position:relative;flex-shrink:0}
.icon-btn:hover,.icon-btn:active{background:var(--surface-2);color:var(--primary);border-color:var(--primary)}
.icon-btn.hidden{display:none}
.icon-btn.reset-btn:hover{background:var(--danger-light);color:var(--danger);border-color:var(--danger)}
.icon-btn .badge{position:absolute;top:-4px;right:-4px;min-width:16px;height:16px;border-radius:50%;background:var(--danger);color:#fff;font-size:.6rem;font-weight:700;display:flex;align-items:center;justify-content:center;padding:0 4px;border:2px solid var(--surface)}
.icon-btn:not(.has-badge) .badge{display:none}
.demo-badge{display:flex;align-items:center;gap:.35rem;padding:clamp(.25rem,.5vw,.35rem) clamp(.45rem,.8vw,.7rem);border-radius:50px;background:var(--amber-light);color:#92400e;font-size:clamp(.58rem,.75vw,.7rem);font-weight:700;text-transform:uppercase;border:1px solid rgba(245,158,11,.4)}
[data-theme="dark"] .demo-badge{color:#fcd34d}
.search-filter-row{display:flex;flex-direction:column;gap:.45rem}
.search-bar{position:relative}
.search-bar i.fa-search{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--text-3);font-size:.88rem;pointer-events:none}
.search-bar input{width:100%;padding:clamp(.4rem,.7vh,.6rem) 2.5rem clamp(.4rem,.7vh,.6rem) 2.4rem;border-radius:var(--radius-full);border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:clamp(.78rem,.9vw,.88rem);outline:none;transition:.15s;box-shadow:var(--shadow-sm);font-family:inherit}
.search-bar input:focus{border-color:var(--primary);box-shadow:0 0 0 4px rgba(37,99,235,.15)}
.search-clear{position:absolute;right:8px;top:50%;transform:translateY(-50%);width:28px;height:28px;border-radius:50%;border:none;background:var(--surface-2);color:var(--text-2);cursor:pointer;display:none;align-items:center;justify-content:center;font-size:.78rem}
.search-clear.show{display:flex}
.filters{display:grid;grid-template-columns:1fr 1fr;gap:.5rem;max-width:600px}
.chip{display:flex;align-items:center;gap:.4rem;padding:clamp(.32rem,.6vh,.5rem) clamp(.55rem,1vw,.85rem);border-radius:var(--radius-full);border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:clamp(.7rem,.85vw,.82rem);cursor:pointer;transition:.15s;min-width:0;box-shadow:var(--shadow-sm);text-align:left;position:relative;overflow:hidden}
.chip:active{transform:scale(.98)}
.chip.has-value{background:var(--primary);color:#fff;border-color:var(--primary)}
.chip.has-value .chip-label{color:#fff;opacity:.85}
.chip-label{font-size:clamp(.55rem,.7vw,.68rem);color:var(--text-3);text-transform:uppercase;font-weight:700;flex-shrink:0}
.chip-value{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1;min-width:0}
.chip-arrow{opacity:.5;font-size:.68rem;flex-shrink:0}
.chip select{position:absolute;inset:0;opacity:0;cursor:pointer;font-size:1rem;appearance:none;width:100%;height:100%;z-index:5}
.chip > span,.chip > i{pointer-events:none}
.chip > select{pointer-events:auto}
.result-count{display:none;align-items:center;gap:.4rem;margin-top:.45rem;padding:clamp(.25rem,.5vw,.4rem) clamp(.55rem,.8vw,.75rem);border-radius:var(--radius-full);background:var(--surface-2);border:1px solid var(--border);color:var(--text-2);font-size:clamp(.65rem,.8vw,.78rem);font-weight:600;width:fit-content;box-shadow:var(--shadow-sm)}
.result-count.show{display:inline-flex}
.result-count b{color:var(--primary);font-weight:800}
.result-count.empty{background:var(--danger-light);border-color:rgba(220,38,38,.3);color:var(--danger)}
.result-count.empty i,.result-count.empty b{color:var(--danger)}
.fab-group{position:fixed;bottom:calc(20px + env(safe-area-inset-bottom));right:20px;z-index:1000;display:flex;flex-direction:column;gap:.5rem;align-items:flex-end;pointer-events:none}
.fab-group > *{pointer-events:auto}
.fab-btn{width:clamp(42px,5vw,52px);height:clamp(42px,5vw,52px);border-radius:50%;border:none;background:var(--surface);color:var(--text-2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:clamp(.95rem,1.2vw,1.15rem);box-shadow:var(--shadow-fab);transition:transform .2s,background .2s,color .2s;position:relative;border:2px solid var(--surface)}
.fab-btn:hover{transform:scale(1.08);background:var(--primary-light);color:var(--primary-dark)}
.fab-btn.active{background:var(--primary);color:#fff;border-color:var(--primary)}
.fab-main{width:clamp(46px,5.5vw,56px);height:clamp(46px,5.5vw,56px);font-size:clamp(1.05rem,1.4vw,1.3rem);background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;box-shadow:0 8px 24px rgba(124,58,237,.4)}
.fab-main i{transition:transform .3s}
.fab-group.open .fab-main i{transform:rotate(180deg)}
.fab-sub{opacity:0;transform:translateY(10px) scale(.8);pointer-events:none!important;transition:opacity .2s,transform .25s}
.fab-group.open .fab-sub{opacity:1;transform:translateY(0) scale(1);pointer-events:auto!important}
body:not(.show-pinyin) .card-pinyin{display:none!important}
body:not(.show-vi) .card-vi{display:none!important}
body:not(.show-practice) .card-practice{display:none!important}
body.show-practice .card-zh,body.show-practice .card-pinyin{display:none!important}
body.show-practice .card-vi{display:block!important;font-size:1rem;font-weight:600;color:var(--text);margin-bottom:.55rem;line-height:1.4}
body.show-practice .card-body{background:linear-gradient(135deg,var(--surface-2),rgba(37,99,235,.06));padding:.75rem .85rem;border-radius:10px;border-left:3px solid var(--primary)}
.ai-correct{color:var(--success);font-weight:700}
.ai-partial{color:var(--amber);font-weight:700}
.ai-wrong{color:var(--danger);font-weight:700}
.ai-reason{display:block;font-size:.68rem;color:var(--text-3);font-weight:400;margin-top:.2rem;font-style:italic;line-height:1.3}
.answer-inline-display{display:flex;align-items:center;justify-content:center;gap:.4rem;margin-top:.35rem;padding:.35rem .6rem;background:linear-gradient(135deg,rgba(37,99,235,.08),rgba(37,99,235,.04));border:1px dashed rgba(37,99,235,.3);border-radius:8px;flex-wrap:wrap}
[data-theme="dark"] .answer-inline-display{background:linear-gradient(135deg,rgba(59,130,246,.15),rgba(59,130,246,.08));border-color:rgba(59,130,246,.4)}
.answer-inline-label{font-size:.7rem;font-weight:700;color:var(--primary-dark);text-transform:uppercase;display:inline-flex;align-items:center;gap:.25rem}
[data-theme="dark"] .answer-inline-label{color:#93c5fd}
.answer-inline-text{font-family:var(--font-zh);font-size:1.05rem;font-weight:600;color:var(--text);letter-spacing:.03em;word-break:break-all}
.main{padding:clamp(.15rem,.5vh,.5rem) 0 clamp(2rem,5vh,3rem)}
.demo-banner{background:linear-gradient(135deg,#fef3c7,#fde68a);border:1.5px solid #f59e0b;border-radius:var(--radius);padding:clamp(.7rem,1.5vw,.9rem) clamp(.8rem,1.5vw,1.1rem);margin-bottom:1rem;display:flex;align-items:center;gap:.75rem;flex-wrap:wrap}
[data-theme="dark"] .demo-banner{background:linear-gradient(135deg,rgba(245,158,11,.15),rgba(245,158,11,.25));border-color:#f59e0b}
.demo-banner-icon{width:36px;height:36px;border-radius:50%;background:var(--amber);color:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.demo-banner-text{flex:1;min-width:200px}
.demo-banner-text .title{font-weight:700;font-size:.9rem;color:#92400e;margin-bottom:.15rem}
[data-theme="dark"] .demo-banner-text .title{color:#fcd34d}
.demo-banner-text .desc{font-size:.78rem;color:#78350f;line-height:1.5}
[data-theme="dark"] .demo-banner-text .desc{color:#fde68a}
.demo-banner-text .desc b{color:#dc2626}
.demo-banner-btn{padding:.5rem .9rem;border-radius:50px;border:none;background:var(--amber);color:#fff;font-size:.8rem;font-weight:700;cursor:pointer;font-family:inherit;display:flex;align-items:center;gap:.35rem;white-space:nowrap}
.demo-banner-btn:hover{background:#d97706}
.mobile-view{display:grid;grid-template-columns:1fr;gap:clamp(.65rem,1.6vw,1rem);max-width:100%}
@media(min-width:769px){.mobile-view{grid-template-columns:1fr 1fr;gap:clamp(1rem,2vw,1.3rem)}}
@media(min-width:1800px){.mobile-view{grid-template-columns:1fr 1fr 1fr;gap:1.3rem}}

/* ============================================================ */
/* DATASET SELECTOR - 2 CAP (Bo du lieu + Chuyen nganh)          */
/* ============================================================ */
.dataset-selector{
    margin-bottom:.75rem;
    padding:.75rem .9rem;
    background:linear-gradient(135deg,var(--surface),var(--surface-2));
    border:1.5px solid var(--border);
    border-radius:14px;
    box-shadow:var(--shadow-sm);
}
.ds-label{
    display:flex;align-items:center;gap:.4rem;
    font-size:.7rem;font-weight:800;
    color:var(--text-3);text-transform:uppercase;
    letter-spacing:.5px;margin-bottom:.5rem;
}
.ds-label i{color:var(--primary);font-size:.85rem}
.ds-main-row{
    display:grid;grid-template-columns:1fr 1fr 1fr;gap:.5rem;
}
@media(max-width:768px){
    .ds-main-row{grid-template-columns:1fr 1fr;}
}
@media(max-width:500px){
    .ds-main-row{grid-template-columns:1fr;}
}
@media(max-width:500px){
    .ds-main-row{grid-template-columns:1fr}
}
.ds-btn{
    display:flex;align-items:center;gap:.5rem;
    padding:.65rem .85rem;
    border-radius:11px;
    border:1.5px solid var(--border);
    background:var(--surface);
    color:var(--text);
    font-size:.82rem;font-weight:700;
    font-family:inherit;cursor:pointer;
    transition:.2s;text-align:left;
    position:relative;
}
.ds-btn:hover{
    border-color:var(--primary);
    background:var(--primary-light);
    transform:translateY(-1px);
}
.ds-btn.active{
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;border-color:transparent;
    box-shadow:0 4px 12px rgba(124,58,237,.35);
}
.ds-btn i:first-child{
    font-size:1rem;flex-shrink:0;
}
.ds-btn span{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis}
.ds-arrow{
    font-size:.7rem;opacity:.7;transition:transform .25s;
}
.ds-btn.active .ds-arrow{transform:rotate(180deg)}

/* Badge NEW cho nut Chuyen nganh */
.ds-btn[data-dataset-group="chuyen-nganh"]{
    overflow:visible;
}
.ds-btn[data-dataset-group="chuyen-nganh"] .ds-new-badge{
    position:absolute;
    top:-10px;
    right:-8px;
    padding:.18rem .5rem;
    border-radius:50px;
    background:linear-gradient(135deg,#ef4444,#dc2626 50%,#b91c1c);
    color:#fff;
    font-size:.6rem;
    font-weight:900;
    letter-spacing:.5px;
    text-transform:uppercase;
    box-shadow:
        0 2px 8px rgba(220,38,38,.5),
        0 0 0 2px var(--surface);
    animation:dsNewPulse 1.6s ease-in-out infinite;
    z-index:10;
    pointer-events:none;
    line-height:1.2;
    white-space:nowrap;
}
.ds-btn[data-dataset-group="chuyen-nganh"] .ds-new-badge::before{
    content:'';
    position:absolute;
    inset:-4px;
    border-radius:50px;
    background:radial-gradient(circle,rgba(220,38,38,.4),transparent 70%);
    animation:dsNewGlow 1.6s ease-in-out infinite;
    z-index:-1;
}
@keyframes dsNewPulse{
    0%,100%{
        transform:scale(1);
        box-shadow:
            0 2px 8px rgba(220,38,38,.5),
            0 0 0 2px var(--surface);
    }
    50%{
        transform:scale(1.12);
        box-shadow:
            0 4px 14px rgba(220,38,38,.8),
            0 0 0 2px var(--surface);
    }
}
@keyframes dsNewGlow{
    0%,100%{opacity:.4;transform:scale(1)}
    50%{opacity:.9;transform:scale(1.4)}
}
.ds-btn[data-dataset-group="chuyen-nganh"].active .ds-new-badge{
    display:none;
}
[data-theme="dark"] .ds-btn[data-dataset-group="chuyen-nganh"] .ds-new-badge{
    box-shadow:
        0 2px 8px rgba(220,38,38,.7),
        0 0 0 2px var(--surface-2);
}

.ds-sub-wrap{
    margin-top:.65rem;padding-top:.65rem;
    border-top:1.5px dashed var(--border);
    animation:dsFadeIn .25s ease-out;
}
@keyframes dsFadeIn{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:translateY(0)}}
.ds-sub-label{
    display:flex;align-items:center;gap:.35rem;
    font-size:.68rem;font-weight:800;
    color:var(--text-3);text-transform:uppercase;
    letter-spacing:.4px;margin-bottom:.5rem;
}
.ds-sub-label i{color:var(--amber);font-size:.8rem}

/* ═══════════════════════════════════════════════════════════ */
/* SUB-BUTTONS CHUYÊN NGÀNH - FIX HIỂN THỊ ĐẦY ĐỦ DẤU TIẾNG VIỆT */
/* ═══════════════════════════════════════════════════════════ */
.ds-sub-grid{
    display:flex;
    flex-wrap:wrap;
    gap:.5rem;
}
.ds-sub-btn{
    display:inline-flex;
    align-items:center;
    justify-content:flex-start;
    gap:.45rem;
    padding:.62rem 1.05rem .65rem;
    border-radius:50px;
    background:linear-gradient(135deg,
        color-mix(in srgb, var(--ds-color, #2563eb) 12%, var(--surface)),
        color-mix(in srgb, var(--ds-color, #2563eb) 4%, var(--surface)));
    border:2px solid color-mix(in srgb, var(--ds-color, #2563eb) 40%, var(--border));
    color:var(--text);
    font-size:.78rem;
    font-weight:800;
    font-family:inherit;
    cursor:pointer;
    transition:all .2s ease;
    text-align:left;
    position:relative;
    white-space:nowrap;
    box-shadow:0 2px 6px color-mix(in srgb, var(--ds-color, #2563eb) 18%, transparent);
    letter-spacing:0;
    line-height:1.5;
    overflow:visible;
    text-rendering:optimizeLegibility;
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale;
    font-feature-settings:"kern" 1,"liga" 1;
    -webkit-text-size-adjust:100%;
    text-size-adjust:100%;
}
.ds-sub-btn i:first-child{
    font-size:.95rem;
    color:var(--ds-color, var(--primary));
    transition:.2s;
    flex-shrink:0;
    line-height:1;
}
.ds-sub-btn span{
    flex:1 1 auto;
    min-width:0;
    display:inline-block;
    line-height:1.5;
    padding:.06em 0 .1em;
    text-rendering:optimizeLegibility;
    overflow-wrap:break-word;
    word-break:normal;
    white-space:nowrap;
}
.ds-sub-btn:hover{
    border-color:var(--ds-color, var(--primary));
    background:linear-gradient(135deg,
        color-mix(in srgb, var(--ds-color, #2563eb) 20%, var(--surface)),
        color-mix(in srgb, var(--ds-color, #2563eb) 8%, var(--surface)));
    transform:translateY(-2px);
    box-shadow:0 6px 16px color-mix(in srgb, var(--ds-color, #2563eb) 30%, transparent);
}
.ds-sub-btn.active{
    background:linear-gradient(135deg,
        var(--ds-color, var(--primary)),
        color-mix(in srgb, var(--ds-color, #2563eb) 72%, #000));
    color:#fff;
    border-color:var(--ds-color, var(--primary));
    box-shadow:0 6px 18px color-mix(in srgb, var(--ds-color, #2563eb) 55%, transparent);
    transform:translateY(-1px);
}
.ds-sub-btn.active i:first-child{
    color:#fff;
}
@media(max-width:500px){
    .ds-sub-btn{
        padding:.55rem .85rem .58rem;
        font-size:.74rem;
        line-height:1.5;
    }
    .ds-sub-btn i:first-child{ font-size:.85rem; }
    .ds-sub-btn span{
        line-height:1.5;
        padding:.05em 0 .08em;
    }
}

/* KHOA CHUYEN NGANH - Demo/Trial chua gia han */
.ds-sub-btn.locked {
    opacity: 0.6;
    cursor: not-allowed;
    filter: grayscale(0.4);
    padding-right: 1.9rem;
}
.ds-sub-btn.locked:hover {
    transform: none;
    background: var(--surface);
    border-color: var(--border);
    box-shadow: 0 1px 2px rgba(15,23,42,.04);
}
.ds-sub-btn.locked i:first-child {
    color: var(--text-3) !important;
}
.ds-sub-lock {
    position: absolute;
    top: 50%;
    right: 6px;
    transform: translateY(-50%);
    font-size: 0.58rem;
    color: #dc2626;
    background: rgba(220, 38, 38, 0.14);
    padding: 2px 4px;
    border-radius: 5px;
    line-height: 1;
    pointer-events: none;
    box-shadow: 0 1px 3px rgba(220, 38, 38, 0.2);
}
[data-theme="dark"] .ds-sub-lock {
    color: #fca5a5;
    background: rgba(220, 38, 38, 0.3);
}
.ds-main-lock {
    font-size: 0.7rem;
    color: #dc2626;
    margin-left: 0.35rem;
    padding: 2px 5px;
    background: rgba(220, 38, 38, 0.12);
    border-radius: 5px;
    line-height: 1;
    display: inline-flex;
    align-items: center;
    flex-shrink: 0;
}
[data-theme="dark"] .ds-main-lock {
    color: #fca5a5;
    background: rgba(220, 38, 38, 0.28);
}
.ds-btn[data-dataset-group="chuyen-nganh"].has-lock {
    border-color: rgba(220, 38, 38, 0.35);
}
.ds-btn[data-dataset-group="chuyen-nganh"].has-lock:hover {
    border-color: #dc2626;
    background: rgba(220, 38, 38, 0.06);
}
.ds-btn[data-dataset-group="chuyen-nganh"].has-lock.active {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    border-color: transparent;
}
.ds-btn[data-dataset-group="chuyen-nganh"].has-lock.active {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    border-color: transparent;
}

/* ═══════════════════════════════════════════════════════════ */
/* FAVORITES TAB ROW — nằm dưới ds-sub-wrap                     */
/* Tự động bị đẩy xuống khi mở dropdown Chuyên ngành            */
/* ═══════════════════════════════════════════════════════════ */
.ds-fav-row {
    display: grid;
    grid-template-columns: 1fr;
    gap: .5rem;
    margin-top: .65rem;
    padding-top: .65rem;
    border-top: 1.5px dashed var(--border);
    animation: dsFadeIn .25s ease-out;
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"] {
    display: flex;
    align-items: center;
    gap: .5rem;
    padding: .65rem .85rem;
    border-radius: 11px;
    border: 2px solid rgba(239, 68, 68, 0.35);
    background: linear-gradient(135deg, #fef2f2, #fee2e2);
    color: #dc2626;
    font-size: .82rem;
    font-weight: 800;
    font-family: inherit;
    cursor: pointer;
    transition: all .2s ease;
    text-align: left;
    position: relative;
    overflow: visible;
    width: 100%;
    justify-content: flex-start;
    box-shadow: 0 2px 6px rgba(239, 68, 68, 0.1);
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"] i:first-child {
    color: #ef4444;
    font-size: 1rem;
    flex-shrink: 0;
    transition: color .2s;
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"] span {
    flex: 1;
    min-width: 0;
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"]:hover {
    border-color: #ef4444;
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.25);
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"].active {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    border-color: #dc2626;
    color: #fff;
    box-shadow: 0 4px 14px rgba(239, 68, 68, 0.45);
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"].active i:first-child {
    color: #fff;
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"] .ds-fav-badge {
    position: absolute;
    top: -8px;
    right: -6px;
    min-width: 22px;
    height: 22px;
    padding: 0 .4rem;
    border-radius: 50px;
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: #fff;
    font-size: .65rem;
    font-weight: 900;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px rgba(239, 68, 68, .5), 0 0 0 2px var(--surface);
    animation: favBadgePulse 2s ease-in-out infinite;
    z-index: 10;
    line-height: 1;
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"] .ds-fav-badge[data-count="0"] {
    display: none;
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"] .ds-fav-lock {
    position: absolute;
    top: -8px;
    right: -6px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: linear-gradient(135deg, #dc2626, #b91c1c);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: .62rem;
    box-shadow: 0 2px 8px rgba(220, 38, 38, .55), 0 0 0 2px var(--surface);
    z-index: 10;
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"].fav-locked {
    opacity: .65;
    cursor: pointer;
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"].fav-locked:hover {
    opacity: .85;
    border-color: #dc2626;
    background: rgba(220, 38, 38, .06);
}
.ds-fav-row .ds-btn[data-dataset-group="favorites"].fav-locked i:first-child {
    color: #dc2626;
}
[data-theme="dark"] .ds-fav-row .ds-btn[data-dataset-group="favorites"] {
    background: linear-gradient(135deg, rgba(239, 68, 68, .15), rgba(220, 38, 38, .1));
    border-color: rgba(239, 68, 68, .5);
    color: #fca5a5;
}
[data-theme="dark"] .ds-fav-row .ds-btn[data-dataset-group="favorites"]:hover {
    background: linear-gradient(135deg, rgba(239, 68, 68, .25), rgba(220, 38, 38, .18));
    color: #fecaca;
}
[data-theme="dark"] .ds-fav-row .ds-btn[data-dataset-group="favorites"].active {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: #fff;
}

/* ============================================================ */
/* FLASHCARD UI */
/* ============================================================ */
/* FLASHCARD UI */
/* ============================================================ */
.card{
    position:relative;
    background:var(--surface);
    border-radius:18px;
    border:1px solid var(--border);
    padding:clamp(.85rem,1.5vw,1.05rem);
    padding-left:clamp(1rem,1.8vw,1.25rem);
    box-shadow:0 1px 3px rgba(15,23,42,.04),0 4px 12px rgba(15,23,42,.04);
    transition:transform .25s cubic-bezier(.34,1.56,.64,1),box-shadow .25s,border-color .25s;
    cursor:pointer;
    user-select:none;
    overflow:hidden;
}
.card::before{
    content:'';
    position:absolute;
    left:0;
    top:0;
    bottom:0;
    width:5px;
    background:linear-gradient(180deg,#94a3b8,#64748b);
    border-radius:18px 0 0 18px;
    transition:width .2s;
}
.card[data-hsk="HSK1"]::before{background:linear-gradient(180deg,#22c55e,#16a34a)}
.card[data-hsk="HSK2"]::before{background:linear-gradient(180deg,#3b82f6,#2563eb)}
.card[data-hsk="HSK3"]::before{background:linear-gradient(180deg,#8b5cf6,#7c3aed)}
.card[data-hsk="HSK4"]::before{background:linear-gradient(180deg,#f59e0b,#d97706)}
.card[data-hsk="HSK5"]::before{background:linear-gradient(180deg,#ef4444,#dc2626)}
.card[data-hsk="HSK6"]::before{background:linear-gradient(180deg,#ec4899,#db2777)}

.card.tapped{animation:tapPulse .6s}
@keyframes tapPulse{0%{box-shadow:0 0 0 0 rgba(37,99,235,.4)}70%{box-shadow:0 0 0 14px rgba(37,99,235,0)}100%{box-shadow:0 0 0 0 rgba(37,99,235,0)}}

.card:hover{
    transform:translateY(-3px);
    box-shadow:0 4px 8px rgba(15,23,42,.06),0 12px 32px rgba(15,23,42,.1);
    border-color:var(--border-strong);
}

.card.focused{
    transform:scale(1.02);
    box-shadow:0 12px 40px rgba(37,99,235,.25);
    border-color:var(--primary);
    background:linear-gradient(135deg,var(--surface) 0%,rgba(37,99,235,.05) 100%);
}
.card.focused::before{width:6px}
[data-theme="dark"] .card{
    box-shadow:0 1px 3px rgba(0,0,0,.3),0 4px 12px rgba(0,0,0,.2);
}
[data-theme="dark"] .card:hover{
    box-shadow:0 4px 8px rgba(0,0,0,.4),0 12px 32px rgba(0,0,0,.3);
}
[data-theme="dark"] .card.focused{
    background:linear-gradient(135deg,var(--surface) 0%,rgba(59,130,246,.15) 100%);
    box-shadow:0 12px 40px rgba(59,130,246,.35);
}
.card.focused .card-zh{
    font-size:clamp(1.65rem,2.5vw,2rem);
    font-weight:600;
    line-height:1.5;
    letter-spacing:.02em;
}

.card-header{
    display:flex;
    align-items:center;
    gap:.5rem;
    margin-bottom:.7rem;
    padding-bottom:.65rem;
    border-bottom:1px dashed var(--border);
    position:relative;
}
.card-stt{
    width:auto;
    min-width:clamp(26px,2.5vw,30px);
    height:clamp(26px,2.5vw,30px);
    padding:0 .5rem;
    border-radius:var(--radius-full);
    background:linear-gradient(135deg,#6366f1,#8b5cf6);
    color:#fff;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:clamp(.66rem,.8vw,.74rem);
    font-weight:800;
    flex-shrink:0;
    box-shadow:0 2px 6px rgba(99,102,241,.35);
    letter-spacing:.02em;
}
.card-meta{
    display:flex;
    gap:.3rem;
    align-items:center;
    flex:1;
    min-width:0;
    flex-wrap:wrap;
}

.card-tag{
    display:inline-flex;
    align-items:center;
    padding:.18rem .55rem;
    border-radius:var(--radius-full);
    background:var(--surface-2);
    color:var(--text-2);
    font-size:clamp(.58rem,.72vw,.68rem);
    font-weight:700;
    white-space:nowrap;
    border:1px solid var(--border);
    letter-spacing:.01em;
}
.card-tag.hsk{
    background:linear-gradient(135deg,rgba(99,102,241,.15),rgba(139,92,246,.12));
    color:#5b21b6;
    border-color:rgba(139,92,246,.3);
    font-weight:800;
}
[data-theme="dark"] .card-tag.hsk{
    background:linear-gradient(135deg,rgba(139,92,246,.25),rgba(167,139,250,.15));
    color:#c4b5fd;
    border-color:rgba(167,139,250,.4);
}
.card-tag.topic{
    background:linear-gradient(135deg,rgba(245,158,11,.15),rgba(217,119,6,.12));
    color:#92400e;
    border-color:rgba(245,158,11,.3);
    font-weight:800;
}
[data-theme="dark"] .card-tag.topic{
    background:linear-gradient(135deg,rgba(245,158,11,.25),rgba(217,119,6,.15));
    color:#fcd34d;
    border-color:rgba(245,158,11,.4);
}
.card-tag.subject{
    background:linear-gradient(135deg,rgba(22,163,74,.12),rgba(21,128,61,.08));
    color:#15803d;
    border-color:rgba(22,163,74,.25);
}
[data-theme="dark"] .card-tag.subject{
    background:linear-gradient(135deg,rgba(22,163,74,.2),rgba(21,128,61,.12));
    color:#4ade80;
    border-color:rgba(22,163,74,.4);
}

.card-tag.tag-clickable {
    cursor: pointer;
    user-select: none;
    transition: transform .15s cubic-bezier(.34,1.56,.64,1),
                box-shadow .2s ease,
                filter .2s ease;
    position: relative;
}
.card-tag.tag-clickable::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: currentColor;
    opacity: 0;
    transition: opacity .15s ease;
    pointer-events: none;
}
.card-tag.tag-clickable:hover {
    transform: translateY(-1px) scale(1.05);
    filter: brightness(1.1);
    box-shadow: 0 4px 10px rgba(0,0,0,.15);
}
.card-tag.tag-clickable:hover::after {
    opacity: 0.08;
}
.card-tag.tag-clickable:active {
    transform: translateY(0) scale(.98);
}
[data-theme="dark"] .card-tag.tag-clickable:hover {
    filter: brightness(1.3);
}
@media (hover: none) {
    .card-tag.tag-clickable:active {
        transform: scale(.95);
        box-shadow: 0 2px 6px rgba(0,0,0,.2);
    }
}

.card-body{
    margin-bottom:.7rem;
    padding-left:.15rem;
}
.card-vi{
    font-size:clamp(.78rem,.9vw,.88rem);
    color:var(--text-2);
    margin-bottom:.5rem;
    line-height:1.5;
    font-weight:500;
    position:relative;
    padding-left:.85rem;
}
.card-vi::before{
    content:'';
    position:absolute;
    left:0;
    top:.55em;
    width:5px;
    height:5px;
    border-radius:50%;
    background:linear-gradient(135deg,#f59e0b,#d97706);
    box-shadow:0 0 0 2px rgba(245,158,11,.2);
}
.card-zh{
    font-size:clamp(1.15rem,1.6vw,1.35rem);
    font-weight:600;
    color:var(--text);
    margin-bottom:.5rem;
    line-height:1.55;
    font-family:var(--font-zh);
    letter-spacing:.03em;
}
.card-pinyin{
    font-size:clamp(.72rem,.88vw,.82rem);
    font-style:italic;
    color:var(--primary-dark);
    background:linear-gradient(135deg,rgba(37,99,235,.08),rgba(37,99,235,.04));
    padding:.3rem .7rem;
    border-radius:50px;
    display:inline-block;
    font-weight:500;
    border:1px solid rgba(37,99,235,.15);
    letter-spacing:.02em;
}
[data-theme="dark"] .card-pinyin{
    background:linear-gradient(135deg,rgba(59,130,246,.2),rgba(59,130,246,.1));
    color:#93c5fd;
    border-color:rgba(59,130,246,.3);
}

.card-excel-row{
    display:inline-flex;
    align-items:center;
    gap:.3rem;
    padding:.18rem .55rem;
    border-radius:var(--radius-full);
    background:linear-gradient(135deg,rgba(22,163,74,.12),rgba(22,163,74,.08));
    color:#15803d;
    font-size:clamp(.58rem,.72vw,.68rem);
    font-weight:800;
    white-space:nowrap;
    border:1px solid rgba(22,163,74,.25);
    letter-spacing:.02em;
}
.card-excel-row i{font-size:.75em;opacity:.85}
[data-theme="dark"] .card-excel-row{
    background:linear-gradient(135deg,rgba(22,163,74,.2),rgba(22,163,74,.12));
    color:#4ade80;
    border-color:rgba(22,163,74,.4);
}

.card-practice{display:flex;align-items:center;gap:.4rem;padding-top:.6rem;border-top:1px dashed var(--border);flex-wrap:wrap}
.card-practice .practice-input{flex:1;min-width:120px}
.card-check{font-size:.75rem;font-weight:700;min-width:55px;text-align:center;width:100%}
.audio-btn{width:clamp(28px,2.8vw,32px);height:clamp(28px,2.8vw,32px);border-radius:50%;border:none;background:var(--primary-light);color:var(--primary-dark);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;font-size:clamp(.72rem,.9vw,.85rem);transition:.15s}
.audio-btn:hover,.audio-btn:active{background:var(--primary);color:#fff;transform:scale(1.08)}
.audio-btn.speaking{background:var(--danger);color:#fff;animation:pulse 1s infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(220,38,38,.6)}50%{box-shadow:0 0 0 10px rgba(220,38,38,0)}}
.write-btn{width:clamp(28px,2.8vw,32px);height:clamp(28px,2.8vw,32px);border-radius:50%;border:none;background:var(--amber-light);color:#92400e;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;font-size:clamp(.7rem,.85vw,.8rem);transition:.15s}
.write-btn:hover,.write-btn:active{background:var(--amber);color:#fff;transform:scale(1.08)}
.practice-full-btn{width:clamp(28px,2.8vw,32px);height:clamp(28px,2.8vw,32px);border-radius:50%;border:none;background:var(--primary-light);color:var(--primary-dark);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;font-size:clamp(.7rem,.85vw,.8rem);transition:.15s}
.practice-full-btn:hover,.practice-full-btn:active{background:var(--primary);color:#fff;transform:scale(1.08)}
.toggle-check-btn{width:clamp(28px,2.8vw,32px);height:clamp(28px,2.8vw,32px);border-radius:50%;border:1px solid var(--border);background:var(--surface-2);color:var(--text-2);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;font-size:clamp(.7rem,.85vw,.8rem);transition:.15s;flex-shrink:0}
.toggle-check-btn:hover{background:var(--primary-light);color:var(--primary-dark);border-color:var(--primary)}
.toggle-check-btn.active{background:var(--primary);color:#fff;border-color:var(--primary)}
.action-group{display:flex;gap:.3rem;justify-content:center;align-items:center}
.practice-input{width:100%;min-width:120px;padding:clamp(.35rem,.6vh,.5rem) clamp(.55rem,.8vw,.8rem);border-radius:var(--radius-full);border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:clamp(.78rem,.9vw,.9rem);outline:none;transition:.15s;font-family:var(--font-zh)}
.practice-input:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(37,99,235,.15)}
.practice-input,.audio-btn,.write-btn,.card-practice{cursor:auto}
.load-more{grid-column:1 / -1;display:block;width:100%;padding:clamp(.6rem,1.2vh,.9rem);margin-top:.5rem;border-radius:var(--radius);border:1.5px dashed var(--border-strong);background:var(--surface);color:var(--primary);font-weight:700;font-size:clamp(.78rem,.9vw,.88rem);cursor:pointer;transition:.15s;font-family:inherit}
.load-more:hover{background:var(--primary-light);border-color:var(--primary)}
.load-more.locked{border-color:var(--amber);color:#92400e;background:var(--amber-light)}
.load-more.locked.expired{border-color:var(--danger);color:var(--danger);background:var(--danger-light)}
.end-note{grid-column:1 / -1;text-align:center;padding:1rem;color:var(--text-3);font-size:.82rem}
.end-note i{color:var(--success);margin-right:.35rem}
.no-data{grid-column:1 / -1;text-align:center;padding:3rem 1rem;color:var(--text-3);background:var(--surface);border-radius:var(--radius);border:1px solid var(--border)}
.no-data i{font-size:2.5rem;margin-bottom:.75rem;color:var(--border-strong);display:block}
.practice-full-modal{position:fixed;inset:0;background:var(--bg);z-index:2500;display:none;flex-direction:column;animation:fadeIn .2s;overflow:hidden;height:100vh;height:100dvh}
.practice-full-modal.show{display:flex}
body.practice-full-open .search-bar,body.practice-full-open .filters,body.practice-full-open .result-count{display:none!important}
body.practice-full-open .demo-banner,body.practice-full-open .expiry-banner{display:none!important}
.practice-full-header{display:flex;align-items:center;gap:clamp(.4rem,.8vw,.75rem);padding:clamp(.45rem,1vh,.7rem) clamp(.85rem,2vw,1.25rem);background:var(--surface);border-bottom:1px solid var(--border);flex:0 0 auto;min-height:clamp(48px,7vh,60px);box-shadow:0 2px 8px rgba(15,23,42,.04);overflow:visible;flex-wrap:nowrap;width:100%}
.practice-full-header .pf-counter{font-size:clamp(.68rem,.88vw,.8rem);font-weight:800;color:#fff;background:linear-gradient(135deg,#4f46e5,#7c3aed);padding:.35rem .75rem;border-radius:50px;white-space:nowrap;flex-shrink:0}
.practice-full-header .pf-tags{display:flex;gap:.3rem;flex:1 1 auto;min-width:0;flex-wrap:nowrap;overflow-x:auto;overflow-y:hidden;scrollbar-width:none;padding:2px 0;max-width:100%}
.practice-full-header .pf-tags::-webkit-scrollbar{display:none}
.practice-full-header .pf-tags .card-tag{flex-shrink:0;font-weight:700}
.practice-full-header .pf-close{width:clamp(30px,3vw,36px);height:clamp(30px,3vw,36px);border-radius:50%;border:none;background:var(--surface-2);color:var(--text-2);cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.practice-full-header .pf-close:hover{background:var(--danger-light);color:var(--danger)}
.pf-brand{display:flex;align-items:center;gap:clamp(.4rem,.8vw,.65rem);flex:0 0 auto;min-width:0}
.pf-brand-icon{width:clamp(30px,2.8vw,38px);height:clamp(30px,2.8vw,38px);border-radius:clamp(8px,.9vw,11px);background:linear-gradient(135deg,#6366f1 0%,#8b5cf6 40%,#d946ef 100%);display:flex;align-items:center;justify-content:center;color:#fff;font-size:clamp(.78rem,1vw,.95rem);flex-shrink:0}
.pf-brand-text{display:flex;flex-direction:column;line-height:1.15;min-width:0;overflow:hidden;gap:2px}
.pf-brand-title{font-size:clamp(.8rem,1vw,.95rem);font-weight:900;background:linear-gradient(135deg,#1e293b 0%,#4f46e5 50%,#7c3aed 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;white-space:nowrap}
[data-theme="dark"] .pf-brand-title{background:linear-gradient(135deg,#f1f5f9 0%,#a5b4fc 50%,#c4b5fd 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.pf-brand-sub{display:inline-flex;align-items:center;gap:.25rem;font-size:clamp(.58rem,.72vw,.68rem);font-weight:700;color:#5b21b6;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pf-brand-sub::before{content:'\2726';color:#d946ef;font-size:.95em;animation:sparklePF 2.5s ease-in-out infinite}
@keyframes sparklePF{0%,100%{opacity:.65;transform:scale(1) rotate(0deg)}50%{opacity:1;transform:scale(1.2) rotate(18deg)}}
[data-theme="dark"] .pf-brand-sub{color:#ddd6fe}
[data-theme="dark"] .pf-brand-sub::before{color:#f0abfc}
@media (max-width:768px){.pf-brand-title{font-size:.75rem}.pf-brand-sub{font-size:.55rem;gap:.2rem}.pf-brand-icon{width:28px;height:28px;font-size:.72rem;border-radius:8px}.pf-brand{gap:.4rem}}
@media (max-width:400px){.pf-brand-title{font-size:.7rem}.pf-brand-sub{font-size:.5rem}.pf-brand-icon{width:24px;height:24px;font-size:.65rem}}

/* TIKTOK FLOAT */
.pf-tiktok-float{position:fixed;left:clamp(14px,2vw,22px);bottom:calc(80px + env(safe-area-inset-bottom));display:inline-flex;align-items:center;gap:clamp(.4rem,.6vw,.55rem);padding:clamp(.35rem,.55vw,.5rem) clamp(.7rem,1vw,.9rem) clamp(.35rem,.55vw,.5rem) clamp(.35rem,.55vw,.5rem);border-radius:999px;background:linear-gradient(135deg,#25f4ee 0%,#000 50%,#fe2c55 100%);color:#fff;text-decoration:none;font-family:inherit;min-width:clamp(120px,15vw,180px);max-width:clamp(160px,22vw,240px);box-shadow:0 10px 28px rgba(254,44,85,.4),0 4px 14px rgba(0,0,0,.35);z-index:2400;transition:transform .25s cubic-bezier(.34,1.56,.64,1),box-shadow .25s ease;overflow:hidden;cursor:pointer}
.pf-tiktok-float:hover{transform:translateY(-3px) scale(1.04);box-shadow:0 14px 36px rgba(254,44,85,.6),0 6px 20px rgba(0,0,0,.45),0 0 0 3px rgba(37,244,238,.5)}
.pf-tiktok-avatar-wrap{position:relative;width:clamp(28px,3vw,36px);height:clamp(28px,3vw,36px);border-radius:50%;flex-shrink:0;background:linear-gradient(135deg,#25f4ee,#fe2c55);display:flex;align-items:center;justify-content:center;padding:2px;box-shadow:0 0 0 2px rgba(255,255,255,.9)}
.pf-tiktok-avatar{width:100%;height:100%;border-radius:50%;object-fit:cover;display:block;background:#fff}
.pf-tiktok-fallback-icon{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-size:clamp(.9rem,1.1vw,1.1rem);background:linear-gradient(135deg,#25f4ee,#000,#fe2c55);border-radius:50%;pointer-events:none;z-index:-1}
.pf-tiktok-avatar[src]:not([src=""]) + .pf-tiktok-fallback-icon{display:none}
.pf-tiktok-content{display:flex;flex-direction:column;line-height:1.1;min-width:0;flex:1;text-align:left}
.pf-tiktok-label{font-size:clamp(.5rem,.62vw,.6rem);font-weight:600;opacity:.8;letter-spacing:.4px;text-transform:uppercase;white-space:nowrap}
.pf-tiktok-name{font-size:clamp(.7rem,.88vw,.82rem);font-weight:800;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%}
.pf-tiktok-badge{font-size:clamp(.85rem,1.1vw,1rem);flex-shrink:0;animation:tiktokPulse 2s ease-in-out infinite}
@keyframes tiktokPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
@media (max-width:500px){.pf-tiktok-float{min-width:110px;max-width:min(65vw,180px);padding:.3rem .6rem .3rem .3rem;left:12px;bottom:calc(78px + env(safe-area-inset-bottom))}.pf-tiktok-avatar-wrap{width:26px;height:26px}.pf-tiktok-label{font-size:.5rem}.pf-tiktok-name{font-size:.68rem}.pf-tiktok-badge{font-size:.8rem}}
@media (max-width:500px) and (max-height:700px){.pf-tiktok-float{bottom:calc(72px + env(safe-area-inset-bottom))}}
@media (max-height:550px) and (orientation:landscape){.pf-tiktok-float{bottom:calc(64px + env(safe-area-inset-bottom))}}
@media (max-height:420px) and (orientation:landscape){.pf-tiktok-float{bottom:calc(56px + env(safe-area-inset-bottom));transform:scale(.85);transform-origin:left bottom}}
.practice-full-modal:not(.show) .pf-tiktok-float{display:none!important}
body.practice-full-open .pf-tiktok-float {
    display: none !important;}

/* ============================================================ */
/* FILTERS trong Practice Full                                    */
/* ============================================================ */
.pf-filters{padding:clamp(.4rem,1vh,.55rem) clamp(.85rem,2vw,1.25rem) clamp(.35rem,.8vh,.45rem);background:var(--surface);border-bottom:1px solid var(--border);flex:0 0 auto;overflow:visible}
.pf-filter-row{display:grid;grid-template-columns:1fr 1fr;gap:.5rem}
.pf-chip{display:flex;align-items:center;gap:.4rem;padding:clamp(.25rem,.5vh,.4rem) clamp(.5rem,.8vw,.75rem);border-radius:var(--radius-full);border:1.5px solid var(--border);background:var(--bg);color:var(--text);font-size:clamp(.68rem,.85vw,.78rem);cursor:pointer;min-width:0;position:relative;overflow:hidden}
.pf-chip.has-value{background:var(--primary);color:#fff;border-color:var(--primary)}
.pf-chip-label{font-size:clamp(.55rem,.7vw,.62rem);color:var(--text-3);text-transform:uppercase;font-weight:700;flex-shrink:0}
.pf-chip.has-value .pf-chip-label{color:#fff;opacity:.85}
.pf-chip-value{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1;min-width:0}
.pf-chip-arrow{opacity:.5;font-size:.62rem;flex-shrink:0}
.pf-chip select{position:absolute;inset:0;opacity:0;cursor:pointer;appearance:none;width:100%;height:100%;z-index:5}

/* ============================================================ */
/* KHOI GOP: BO DU LIEU + TIM KIEM + CHON CAU                    */
/* ============================================================ */
.pf-dataset-row {
    display: flex;
    align-items: center;
    gap: .5rem;
    margin-top: .45rem;
    padding: .5rem .65rem;
    background: linear-gradient(135deg,
        rgba(99, 102, 241, 0.08),
        rgba(139, 92, 246, 0.06));
    border: 1.5px solid rgba(139, 92, 246, 0.25);
    border-radius: 12px;
    position: relative;
    transition: .2s;
    flex-wrap: wrap;
}
[data-theme="dark"] .pf-dataset-row {
    background: linear-gradient(135deg,
        rgba(99, 102, 241, 0.15),
        rgba(139, 92, 246, 0.12));
    border-color: rgba(165, 180, 252, 0.3);
}
.pf-dataset-row.has-locked-options {
    border-color: rgba(139, 92, 246, 0.25);
}
.pf-dataset-label {
    font-size: clamp(.6rem, .72vw, .68rem);
    font-weight: 800;
    color: #5b21b6;
    text-transform: uppercase;
    letter-spacing: .4px;
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: .3rem;
    flex-shrink: 0;
}
[data-theme="dark"] .pf-dataset-label {
    color: #c4b5fd;
}
.pf-dataset-label i {
    color: #d946ef;
    font-size: .9em;
}
.pf-dataset-select {
    flex: 1 1 160px;
    min-width: 0;
    padding: clamp(.32rem, .55vh, .45rem) 2rem clamp(.32rem, .55vh, .45rem) .75rem;
    border-radius: 999px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-size: clamp(.72rem, .85vw, .82rem);
    font-weight: 700;
    font-family: inherit;
    outline: none;
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'><path fill='%2394a3b8' d='M6 9L1 4h10z'/></svg>");
    background-repeat: no-repeat;
    background-position: right 12px center;
    background-size: 10px;
    transition: .15s;
}
.pf-dataset-select:focus {
    border-color: #8b5cf6;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15);
}
.pf-dataset-select option.locked-opt {
    color: #94a3b8;
}

.pf-dataset-search {
    flex: 1 1 100%;
    min-width: 0;
    position: relative;
}
.pf-dataset-search i.fa-search {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-3);
    font-size: .78rem;
    pointer-events: none;
}
.pf-dataset-search input {
    width: 100%;
    padding: clamp(.32rem, .55vh, .45rem) 2rem clamp(.32rem, .55vh, .45rem) 2rem;
    border-radius: 999px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-size: clamp(.72rem, .85vw, .82rem);
    font-family: inherit;
    outline: none;
    transition: .15s;
}
.pf-dataset-search input:focus {
    border-color: #8b5cf6;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15);
}
.pf-dataset-search .pf-search-clear {
    position: absolute;
    right: 6px;
    top: 50%;
    transform: translateY(-50%);
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: none;
    background: var(--surface-2);
    color: var(--text-2);
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    font-size: .7rem;
}
.pf-dataset-search .pf-search-clear.show { display: flex; }

@media (min-width: 600px) {
    .pf-dataset-search {
        flex: 1 1 auto;
        max-width: 45%;
    }
}

.pf-dataset-row .pf-quick-nav {
    flex: 1 1 100%;
    width: 100%;
    margin-top: .25rem;
    padding-top: .5rem;
    border-top: 1px dashed rgba(139, 92, 246, 0.25);
    display: flex !important;
    align-items: center;
    gap: .5rem;
    visibility: visible !important;
    opacity: 1 !important;
}
[data-theme="dark"] .pf-dataset-row .pf-quick-nav {
    border-top-color: rgba(165, 180, 252, 0.25);
}
.pf-quick-nav-label {
    font-size: clamp(.55rem, .72vw, .68rem);
    font-weight: 700;
    color: var(--text-3);
    text-transform: uppercase;
    white-space: nowrap;
    flex-shrink: 0;
}
.pf-quick-nav-select {
    flex: 1 1 auto;
    min-width: 0;
    padding: clamp(.25rem, .5vh, .45rem) 2rem;
    border-radius: var(--radius-full);
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-size: clamp(.68rem, .85vw, .78rem);
    font-family: inherit;
    outline: none;
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'><path fill='%2394a3b8' d='M6 9L1 4h10z'/></svg>");
    background-repeat: no-repeat;
    background-position: right 12px center;
    background-size: 10px;
    transition: .15s;
}
.pf-quick-nav-select:focus {
    border-color: #8b5cf6;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15);
}

@media (max-width: 500px) {
    .pf-dataset-label {
        font-size: .58rem;
        gap: .2rem;
    }
    .pf-dataset-label i { display: none; }
    .pf-dataset-select {
        font-size: .7rem;
        padding-left: .6rem;
    }
}

.practice-full-body{flex:1 1 auto;min-height:0;overflow-y:auto;padding:clamp(.85rem,2vh,1.5rem) clamp(.75rem,2vw,1.25rem) calc(80px + env(safe-area-inset-bottom));display:flex;flex-direction:column;align-items:center;justify-content:flex-start;scrollbar-width:thin}
.practice-full-content{width:100%;max-width:clamp(320px,60vw,700px);display:flex;flex-direction:column;gap:clamp(.65rem,1.5vh,1.25rem);margin-top:auto;margin-bottom:auto}
.practice-full-vi{font-size:clamp(1.15rem,2.2vw,1.65rem);font-weight:600;color:var(--text);text-align:center;line-height:1.45;padding:clamp(.7rem,1.5vh,1.1rem) clamp(.6rem,1.5vw,.9rem);background:linear-gradient(135deg,var(--surface-2),rgba(37,99,235,.06));border-radius:16px;border-left:4px solid var(--primary)}
@media(min-width:769px){.practice-full-vi{font-size:clamp(1.4rem,2.5vw,2rem)}}
.practice-full-input-wrap{display:flex;flex-direction:column;gap:clamp(.4rem,.8vh,.65rem)}
.practice-input-row{position:relative;display:flex;align-items:stretch;gap:.5rem}
.practice-input-row .practice-full-input{flex:1;min-width:0}
.practice-full-input{width:100%;padding:clamp(.7rem,1.5vh,.9rem) clamp(.85rem,1.5vw,1.1rem);font-size:clamp(1.15rem,2.2vw,1.35rem);font-family:var(--font-zh);border-radius:14px;border:2px solid var(--border);background:var(--surface);color:var(--text);outline:none;transition:border-color .15s,box-shadow .15s;text-align:center;letter-spacing:.05em;box-shadow:0 2px 8px rgba(15,23,42,.04);resize:none;overflow-y:hidden;min-height:calc(1em * 1.5 + 1.4rem);max-height:40vh;line-height:1.5;word-break:break-word;white-space:pre-wrap;display:block}
.practice-full-input:focus{border-color:var(--primary);box-shadow:0 0 0 4px rgba(37,99,235,.15),0 8px 24px rgba(37,99,235,.15)}
.practice-full-input.multiline{text-align:left}
@media(min-width:769px){.practice-full-input{font-size:clamp(1.35rem,2.6vw,1.6rem);padding:clamp(.85rem,1.8vh,1rem) clamp(1rem,2vw,1.3rem)}}
@media(min-width:1400px){.practice-full-input{font-size:1.7rem;padding:1.05rem 1.4rem}}

.practice-speak-btn{
    width:auto;
    min-width:clamp(38px,4.5vw,46px);
    padding:0 clamp(.45rem,.8vw,.65rem);
    border-radius:14px;
    border:2px solid var(--primary);
    background:var(--primary-light);
    color:var(--primary-dark);
    font-size:clamp(.9rem,1.3vw,1.1rem);
    cursor:pointer;
    display:flex;
    align-items:center;
    justify-content:center;
    flex-shrink:0;
    transition:transform .15s,background .2s,color .2s,border-color .2s;
    position:relative;
}
.practice-speak-btn:hover,.practice-speak-btn:active{background:var(--primary);color:#fff;transform:scale(1.05)}
.practice-speak-btn.speaking{background:var(--danger);color:#fff;border-color:var(--danger);animation:pulse 1s infinite}
.practice-speak-btn.speaking::after{
    content:'';
    position:absolute;
    inset:-2px;
    border-radius:14px;
    border:2px solid var(--danger);
    animation:speakingRing 1s infinite;
}
@keyframes speakingRing{0%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(1.15)}}
.practice-speak-btn:disabled{opacity:.4;cursor:not-allowed}
[data-theme="dark"] .practice-speak-btn{background:rgba(59,130,246,.22);color:#93c5fd;border-color:rgba(59,130,246,.5)}
.practice-speak-btn.speaking i.fa-stop{animation:stopPulse .8s ease-in-out infinite}
@keyframes stopPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.2)}}

.char-preview{display:flex;justify-content:center;flex-wrap:wrap;gap:clamp(.3rem,.6vw,.45rem);min-height:clamp(1.75rem,3vh,2.25rem);padding:clamp(.4rem,.8vh,.65rem) clamp(.5rem,1.2vw,.9rem);background:var(--surface-2);border-radius:12px;border:1px dashed var(--border);user-select:none}
.char-preview:empty{display:none}
.char-slot{font-family:var(--font-zh);font-size:clamp(1.15rem,2vw,1.5rem);font-weight:500;display:inline-flex;align-items:center;justify-content:center;min-width:clamp(1.3rem,2.2vw,1.7rem);height:clamp(1.75rem,3vh,2.25rem);padding:0 .35rem;border-radius:8px;line-height:1}
@media(min-width:769px){.char-slot{font-size:clamp(1.4rem,2.5vw,1.8rem);min-width:2rem;height:2.6rem}}
.char-slot.correct{color:var(--text);font-weight:700;background:rgba(22,163,74,.12)}
.char-slot.wrong{color:#fff;background:var(--danger);animation:shakeWrong .3s;box-shadow:0 2px 8px rgba(220,38,38,.35);cursor:pointer;position:relative}
.char-slot.wrong:hover{transform:scale(1.15);z-index:5}
.char-slot.wrong.highlight{animation:blinkHighlight 0.6s ease-in-out 2}
@keyframes blinkHighlight{0%,100%{transform:scale(1.15);background:var(--danger)}50%{transform:scale(1.25);background:#ef4444}}
.char-slot.ghost{color:var(--text);opacity:.12;font-weight:400;background:transparent;pointer-events:none}
.char-slot.extra{color:#fff;background:var(--amber);box-shadow:0 2px 8px rgba(245,158,11,.35);cursor:pointer}
.char-slot.extra:hover{transform:scale(1.15);z-index:5}
.char-slot.ghost-missing{color:var(--text-3);opacity:.5;background:transparent;border:1px dashed var(--border);cursor:pointer;font-size:1.15rem}
.char-slot.ghost-missing:hover{opacity:.9;border-color:var(--primary);color:var(--primary);transform:scale(1.1)}
@keyframes shakeWrong{0%,100%{transform:translateX(0)}25%{transform:translateX(-3px)}75%{transform:translateX(3px)}}
.inline-char-preview{display:flex;flex-wrap:wrap;gap:.25rem;margin-top:.4rem;width:100%}
.inline-char-preview .char-slot{font-size:.95rem;min-width:1.1rem;height:1.5rem;padding:0 .25rem;border-radius:5px}
.practice-full-status{text-align:center;font-size:clamp(.8rem,1vw,.95rem);font-weight:700;min-height:1.4rem}
.practice-full-status.correct{color:var(--success)}
.practice-full-status.partial{color:var(--amber)}
.practice-full-status.wrong{color:var(--danger)}
.reveal-actions{display:grid;grid-template-columns:1fr 1fr;gap:clamp(.5rem,1vw,.7rem)}
.reveal-actions button{width:100%;padding:clamp(.55rem,1.2vh,.75rem);border-radius:14px;border:2px dashed var(--border-strong);background:var(--surface);color:var(--text-2);font-size:clamp(.78rem,.9vw,.88rem);font-weight:600;cursor:pointer;transition:all .2s;font-family:inherit;display:flex;align-items:center;justify-content:center;gap:.5rem}
.reveal-actions button:hover{border-color:var(--primary);color:var(--primary);background:var(--primary-light)}
#pfHintBtn.active{background:var(--amber);color:#fff;border-color:var(--amber);border-style:solid}
#pfRevealBtn.revealed{background:var(--success);color:#fff;border-color:var(--success);border-style:solid}
.answer-reveal{display:none;flex-direction:column;gap:.7rem;padding:clamp(.85rem,1.5vw,1.1rem);background:var(--surface-2);border-radius:14px;border:1px solid var(--border)}
.answer-reveal.show{display:flex}
.answer-chars{display:flex;justify-content:center;flex-wrap:wrap;gap:.45rem}
.answer-phrase-btn{font-family:var(--font-zh);font-size:clamp(1.1rem,1.8vw,1.35rem);font-weight:500;padding:clamp(.35rem,.8vh,.45rem) clamp(.65rem,1.2vw,.85rem);border-radius:12px;border:2px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;transition:transform .25s cubic-bezier(.34,1.56,.64,1),background .2s,color .2s;display:inline-flex;align-items:center;justify-content:center}
@media(hover:hover) and (pointer:fine){.answer-phrase-btn:hover{transform:scale(1.35);background:var(--primary);color:#fff;border-color:var(--primary);z-index:10}}
.answer-phrase-btn.zoom-in{transform:scale(1.35);background:var(--primary);color:#fff;border-color:var(--primary);z-index:10}
.answer-phrase-btn.speaking{background:var(--primary);color:#fff;border-color:var(--primary);animation:pulse 1s infinite}
@media(min-width:769px){.answer-phrase-btn{font-size:clamp(1.3rem,2.2vw,1.6rem);padding:.55rem 1rem}}
.answer-pinyin{text-align:center;font-size:clamp(.78rem,.95vw,.9rem);font-style:italic;color:var(--primary-dark);font-weight:500}
.answer-actions{display:flex;justify-content:center;gap:.5rem;flex-wrap:wrap}
.answer-actions button{padding:.55rem 1rem;border-radius:50px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:.82rem;font-weight:600;cursor:pointer;font-family:inherit;display:inline-flex;align-items:center;gap:.4rem}
.answer-actions button:hover{background:var(--surface-2);border-color:var(--primary);color:var(--primary)}
.answer-actions button.primary{background:var(--primary);color:#fff;border-color:var(--primary)}

.answer-phrase-btn.reading{
    background:linear-gradient(135deg,#f59e0b,#d97706) !important;
    color:#fff !important;
    border-color:#f59e0b !important;
    transform:scale(1.2) !important;
    box-shadow:0 8px 20px rgba(245,158,11,.5) !important;
    transition:all .15s ease-out;
}
.answer-phrase-wrap{
    position:relative;
    display:inline-flex;
}
.answer-phrase-tooltip{
    position:absolute;
    bottom:calc(100% + 10px);
    left:50%;
    transform:translateX(-50%) translateY(6px) scale(.95);
    background:linear-gradient(135deg,#f59e0b,#d97706);
    color:#fff;
    padding:.4rem .75rem;
    border-radius:12px;
    font-size:.78rem;
    font-style:italic;
    font-weight:700;
    white-space:nowrap;
    border:1px solid rgba(255,255,255,.3);
    box-shadow:0 12px 32px rgba(245,158,11,.5),0 4px 12px rgba(0,0,0,.15);
    pointer-events:none;
    opacity:0;
    visibility:hidden;
    transition:opacity .2s,transform .2s,visibility .2s;
    z-index:1000;
    letter-spacing:.02em;
    text-shadow:0 1px 2px rgba(0,0,0,.15);
}
.answer-phrase-tooltip::after{
    content:'';
    position:absolute;
    top:100%;
    left:50%;
    transform:translateX(-50%);
    border:7px solid transparent;
    border-top-color:#d97706;
    filter:drop-shadow(0 2px 2px rgba(245,158,11,.3));
}
.answer-phrase-tooltip.show{
    opacity:1;
    visibility:visible;
    transform:translateX(-50%) translateY(0) scale(1);
}
.answer-phrase-wrap.active-wrap{
    z-index:100 !important;
    position:relative;
}
.answer-phrase-btn.reading{
    position:relative;
    z-index:10;
}
@media (max-width:768px){
    .answer-phrase-btn.reading{
        transform:scale(1.15) !important;
    }
    .answer-phrase-tooltip{
        font-size:.72rem;
        padding:.3rem .55rem;
        max-width:80vw;
        white-space:normal;
        text-align:center;
    }
}

/* ============================================================ */
/* NAV - 3 NUT TO DEU NHAU + MINI GROUP                          */
/* ============================================================ */
.practice-full-nav{
    display:flex;
    gap:.65rem;
    padding:.65rem 1rem;
    background:var(--surface);
    border-top:1px solid var(--border);
    flex:0 0 auto;
    justify-content:center;
    align-items:center;
    min-height:72px;
}

.pf-nav-icon{
    width:clamp(42px,5vw,50px);
    height:clamp(42px,5vw,50px);
    border-radius:50%;
    border:1.5px solid var(--border);
    background:var(--surface);
    color:var(--text-2);
    cursor:pointer;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    font-size:clamp(.95rem,1.15vw,1.1rem);
    font-family:inherit;
    padding:0;
    flex-shrink:0;
    transition:transform .15s cubic-bezier(.34,1.56,.64,1),background .2s,color .2s,border-color .2s,box-shadow .2s,opacity .2s;
    box-shadow:0 2px 6px rgba(15,23,42,.06);
    position:relative;
}
.pf-nav-icon:disabled{
    opacity:.3;
    cursor:not-allowed;
}

.pf-nav-icon.main-nav{
    width:clamp(56px,7vw,68px);
    height:clamp(56px,7vw,68px);
    font-size:clamp(1.3rem,1.8vw,1.6rem);
    border-width:2px;
}
.pf-nav-icon.main-nav:not(.primary):not(.speak){
    background:var(--surface);
    color:var(--text);
    border:2px solid var(--border);
    box-shadow:0 4px 12px rgba(15,23,42,.12);
}
.pf-nav-icon.main-nav:not(.primary):not(.speak):hover:not(:disabled){
    transform:scale(1.12);
    border-color:var(--primary);
    color:var(--primary);
    box-shadow:0 8px 20px rgba(37,99,235,.3);
}
.pf-nav-icon.main-nav:not(.primary):not(.speak):active:not(:disabled){
    transform:scale(1.02);
}
.pf-nav-icon.main-nav.primary{
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;
    border-color:transparent;
    box-shadow:0 8px 22px rgba(124,58,237,.5);
    transform:scale(1.08);
}
.pf-nav-icon.main-nav.primary:hover:not(:disabled){
    transform:scale(1.15);
    background:linear-gradient(135deg,#4338ca,#6d28d9);
    box-shadow:0 12px 30px rgba(124,58,237,.65);
}
.pf-nav-icon.main-nav.primary:active:not(:disabled){
    transform:scale(1.05);
}
.pf-nav-icon.main-nav.speak{
    background:linear-gradient(135deg,#3b82f6,#2563eb);
    color:#fff;
    border-color:transparent;
    box-shadow:0 8px 22px rgba(37,99,235,.45);
}
.pf-nav-icon.main-nav.speak:hover:not(:disabled){
    transform:scale(1.12);
    background:linear-gradient(135deg,#2563eb,#1d4ed8);
    box-shadow:0 12px 30px rgba(37,99,235,.65);
}
.pf-nav-icon.main-nav.speak.speaking{
    background:linear-gradient(135deg,#dc2626,#b91c1c);
    color:#fff;
    border-color:transparent;
    animation:pulse 1s infinite;
}
.pf-nav-icon.main-nav.speak.speaking::after{
    content:'';
    position:absolute;
    inset:-3px;
    border-radius:50%;
    border:2px solid var(--danger);
    animation:speakingRing 1s infinite;
}
.pf-nav-icon.main-nav.speak i.fa-stop{
    animation:stopPulse .8s ease-in-out infinite;
}

.pf-nav-icon.mini-nav{
    width:clamp(44px,5vw,52px);
    height:clamp(44px,5vw,52px);
    font-size:clamp(.9rem,1.1vw,1rem);
    border-width:1.5px;
    opacity:.85;
}
.pf-nav-icon.mini-nav:hover:not(:disabled){
    opacity:1;
    transform:scale(1.08);
}
.pf-nav-icon.mini-nav.voice{
    background:rgba(6,182,212,.12);
    color:#0891b2;
    border-color:rgba(6,182,212,.35);
}
.pf-nav-icon.mini-nav.voice:hover:not(:disabled){
    background:linear-gradient(135deg,#06b6d4,#0891b2);
    color:#fff;
    border-color:#0891b2;
    box-shadow:0 6px 16px rgba(6,182,212,.4);
}

.pf-nav-icon.mini-nav.random{
    background:var(--surface);
    color:var(--text-2);
    border-color:var(--border);
}
.pf-nav-icon.mini-nav.random:hover:not(:disabled){
    transform:scale(1.08);
    border-color:#f59e0b;
    color:#d97706;
    background:rgba(245,158,11,.1);
}
.pf-nav-icon.mini-nav.random.active{
    background:linear-gradient(135deg, #f59e0b, #d97706);
    color:#fff;
    border-color:transparent;
    box-shadow:0 4px 12px rgba(245,158,11,.5);
    opacity:1;
    animation:randomPulse 2s ease-in-out infinite;
}
.pf-nav-icon.mini-nav.random.active:hover:not(:disabled){
    transform:scale(1.12);
    box-shadow:0 6px 18px rgba(245,158,11,.7);
    border-color:transparent;
}
.pf-nav-icon.mini-nav.random.active i{
    animation:diceShake 0.6s ease-in-out;
}
@keyframes randomPulse{
    0%,100%{ box-shadow:0 4px 12px rgba(245,158,11,.5); }
    50%{ box-shadow:0 4px 18px rgba(245,158,11,.85); }
}
@keyframes diceShake{
    0%,100%{ transform:rotate(0deg); }
    25%{ transform:rotate(-15deg); }
    75%{ transform:rotate(15deg); }
}
[data-theme="dark"] .pf-nav-icon.mini-nav.random{
    background:var(--surface-2);
    color:var(--text-2);
    border-color:var(--border);
}
[data-theme="dark"] .pf-nav-icon.mini-nav.random.active{
    background:linear-gradient(135deg, #fbbf24, #f59e0b);
    color:#1e1b4b;
}

.practice-full-nav .mini-group{
    display:flex;
    gap:.35rem;
    margin-left:.5rem;
    padding-left:.75rem;
    border-left:1.5px solid var(--border);
}

[data-theme="dark"] .pf-nav-icon.main-nav:not(.primary):not(.speak){
    background:var(--surface-2);
    color:var(--text);
    border-color:var(--border);
    box-shadow:0 2px 6px rgba(0,0,0,.3);
}
[data-theme="dark"] .pf-nav-icon.main-nav:not(.primary):not(.speak):hover:not(:disabled){
    border-color:var(--primary);
    color:#93c5fd;
}

@media(max-width:768px){
    .practice-full-nav{
        gap:.5rem;
        padding:.55rem .7rem;
        min-height:66px;
    }
    .pf-nav-icon.main-nav{
        width:54px;
        height:54px;
        font-size:1.25rem;
    }
    .pf-nav-icon.mini-nav{
        width:44px;
        height:44px;
        font-size:.9rem;
    }
}
@media(max-width:400px){
    .practice-full-nav{
        gap:.4rem;
        padding:.5rem .5rem;
    }
    .pf-nav-icon.main-nav{
        width:50px;
        height:50px;
        font-size:1.15rem;
    }
    .pf-nav-icon.mini-nav{
        width:40px;
        height:40px;
        font-size:.85rem;
    }
    .practice-full-nav .mini-group{
        gap:.25rem;
        padding-left:.5rem;
    }
}

@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.writer-modal{position:fixed;inset:0;background:rgba(15,23,42,.7);backdrop-filter:blur(4px);z-index:2000;display:none;align-items:center;justify-content:center;padding:1rem;animation:fadeIn .2s}
.writer-modal.show{display:flex}
.writer-box{background:var(--surface);border-radius:20px;padding:clamp(1rem,2vw,1.5rem) clamp(.9rem,1.5vw,1.25rem);max-width:420px;width:100%;max-height:calc(100vh - 2rem);overflow-y:auto;box-shadow:0 20px 60px rgba(0,0,0,.3);position:relative}
.writer-close{position:absolute;top:10px;right:10px;width:34px;height:34px;border-radius:50%;border:none;background:var(--surface-2);color:var(--text-2);cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:5}
.writer-close:hover{background:var(--danger-light);color:var(--danger)}
.writer-char-info{text-align:center;margin-bottom:.75rem}
.writer-char-info .vi-small{font-size:.85rem;color:var(--text-2);margin-bottom:.3rem;line-height:1.4}
.writer-char-info .pinyin-small{font-size:.8rem;font-style:italic;color:var(--primary-dark);background:var(--surface-2);padding:.2rem .6rem;border-radius:6px;display:inline-block}
[data-theme="dark"] .writer-char-info .pinyin-small{background:rgba(59,130,246,.18);color:#93c5fd}
.writer-chars{display:flex;gap:.4rem;justify-content:center;flex-wrap:wrap;margin-bottom:.75rem}
.writer-char-btn{width:clamp(36px,4vw,42px);height:clamp(36px,4vw,42px);border-radius:10px;border:1.5px solid var(--border);background:var(--surface-2);color:var(--text);font-family:var(--font-zh);font-size:clamp(1.1rem,1.5vw,1.3rem);cursor:pointer;display:flex;align-items:center;justify-content:center;padding:0}
.writer-char-btn:hover{border-color:var(--primary)}
.writer-char-btn.active{background:var(--primary);color:#fff;border-color:var(--primary)}
.writer-target{width:clamp(220px,60vw,280px);height:clamp(220px,60vw,280px);margin:0 auto;background:#fff;border-radius:14px;position:relative;box-shadow:inset 0 0 0 2px var(--border);overflow:hidden;background-image:linear-gradient(to right,transparent calc(50% - 0.5px),#e2e8f0 calc(50% - 0.5px),#e2e8f0 calc(50% + 0.5px),transparent calc(50% + 0.5px)),linear-gradient(to bottom,transparent calc(50% - 0.5px),#e2e8f0 calc(50% - 0.5px),#e2e8f0 calc(50% + 0.5px),transparent calc(50% + 0.5px)),linear-gradient(45deg,transparent calc(50% - 0.5px),#e2e8f0 calc(50% - 0.5px),#e2e8f0 calc(50% + 0.5px),transparent calc(50% + 0.5px)),linear-gradient(-45deg,transparent calc(50% - 0.5px),#e2e8f0 calc(50% - 0.5px),#e2e8f0 calc(50% + 0.5px),transparent calc(50% + 0.5px))}
.writer-target svg{display:block;width:100%;height:100%;position:relative;z-index:1}
.writer-controls{display:flex;gap:.4rem;justify-content:center;margin-top:1rem;flex-wrap:wrap}
.writer-btn{padding:clamp(.5rem,.9vw,.6rem) clamp(.7rem,1.2vw,.95rem);border-radius:10px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:clamp(.72rem,.85vw,.82rem);font-weight:600;cursor:pointer;display:flex;align-items:center;gap:.35rem;font-family:inherit}
.writer-btn:hover{background:var(--primary-light);border-color:var(--primary);color:var(--primary-dark)}
.writer-btn.primary{background:var(--primary);color:#fff;border-color:var(--primary)}
.writer-loading{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:var(--text-3);gap:.5rem;padding:1rem;text-align:center}
.writer-loading i{font-size:1.8rem;color:var(--primary)}
.writer-score{text-align:center;margin-top:.6rem;font-size:.82rem;color:var(--text-2);min-height:1.2em}
.writer-score.success{color:var(--success);font-weight:600}
.writer-score.error{color:var(--danger);font-weight:600}
.trial-badge{display:none;align-items:center;gap:.35rem;padding:clamp(.22rem,.5vw,.35rem) clamp(.45rem,.8vw,.7rem);border-radius:50px;background:linear-gradient(135deg,#fbbf24,#f59e0b);color:#1e1b4b;font-size:clamp(.58rem,.75vw,.68rem);font-weight:800;text-transform:uppercase;white-space:nowrap}
.trial-badge.show{display:flex}
[data-theme="dark"] .audio-btn{background:rgba(59,130,246,.22);color:#93c5fd;border:1px solid rgba(59,130,246,.35)}
@media (min-width:1000px){.search-filter-row{display:grid;grid-template-columns:1fr auto;gap:.55rem;align-items:center}.search-bar{margin-bottom:0}.filters{display:grid;grid-template-columns:160px 180px;gap:.4rem;max-width:none;margin-bottom:0}}
@media (min-width:1400px){.filters{grid-template-columns:180px 200px}}
@media (min-width:769px) and (max-height:700px){.practice-full-body{padding:.75rem .85rem}.practice-full-content{gap:.75rem}.practice-full-vi{font-size:1.3rem;padding:.7rem .6rem}.practice-full-input{font-size:1.3rem;padding:.7rem .9rem}.practice-speak-btn{min-width:42px}.char-slot{font-size:1.3rem;min-width:1.5rem;height:1.9rem}.practice-full-nav{padding:.5rem .85rem}.pf-nav-icon{width:44px;height:44px;font-size:1rem}}

@media (min-width:769px) and (max-height:550px) and (hover:hover) and (pointer:fine){
    .practice-full-header{padding:.3rem .85rem}
    .pf-filters{padding:.25rem .85rem .2rem}
    .practice-full-body{padding:.5rem .6rem}
    .practice-full-content{gap:.5rem}
    .practice-full-vi{font-size:1.1rem;padding:.55rem .5rem}
    .practice-full-input{font-size:1.15rem;padding:.55rem .8rem}
    .char-slot{font-size:1.1rem;min-width:1.25rem;height:1.6rem}
    .practice-full-nav{padding:.4rem .65rem}
    .pf-nav-icon{width:38px;height:38px;font-size:.9rem}
}

@media(max-width:768px){.container{padding:0 .7rem}.header-inner{gap:.5rem;margin-bottom:.4rem}.main{padding:.15rem 0 2rem}.practice-full-header{padding:.5rem .85rem;gap:.5rem}.pf-filters{padding:.4rem .85rem .3rem}.practice-full-body{padding:.85rem .7rem calc(80px + env(safe-area-inset-bottom))}.practice-full-content{gap:.85rem}.practice-full-vi{font-size:1.2rem;padding:.75rem .6rem}.practice-full-input{font-size:1.2rem;padding:.75rem .85rem}.practice-speak-btn{min-width:40px;padding:0 .5rem;font-size:.95rem;border-radius:12px}.char-slot{font-size:1.2rem;min-width:1.4rem;height:1.85rem}.answer-phrase-btn{font-size:1.2rem;padding:.35rem .65rem}.reveal-actions button{padding:.6rem;font-size:.8rem}.reveal-actions{grid-template-columns:1fr 1fr;gap:.5rem}}
@media(max-width:400px){.practice-full-body{padding:.7rem .5rem calc(80px + env(safe-area-inset-bottom))}.practice-full-content{gap:.7rem}.practice-full-vi{font-size:1.1rem;padding:.65rem .5rem}.practice-full-input{font-size:1.1rem;padding:.65rem .75rem}.practice-speak-btn{min-width:38px}.reveal-actions{grid-template-columns:1fr}}
.practice-full-header .card-tag{padding:.22rem .6rem;font-size:clamp(.6rem,.75vw,.7rem);font-weight:700;border-radius:50px;flex-shrink:0}
.practice-full-header .card-tag.hsk{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff}
.practice-full-header .card-tag.topic{background:linear-gradient(135deg,#f59e0b,#d97706);color:#fff}
.practice-full-header .card-tag:not(.hsk):not(.topic){background:var(--surface-2);color:var(--text-2);border:1px solid var(--border)}

.chip.has-value{animation:chipPulse 2s ease-in-out infinite}
.pf-chip.has-value{animation:chipPulse 2s ease-in-out infinite}
@keyframes chipPulse{
    0%,100%{box-shadow:0 4px 12px rgba(139,92,235,.3)}
    50%{box-shadow:0 4px 18px rgba(37,99,235,.5)}
}
.practice-full-header .card-tag.excel-tag{
    background:linear-gradient(135deg,rgba(22,163,74,.15),rgba(22,163,74,.1));
    color:#15803d;
    border:1px solid rgba(22,163,74,.3);
    display:inline-flex;
    align-items:center;
    gap:.3rem;
}
[data-theme="dark"] .practice-full-header .card-tag.excel-tag{
    background:linear-gradient(135deg,rgba(22,163,74,.25),rgba(22,163,74,.15));
    color:#4ade80;
    border-color:rgba(22,163,74,.5);
}

@media (min-width:769px){
    .header-inner{
        display:flex!important;
        align-items:center!important;
        gap:clamp(.4rem,.8vw,.75rem)!important;
        flex-wrap:nowrap!important;
        overflow:visible;
        width:100%;
        position:relative;
    }
    .header-inner .logo{
        flex:0 0 auto!important;
        min-width:0!important;
        overflow:hidden;
    }
    .header-inner .logo-text{
        max-width:100%;
    }
    .header-inner .tiktok-bar{
        flex:1 1 auto!important;
        min-width:0!important;
        max-width:none!important;
        width:auto!important;
        margin:0!important;
        padding:clamp(.3rem,.5vw,.42rem) clamp(.55rem,.8vw,.75rem)!important;
        gap:clamp(.35rem,.6vw,.5rem)!important;
        font-size:clamp(.65rem,.8vw,.78rem)!important;
        border-radius:50px!important;
        position:relative;
        z-index:3;
        align-self:center;
    }
    .header-inner .tiktok-bar .tiktok-bar-avatar{
        width:clamp(24px,2.4vw,30px)!important;
        height:clamp(24px,2.4vw,30px)!important;
        flex-shrink:0;
    }
    .header-inner .tiktok-bar .tiktok-bar-info{
        min-width:0;
        overflow:hidden;
        flex:1 1 auto;
    }
    .header-inner .tiktok-bar .tiktok-nick{
        font-size:clamp(.7rem,.85vw,.82rem)!important;
        overflow:hidden;
        text-overflow:ellipsis;
        white-space:nowrap;
    }
    .header-inner .tiktok-bar .tiktok-user{
        font-size:clamp(.6rem,.72vw,.7rem)!important;
        overflow:hidden;
        text-overflow:ellipsis;
        white-space:nowrap;
    }
    .header-inner .tiktok-bar .tiktok-bar-link{
        padding:clamp(.28rem,.4vw,.38rem) clamp(.5rem,.7vw,.7rem)!important;
        font-size:clamp(.62rem,.75vw,.72rem)!important;
        flex-shrink:0;
        white-space:nowrap;
    }
    .header-inner .header-actions{
        flex:0 0 auto!important;
        margin-left:0!important;
        display:flex!important;
        gap:.4rem!important;
        align-items:center!important;
        position:relative;
        z-index:5;
    }
}

.practice-full-header .pf-counter{
    flex-shrink:0;
    max-width:46vw;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    letter-spacing:.02em;
}
.practice-full-header .pf-tags{
    flex:1 1 auto;
    min-width:0;
    display:flex;
    gap:.3rem;
    overflow-x:auto;
    overflow-y:hidden;
    scrollbar-width:thin;
    padding-bottom:2px;
}
.practice-full-header .pf-tags::-webkit-scrollbar{height:4px}
.practice-full-header .pf-tags::-webkit-scrollbar-thumb{
    background:var(--border-strong);
    border-radius:4px;
}
@media (max-width:520px){
    .practice-full-header .pf-counter{
        font-size:.66rem;
        padding:.3rem .55rem;
        max-width:56vw;
    }
    .pf-brand-sub{display:none}
}

@media (max-width:1024px) and (max-height:550px) and (orientation:landscape){
    .practice-full-header{padding:.35rem .75rem;gap:.35rem;min-height:44px}
    .pf-brand-sub{display:none}
    .pf-brand-title{font-size:.72rem}
    .pf-filters{padding:.3rem .75rem .25rem}
    .pf-dataset-row{padding:.3rem .5rem;gap:.4rem;margin-top:.3rem}
    .pf-dataset-search input{padding:.28rem 2rem;font-size:.72rem}
    .pf-dataset-select{padding:.28rem 1.8rem .28rem .6rem;font-size:.72rem}
    .pf-dataset-row .pf-quick-nav{
        padding-top:.3rem;
        margin-top:.15rem;
    }
    .pf-quick-nav-select{padding:.22rem 1.8rem .22rem .5rem;font-size:.68rem}
    .pf-filter-row{gap:.4rem}
    .pf-chip{padding:.2rem .5rem;font-size:.68rem}
    .practice-full-body{padding:.5rem .7rem calc(70px + env(safe-area-inset-bottom))}
    .practice-full-content{gap:.5rem}
    .practice-full-vi{font-size:1.05rem;padding:.55rem .55rem;line-height:1.35}
    .practice-full-input{font-size:1.1rem;padding:.55rem .75rem}
    .practice-speak-btn{min-width:38px;font-size:.9rem}
    .char-slot{font-size:1.05rem;min-width:1.2rem;height:1.55rem}
    .reveal-actions button{padding:.45rem .5rem;font-size:.75rem}
    .practice-full-nav{padding:.4rem .7rem;min-height:44px}
    .pf-nav-icon{width:38px;height:38px;font-size:.9rem}
    .pf-tiktok-float{transform:scale(.85);transform-origin:left bottom;left:8px;bottom:calc(4px + env(safe-area-inset-bottom))}
}

@media (max-width:1024px) and (max-height:420px) and (orientation:landscape){
    .pf-dataset-row{
        padding:.25rem .45rem;
        gap:.3rem;
        margin-top:.2rem;
    }
    .pf-dataset-row .pf-quick-nav{
        display:flex !important;
        padding-top:.25rem;
        margin-top:.1rem;
        gap:.35rem;
    }
    .pf-quick-nav-label{
        font-size:.55rem;
    }
    .pf-quick-nav-select{
        padding:.18rem 1.6rem .18rem .45rem;
        font-size:.62rem;
    }
    .pf-dataset-label{
        font-size:.55rem;
    }
    .pf-dataset-label i{display:none}
    .pf-dataset-select{
        padding:.2rem 1.6rem .2rem .5rem;
        font-size:.65rem;
    }
    .pf-dataset-search input{
        padding:.2rem 1.8rem .2rem 1.8rem;
        font-size:.65rem;
    }
    .practice-full-header .pf-tags{overflow-x:auto}
    .practice-full-vi{font-size:.95rem;padding:.45rem .5rem}
    .practice-full-input{font-size:1rem;padding:.5rem .7rem}
}

@media (max-width:768px) and (max-height:700px){
    .pf-dataset-row{
        padding:.4rem .55rem;
        gap:.4rem;
    }
    .pf-dataset-row .pf-quick-nav{
        display:flex !important;
        padding-top:.35rem;
        margin-top:.15rem;
    }
    .pf-quick-nav-select{
        padding:.22rem 1.8rem .22rem .5rem;
        font-size:.7rem;
    }
    .pf-dataset-select{
        font-size:.72rem;
        padding-top:.25rem;
        padding-bottom:.25rem;
    }
    .pf-dataset-search input{
        font-size:.72rem;
        padding-top:.25rem;
        padding-bottom:.25rem;
    }
}

.voice-modal{position:fixed;inset:0;background:rgba(15,23,42,.8);backdrop-filter:blur(6px);z-index:4000;display:none;align-items:center;justify-content:center;padding:1rem;animation:fadeIn .2s}
.voice-modal.show{display:flex}
.voice-box{background:var(--surface);border-radius:20px;width:100%;max-width:460px;max-height:calc(100vh - 2rem);overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.4);display:flex;flex-direction:column;animation:voiceSlideUp .3s cubic-bezier(.34,1.56,.64,1)}
@keyframes voiceSlideUp{from{transform:translateY(30px) scale(.95);opacity:0}to{transform:translateY(0) scale(1);opacity:1}}
.voice-header{padding:1.1rem 1.25rem;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;gap:.75rem;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff}
.voice-header h2{font-size:1.05rem;font-weight:800;display:flex;align-items:center;gap:.5rem;color:#fff;margin:0}
.voice-header h2 i{color:#67e8f9}
.voice-close{width:32px;height:32px;border-radius:50%;border:none;background:rgba(255,255,255,.2);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.95rem;transition:.15s;flex-shrink:0}
.voice-close:hover{background:rgba(255,255,255,.35)}
.voice-body{padding:1.25rem;overflow-y:auto;display:flex;flex-direction:column;gap:1.1rem}
.voice-group{display:flex;flex-direction:column;gap:.5rem}
.voice-group-label{font-size:.72rem;font-weight:800;color:var(--text-3);text-transform:uppercase;letter-spacing:.5px;display:flex;align-items:center;justify-content:space-between;gap:.5rem}
.voice-group-label .voice-value{font-size:.85rem;font-weight:900;color:var(--primary);background:var(--primary-light);padding:.15rem .6rem;border-radius:50px;text-transform:none;letter-spacing:0}
.voice-slider-row{display:flex;align-items:center;gap:.6rem}
.voice-slider-row button{width:34px;height:34px;border-radius:50%;border:1.5px solid var(--border);background:var(--surface-2);color:var(--text);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.9rem;font-weight:800;transition:.15s;flex-shrink:0;font-family:inherit}
.voice-slider-row button:hover{background:var(--primary-light);color:var(--primary-dark);border-color:var(--primary)}
.voice-slider-row button:active{transform:scale(.94)}
.voice-slider{flex:1;-webkit-appearance:none;appearance:none;height:6px;border-radius:50px;background:var(--border);outline:none;cursor:pointer}
.voice-slider::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#4f46e5,#7c3aed);cursor:pointer;box-shadow:0 2px 8px rgba(124,58,237,.4);border:2px solid #fff}
.voice-slider::-moz-range-thumb{width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#4f46e5,#7c3aed);cursor:pointer;box-shadow:0 2px 8px rgba(124,58,237,.4);border:2px solid #fff}
.voice-slider::-moz-range-track{height:6px;border-radius:50px;background:var(--border)}
.voice-preset-row{display:flex;gap:.35rem;flex-wrap:wrap}
.voice-preset-btn{padding:.3rem .7rem;border-radius:50px;border:1.5px solid var(--border);background:var(--surface);color:var(--text-2);font-size:.72rem;font-weight:700;cursor:pointer;font-family:inherit;transition:.15s}
.voice-preset-btn:hover{border-color:var(--primary);color:var(--primary)}
.voice-preset-btn.active{background:var(--primary);color:#fff;border-color:var(--primary)}
.voice-select{width:100%;padding:.6rem .85rem;border-radius:10px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:.85rem;font-family:inherit;outline:none;cursor:pointer}
.voice-select:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(37,99,235,.15)}
.voice-test-btn{padding:.75rem 1rem;border-radius:12px;border:none;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;font-size:.88rem;font-weight:800;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:.5rem;transition:.15s;font-family:inherit;box-shadow:0 4px 12px rgba(124,58,237,.35)}
.voice-test-btn:hover{transform:translateY(-1px);box-shadow:0 6px 18px rgba(124,58,237,.5)}
.voice-test-btn.speaking{background:var(--danger);box-shadow:0 4px 12px rgba(220,38,38,.5)}
.voice-note{padding:.6rem .8rem;border-radius:10px;background:var(--surface-2);border:1px solid var(--border);font-size:.72rem;color:var(--text-3);line-height:1.5;display:flex;align-items:flex-start;gap:.4rem}
.voice-note i{color:var(--primary);margin-top:.1rem;flex-shrink:0}
.voice-reset{padding:.55rem;border-radius:10px;border:1.5px solid var(--border);background:var(--surface);color:var(--text-2);font-size:.78rem;font-weight:600;cursor:pointer;font-family:inherit;display:flex;align-items:center;justify-content:center;gap:.4rem;transition:.15s}
.voice-reset:hover{background:var(--danger-light);color:var(--danger);border-color:var(--danger)}
[data-theme="dark"] .voice-slider{background:var(--surface-2)}

/* ═══════════════════════════════════════════════════════════ */
/* ONBOARDING MODAL - CHỌN CHỦ ĐỀ QUAN TÂM                     */
/* ĐÃ SỬA: gọn gàng, không tràn màn hình, header/footer cố định */
/* ═══════════════════════════════════════════════════════════ */
.onboarding-modal {
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    z-index: 5000;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    animation: obFadeIn .3s ease;
}
.onboarding-modal.show { display: flex; }
@keyframes obFadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}

.onboarding-box {
    background: var(--surface);
    border-radius: 24px;
    width: 100%;
    max-width: 560px;
    max-height: min(85vh, 640px);
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.4),
                0 0 0 1px rgba(139, 92, 246, 0.15);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    animation: obSlideUp .4s cubic-bezier(.34, 1.56, .64, 1);
    position: relative;
}
@keyframes obSlideUp {
    from { transform: translateY(40px) scale(.95); opacity: 0; }
    to   { transform: translateY(0) scale(1);      opacity: 1; }
}

/* Nút X đóng góc trên phải */
.onboarding-close {
    position: absolute;
    top: 14px;
    right: 14px;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: none;
    background: var(--surface-2);
    color: var(--text-2);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: .85rem;
    z-index: 5;
    transition: .15s;
    font-family: inherit;
}
.onboarding-close:hover {
    background: var(--danger-light);
    color: var(--danger);
    transform: scale(1.08);
}
.onboarding-close:active {
    transform: scale(.95);
}

.onboarding-header {
    padding: 1.5rem 1.5rem 1rem;
    background: linear-gradient(135deg,
        rgba(99, 102, 241, 0.08),
        rgba(217, 70, 239, 0.08));
    border-bottom: 1px solid var(--border);
    text-align: center;
    position: relative;
    flex-shrink: 0;
}
.onboarding-icon {
    width: 60px;
    height: 60px;
    margin: 0 auto .75rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #6366f1, #a855f7, #d946ef);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-size: 1.6rem;
    box-shadow: 0 10px 24px rgba(139, 92, 246, 0.45);
    animation: obIconFloat 3s ease-in-out infinite;
}
@keyframes obIconFloat {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50%      { transform: translateY(-4px) rotate(-3deg); }
}
.onboarding-title {
    font-size: 1.25rem;
    font-weight: 900;
    color: var(--text);
    margin-bottom: .3rem;
    letter-spacing: -0.02em;
}
.onboarding-subtitle {
    font-size: .84rem;
    color: var(--text-2);
    line-height: 1.5;
    max-width: 440px;
    margin: 0 auto;
}

.onboarding-counter {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    margin-top: .75rem;
    padding: .35rem .85rem;
    border-radius: 50px;
    background: var(--surface-2);
    border: 1.5px solid var(--border);
    font-size: .78rem;
    font-weight: 800;
    color: var(--text-2);
    transition: all .2s ease;
}
.onboarding-counter.ok {
    background: linear-gradient(135deg, rgba(22,163,74,.12), rgba(34,197,94,.08));
    border-color: rgba(22,163,74,.4);
    color: #15803d;
}
.onboarding-counter.full {
    background: linear-gradient(135deg, rgba(245,158,11,.15), rgba(251,191,36,.1));
    border-color: rgba(245,158,11,.5);
    color: #92400e;
}
[data-theme="dark"] .onboarding-counter.ok { color: #4ade80; }
[data-theme="dark"] .onboarding-counter.full { color: #fcd34d; }

/* Body: CHỈ phần này scroll */
.onboarding-body {
    padding: 1.15rem 1.5rem;
    overflow-y: auto;
    flex: 1 1 auto;
    min-height: 0;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: thin;
    overscroll-behavior: contain;
}
.onboarding-body::-webkit-scrollbar {
    width: 6px;
}
.onboarding-body::-webkit-scrollbar-track {
    background: transparent;
}
.onboarding-body::-webkit-scrollbar-thumb {
    background: var(--border-strong);
    border-radius: 3px;
}
.onboarding-body::-webkit-scrollbar-thumb:hover {
    background: var(--text-3);
}

.onboarding-section-label {
    font-size: .7rem;
    font-weight: 800;
    color: var(--text-3);
    text-transform: uppercase;
    letter-spacing: .5px;
    margin-bottom: .6rem;
    display: flex;
    align-items: center;
    gap: .4rem;
}
.onboarding-section-label i { color: var(--primary); }

.onboarding-topics {
    display: flex;
    flex-wrap: wrap;
    gap: .5rem;
    margin-bottom: .5rem;
}
.onboarding-topic {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    padding: .5rem .95rem;
    border-radius: 50px;
    border: 2px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-size: .8rem;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
    transition: all .2s ease;
    position: relative;
    user-select: none;
    line-height: 1.5;
}
.onboarding-topic:hover {
    border-color: var(--primary);
    background: var(--primary-light);
    transform: translateY(-1px);
}
.onboarding-topic.selected {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
}
.onboarding-topic.selected::before {
    content: '\2713';
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    font-size: .7rem;
    font-weight: 900;
    flex-shrink: 0;
}
.onboarding-topic .count {
    font-size: .68rem;
    font-weight: 700;
    padding: .1rem .45rem;
    border-radius: 50px;
    background: var(--surface-2);
    color: var(--text-3);
    margin-left: .15rem;
}
.onboarding-topic.selected .count {
    background: rgba(255, 255, 255, 0.25);
    color: #fff;
}
.onboarding-topic.disabled {
    opacity: .4;
    cursor: not-allowed;
    pointer-events: none;
}
.onboarding-empty {
    padding: 1.5rem;
    text-align: center;
    color: var(--text-3);
    font-size: .85rem;
}

.onboarding-footer {
    padding: 1rem 1.5rem 1.15rem;
    border-top: 1px solid var(--border);
    display: flex;
    gap: .6rem;
    justify-content: flex-end;
    align-items: center;
    background: var(--surface);
    flex-wrap: wrap;
    flex-shrink: 0;
    box-shadow: 0 -4px 12px -8px rgba(15, 23, 42, 0.15);
}
[data-theme="dark"] .onboarding-footer {
    box-shadow: 0 -4px 12px -8px rgba(0, 0, 0, 0.4);
}
.onboarding-btn {
    padding: .75rem 1.4rem;
    border-radius: 12px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-size: .88rem;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: .5rem;
    transition: all .2s ease;
}
.onboarding-btn:hover {
    background: var(--surface-2);
    border-color: var(--primary);
    color: var(--primary);
}
.onboarding-btn.primary {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 6px 16px rgba(124, 58, 237, 0.35);
}
.onboarding-btn.primary:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(124, 58, 237, 0.5);
}
.onboarding-btn.primary:disabled {
    opacity: .5;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
    background: linear-gradient(135deg, #94a3b8, #64748b);
}
.onboarding-btn.ghost {
    background: transparent;
    border-color: transparent;
    color: var(--text-3);
    font-weight: 600;
    font-size: .82rem;
    padding: .5rem .8rem;
}
.onboarding-btn.ghost:hover {
    color: var(--text-2);
    background: var(--surface-2);
}

/* Icon fallback — đảm bảo icon luôn hiện dù FA chưa load */
.onboarding-btn.primary i.fa-check::before {
    content: '\2713';
    font-family: inherit;
    font-weight: 900;
    font-style: normal;
}
.onboarding-btn.primary i.fa-rocket::before {
    content: '\2713';
    font-family: inherit;
    font-weight: 900;
    font-style: normal;
}
.onboarding-btn.ghost i.fa-forward::before {
    content: '\00BB';
    font-family: inherit;
    font-weight: 900;
    font-style: normal;
}

/* ══════════════════════════════════════════════════════════════ */
/* BANNER "CHỦ ĐỀ GỢI Ý" - REDESIGN                              */
/* ══════════════════════════════════════════════════════════════ */
.onboarding-active-banner {
    display: flex;
    align-items: center;
    gap: .6rem;
    padding: .8rem 1rem;
    margin-bottom: 1rem;
    background: linear-gradient(135deg,
        rgba(99,102,241,.08),
        rgba(139,92,246,.08));
    border: 1.5px solid rgba(139,92,246,.3);
    border-radius: 14px;
    font-size: .85rem;
    color: var(--text);
    animation: obBannerIn .35s cubic-bezier(.34,1.56,.64,1);
    flex-wrap: wrap;
    position: relative;
    overflow: visible;
}
@keyframes obBannerIn {
    from { opacity: 0; transform: translateY(-6px); }
    to   { opacity: 1; transform: translateY(0); }
}

.onboarding-active-banner .ob-icon {
    font-size: 1.1rem;
    color: #d946ef;
    flex-shrink: 0;
    line-height: 1;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    background: linear-gradient(135deg, rgba(217,70,239,.15), rgba(139,92,246,.15));
    border-radius: 50%;
    animation: obIconSpin 3s ease-in-out infinite;
}
@keyframes obIconSpin {
    0%, 100% { transform: rotate(0deg) scale(1); }
    50%      { transform: rotate(8deg) scale(1.08); }
}

.onboarding-active-banner .ob-label {
    font-weight: 800;
    font-size: .84rem;
    color: var(--text);
    white-space: nowrap;
    flex-shrink: 0;
}

.onboarding-active-banner .ob-chips {
    display: flex;
    flex-wrap: wrap;
    gap: .35rem;
    align-items: center;
    flex: 1 1 auto;
    min-width: 0;
    overflow: visible;
}

.onboarding-active-banner .ob-chip {
    padding: .3rem .75rem;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: #fff;
    border-radius: 50px;
    font-weight: 700;
    font-size: .76rem;
    box-shadow: 0 2px 6px rgba(139,92,246,.3);
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: .25rem;
    transition: transform .18s ease, box-shadow .18s ease;
    cursor: default;
    line-height: 1.4;
}
.onboarding-active-banner .ob-chip:hover {
    transform: translateY(-1px) scale(1.03);
    box-shadow: 0 4px 12px rgba(139,92,246,.5);
}

/* ═══════════════════════════════════════════════════════════ */
/* CHIP "+N CHỦ ĐỀ KHÁC" - Giới hạn hiển thị khi chọn nhiều    */
/* ═══════════════════════════════════════════════════════════ */
.onboarding-active-banner .ob-chip-more {
    background: linear-gradient(135deg, #94a3b8, #64748b) !important;
    position: relative;
    font-style: italic;
    letter-spacing: .2px;
    cursor: help;
}
.onboarding-active-banner .ob-chip-more:hover {
    background: linear-gradient(135deg, #64748b, #475569) !important;
    transform: translateY(-1px) scale(1.05);
    box-shadow: 0 4px 12px rgba(100, 116, 139, .5);
}

/* Tooltip cho chip "+N" khi hover */
.onboarding-active-banner .ob-chip-more::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: calc(100% + 8px);
    left: 50%;
    transform: translateX(-50%) translateY(4px);
    background: #0f172a;
    color: #fff;
    padding: .5rem .75rem;
    border-radius: 8px;
    font-size: .72rem;
    font-weight: 500;
    font-style: normal;
    white-space: normal;
    width: max-content;
    max-width: min(320px, 80vw);
    line-height: 1.4;
    text-align: left;
    box-shadow: 0 8px 24px rgba(0,0,0,.25);
    opacity: 0;
    visibility: hidden;
    transition: opacity .2s, transform .2s, visibility .2s;
    z-index: 100;
    pointer-events: none;
    letter-spacing: 0;
}
.onboarding-active-banner .ob-chip-more:hover::after {
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) translateY(0);
}

/* Mũi tên nhỏ cho tooltip */
.onboarding-active-banner .ob-chip-more::before {
    content: '';
    position: absolute;
    bottom: calc(100% + 2px);
    left: 50%;
    transform: translateX(-50%) translateY(4px);
    border: 6px solid transparent;
    border-top-color: #0f172a;
    opacity: 0;
    visibility: hidden;
    transition: opacity .2s, transform .2s, visibility .2s;
    z-index: 101;
    pointer-events: none;
}
.onboarding-active-banner .ob-chip-more:hover::before {
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) translateY(0);
}

[data-theme="dark"] .onboarding-active-banner .ob-chip-more::after {
    background: #1e293b;
    border: 1px solid #334155;
}
[data-theme="dark"] .onboarding-active-banner .ob-chip-more::before {
    border-top-color: #1e293b;
}

.onboarding-active-banner .ob-count {
    color: var(--text-3);
    font-size: .75rem;
    font-weight: 600;
    white-space: nowrap;
    flex-shrink: 0;
}

.onboarding-active-banner .ob-change-btn {
    padding: .38rem .85rem;
    border-radius: 50px;
    border: 1.5px solid var(--primary);
    background: var(--surface);
    color: var(--primary);
    font-weight: 700;
    font-size: .76rem;
    cursor: pointer;
    font-family: inherit;
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    transition: all .18s ease;
    box-shadow: 0 1px 3px rgba(37,99,235,.15);
}
.onboarding-active-banner .ob-change-btn i {
    font-size: .8rem;
    transition: transform .35s ease;
}
.onboarding-active-banner .ob-change-btn:hover {
    background: var(--primary);
    color: #fff;
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(37,99,235,.35);
}
.onboarding-active-banner .ob-change-btn:hover i {
    transform: rotate(180deg);
}
.onboarding-active-banner .ob-change-btn:active {
    transform: translateY(0) scale(.97);
}

/* ═══════════════════════════════════════════════════════════ */
/* THỐNG KÊ KHOÁ - DÒNG 2 CỦA BANNER CHỦ ĐỀ                     */
/* ═══════════════════════════════════════════════════════════ */
.onboarding-active-banner .ob-stats-bar {
    display: flex;
    align-items: center;
    gap: .75rem;
    flex-wrap: wrap;
    width: 100%;
    padding-top: .65rem;
    margin-top: .35rem;
    border-top: 1px dashed rgba(139,92,246,.35);
}

.onboarding-active-banner .ob-stat-item {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    padding: .4rem .75rem;
    background: rgba(255,255,255,.6);
    border: 1.5px solid rgba(245,158,11,.4);
    border-radius: 50px;
    font-size: .78rem;
    font-weight: 700;
    color: var(--text);
    line-height: 1.35;
    box-shadow: 0 1px 3px rgba(245,158,11,.1);
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-item {
    background: rgba(30,41,59,.7);
    border-color: rgba(245,158,11,.5);
}

.onboarding-active-banner .ob-stat-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: linear-gradient(135deg, #fef3c7, #fde68a);
    color: #b45309;
    font-size: .75rem;
    flex-shrink: 0;
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-icon {
    background: linear-gradient(135deg, rgba(245,158,11,.25), rgba(217,119,6,.2));
    color: #fcd34d;
}

.onboarding-active-banner .ob-stat-industry .ob-stat-icon {
    background: linear-gradient(135deg, #dbeafe, #bfdbfe);
    color: #1d4ed8;
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-industry .ob-stat-icon {
    background: linear-gradient(135deg, rgba(59,130,246,.25), rgba(37,99,235,.2));
    color: #93c5fd;
}
.onboarding-active-banner .ob-stat-industry {
    border-color: rgba(59,130,246,.4);
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-industry {
    border-color: rgba(59,130,246,.5);
}

.onboarding-active-banner .ob-stat-text {
    white-space: nowrap;
    font-weight: 600;
    color: var(--text-2);
}
.onboarding-active-banner .ob-stat-text b {
    color: #dc2626;
    font-weight: 900;
    font-size: 1.1em;
    margin: 0 .1em;
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-text b {
    color: #fca5a5;
}

.onboarding-active-banner .ob-cta-btn {
    margin-left: auto;
    padding: .5rem 1rem;
    border-radius: 50px;
    border: none;
    background: linear-gradient(135deg, #4f46e5, #7c3aed 50%, #a855f7);
    color: #fff;
    font-weight: 800;
    font-size: .78rem;
    cursor: pointer;
    font-family: inherit;
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    white-space: nowrap;
    box-shadow: 0 4px 14px rgba(124,58,237,.4);
    transition: transform .15s ease, box-shadow .2s ease;
    text-transform: uppercase;
    letter-spacing: .3px;
    animation: obCtaPulse 2.5s ease-in-out infinite;
}
.onboarding-active-banner .ob-cta-btn:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 8px 22px rgba(124,58,237,.65);
}
.onboarding-active-banner .ob-cta-btn:active {
    transform: translateY(0) scale(.98);
}
@keyframes obCtaPulse {
    0%, 100% { box-shadow: 0 4px 14px rgba(124,58,237,.4); }
    50%      { box-shadow: 0 4px 20px rgba(124,58,237,.7); }
}

[data-theme="dark"] .onboarding-active-banner {
    background: linear-gradient(135deg,
        rgba(99,102,241,.15),
        rgba(139,92,246,.15));
    border-color: rgba(165,180,252,.35);
}
[data-theme="dark"] .onboarding-active-banner .ob-icon {
    background: linear-gradient(135deg, rgba(217,70,239,.25), rgba(139,92,246,.2));
}
[data-theme="dark"] .onboarding-active-banner .ob-change-btn {
    background: var(--surface-2);
}

@media (max-width: 500px) {
    .onboarding-active-banner {
        padding: .7rem .8rem;
        gap: .5rem;
    }
    .onboarding-active-banner .ob-icon {
        width: 24px;
        height: 24px;
        font-size: .95rem;
    }
    .onboarding-active-banner .ob-label {
        font-size: .76rem;
    }
    .onboarding-active-banner .ob-chip {
        font-size: .7rem;
        padding: .24rem .6rem;
    }
    .onboarding-active-banner .ob-chip-more {
        font-size: .68rem;
        padding: .22rem .55rem;
    }
    .onboarding-active-banner .ob-chip-more::after {
        font-size: .68rem;
        max-width: 90vw;
        padding: .4rem .6rem;
    }
    .onboarding-active-banner .ob-count {
        font-size: .7rem;
    }
    .onboarding-active-banner .ob-change-btn {
        padding: .32rem .7rem;
        font-size: .72rem;
    }
    .onboarding-active-banner .ob-stats-bar {
        gap: .5rem;
        padding-top: .55rem;
    }
    .onboarding-active-banner .ob-stat-item {
        font-size: .72rem;
        padding: .35rem .65rem;
    }
    .onboarding-active-banner .ob-stat-icon {
        width: 20px;
        height: 20px;
        font-size: .68rem;
    }
    .onboarding-active-banner .ob-cta-btn {
        margin-left: 0;
        width: 100%;
        justify-content: center;
        padding: .55rem .85rem;
        font-size: .75rem;
    }
}

/* ═══════════════════════════════════════════════════════════ */
/* ONBOARDING MODAL - MOBILE (bottom sheet)                    */
/* ═══════════════════════════════════════════════════════════ */
@media (max-width: 500px) {
    .onboarding-modal {
        padding: .5rem;
        align-items: flex-end;
    }
    .onboarding-box {
        max-width: 100%;
        max-height: 88vh;
        border-radius: 20px 20px 16px 16px;
        animation: obSlideUpMobile .35s cubic-bezier(.34, 1.56, .64, 1);
    }
    @keyframes obSlideUpMobile {
        from { transform: translateY(100%); opacity: 0; }
        to   { transform: translateY(0);    opacity: 1; }
    }
    .onboarding-close {
        top: 10px;
        right: 10px;
        width: 28px;
        height: 28px;
        font-size: .78rem;
    }
    .onboarding-header {
        padding: 1.1rem 1.1rem .85rem;
    }
    .onboarding-icon {
        width: 48px;
        height: 48px;
        font-size: 1.25rem;
        margin-bottom: .5rem;
        border-radius: 14px;
    }
    .onboarding-title {
        font-size: 1.05rem;
    }
    .onboarding-subtitle {
        font-size: .76rem;
    }
    .onboarding-counter {
        font-size: .72rem;
        padding: .3rem .7rem;
        margin-top: .6rem;
    }
    .onboarding-body {
        padding: .9rem 1.1rem;
    }
    .onboarding-topic {
        padding: .45rem .85rem;
        font-size: .76rem;
    }
    .onboarding-topic .count {
        font-size: .64rem;
    }
    .onboarding-footer {
        padding: .85rem 1.1rem 1rem;
        gap: .5rem;
    }
    .onboarding-btn {
        padding: .65rem 1.15rem;
        font-size: .82rem;
        border-radius: 11px;
    }
    .onboarding-btn.ghost {
        padding: .45rem .7rem;
        font-size: .78rem;
    }
}

/* ═══════════════════════════════════════════════════════════ */
/* ICON KHOÁ + SỐ CÂU BỊ KHOÁ TRÊN CHIP CHỦ ĐỀ                 */
/* ═══════════════════════════════════════════════════════════ */
.onboarding-topic .topic-lock {
    display: inline-flex;
    align-items: center;
    gap: .2rem;
    margin-left: .25rem;
    padding: .1rem .45rem;
    border-radius: 50px;
    background: linear-gradient(135deg, rgba(220,38,38,.15), rgba(185,28,28,.1));
    color: #b91c1c;
    font-size: .65rem;
    font-weight: 900;
    border: 1px solid rgba(220,38,38,.3);
    line-height: 1;
    flex-shrink: 0;
    transition: all .2s ease;
}
.onboarding-topic .topic-lock i {
    font-size: .6rem;
    opacity: .9;
}
[data-theme="dark"] .onboarding-topic .topic-lock {
    background: linear-gradient(135deg, rgba(220,38,38,.3), rgba(185,28,28,.2));
    color: #fca5a5;
    border-color: rgba(248,113,113,.4);
}
.onboarding-topic.selected .topic-lock {
    background: rgba(255,255,255,.25);
    color: #fff;
    border-color: rgba(255,255,255,.4);
}
.onboarding-topic.selected .topic-lock i {
    color: #fff;
    opacity: 1;
}
@media (max-width: 500px) {
    .onboarding-topic .topic-lock {
        font-size: .6rem;
        padding: .08rem .35rem;
        gap: .15rem;
    }
    .onboarding-topic .topic-lock i {
        font-size: .55rem;
    }
}

/* STAT: Giới hạn mỗi chủ đề (XANH LÁ) */
.onboarding-active-banner .ob-stat-pertopic {
    border-color: rgba(22,163,74,.4);
}
.onboarding-active-banner .ob-stat-pertopic .ob-stat-icon {
    background: linear-gradient(135deg, #dcfce7, #bbf7d0);
    color: #15803d;
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-pertopic {
    border-color: rgba(34,197,94,.5);
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-pertopic .ob-stat-icon {
    background: linear-gradient(135deg, rgba(22,163,74,.3), rgba(21,128,61,.2));
    color: #4ade80;
}

/* STAT: Câu khoá trong chủ đề đang chọn (ĐỎ) */
.onboarding-active-banner .ob-stat-selected {
    border-color: rgba(220,38,38,.4);
    background: linear-gradient(135deg, rgba(254,226,226,.5), rgba(254,202,202,.3));
}
.onboarding-active-banner .ob-stat-selected .ob-stat-icon {
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    color: #b91c1c;
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-selected {
    border-color: rgba(248,113,113,.5);
    background: linear-gradient(135deg, rgba(220,38,38,.15), rgba(185,28,28,.1));
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-selected .ob-stat-icon {
    background: linear-gradient(135deg, rgba(220,38,38,.3), rgba(185,28,28,.2));
    color: #fca5a5;
}

/* STAT: Chủ đề khác chưa mở khoá (TÍM) */
.onboarding-active-banner .ob-stat-topics {
    border-color: rgba(139,92,246,.4);
    background: linear-gradient(135deg, rgba(237,233,254,.5), rgba(221,214,254,.3));
}
.onboarding-active-banner .ob-stat-topics .ob-stat-icon {
    background: linear-gradient(135deg, #ede9fe, #ddd6fe);
    color: #6d28d9;
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-topics {
    border-color: rgba(167,139,250,.5);
    background: linear-gradient(135deg, rgba(139,92,246,.15), rgba(109,40,217,.1));
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-topics .ob-stat-icon {
    background: linear-gradient(135deg, rgba(139,92,246,.3), rgba(109,40,217,.2));
    color: #c4b5fd;
}
/* ═══════════════════════════════════════════════════════════ */
/* STATS INLINE — 3 thông tin gộp trên 1 dòng ngang            */
/* ═══════════════════════════════════════════════════════════ */
.onboarding-active-banner .ob-stats-bar.ob-stats-inline {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: .5rem;
    flex-wrap: wrap;
    width: 100%;
    padding-top: .6rem;
    margin-top: .35rem;
    border-top: 1px dashed rgba(139,92,246,.35);
}

.onboarding-active-banner .ob-stat-inline {
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    padding: .3rem .75rem;
    border-radius: 50px;
    background: linear-gradient(135deg, rgba(59,130,246,.1), rgba(37,99,235,.06));
    border: 1.5px solid rgba(59,130,246,.3);
    color: var(--text-2);
    font-size: .76rem;
    font-weight: 700;
    line-height: 1;
    white-space: nowrap;
    transition: all .2s ease;
}
.onboarding-active-banner .ob-stat-inline i {
    font-size: .75rem;
    color: #2563eb;
    flex-shrink: 0;
}
.onboarding-active-banner .ob-stat-inline b {
    color: #dc2626;
    font-weight: 900;
    font-size: 1.05em;
    margin: 0 .1em;
}

/* Chip chủ đề khoá — màu TÍM */
.onboarding-active-banner .ob-stat-inline-topics {
    background: linear-gradient(135deg, rgba(139,92,246,.12), rgba(109,40,217,.06));
    border-color: rgba(139,92,246,.35);
}
.onboarding-active-banner .ob-stat-inline-topics i {
    color: #7c3aed;
}

/* Chip chuyên ngành khoá — màu XANH DƯƠNG */
.onboarding-active-banner .ob-stat-inline-industry {
    background: linear-gradient(135deg, rgba(6,182,212,.12), rgba(8,145,178,.06));
    border-color: rgba(6,182,212,.35);
}
.onboarding-active-banner .ob-stat-inline-industry i {
    color: #0891b2;
}

/* Dark mode */
[data-theme="dark"] .onboarding-active-banner .ob-stat-inline {
    background: linear-gradient(135deg, rgba(59,130,246,.2), rgba(37,99,235,.1));
    border-color: rgba(96,165,250,.4);
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-inline-topics {
    background: linear-gradient(135deg, rgba(139,92,246,.22), rgba(109,40,217,.12));
    border-color: rgba(167,139,250,.45);
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-inline-industry {
    background: linear-gradient(135deg, rgba(6,182,212,.22), rgba(8,145,178,.12));
    border-color: rgba(34,211,238,.45);
}
[data-theme="dark"] .onboarding-active-banner .ob-stat-inline b {
    color: #fca5a5;
}

/* Mobile: cho phép xuống dòng nếu chật */
@media (max-width: 500px) {
    .onboarding-active-banner .ob-stats-bar.ob-stats-inline {
        gap: .35rem;
        padding-top: .5rem;
    }
    .onboarding-active-banner .ob-stat-inline {
        padding: .25rem .6rem;
        font-size: .7rem;
        gap: .25rem;
    }
    .onboarding-active-banner .ob-stat-inline i {
        font-size: .68rem;
    }
}
/* ═══════════════════════════════════════════════════════════════
   ❤️ FAVORITES — Nút tim trên card
   ═══════════════════════════════════════════════════════════════ */
.fav-btn{
    width:clamp(28px,2.8vw,32px);
    height:clamp(28px,2.8vw,32px);
    border-radius:50%;
    border:none;
    background:var(--surface-2);
    color:var(--text-3);
    cursor:pointer;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    font-size:clamp(.72rem,.9vw,.85rem);
    transition:all .2s cubic-bezier(.34,1.56,.64,1);
    flex-shrink:0;
    position:relative;
}
.fav-btn:hover{
    transform:scale(1.15);
    background:rgba(239,68,68,.12);
    color:#ef4444;
}
.fav-btn:active{transform:scale(.92);}
.fav-btn.active{
    color:#ef4444;
    background:rgba(239,68,68,.12);
}
.fav-btn.active i{
    animation:favHeartPop .4s cubic-bezier(.34,1.56,.64,1);
}
@keyframes favHeartPop{
    0%{transform:scale(1);}
    40%{transform:scale(1.4);}
    70%{transform:scale(.9);}
    100%{transform:scale(1);}
}
.fav-btn.active::after{
    content:'';
    position:absolute;
    inset:-4px;
    border-radius:50%;
    border:2px solid rgba(239,68,68,.4);
    animation:favRing .5s ease-out;
    pointer-events:none;
}
@keyframes favRing{
    0%{opacity:1;transform:scale(.8);}
    100%{opacity:0;transform:scale(1.4);}
}

/* Trạng thái KHOÁ */
.fav-btn.locked{
    color:#dc2626;
   {
 background:rgba(220,   38,38,.1);
}
.fav-btn position.locked:hover{
    transform:scale(1:.12);
    background:absolutergba(220,38,38;
,.2);
    color:#b91c1c;
}
.fav-btn.locked i{font-size:.65rem;}
[data-theme="dark"] .fav-btn.locked{
    color:#fca5a5;
    background:rgba(220,38,38,.25);
}
[data-theme="dark"] .fav-btn.locked:hover{
    background:rgba(220,38,38,.4);
    color:#fecaca;
}

/* ═══════════════════════════════════════════════════════════════
   ❤️ FAVORITES — Nút tim trong Practice Full header
   ═══════════════════════════════════════════════════════════════ */
.pf-fav-btn{
    width:clamp(30px,3vw,36px);
    height:clamp(30px,3vw,36px);
    border-radius:50%;
    border:none;
    background:var(--surface-2);
    color:var(--text-2);
    cursor:pointer;
    display:flex;
    align-items:center;
    justify-content:center;
    flex-shrink:0;
    font-size:clamp(.78rem,.95vw,.9rem);
    transition:all .2s cubic-bezier(.34,1.56,.64,1);
    position:relative;
}
.pf-fav-btn:hover{
    background:rgba(239,68,68,.12);
    color:#ef4444;
    transform:scale(1.1);
}
.pf-fav-btn.active{
    color:#ef4444;
    background:rgba(239,68,68,.15);
}
.pf-fav-btn.active i{
    animation:favHeartPop .4s cubic-bezier(.34,1.56,.64,1);
}
.pf-fav-btn.locked{
    color:#dc2626;
    background:rgba(220,38,38,.12);
}
.pf-fav-btn.locked:hover{
    background:rgba(220,38,38,.22);
    color:#b91c1c;
}
[data-theme="dark"] .pf-fav-btn.locked{
    color:#fca5a5;
    background:rgba(220,38,38,.28);
}

/* ═══════════════════════════════════════════════════════════════
   ❤️ FAVORITES — Tab trong dataset selector
   ═══════════════════════════════════════════════════════════════ */
.ds-btn[data-dataset-group="favorites"]{
    position:relative;
    overflow:visible;
}
.ds-btn[data-dataset-group="favorites"] .ds-fav-badge    top:-8px;
    right:-6px;
    min-width:22px;
    height:22px;
    padding:0 .4rem;
    border-radius:50px;
    background:linear-gradient(135deg,#ef4444,#dc2626);
    color:#fff;
    font-size:.65rem;
    font-weight:900;
    display:flex;
    align-items:center;
    justify-content:center;
    box-shadow:0 2px 8px rgba(239,68,68,.5),0 0 0 2px var(--surface);
    animation:favBadgePulse 2s ease-in-out infinite;
    z-index:10;
    line-height:1;
}
.ds-btn[data-dataset-group="favorites"] .ds-fav-badge[data-count="0"]{
    display:none;
}
@keyframes favBadgePulse{
    0%,100%{transform:scale(1);}
    50%{transform:scale(1.1);}
}
.ds-btn[data-dataset-group="favorites"] .ds-fav-lock{
    position:absolute;
    top:-8px;
    right:-6px;
    width:22px;
    height:22px;
    border-radius:50%;
    background:linear-gradient(135deg,#dc2626,#b91c1c);
    color:#fff;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:.62rem;
    box-shadow:0 2px 8px rgba(220,38,38,.55),0 0 0 2px var(--surface);
    z-index:10;
}
.ds-btn[data-dataset-group="favorites"] i:first-child{
    color:#ef4444;
}
.ds-btn[data-dataset-group="favorites"].active i:first-child{
    color:#fff;
}
.ds-btn[data-dataset-group="favorites"].fav-locked{
    opacity:.65;
    cursor:pointer;
}
.ds-btn[data-dataset-group="favorites"].fav-locked:hover{
    opacity:.85;
    border-color:#dc2626;
    background:rgba(220,38,38,.06);
}
.ds-btn[data-dataset-group="favorites"].fav-locked i:first-child{
    color:#dc2626;
}
[data-theme="dark"] .ds-btn[data-dataset-group="favorites"].fav-locked i:first-child{
    color:#fca5a5;
}

/* ═══════════════════════════════════════════════════════════════
   ❤️ FAVORITES — Header của tab (sort + clear all)
   ═══════════════════════════════════════════════════════════════ */
.fav-header{
    display:flex;
    align-items:center;
    gap:.5rem;
    padding:.65rem .85rem;
    background:linear-gradient(135deg,rgba(239,68,68,.08),rgba(220,38,38,.04));
    border:1.5px solid rgba(239,68,68,.25);
    border-radius:12px;
    margin-bottom:.75rem;
    flex-wrap:wrap;
}
[data-theme="dark"] .fav-header{
    background:linear-gradient(135deg,rgba(239,68,68,.15),rgba(220,38,38,.08));
    border-color:rgba(239,68,68,.4);
}
.fav-header .fav-title{
    display:flex;
    align-items:center;
    gap:.45rem;
    font-size:.88rem;
    font-weight:800;
    color:var(--text);
    flex:1 1 auto;
    min-width:0;
}
.fav-header .fav-title i{
    color:#ef4444;
    font-size:1rem;
}
.fav-header .fav-count-text{
    font-size:.72rem;
    font-weight:700;
    color:#dc2626;
    background:rgba(239,68,68,.15);
    padding:.15rem .55rem;
    border-radius:50px;
    letter-spacing:.2px;
}
[data-theme="dark"] .fav-header .fav-count-text{
    color:#fca5a5;
    background:rgba(239,68,68,.25);
}
.fav-header .fav-sort{
    padding:.35rem 1.8rem .35rem .7rem;
    border-radius:50px;
    border:1.5px solid var(--border);
    background:var(--surface);
    color:var(--text);
    font-size:.72rem;
    font-weight:700;
    font-family:inherit;
    outline:none;
    cursor:pointer;
    appearance:none;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'><path fill='%2394a3b8' d='M6 9L1 4h10z'/></svg>");
    background-repeat:no-repeat;
    background-position:right 8px center;
    background-size:9px;
    transition:.15s;
}
.fav-header .fav-sort:hover{
    border-color:#ef4444;
    color:#dc2626;
}
.fav-header .fav-sort:focus{
    border-color:#ef4444;
    box-shadow:0 0 0 3px rgba(239,68,68,.15);
}
.fav-header .fav-clear-all{
    padding:.35rem .75rem;
    border-radius:50px;
    border:1.5px solid rgba(220,38,38,.35);
    background:var(--surface);
    color:#dc2626;
    font-size:.72rem;
    font-weight:700;
    font-family:inherit;
    cursor:pointer;
    display:inline-flex;
    align-items:center;
    gap:.3rem;
    transition:.15s;
}
.fav-header .fav-clear-all:hover{
    background:linear-gradient(135deg,#dc2626,#b91c1c);
    color:#fff;
    border-color:#dc2626;
    transform:translateY(-1px);
    box-shadow:0 4px 10px rgba(220,38,38,.35);
}
.fav-header .fav-clear-all:active{
    transform:translateY(0) scale(.97);
}
[data-theme="dark"] .fav-header .fav-clear-all{
    color:#fca5a5;
    border-color:rgba(248,113,113,.5);
}

/* ═══════════════════════════════════════════════════════════════
   ❤️ FAVORITES — Empty state
   ═══════════════════════════════════════════════════════════════ */
.fav-empty{
    grid-column:1 / -1;
    padding:3rem 1.5rem;
    text-align:center;
    background:linear-gradient(135deg,rgba(239,68,68,.04),rgba(220,38,38,.02));
    border:2px dashed rgba(239,68,68,.25);
    border-radius:16px;
}
[data-theme="dark"] .fav-empty{
    background:linear-gradient(135deg,rgba(239,68,68,.1),rgba(220,38,38,.05));
    border-color:rgba(239,68,68,.35);
}
.fav-empty .fav-empty-icon{
    width:70px;
    height:70px;
    margin:0 auto 1rem;
    border-radius:50%;
    background:linear-gradient(135deg,rgba(239,68,68,.15),rgba(220,38,38,.1));
    color:#ef4444;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:1.8rem;
    animation:favEmptyFloat 3s ease-in-out infinite;
}
@keyframes favEmptyFloat{
    0%,100%{transform:translateY(0) scale(1);}
    50%{transform:translateY(-6px) scale(1.05);}
}
.fav-empty .fav-empty-title{
    font-size:1.05rem;
    font-weight:800;
    color:var(--text);
    margin-bottom:.4rem;
}
.fav-empty .fav-empty-desc{
    font-size:.85rem;
    color:var(--text-2);
    line-height:1.5;
    max-width:420px;
    margin:0 auto;
}
.fav-empty .fav-empty-desc b{
    color:#dc2626;
    font-weight:800;
}
.fav-empty .fav-empty-tip{
    display:inline-flex;
    align-items:center;
    gap:.4rem;
    margin-top:1rem;
    padding:.5rem .9rem;
    border-radius:50px;
    background:var(--surface);
    border:1.5px solid var(--border);
    font-size:.78rem;
    font-weight:600;
    color:var(--text-2);
}
.fav-empty .fav-empty-tip i{
    color:#ef4444;
    font-size:.85rem;
}

/* Empty state cho tier bị khoá */
.fav-locked-empty{
    grid-column:1 / -1;
    padding:3rem 1.5rem;
    text-align:center;
    background:linear-gradient(135deg,rgba(220,38,38,.06),rgba(185,28,28,.03));
    border:2px dashed rgba(220,38,38,.35);
    border-radius:16px;
}
.fav-locked-empty .fav-empty-icon{
    background:linear-gradient(135deg,#dc2626,#b91c1c);
    color:#fff;
    animation:favEmptyFloat 3s ease-in-out infinite;
}
.fav-locked-empty .fav-empty-cta{
    display:inline-flex;
    align-items:center;
    gap:.4rem;
    margin-top:1rem;
    padding:.6rem 1.2rem;
    border-radius:50px;
    border:none;
    background:linear-gradient(135deg,#dc2626,#b91c1c);
    color:#fff;
    font-size:.85rem;
    font-weight:800;
    font-family:inherit;
    cursor:pointer;
    box-shadow:0 6px 18px rgba(220,38,38,.4);
    transition:all .2s;
    animation:favCtaPulse 2.5s ease-in-out infinite;
    text-transform:uppercase;
    letter-spacing:.3px;
}
.fav-locked-empty .fav-empty-cta:hover{
    transform:translateY(-2px) scale(1.03);
    box-shadow:0 10px 26px rgba(220,38,38,.6);
}
@keyframes favCtaPulse{
    0%,100%{box-shadow:0 6px 18px rgba(220,38,38,.4);}
    50%{box-shadow:0 6px 24px rgba(220,38,38,.7);}
}

/* ═══════════════════════════════════════════════════════════════
   ❤️ FAVORITES — Toast
   ═══════════════════════════════════════════════════════════════ */
.fav-toast{
    position:fixed;
    top:80px;
    left:50%;
    transform:translateX(-50%) translateY(-20px);
    padding:.7rem 1.2rem;
    border-radius:50px;
    font-size:.85rem;
    font-weight:800;
    font-family:inherit;
    color:#fff;
    z-index:9999;
    opacity:0;
    transition:opacity .25s ease, transform .3s cubic-bezier(.34,1.56,.64,1);
    pointer-events:none;
    display:flex;
    align-items:center;
    gap:.5rem;
    max-width:90vw;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
    box-shadow:0 8px 24px rgba(0,0,0,.25);
}
.fav-toast.show{
    opacity:1;
    transform:translateX(-50%) translateY(0);
}
.fav-toast.add{
    background:linear-gradient(135deg,#ef4444,#dc2626);
    box-shadow:0 8px 24px rgba(239,68,68,.5);
}
.fav-toast.remove{
    background:linear-gradient(135deg,#64748b,#475569);
    box-shadow:0 8px 24px rgba(100,116,139,.5);
}
.fav-toast.warn{
    background:linear-gradient(135deg,#f59e0b,#d97706);
    box-shadow:0 8px 24px rgba(245,158,11,.5);
}
.fav-toast i{font-size:1rem;}

/* ═══════════════════════════════════════════════════════════════
   ❤️ FAVORITES — Responsive
   ═══════════════════════════════════════════════════════════════ */
@media (max-width:500px){
    .fav-btn{width:30px;height:30px;font-size:.75rem;}
    .fav-header{padding:.55rem .7rem;gap:.4rem;}
    .fav-header .fav-title{font-size:.8rem;}
    .fav-header .fav-count-text{font-size:.68rem;padding:.12rem .45rem;}
    .fav-header .fav-sort,
    .fav-header .fav-clear-all{font-size:.68rem;padding:.3rem .6rem;}
    .fav-header .fav-sort{padding-right:1.6rem;}
    .fav-empty{padding:2.2rem 1rem;}
    .fav-empty .fav-empty-icon{width:58px;height:58px;font-size:1.5rem;}
    .fav-empty .fav-empty-title{font-size:.95rem;}
    .fav-empty .fav-empty-desc{font-size:.78rem;}
    .pf-fav-btn{width:32px;height:32px;}
}
/* ═══════════════════════════════════════════════════════════ */
/* HEADER LOGO - HỌC TIẾNG TRUNG HSK (FIX BADGE HIỂN THỊ)      */
/* ═══════════════════════════════════════════════════════════ */
.logo-text {
    display: flex;
    align-items: center;
    min-width: 0;
    overflow: visible;
}

.logo-text .title {
    font-size: clamp(1.2rem, 2.2vw, 1.75rem);
    font-weight: 900;
    letter-spacing: -0.03em;
    line-height: 1.15;
    display: flex;
    align-items: center;
    gap: 0.55rem;
    min-width: 0;
}

.logo-text .title .title-text {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #a855f7 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
/* Fallback cho trình duyệt không hỗ trợ background-clip */
@supports not ((-webkit-background-clip: text) or (background-clip: text)) {
    .logo-text .title .title-text {
        color: #7c3aed;
        -webkit-text-fill-color: #7c3aed;
    }
}
[data-theme="dark"] .logo-text .title .title-text {
    background: linear-gradient(135deg, #818cf8 0%, #a78bfa 50%, #c084fc 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ⭐ BADGE HSK — Đảm bảo chữ "HSK" luôn hiển thị rõ */
.logo-text .title .hsk-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.22em 0.65em;
    border-radius: 8px;
    background: linear-gradient(135deg, #f59e0b, #ef4444);
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    font-family: inherit;
    font-size: 0.62em;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.15);
    box-shadow: 0 3px 10px rgba(239, 68, 68, 0.45);
    animation: hskBadgePulse 2.5s ease-in-out infinite;
    flex-shrink: 0;
    line-height: 1;
    transform: translateY(-2px);
    white-space: nowrap;
    min-width: 2.8em;
    visibility: visible !important;
    opacity: 1 !important;
}

@keyframes hskBadgePulse {
    0%, 100% {
        box-shadow: 0 3px 10px rgba(239, 68, 68, 0.45);
        transform: translateY(-2px) scale(1);
    }
    50% {
        box-shadow: 0 5px 18px rgba(239, 68, 68, 0.75);
        transform: translateY(-2px) scale(1.06);
    }
}

@media (max-width: 500px) {
    .logo-text .title {
        font-size: 1.1rem;
        gap: 0.4rem;
    }
    .logo-text .title .hsk-badge {
        font-size: 0.6em;
        padding: 0.2em 0.55em;
        min-width: 2.5em;
    }
}
/* ═══════════════════════════════════════════════════════════ */
/* NÚT TỔNG HỢP — Hiển thị ĐỦ nội dung, tự co chữ để /* ═══════════════════════════════════════════════════════════ */
/* NÚT TỔNG HỢP — Auto resize font theo kích thước nút         */
/* ═══════════════════════════════════════════════════════════ */
/* ═══════════════════════════════════════════════════════════ */
/* NÚT TỔNG HỢP — Auto resize font (CSS Container Query + JS)  */
/* ═══════════════════════════════════════════════════════════ */
.ds-btn[data-dataset="tonghop"] {
    min-height: 68px;
    max-height: 68px;
    align-items: center;
    line-height: 1.2;
    padding: .45rem .6rem;
    overflow: hidden;

    /* ⭐ Cho phép dùng đơn vị cqw (container query width) */
    container-type: inline-size;
    container-name: tonghopbtn;
}

.ds-btn[data-dataset="tonghop"] > span {
    flex: 1;
    min-width: 0;
    display: block;
    white.-space: normal;
    word-break: break-word;
    overflow-wrap: anywhere;
    text-align: left;
    line-height: 1.15;

    /* ⭐ Font tự tính theo % chiều rộng nút */
    font-size: clamp(0.6rem, 4.5cqw, 0.85rem);
}

/* Fallback cho trình duyệt cũ không hỗ trợ container query */
@supports not (font-size: 1cqw5) {
    .ds-btn[data-datasetcq="tonghop"] > span {
       w font-size: clamp(0.6rem,, 1.4vw, 0.78 rem);
    }
}

@media (max-width: 500px) {
    .ds-btn[data-dataset="tonghop"] {
        min-height: 62px;
        max-height: 62px;
        padding: .35rem .5rem;
    }
    .ds-btn[data-dataset="tonghop"] > span {
        font-size: clamp(0.58rem, 4.2cqw, 0.72rem);
    }
}

@media (min-width: 501px) and (max-width: 768px) {
    .ds-btn[data-dataset="tonghop"] > span {
        font-size: clamp(0.6rem, 4cqw, 0.75rem);
    }
}

@media (min-width: 1200px) {
    .ds-btn[data-dataset="tonghop"] > span {
        font-size: clamp(0.68rem, 30.85rem);
    }
}
"""
def build_ui_html():
    return r"""
<div class="loading-screen" id="loadingScreen"><i class="fas fa-spinner"></i><div>Đang tải...</div></div>
<div class="sticky-top" id="stickyTop" style="display:none">
<div class="container">
<header class="header"><div class="header-inner">
<div class="logo">
    <div class="logo-icon"><i class="fas fa-language"></i></div>
    <div class="logo-text">
        <div class="title">
            <span class="title-text">Học tiếng Trung</span>
            <span class="hsk-badge">HSK</span>
        </div>
    </div>
</div>
<div class="header-actions">
<div class="trial-badge" id="trialBadge"><i class="fas fa-gem"></i> <span id="trialBadgeText">Trial</span></div>
<div class="demo-badge" id="demoBadge" style="display:none"><i class="fas fa-eye"></i> Demo</div>
<button class="btn-login-header" id="headerLoginBtn" style="display:none"><i class="fas fa-sign-in-alt"></i> <span>Đăng nhập</span></button>
<button class="icon-btn intro-btn" id="introBtn" title="Giới thiệu"><i class="fas fa-info-circle"></i></button>
<button class="icon-btn reset-btn hidden" id="resetBtn" title="Đặt lại bộ lọc"><i class="fas fa-undo-alt"></i><span class="badge" id="resetBadge">0</span></button>
<button class="icon-btn" id="themeToggle" title="Đổi giao diện"><i class="fas fa-moon"></i></button>
<div class="user-menu" id="userMenu" style="display:none">
<img class="user-avatar" id="userAvatar" src="" alt="Avatar">
<div class="user-dropdown show" id="userDropdown">
<div class="user-info"><div class="name" id="userName">-</div><div class="email" id="userEmail">-</div><span class="role" id="userRole">user</span></div>
<div class="user-details" id="userDetails" style="display:none">
<div class="detail-row" id="expiryRow"><div class="detail-icon" id="expiryIconWrap"><i class="fas fa-calendar-check" id="expiryIcon"></i></div><div class="detail-content"><div class="detail-label">Hạn sử dụng</div><div class="detail-value" id="expiryValue">-</div><div class="detail-sub" id="expirySub"></div></div></div>
<div class="detail-progress" id="expiryProgressWrap" style="display:none"><div class="progress-track"><div class="progress-bar" id="expiryProgressBar"></div></div></div>
</div>
<button class="dropdown-item" id="changeNameBtn"><i class="fas fa-user-edit"></i> Đổi tên hiển thị</button>
<button class="dropdown-item" id="openAdminBtn" style="display:none"><i class="fas fa-shield-alt"></i> Quản lý tài khoản</button>
<button class="dropdown-item" id="renewalHistoryBtn"><i class="fas fa-history"></i> Lịch sử gia hạn</button>
<button class="dropdown-renew" id="dropdownRenewBtn" style="display:none"><i class="fas fa-gem"></i><span>Gia hạn tài khoản</span><span class="renew-badge">VIP</span></button>
<button class="dropdown-item danger" id="logoutBtn"><i class="fas fa-sign-out-alt"></i> Đăng xuất</button>
</div>
</div>
</div>
</div></header>
<!-- __TIKTOK_BAR__ -->

<!-- DATASET SELECTOR -->
<div class="dataset-selector" id="datasetSelector">
    <div class="ds-label">
        <i class="fas fa-layer-group"></i>
        <span>Bộ dữ liệu</span>
    </div>
    <div class="ds-main-row">
        <button class="ds-btn ds-btn-primary active" data-dataset="tonghop">
            <i class="fas fa-book-open"></i>
            <span id="dsTonghopLabel">1700+ Câu phản xạ<br>Văn phòng - Công xưởng</span>
        </button>
        <button class="ds-btn ds-btn-primary" data-dataset-group="chuyen-nganh" id="dsChuyenNganhBtn">
            <i class="fas fa-industry"></i>
            <span>Chuyên ngành</span>
            <i class="fas fa-chevron-down ds-arrow"></i>
            <span class="ds-new-badge" id="dsNewBadge">NEW</span>
        </button>
        <!-- __FAV_DATASET_TAB__ -->
    </div>
    <div class="ds-sub-wrap" id="dsSubWrap" style="display:none">
        <div class="ds-sub-label">
            <i class="fas fa-tags"></i>
            <span>Chọn ngành</span>
        </div>
        <div class="ds-sub-grid" id="dsSubGrid"></div>
    </div>
</div>

<div class="search-filter-row">
<div class="search-bar"><i class="fas fa-search"></i>
<input type="text" id="searchInput" placeholder="Tìm kiếm... (VD: hsk1 5)" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
<button class="search-clear" id="clearSearchBtn" aria-label="Xóa"><i class="fas fa-times"></i></button>
</div>
<div class="filters">
<div class="chip" id="hskChip"><span class="chip-label">HSK</span><span class="chip-value" id="hskValue">Tất cả</span><i class="fas fa-chevron-down chip-arrow"></i>
<select id="hskFilter"><option value="">Tất cả</option><option value="HSK1">HSK1</option><option value="HSK2">HSK2</option><option value="HSK3">HSK3</option><option value="HSK4">HSK4</option><option value="HSK5">HSK5</option><option value="HSK6">HSK6</option></select>
</div>
<div class="chip" id="subjectChip"><span class="chip-label">Chủ đề</span><span class="chip-value" id="subjectValue">Tất cả</span><i class="fas fa-chevron-down chip-arrow"></i>
<select id="subjectFilter"><option value="">Tất cả chủ đề</option></select>
</div>
</div>
</div>
<div class="result-count" id="resultCount"><i class="fas fa-list-ul"></i><span>Tìm thấy <b id="resultCountNum">0</b> kết quả</span></div>
</div>
</div>
<div class="fab-group open" id="fabGroup" style="display:none">
<button class="fab-btn fab-sub" id="toggleViBtn" title="Ẩn/hiện Tiếng Việt"><i class="fas fa-language"></i></button>
<button class="fab-btn fab-sub" id="togglePinyinBtn" title="Ẩn/hiện Pinyin"><i class="fas fa-spell-check"></i></button>
<button class="fab-btn fab-sub" id="togglePracticeBtn" title="Ẩn/hiện Ô luyện dịch"><i class="fas fa-keyboard"></i></button>
<button class="fab-btn fab-sub fab-focus" id="toggleFocusBtn" title="Click để tắt Zalo/TikTok (Silent mode)"><i class="fas fa-bell"></i></button>
<button class="fab-btn fab-main" id="fabMainBtn" title="Tùy chọn hiển thị"><i class="fas fa-sliders-h"></i></button>
</div>
<main class="main" id="mainContent" style="display:none">
<div class="container">

<!-- __QUICK_INTRO_BANNER__ -->

<div class="demo-banner" id="demoBanner" style="display:none">
<div class="demo-banner-icon"><i class="fas fa-gift"></i></div>
<div class="demo-banner-text"><div class="title" id="demoBannerTitle">Đăng nhập miễn phí để mở khóa toàn bộ</div>
<div class="desc" id="demoBannerDesc">Đăng nhập bằng <b>Gmail</b> để xem <b>toàn bộ kho câu</b>, không giới luyện viết.<br>Nghe + Luyện viết còn lại hôm nay: <b id="demoRemainingText" style="color:#16a34a">100</b> lượt.</div></div>
<button class="demo-banner-btn" id="demoBannerBtn" onclick="showLoginModal()"><i class="fas fa-sign-in-alt"></i> <span id="demoBannerBtnText">Đăng nhập bằng Gmail</span></button>
</div>
<div class="expiry-banner" id="expiryBanner" style="display:none">
    <div class="expiry-banner-icon" id="expiryBannerIcon">
        <i class="fas fa-hourglass-half"></i>
    </div>
    <div class="expiry-banner-text">
        <div class="title" id="expiryBannerTitle">Tài khoản sắp hết hạn</div>
        <div class="desc" id="expiryBannerDesc">Đang cập nhật...</div>
    </div>
    <button class="expiry-banner-btn" id="expiryContactBtn" type="button">
        <i class="fas fa-gem"></i> Gia hạn ngay
    </button>
</div>
<div class="mobile-view" id="mobileWrapper"><div class="no-data"><i class="fas fa-spinner fa-pulse"></i>Đang tải...</div></div>
</div>
</main>
<div class="writer-modal" id="writerModal">
<div class="writer-box">
<button class="writer-close" id="writerClose" aria-label="Đóng"><i class="fas fa-times"></i></button>
<div class="writer-char-info"><div class="vi-small" id="writerViSmall"></div><div class="pinyin-small" id="writerPinyinSmall"></div></div>
<div class="writer-chars" id="writerChars"></div>
<div class="writer-target" id="writerTarget"></div>
<div class="writer-score" id="writerScore"></div>
<div class="writer-controls">
<button class="writer-btn primary" id="writerAnimate"><i class="fas fa-play"></i> Viết</button>
<button class="writer-btn" id="writerQuiz"><i class="fas fa-pen"></i> Tự viết</button>
<button class="writer-btn" id="writerReset"><i class="fas fa-undo-alt"></i> Xóa</button>
</div>
</div>
</div>
<div class="practice-full-modal" id="practiceFullModal">
<div class="practice-full-header">
<div class="pf-brand"><div class="pf-brand-icon"><i class="fas fa-language"></i></div>
<div class="pf-brand-text"><div class="pf-brand-title">Học tiếng Trung</div><div class="pf-brand-sub">Văn phòng &amp; Công xưởng</div></div>
</div>
<div class="pf-counter" id="pfCounter">Câu 1 / 1</div>
<div class="pf-tags" id="pfTags"></div>
<button class="pf-close" id="pfClose" aria-label="Đóng"><i class="fas fa-times"></i></button>
</div>
<div class="pf-filters">

<div class="pf-filter-row">
<div class="pf-chip" id="pfHskChip"><span class="pf-chip-label">HSK</span><span class="pf-chip-value" id="pfHskValue">Tất cả</span><i class="fas fa-chevron-down pf-chip-arrow"></i>
<select id="pfHskFilter"><option value="">Tất cả</option><option value="HSK1">HSK1</option><option value="HSK2">HSK2</option><option value="HSK3">HSK3</option><option value="HSK4">HSK4</option><option value="HSK5">HSK5</option><option value="HSK6">HSK6</option></select>
</div>
<div class="pf-chip" id="pfSubjectChip"><span class="pf-chip-label">Chủ đề</span><span class="pf-chip-value" id="pfSubjectValue">Tất cả</span><i class="fas fa-chevron-down pf-chip-arrow"></i>
<select id="pfSubjectFilter"><option value="">Tất cả chủ đề</option></select>
</div>
</div>

<div class="pf-dataset-row" id="pfDatasetRow">
    <span class="pf-dataset-label"><i class="fas fa-layer-group"></i> Bộ dữ liệu</span>
    <select class="pf-dataset-select" id="pfDatasetSelect"></select>

    <div class="pf-dataset-search">
    <i class="fas fa-search"></i>
    <input type="text" id="pfSearchInput" placeholder="Tìm kiếm... (VD: hsk1 5)" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
    <button class="pf-search-clear" id="pfClearSearchBtn" aria-label="Xóa"><i class="fas fa-times"></i></button>
</div>

    <div class="pf-quick-nav" id="pfQuickNavWrap">
        <span class="pf-quick-nav-label">Câu:</span>
        <select class="pf-quick-nav-select" id="pfQuickNav"><option value="">-- Chọn câu --</option></select>
    </div>
</div>

</div>
<div class="practice-full-body">
<div class="practice-full-content">
<div class="practice-full-vi" id="pfVi">-</div>
<div class="practice-full-input-wrap">
<div class="practice-input-row">
<textarea class="practice-full-input" id="pfInput" placeholder="Gõ tiếng Trung..." autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" rows="1"></textarea>
<button class="practice-speak-btn" id="pfSpeakBtn" type="button" title="Nghe câu này" aria-label="Nghe câu này"><i class="fas fa-volume-up"></i></button>
</div>
<div class="char-preview" id="pfPreview"></div>
<div class="practice-full-status" id="pfStatus"></div>
</div>
<div class="reveal-actions">
<button id="pfHintBtn"><i class="fas fa-lightbulb"></i> Gợi ý</button>
<button id="pfRevealBtn"><i class="fas fa-eye"></i> Xem đáp án</button>
</div>
<div class="answer-reveal" id="pfAnswer">
<div class="answer-chars" id="pfAnswerChars"></div>
<div class="answer-pinyin" id="pfAnswerPinyin"></div>
</div>
</div>
</div>
<div class="practice-full-nav">
    <button class="pf-nav-icon main-nav" id="pfPrevBtn" type="button" title="Câu trước" aria-label="Câu trước">
        <i class="fas fa-chevron-left"></i>
    </button>
    <button class="pf-nav-icon main-nav primary" id="pfNextBtn" type="button" title="Câu sau" aria-label="Câu sau">
        <i class="fas fa-chevron-right"></i>
    </button>
    <button class="pf-nav-icon main-nav speak" id="pfQuickSpeakBtn" type="button" title="Đọc cả câu" aria-label="Đọc cả câu">
        <i class="fas fa-volume-up"></i>
    </button>
    <div class="mini-group">
        <button class="pf-nav-icon mini-nav random" id="pfRandomToggleBtn" type="button" title="Bật/tắt chế độ nhảy câu ngẫu nhiên" aria-label="Chế độ ngẫu nhiên">
            <i class="fas fa-dice"></i>
        </button>
        <button class="pf-nav-icon mini-nav voice" id="pfVoiceBtn" type="button" title="Cài đặt giọng đọc" aria-label="Cài đặt giọng đọc">
            <i class="fas fa-headphones"></i>
        </button>
    </div>
</div>
<a class="pf-tiktok-float" id="pfTiktokFloat" href="#" target="_blank" rel="noopener noreferrer" title="Theo dõi TikTok">
<span class="pf-tiktok-avatar-wrap">
<img class="pf-tiktok-avatar" id="pfTiktokAvatar" src="" alt="TikTok" onerror="this.style.display='none'">
<i class="fab fa-tiktok pf-tiktok-fallback-icon"></i>
</span>
<span class="pf-tiktok-content">
<span class="pf-tiktok-label">Theo dõi</span>
<span class="pf-tiktok-name" id="pfTiktokName">TikTok</span>
</span>
<i class="fab fa-tiktok pf-tiktok-badge"></i>
</a>
</div>
<div class="voice-modal" id="voiceModal">
    <div class="voice-box">
        <div class="voice-header">
            <h2><i class="fas fa-sliders-h"></i> Cài đặt giọng đọc</h2>
            <button class="voice-close" id="voiceClose" aria-label="Đóng"><i class="fas fa-times"></i></button>
        </div>
        <div class="voice-body">

            <div class="voice-group">
                <div class="voice-group-label">
                    <span><i class="fas fa-tachometer-alt"></i> Tốc độ đọc</span>
                    <span class="voice-value" id="voiceRateValue">1.00×</span>
                </div>
                <div class="voice-slider-row">
                    <button type="button" id="voiceRateMinus" title="Chậm hơn">−</button>
                    <input type="range" class="voice-slider" id="voiceRateSlider" min="0.5" max="1.5" step="0.05" value="1.0">
                    <button type="button" id="voiceRatePlus" title="Nhanh hơn">+</button>
                </div>
                <div class="voice-preset-row">
                    <button class="voice-preset-btn" data-rate="0.6">0.6× Rất chậm</button>
                    <button class="voice-preset-btn" data-rate="0.75">0.75× Chậm</button>
                    <button class="voice-preset-btn" data-rate="0.85">0.85× Chuẩn</button>
                    <button class="voice-preset-btn" data-rate="1.0">1.0× Bình thường</button>
                    <button class="voice-preset-btn" data-rate="1.15">1.15× Nhanh</button>
                </div>
            </div>

            <div class="voice-group">
                <div class="voice-group-label">
                    <span><i class="fas fa-microphone"></i> Giọng đọc tiếng Trung</span>
                </div>
                <select class="voice-select" id="voiceSelect">
                    <option value="">-- Tự động (mặc định) --</option>
                </select>
            </div>

            <div class="voice-group">
                <div class="voice-group-label">
                    <span><i class="fas fa-music"></i> Cao độ (Pitch)</span>
                    <span class="voice-value" id="voicePitchValue">1.00</span>
                </div>
                <div class="voice-slider-row">
                    <button type="button" id="voicePitchMinus" title="Trầm hơn">−</button>
                    <input type="range" class="voice-slider" id="voicePitchSlider" min="0.5" max="1.5" step="0.05" value="1.0">
                    <button type="button" id="voicePitchPlus" title="Cao hơn">+</button>
                </div>
            </div>

            <div class="voice-group">
                <div class="voice-group-label">
                    <span><i class="fas fa-volume-up"></i> Âm lượng</span>
                    <span class="voice-value" id="voiceVolumeValue">100%</span>
                </div>
                <div class="voice-slider-row">
                    <button type="button" id="voiceVolumeMinus" title="Nhỏ hơn">−</button>
                    <input type="range" class="voice-slider" id="voiceVolumeSlider" min="0" max="1" step="0.05" value="1.0">
                    <button type="button" id="voiceVolumePlus" title="To hơn">+</button>
                </div>
            </div>

            <button class="voice-test-btn" id="voiceTestBtn" type="button">
                <i class="fas fa-play"></i> Nghe thử
            </button>

            <button class="voice-reset" id="voiceResetBtn" type="button">
                <i class="fas fa-undo-alt"></i> Khôi phục mặc định
            </button>

            <div class="voice-note">
                <i class="fas fa-info-circle"></i>
                <div>Cài đặt được <b>lưu tự động</b> và áp dụng cho tất cả nút loa. Danh sách giọng đọc phụ thuộc vào <b>trình duyệt và hệ điều hành</b> của bạn.</div>
            </div>

        </div>
    </div>
</div>

<!-- ONBOARDING MODAL - CHON CHU DE QUAN TAM -->
<div class="onboarding-modal" id="onboardingModal">
    <div class="onboarding-box">
        <button class="onboarding-close" id="onboardingCloseBtn" type="button" aria-label="Đóng">
            <i class="fas fa-times"></i>
        </button>
        <div class="onboarding-header">
            <div class="onboarding-icon">
                <i class="fas fa-compass"></i>
            </div>
            <div class="onboarding-title" id="onboardingTitle">Bạn quan tâm chủ đề nào?</div>
            <div class="onboarding-subtitle" id="onboardingSubtitle">
                Chọn các chủ đề — chúng tôi sẽ gợi ý câu phù hợp nhất
            </div>
            <div class="onboarding-counter" id="onboardingCounter">
                <i class="fas fa-hand-pointer"></i>
                <span>Đã chọn <b id="onboardingSelectedCount">0</b> / <b id="onboardingMaxCount">3</b></span>
            </div>
        </div>
        <div class="onboarding-body">
            <div class="onboarding-section-label">
                <i class="fas fa-tags"></i>
                <span>Chủ đề có sẵn trong kho</span>
            </div>
            <div class="onboarding-topics" id="onboardingTopics">
                <div class="onboarding-empty">
                    <i class="fas fa-spinner fa-pulse"></i> Đang tải...
                </div>
            </div>
        </div>
        <div class="onboarding-footer">
            <button class="onboarding-btn ghost" id="onboardingSkipBtn" type="button">
                <i class="fas fa-forward"></i> Bỏ qua
            </button>
            <button class="onboarding-btn primary" id="onboardingStartBtn" type="button" disabled>
                <i class="fas fa-check"></i> Bắt đầu học
            </button>
        </div>
    </div>
</div>
"""
def build_ui_js():
    return r"""
var filtered = [];
var state = { search:'', hsk:'', subject:'' };
var PAGE_SIZE = 50;
var renderedCount = 0;
var focusedStt = null;
var mobileWrapper;
var currentBtn = null;

var displayState = { vi: true, pinyin: false, practice: false };

/* HELPER: TIER HIEN TAI CO DUOC MO CHUYEN NGANH KHONG? */
function canAccessChuyenNganh() {
    return (typeof window.APP_TIER !== 'undefined' && window.APP_TIER === 'active');
}
/* ═══════════════════════════════════════════════════════════ */
/* NORMALIZE HSK — Gộp HSK 7, 8, 9 và mọi file (1)(2)(3)...    */
/*   "HSK 7-9 (1)" / "HSK 7-9 (2)" / "HSK 7-9 (3)"  → "HSK7-9" */
/*   "HSK 7-9" / "HSK7-9" / "HSK 7" / "HSK 8" / "HSK 9" → "HSK7-9" */
/*   "HSK 1" / "HSK 2 (5)" / "hsk3"                 → "HSK1"/"HSK2"/"HSK3" */
/* ═══════════════════════════════════════════════════════════ */
function normalizeHsk(hsk) {
    if (!hsk) return '';
    var s = String(hsk).toUpperCase().trim();

    // Bỏ hậu tố "(1)", "(2)", "(3)"...
    s = s.replace(/\([^)]*\)/g, '').trim();

    // Bỏ mọi khoảng trắng
    s = s.replace(/\s+/g, '');

    // Tách số HSK
    var m = s.match(/^HSK(\d+)(?:[-–](\d+))?$/);
    if (!m) return s;

    var from = parseInt(m[1], 10);
    var to   = m[2] ? parseInt(m[2], 10) : from;

    // HSK 7, 8, 9 → gộp hết thành "HSK7-9"
    if (from >= 7 || to >= 7) return 'HSK7-9';

    // HSK 1-6 giữ nguyên
    return 'HSK' + from;
}

function waitForData(callback) {
    if (window.__dataLoaded) {
        callback();
    } else if (window.__dataLoadPromise) {
        window.__dataLoadPromise.then(callback);
    } else {
        window.addEventListener('dataLoaded', callback, { once: true });
    }
}
/* ═══════════════════════════════════════════════════════════ */
/* SHOW SEARCH TOAST — Thông báo kết quả tìm kiếm đặc biệt     */
/* ═══════════════════════════════════════════════════════════ */
function showSearchToast(message) {
    var old = document.getElementById('searchToast');
    if (old) old.remove();

    var toast = document.createElement('div');
    toast.id = 'searchToast';
    toast.textContent = message;
    toast.style.cssText = [
        'position:fixed','top:80px','left:50%',
        'transform:translateX(-50%) translateY(-20px)',
        'padding:.7rem 1.2rem',
        'background:linear-gradient(135deg,#2563eb,#7c3aed)',
        'color:#fff','border-radius:50px',
        'font-size:.85rem','font-weight:700','font-family:inherit',
        'box-shadow:0 8px 24px rgba(37,99,235,.45)',
        'z-index:9999','opacity:0',
        'transition:opacity .25s ease, transform .3s cubic-bezier(.34,1.56,.64,1)',
        'pointer-events:none','max-width:90vw',
        'text-overflow:ellipsis','overflow:hidden','white-space:nowrap'
    ].join(';');

    document.body.appendChild(toast);

    requestAnimationFrame(function() {
        toast.style.opacity = '1';
        toast.style.transform = 'translateX(-50%) translateY(0)';
    });

    setTimeout(function() {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(-50%) translateY(-20px)';
        setTimeout(function() { if (toast.parentNode) toast.remove(); }, 300);
    }, 2200);
}
/* THONG BAO KHOA CHUYEN NGANH */
function showChuyenNganhLockMessage() {
    if (typeof currentUser === 'undefined' || !currentUser) {
        if (confirm('Bộ dữ liệu Chuyên ngành\n\n' +
                    'Bạn cần ĐĂNG NHẬP và GIA HẠN để mở khoá.\n\n' +
                    'Đăng nhập ngay?')) {
            if (typeof showLoginModal === 'function') showLoginModal();
        }
    } else {
        if (confirm('Bộ dữ liệu Chuyên ngành\n\n' +
                    'Chỉ tài khoản ĐÃ GIA HẠN mới mở được.\n\n' +
                    'Gia hạn ngay?')) {
            if (typeof openRenewalModal === 'function') openRenewalModal();
        }
    }
}

function showPracticeFullLockMessage() {
    if (typeof currentUser === 'undefined' || !currentUser) {
        if (confirm('Chế độ luyện tập Chuyên ngành\n\n' +
                    'Bạn cần ĐĂNG NHẬP và GIA HẠN để mở khoá.\n\n' +
                    'Đăng nhập ngay?')) {
            if (typeof showLoginModal === 'function') showLoginModal();
        }
    } else {
        if (confirm('Chế độ luyện tập Chuyên ngành\n\n' +
                    'Chỉ tài khoản ĐÃ GIA HẠN mới mở được.\n\n' +
                    'Gia hạn ngay?')) {
            if (typeof openRenewalModal === 'function') openRenewalModal();
        }
    }
}
/* ⭐ Auto-fit font-size cho label — chỉ chạy khi CSS không đủ */
function autoFitLabel(el) {
    if (!el) return;
    var parent = el.closest('.ds-btn') || el.parentElement;
    if (!parent) return;

    // ⭐ Bước 1: Reset về font-size từ CSS (xóa inline style cũ)
    el.style.fontSize = '';

    // ⭐ Bước 2: Đo chiều cao khả dụng
    var parentH = parent.clientHeight;
    var parentStyle = getComputedStyle(parent);
    var padTop = parseFloat(parentStyle.paddingTop) || 0;
    var padBot = parseFloat(parentStyle.paddingBottom) || 0;
    var availableH = parentH - padTop - padBot - 2;

    // ⭐ Bước 3: Kiểm tra có overflow không
    var hasOverflowH = el.scrollHeight > availableH;
    var hasOverflowW = el.scrollWidth > el.clientWidth + 2;

    // ⭐ Nếu CSS đã đủ → không cần can thiệp
    if (!hasOverflowH && !hasOverflowW) {
        return;
    }

    // ⭐ Bước 4: CSS không đủ → JS tự co font đến khi vừa
    var size = parseFloat(getComputedStyle(el).fontSize) || 12;
    var minSize = 8;
    var safety = 0;

    while (safety < 60 && size > minSize) {
        size -= 0.2;
        el.style.fontSize = size + 'px';

        var okH = el.scrollHeight <= availableH;
        var okW = el.scrollWidth <= el.clientWidth + 2;

        if (okH && okW) break;
        safety++;
    }
}
/* ============================================================ */
/* DATASET SWITCHING                                             */
/* ============================================================ */
function initDatasetSelector() {
    if (typeof DATASET_REGISTRY === 'undefined' || !DATASET_REGISTRY) {
        if (window.__dataLoadPromise) {
            window.__dataLoadPromise.then(function() { initDatasetSelector(); });
        }
        return;
    }
    if (!DATASET_REGISTRY.tonghop) return;
    var labelEl = $('dsTonghopLabel');
    if (labelEl) {
        var count = DATASET_REGISTRY.tonghop.count
                 || (DATASET_REGISTRY.tonghop.data || []).length;
        labelEl.innerHTML = count + '+ Câu phản xạ<br>Văn phòng - Công xưởng';
        labelEl.title = 'Văn phòng - Công xưởng';

        // ⭐ Auto-fit sau khi layout ổn định
        requestAnimationFrame(function() {
            requestAnimationFrame(function() {
                autoFitLabel(labelEl);
            });
        });

        // ⭐ Re-fit khi resize window (throttled)
        if (!window.__tonghopResizeBound) {
            window.__tonghopResizeBound = true;
            var _resizeTimer = null;
            window.addEventListener('resize', function() {
                clearTimeout(_resizeTimer);
                _resizeTimer = setTimeout(function() {
                    autoFitLabel(labelEl);
                }, 150);
            });
        }
    }

    var chuyenNganhKeys = Object.keys(DATASET_REGISTRY).filter(function(id) {
        return id !== 'tonghop';
    });

    var cnBtn = $('dsChuyenNganhBtn');
    if (chuyenNganhKeys.length === 0) {
        if (cnBtn) cnBtn.style.display = 'none';
        return;
    }

    var canAccess = canAccessChuyenNganh();

    var subGrid = $('dsSubGrid');
    if (subGrid) {
        subGrid.innerHTML = '';
        chuyenNganhKeys.forEach(function(id) {
            var ds = DATASET_REGISTRY[id];

            var btn = document.createElement('button');
            btn.className = 'ds-sub-btn' + (canAccess ? '' : ' locked');
            btn.dataset.dataset = ds.id;
            btn.dataset.locked = canAccess ? '0' : '1';
            btn.style.setProperty('--ds-color', ds.color || '#64748b');
            btn.title = ds.name + ' (' + ds.count + ' câu)' +
                        (canAccess ? '' : ' - Cần gia hạn để mở khoá');

            var icon = document.createElement('i');
            icon.className = 'fas ' + (ds.icon || 'fa-folder');
            btn.appendChild(icon);

            var nameSpan = document.createElement('span');
            nameSpan.textContent = ds.name.normalize ? ds.name.normalize('NFC') : ds.name;
            btn.appendChild(nameSpan);

            if (!canAccess) {
                var lock = document.createElement('i');
                lock.className = 'fas fa-lock ds-sub-lock';
                btn.appendChild(lock);
            }

            subGrid.appendChild(btn);
        });
    }

    if (cnBtn) {
        var oldLock = cnBtn.querySelector('.ds-main-lock');
        if (oldLock) oldLock.remove();

        if (!canAccess) {
            var span = cnBtn.querySelector('span');
            if (span) {
                span.insertAdjacentHTML('afterend',
                    '<i class="fas fa-lock ds-main-lock"></i>');
            }
            cnBtn.classList.add('has-lock');
            cnBtn.title = 'Cần đăng nhập + gia hạn để mở khoá chuyên ngành';
        } else {
            cnBtn.classList.remove('has-lock');
            cnBtn.title = 'Chọn chuyên ngành';
        }
    }

    /* NÚT TỔNG HỢP — Click để về tab tổng hợp */
    document.querySelectorAll('.ds-btn[data-dataset="tonghop"]').forEach(function(btn) {
        if (btn.__boundDataset) return;
        btn.__boundDataset = true;
        btn.addEventListener('click', function() {
            switchDataset('tonghop');
            var sub = $('dsSubWrap');
            if (sub) sub.style.display = 'none';

            document.querySelectorAll('.ds-btn').forEach(function(b) {
                b.classList.remove('active');
            });
            btn.classList.add('active');
        });
    });

    /* NÚT CHUYÊN NGÀNH — Click để mở/đóng dropdown */
    if (cnBtn && !cnBtn.__boundToggle) {
        cnBtn.__boundToggle = true;
        cnBtn.addEventListener('click', function() {
            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';
            if (isOpen) {
                sub.style.display = 'none';
                cnBtn.classList.remove('active');
            } else {
                sub.style.display = 'block';

                document.querySelectorAll('.ds-btn').forEach(function(b) {
                    b.classList.remove('active');
                });
                cnBtn.classList.add('active');
            }
        });
    }

    /* SUB-BUTTONS CHUYÊN NGÀNH — Click để chuyển dataset */
    document.querySelectorAll('.ds-sub-btn').forEach(function(btn) {
        if (btn.__boundSub) return;
        btn.__boundSub = true;
        btn.addEventListener('click', function(e) {
            if (this.dataset.locked === '1') {
                e.preventDefault();
                e.stopPropagation();
                showChuyenNganhLockMessage();
                return;
            }
            var id = this.dataset.dataset;
            document.querySelectorAll('.ds-sub-btn').forEach(function(b) {
                b.classList.remove('active');
            });
            this.classList.add('active');
            switchDataset(id);

            document.querySelectorAll('.ds-btn').forEach(function(b) {
                b.classList.remove('active');
            });
            if (cnBtn) cnBtn.classList.add('active');
        });
    });

    markCurrentDatasetActive();
}

function switchDataset(datasetId) {
    if (!DATASET_REGISTRY[datasetId]) return;

    /* ❤️ Nếu rời tab Yêu thích → reset cờ */
    if (typeof favState !== 'undefined' && favState.currentView) {
        favState.currentView = false;
    }

    if (datasetId !== 'tonghop' && !canAccessChuyenNganh()) {
        showChuyenNganhLockMessage();
        return;
    }

    if (typeof window.__switchRawData === 'function') {
        window.__switchRawData(datasetId);
    }

    window.__onboardingOverride = null;

    state = { search:'', hsk:'', subject:'' };
    if ($('searchInput')) $('searchInput').value = '';
    if ($('hskFilter')) $('hskFilter').value = '';
    if ($('subjectFilter')) $('subjectFilter').value = '';

    buildFilters();
    applyFilter();
    updateResultCount();

    if ($('fabGroup')) $('fabGroup').classList.remove('open');

    /* ❤️ Cập nhật lock state cho tab (bao gồm tab Yêu thích) */
    if (typeof favUpdateLockState === 'function') favUpdateLockState();

    /* Khôi phục banner chủ đề sau khi đổi dataset */
    var saved = loadOnboardingSelection();
    if (saved && Array.isArray(saved.topics) && saved.topics.length > 0) {
        var cfg = getOnboardingConfig();
        if (cfg) {
            if (datasetId === 'tonghop') {
                window.__onboardingAutoPicked = !!saved.auto_picked;
                applyOnboardingSelection(saved.topics, false);
            }
        }
    }
}

/* ============================================================ */
/* VOICE SETTINGS                                                */
/* ============================================================ */
var voiceState = {
    rate: 1.0,
    pitch: 1.0,
    volume: 1.0,
    voiceURI: ''
};

var DEFAULT_VOICE = { rate: 1.0, pitch: 1.0, volume: 1.0, voiceURI: '' };

function loadVoiceSettings() {
    try {
        var saved = JSON.parse(localStorage.getItem('voiceSettings') || 'null');
        if (saved && typeof saved === 'object') {
            if (typeof saved.rate === 'number')   voiceState.rate   = Math.max(0.5, Math.min(1.5, saved.rate));
            if (typeof saved.pitch === 'number')  voiceState.pitch  = Math.max(0.5, Math.min(1.5, saved.pitch));
            if (typeof saved.volume === 'number') voiceState.volume = Math.max(0,   Math.min(1,   saved.volume));
            if (typeof saved.voiceURI === 'string') voiceState.voiceURI = saved.voiceURI;
        }
    } catch(e) {}
}

function saveVoiceSettings() {
    try { localStorage.setItem('voiceSettings', JSON.stringify(voiceState)); } catch(e) {}
}

function applyVoiceSettings(utterance) {
    if (!utterance) return;
    utterance.rate   = voiceState.rate;
    utterance.pitch  = voiceState.pitch;
    utterance.volume = voiceState.volume;
    var v = pickVoice();
    if (v) utterance.voice = v;
}

function pickVoice() {
    if (!('speechSynthesis' in window)) return null;
    var voices = speechSynthesis.getVoices();
    if (!voices.length) return null;

    if (voiceState && voiceState.voiceURI) {
        var chosen = voices.find(function(v) { return v.voiceURI === voiceState.voiceURI; });
        if (chosen) return chosen;
    }

    var priorities = [
        function(v){ return v.lang === 'zh-CN' && /Ting-?Ting/i.test(v.name); },
        function(v){ return v.lang === 'zh-CN' && /Siri/i.test(v.name); },
        function(v){ return v.lang === 'zh-CN' && v.localService; },
        function(v){ return v.lang === 'zh-CN'; },
        function(v){ return v.lang === 'zh-TW'; },
        function(v){ return v.lang && v.lang.indexOf('zh') === 0; }
    ];
    for (var i = 0; i < priorities.length; i++) {
        var found = voices.find(priorities[i]);
        if (found) return found;
    }
    return null;
}

function getChineseVoice() { return pickVoice(); }

/* ============================================================ */
/* TIER HELPERS — EXPIRED DÙNG Y HỆT DEMO                        */
/* ============================================================ */
function getTierInfo() {
    if (typeof window.APP_TIER !== 'undefined' && window.APP_LIMITS) {
        var tier = window.APP_TIER;
        var maxQ = window.APP_LIMITS.maxQuestions;
        var maxH = window.APP_LIMITS.maxHSK;

        if (tier === 'expired') {
            if (!maxQ || maxQ <= 0) {
                maxQ = (typeof DEMO_LIMIT === 'number') ? DEMO_LIMIT : 60;
            }
            if (!maxH || maxH <= 0) {
                maxH = (typeof DEMO_HSK_MAX === 'number') ? DEMO_HSK_MAX : 3;
            }
        }

        return {
            tier: tier,
            maxQuestions: maxQ,
            maxHSK: maxH,
            unlimitedWriting: !!window.APP_LIMITS.unlimitedWriting,
            isTrial: !!window.APP_LIMITS.isTrial,
            email: window.APP_LIMITS.email
        };
    }
    return {
        tier: 'demo',
        maxQuestions: (typeof DEMO_LIMIT === 'number') ? DEMO_LIMIT : 60,
        maxHSK: (typeof DEMO_HSK_MAX === 'number') ? DEMO_HSK_MAX : 3,
        unlimitedWriting: false,
        isTrial: false,
        email: null
    };
}

function isDemoTier()   { return getTierInfo().tier === 'demo'; }
function isTrialTier()  { return getTierInfo().tier === 'trial'; }
function isActiveTier() { return getTierInfo().tier === 'active'; }
function isExpiredTier(){ return getTierInfo().tier === 'expired'; }
function isLimitedTier(){ var t = getTierInfo().tier; return t === 'demo' || t === 'trial' || t === 'expired'; }

/* ═══════════════════════════════════════════════════════════ */
/* MỚI: TÍNH SỐ CÂU TỐI ĐA MỖI CHỦ ĐỀ                          */
/* Công thức: ceil(limit / tổng_số_chủ_đề_trong_kho)            */
/* ═══════════════════════════════════════════════════════════ */
function getMaxPerTopic(limit, poolData) {
    var subjectSet = {};
    (poolData || RAW_DATA).forEach(function(r) {
        var s = (r.subject || '').trim();
        if (s) subjectSet[s] = 1;
    });
    var totalTopics = Object.keys(subjectSet).length;
    if (totalTopics === 0) return 1;
    if (!limit || limit <= 0) return 1;
    return Math.max(1, Math.ceil(limit / totalTopics));
}

/* ═══════════════════════════════════════════════════════════ */
/* MỚI: TÍNH THỐNG KÊ KHOÁ CHO BANNER                           */
/* ═══════════════════════════════════════════════════════════ */
function computeLockStats(selectedTopics, allowedHsk, maxQ, isUnlimited) {
    var stats = {
        lockedInSelected: 0,
        totalInSelected: 0,
        lockedTopics: 0,
        totalTopics: 0,
        maxPerTopic: 1
    };
    if (!selectedTopics || selectedTopics.length === 0) return stats;

    var allTopicsSet = {};
    RAW_DATA.forEach(function(r) {
        var s = (r.subject || '').trim();
        if (s) allTopicsSet[s] = 1;
    });
    stats.totalTopics = Object.keys(allTopicsSet).length;
    stats.lockedTopics = Math.max(0, stats.totalTopics - selectedTopics.length);

    if (isUnlimited) return stats;
    stats.maxPerTopic = getMaxPerTopic(maxQ, RAW_DATA);

    RAW_DATA.forEach(function(r) {
        var s = (r.subject || '').trim();
        if (selectedTopics.indexOf(s) === -1) return;
        // ⭐ DÙNG normalizeHsk
        if (allowedHsk && allowedHsk.length > 0 && allowedHsk.indexOf(normalizeHsk(r.hsk)) === -1) return;
        stats.totalInSelected++;
    });

    var canTake = Math.min(selectedTopics.length * stats.maxPerTopic, maxQ);
    canTake = Math.min(canTake, stats.totalInSelected);
    stats.lockedInSelected = Math.max(0, stats.totalInSelected - canTake);
    return stats;
}

/* ═══════════════════════════════════════════════════════════ */
/* SỬA: GET LIMITED DATA — GIỚI HẠN SỐ CÂU MỖI CHỦ ĐỀ           */
/* ═══════════════════════════════════════════════════════════ */
function getLimitedData() {
    if (!window.__dataLoaded || !RAW_DATA || RAW_DATA.length === 0) {
        return [];
    }
    if (window.__onboardingOverride && Array.isArray(window.__onboardingOverride)
        && window.__onboardingOverride.length > 0
        && !state.search && !state.hsk && !state.subject) {
        return window.__onboardingOverride;
    }

    var info = getTierInfo();
    if (info.tier === 'active') return RAW_DATA;

    var max = (typeof info.maxQuestions === 'number' && info.maxQuestions > 0)
              ? info.maxQuestions
              : ((typeof DEMO_LIMIT === 'number') ? DEMO_LIMIT : 60);

    var allowedHsk = getAllowedHskList();
    if (!allowedHsk || allowedHsk.length === 0) {
        return RAW_DATA.slice(0, max);
    }

    // ⭐ DÙNG normalizeHsk ĐỂ SO SÁNH
    var poolByHsk = RAW_DATA.filter(function(r) {
        return allowedHsk.indexOf(normalizeHsk(r.hsk)) !== -1;
    });

    var maxPerTopic = getMaxPerTopic(max, RAW_DATA);

    var topicCount = {};
    var result = [];
    var perHsk = Math.ceil(max / allowedHsk.length);
    var hskCount = {};
    allowedHsk.forEach(function(h) { hskCount[h] = 0; });

    for (var i = 0; i < poolByHsk.length && result.length < max; i++) {
        var r = poolByHsk[i];
        var s = (r.subject || '').trim() || '__no_subject__';
        if ((topicCount[s] || 0) >= maxPerTopic) continue;

        var rHskNorm = normalizeHsk(r.hsk);   // ⭐ CHUẨN HOÁ
        if (rHskNorm && hskCount[rHskNorm] !== undefined && hskCount[rHskNorm] >= perHsk) continue;

        result.push(r);
        topicCount[s] = (topicCount[s] || 0) + 1;
        if (rHskNorm && hskCount[rHskNorm] !== undefined) hskCount[rHskNorm]++;
    }

    if (result.length < max) {
        var usedIds = {};
        result.forEach(function(r) { usedIds[r.stt] = true; });
        for (var j = 0; j < poolByHsk.length && result.length < max; j++) {
            var r2 = poolByHsk[j];
            if (usedIds[r2.stt]) continue;
            var s2 = (r2.subject || '').trim() || '__no_subject__';
            if ((topicCount[s2] || 0) >= maxPerTopic) continue;
            result.push(r2);
            usedIds[r2.stt] = true;
            topicCount[s2] = (topicCount[s2] || 0) + 1;
        }
    }

    return result;
}

function getAllowedHskList() {
    var info = getTierInfo();
    var max = info.maxHSK;
    if (max === Infinity || max >= 6 || info.tier === 'active') {
        return ['HSK1','HSK2','HSK3','HSK4','HSK5','HSK6','HSK7-9'];
    }
    var list = [];
    for (var i = 1; i <= max; i++) list.push('HSK' + i);
    return list;
}

function getAllowedSubjectList() {
    if (!window.__dataLoaded || !RAW_DATA || RAW_DATA.length === 0) {
        return [];
    }
    var info = getTierInfo();
    if (info.tier === 'active') {
        var set = {};
        RAW_DATA.forEach(function(r) { if (r.subject) set[r.subject] = 1; });
        return Object.keys(set).sort();
    }
    var set2 = {};
    getLimitedData().forEach(function(r) { if (r.subject) set2[r.subject] = 1; });
    return Object.keys(set2).sort();
}

function shouldCountUsage() {
    var t = getTierInfo().tier;
    return t === 'demo' || t === 'expired';
}

function getDemoUsage() {
    try {
        var today = new Date().toDateString();
        var data = JSON.parse(localStorage.getItem('demo_usage') || '{}');
        if (data.date !== today) {
            data = { date: today, count: 0 };
            localStorage.setItem('demo_usage', JSON.stringify(data));
        }
        return data.count;
    } catch(e) { return 0; }
}

function incDemoUsage() {
    if (!shouldCountUsage()) return;
    try {
        var today = new Date().toDateString();
        var data = JSON.parse(localStorage.getItem('demo_usage') || '{}');
        if (data.date !== today) data = { date: today, count: 0 };
        data.count++;
        localStorage.setItem('demo_usage', JSON.stringify(data));
    } catch(e) {}
}

function getDemoRemaining() {
    if (!shouldCountUsage()) return Infinity;
    return Math.max(0, DEMO_DAILY_LIMIT - getDemoUsage());
}

function canUseFeature() {
    var info = getTierInfo();
    if (info.tier === 'expired') return getDemoUsage() < DEMO_DAILY_LIMIT;
    if (info.tier === 'demo') return getDemoUsage() < DEMO_DAILY_LIMIT;
    return true;
}

function updateDemoRemaining() {
    var el = $('demoRemainingText');
    if (!el) return;
    if (!shouldCountUsage()) return;
    var remaining = getDemoRemaining();
    el.textContent = remaining;
    if (remaining < 20) el.style.color = '#dc2626';
    else if (remaining < 50) el.style.color = '#f59e0b';
    else el.style.color = '#16a34a';
}

function showLimitMessage() {
    var info = getTierInfo();
    if (info.tier === 'expired') {
        if (confirm('Bạn đã dùng hết ' + DEMO_DAILY_LIMIT + ' lượt miễn phí hôm nay.\n\n' +
                    '(Tài khoản đã hết hạn — đang dùng chế độ Demo)\n\n' +
                    'Gia hạn để dùng KHÔNG GIỚI HẠN!')) {
            if (typeof openRenewalModal === 'function') openRenewalModal();
        }
        return;
    }
    if (info.tier === 'demo') {
        if (confirm('Bạn đã dùng hết ' + DEMO_DAILY_LIMIT + ' lượt miễn phí hôm nay.\n\n' +
                    '(Bao gồm NGHE và LUYỆN VIẾT)\n\n' +
                    'Đăng nhập Google để dùng KHÔNG GIỚI HẠN!')) {
            if (typeof showLoginModal === 'function') showLoginModal();
        }
        return;
    }
}

/* ============================================================ */
/* UTILS                                                         */
/* ============================================================ */
function escapeHtml(str) {
    if (str === null || str === undefined) return '';
    return String(str)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function escapeJs(str) {
    if (str === null || str === undefined) return '';
    return String(str)
        .replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/"/g, '\\"')
        .replace(/\n/g, '\\n').replace(/\r/g, '');
}

function formatTimeDiff(ms) {
    var s = Math.floor(ms / 1000);
    if (s < 60) return 'Vừa xong';
    var m = Math.floor(s / 60);
    if (m < 60) return m + ' phút trước';
    var h = Math.floor(m / 60);
    if (h < 24) return h + ' giờ trước';
    var d = Math.floor(h / 24);
    if (d < 30) return d + ' ngày trước';
    var mo = Math.floor(d / 30);
    return mo + ' tháng trước';
}

/* ============================================================ */
/* TAG CLICKABLE                                                 */
/* ============================================================ */
window.searchByTag = function(evt, type, value) {
    if (evt) {
        evt.stopPropagation();
        if (evt.preventDefault) evt.preventDefault();
    }
    if (!value) return;

    var searchInput = $('searchInput');
    if (!searchInput) return;

    var pfModal = $('practiceFullModal');
    if (pfModal && pfModal.classList.contains('show')) {
        if (typeof closePracticeFull === 'function') closePracticeFull();
    }

    if ($('hskFilter')) $('hskFilter').value = '';
    if ($('subjectFilter')) $('subjectFilter').value = '';

    window.__onboardingOverride = null;
    var obBanner = $('onboardingActiveBanner');
    if (obBanner) obBanner.remove();

    searchInput.value = value;

    state.search = value.toLowerCase().trim();
    state.hsk = '';
    state.subject = '';

    renderedCount = 0;
    applyFilter();

    var mainEl = $('mainContent');
    if (mainEl) {
        var yOffset = mainEl.getBoundingClientRect().top + window.scrollY - 100;
        window.scrollTo({ top: yOffset, behavior: 'smooth' });
    }

    setTimeout(function() {
        searchInput.focus();
        try { searchInput.setSelectionRange(0, searchInput.value.length); } catch(e) {}
    }, 300);

    var clearBtn = $('clearSearchBtn');
    if (clearBtn) clearBtn.classList.add('show');

    var label = type === 'topic' ? 'chủ điểm' : 'chủ đề';
    showTagToast('Đang lọc theo ' + label + ': "' + value + '"');
};

function showTagToast(message) {
    var old = document.getElementById('tagToast');
    if (old) old.remove();

    var toast = document.createElement('div');
    toast.id = 'tagToast';
    toast.textContent = message;
    toast.style.cssText = [
        'position:fixed','top:80px','left:50%',
        'transform:translateX(-50%) translateY(-20px)',
        'padding:.7rem 1.2rem',
        'background:linear-gradient(135deg,#4f46e5,#7c3aed)',
        'color:#fff','border-radius:50px',
        'font-size:.85rem','font-weight:700','font-family:inherit',
        'box-shadow:0 8px 24px rgba(124,58,237,.45)',
        'z-index:9999','opacity:0',
        'transition:opacity .25s ease, transform .3s cubic-bezier(.34,1.56,.64,1)',
        'pointer-events:none','max-width:90vw',
        'text-overflow:ellipsis','overflow:hidden','white-space:nowrap'
    ].join(';');

    document.body.appendChild(toast);

    requestAnimationFrame(function() {
        toast.style.opacity = '1';
        toast.style.transform = 'translateX(-50%) translateY(0)';
    });

    setTimeout(function() {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(-50%) translateY(-20px)';
        setTimeout(function() { if (toast.parentNode) toast.remove(); }, 300);
    }, 2000);
}

/* ═══════════════════════════════════════════════════════════ */
/* ONBOARDING - CHỌN CHỦ ĐỀ QUAN TÂM                             */
/* EXPIRED dùng config giống DEMO                                */
/* ═══════════════════════════════════════════════════════════ */
var _onboardingSelected = {};
var _onboardingConfig = null;

function getOnboardingConfig() {
    if (typeof ONBOARDING_CONFIG === 'undefined' || !ONBOARDING_CONFIG) return null;

    var info = getTierInfo();
    var tier = info.tier;
    // ⭐ Bỏ onboarding cho active + admin
    if (tier === 'active') return null;
    if (typeof currentUser !== 'undefined' && currentUser && currentUser.role === 'admin') return null;

    var configKey = tier;
    if (tier === 'expired') configKey = 'demo';

    if (configKey !== 'demo' && configKey !== 'trial' && configKey !== 'active') return null;

    var cfg = ONBOARDING_CONFIG[configKey];
    if (!cfg) return null;
    if (cfg.enabled === false) return null;

    if (typeof cfg.topics_per_user !== 'number') cfg.topics_per_user = -1;
    if (typeof cfg.max_questions   !== 'number') cfg.max_questions   = -1;
    if (!Array.isArray(cfg.hsk_allowed) || cfg.hsk_allowed.length === 0) {
        cfg.hsk_allowed = [1, 2, 3, 4, 5, 6];
    }

    return cfg;
}

function getOnboardingStorageKey() {
    var info = getTierInfo();
    if (info.tier === 'demo') return 'onboarding_demo';
    if (info.tier === 'trial' && info.email)  return 'onboarding_trial_' + info.email;
    if (info.tier === 'active' && info.email) return 'onboarding_active_' + info.email;
    if (info.tier === 'active') return 'onboarding_active_guest';
    if (info.tier === 'expired' && info.email) return 'onboarding_expired_' + info.email;
    if (info.tier === 'expired') return 'onboarding_expired_guest';
    return null;
}

function getAvailableTopicsForTier() {
    var info = getTierInfo();
    var allowedHsk = getAllowedHskList();

    var subjectMap = {};
    RAW_DATA.forEach(function(r) {
        // ⭐ DÙNG normalizeHsk
        if (info.tier !== 'active' && allowedHsk.indexOf(normalizeHsk(r.hsk)) === -1) return;
        var s = (r.subject || '').trim();
        if (!s) return;
        subjectMap[s] = (subjectMap[s] || 0) + 1;
    });

    var list = Object.keys(subjectMap).map(function(name) {
        return { name: name, count: subjectMap[name] };
    });
    list.sort(function(a, b) { return b.count - a.count; });
    return list;
}

function loadOnboardingSelection() {
    var key = getOnboardingStorageKey();
    if (!key) return null;
    try {
        var saved = JSON.parse(localStorage.getItem(key) || 'null');
        if (saved && Array.isArray(saved.topics) && saved.topics.length > 0) {
            return saved;
        }
    } catch(e) {}
    return null;
}
function saveOnboardingSelection(topics, autoPicked) {
    var key = getOnboardingStorageKey();
    if (!key) return;
    try {
        localStorage.setItem(key, JSON.stringify({
            topics: topics,
            auto_picked: !!autoPicked,
            savedAt: Date.now()
        }));
    } catch(e) {}
}

/* ═══════════════════════════════════════════════════════════ */
/* SỬA: MAYBE SHOW ONBOARDING — LUÔN VẼ BANNER NẾU CÓ SELECTION */
/* ═══════════════════════════════════════════════════════════ */
function maybeShowOnboarding() {
    /* ⭐ KHÔNG TỰ ĐỘNG HIỆN MODAL LÚC KHỞI ĐỘNG
       - Lần đầu vào → tự động chọn TẤT CẢ chủ đề có thể
       - User bấm nút "Đổi" → mới mở modal (giữ nguyên logic onChangeTopicsClick)
    */
    var info = getTierInfo();

    /* Bỏ qua cho active + admin */
    if (info.tier === 'active') return;
    if (typeof currentUser !== 'undefined' && currentUser && currentUser.role === 'admin') return;

    /* Chỉ demo / trial / expired */
    if (info.tier !== 'demo' && info.tier !== 'trial' && info.tier !== 'expired') return;

    if (typeof RAW_DATA === 'undefined' || !RAW_DATA || RAW_DATA.length === 0) {
        setTimeout(maybeShowOnboarding, 300);
        return;
    }

    var mainContent = $('mainContent');
    if (!mainContent || mainContent.style.display === 'none') {
        setTimeout(maybeShowOnboarding, 300);
        return;
    }

    /* ⭐ Nếu đã có override → chỉ apply filter (không hiện modal) */
    if (window.__onboardingOverride
        && Array.isArray(window.__onboardingOverride)
        && window.__onboardingOverride.length > 0) {
        if (typeof applyFilter === 'function') applyFilter();
        if (typeof updateResultCount === 'function') updateResultCount();
        return;
    }

    /* ⭐ Có selection cũ → apply + KHÔNG hiện modal */
    var saved = loadOnboardingSelection();
    if (saved && Array.isArray(saved.topics) && saved.topics.length > 0) {
        window.__onboardingAutoPicked = !!saved.auto_picked;
        if (typeof applyOnboardingSelection === 'function') {
            applyOnboardingSelection(saved.topics, false);
        }
        if (typeof applyFilter === 'function') applyFilter();
        if (typeof updateResultCount === 'function') updateResultCount();
        return;
    }

    /* ⭐ LẦN ĐẦU VÀO: tự động chọn TẤT CẢ chủ đề — KHÔNG hiện modal */
    var allTopics = getAvailableTopicsForTier();
    if (allTopics.length === 0) return;

    var pickedTopics = allTopics.map(function(t) { return t.name; });

    window.__onboardingAutoPicked = true;
    saveOnboardingSelection(pickedTopics, true);

    if (typeof applyOnboardingSelection === 'function') {
        applyOnboardingSelection(pickedTopics, false);
    }
    if (typeof applyFilter === 'function') applyFilter();
    if (typeof updateResultCount === 'function') updateResultCount();
}
function showOnboardingModal() {
    var cfg = getOnboardingConfig();
    if (!cfg) return;

    _onboardingConfig = cfg;

    var saved = loadOnboardingSelection();
    if (saved && Array.isArray(saved.topics)) {
        _onboardingSelected = {};
        saved.topics.forEach(function(t) { _onboardingSelected[t] = true; });
    } else {
        _onboardingSelected = {};
    }

    var titleEl = $('onboardingTitle');
    var subtitleEl = $('onboardingSubtitle');
    if (titleEl) titleEl.textContent = cfg.title || 'Bạn quan tâm chủ đề nào?';
    if (subtitleEl) subtitleEl.textContent = cfg.subtitle || '';

    renderOnboardingTopics();
    updateOnboardingUI();

    var modal = $('onboardingModal');
    if (modal) modal.classList.add('show');
}

function renderOnboardingTopics() {
    var container = $('onboardingTopics');
    if (!container) return;

    var topics = getAvailableTopicsForTier();
    if (topics.length === 0) {
        container.innerHTML = '<div class="onboarding-empty">' +
            '<i class="fas fa-inbox"></i> Chưa có chủ đề nào trong kho</div>';
        return;
    }

    var cfg = getOnboardingConfig();
    var isUnlimited = !cfg || cfg.max_questions === -1 || cfg.max_questions === Infinity;
    var maxQ = (cfg && cfg.max_questions > 0) ? cfg.max_questions : getTierInfo().maxQuestions;

    var allowedHsk;
    if (cfg && cfg.hsk_allowed && cfg.hsk_allowed.length > 0) {
        allowedHsk = cfg.hsk_allowed.map(function(n) { return 'HSK' + n; });
    } else {
        allowedHsk = getAllowedHskList();
    }

    // ⭐ Mở 50% số chủ đề (hardcode 0.5)
    var UNLOCK_RATIO = 0.5;

    var allTopicsFirstStt = {};
    RAW_DATA.forEach(function(r) {
        // ⭐ DÙNG normalizeHsk
        if (allowedHsk.indexOf(normalizeHsk(r.hsk)) === -1) return;
        var s = (r.subject || '').trim();
        if (!s) return;
        var stt = parseInt(r.stt);
        if (isNaN(stt)) stt = 999999;
        if (allTopicsFirstStt[s] === undefined || stt < allTopicsFirstStt[s]) {
            allTopicsFirstStt[s] = stt;
        }
    });
    var allTopicsList = Object.keys(allTopicsFirstStt);
    var unlockedCount = Math.floor(allTopicsList.length * UNLOCK_RATIO);
    if (unlockedCount < 1 && allTopicsList.length > 0) unlockedCount = 1;

    var sortedAllTopics = allTopicsList.slice().sort(function(a, b) {
        return (allTopicsFirstStt[a] || 0) - (allTopicsFirstStt[b] || 0);
    });
    var unlockedTopics = sortedAllTopics.slice(0, unlockedCount);

    var maxPerTopic = isUnlimited ? Infinity :
                      Math.max(1, Math.ceil(maxQ / Math.max(1, unlockedCount)));

    container.innerHTML = '';
    topics.forEach(function(t) {
        var isUnlocked = isUnlimited || (unlockedTopics.indexOf(t.name) !== -1);
        var lockedInTopic = 0;
        if (isUnlocked && !isUnlimited && t.count > maxPerTopic) {
            lockedInTopic = t.count - maxPerTopic;
        }

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'onboarding-topic' + (_onboardingSelected[t.name] ? ' selected' : '');
        btn.dataset.topic = t.name;

        if (!isUnlocked) {
            btn.classList.add('disabled');
            btn.disabled = true;
            btn.title = t.name + '\n🔒 Chủ đề này bị khoá\n(Không nằm trong ' +
                        unlockedCount + '/' + allTopicsList.length + ' chủ đề được mở)';

            var nameSpan = document.createElement('span');
            nameSpan.textContent = t.name.normalize ? t.name.normalize('NFC') : t.name;
            btn.appendChild(nameSpan);

            var lockCountSpan = document.createElement('span');
            lockCountSpan.className = 'count';
            lockCountSpan.innerHTML = '<i class="fas fa-lock" style="font-size:.7em"></i>';
            btn.appendChild(lockCountSpan);
        } else {
            btn.title = t.name + '\nTổng: ' + t.count + ' câu' +
                        (lockedInTopic > 0
                            ? '\n🔒 Còn ' + lockedInTopic + ' câu bị khoá (chỉ lấy tối đa ' + maxPerTopic + ' câu)'
                            : '');

            var nameSpan2 = document.createElement('span');
            nameSpan2.textContent = t.name.normalize ? t.name.normalize('NFC') : t.name;
            btn.appendChild(nameSpan2);

            var countSpan = document.createElement('span');
            countSpan.className = 'count';
            countSpan.textContent = t.count;
            btn.appendChild(countSpan);

            if (lockedInTopic > 0) {
                var lockSpan = document.createElement('span');
                lockSpan.className = 'topic-lock';
                lockSpan.innerHTML = '<i class="fas fa-lock"></i>' + lockedInTopic;
                btn.appendChild(lockSpan);
            }

            btn.addEventListener('click', function() {
                onToggleOnboardingTopic(this.dataset.topic);
            });
        }

        container.appendChild(btn);
    });
}
function onToggleOnboardingTopic(topicName) {
    if (!_onboardingConfig) return;
    var max = _onboardingConfig.topics_per_user;
    var isUnlimited = (max === -1 || max === Infinity);

    if (_onboardingSelected[topicName]) {
        delete _onboardingSelected[topicName];
    } else {
        var currentCount = Object.keys(_onboardingSelected).length;
        if (!isUnlimited && currentCount >= max) {
            showTagToast('Chỉ được chọn tối đa ' + max + ' chủ đề');
            return;
        }
        _onboardingSelected[topicName] = true;
    }

    var btn = null;
    document.querySelectorAll('.onboarding-topic').forEach(function(b) {
        if (b.dataset.topic === topicName) btn = b;
    });
    if (btn) btn.classList.toggle('selected', !!_onboardingSelected[topicName]);
    updateOnboardingUI();
}

function updateOnboardingUI() {
    if (!_onboardingConfig) return;
    var selected = Object.keys(_onboardingSelected).length;
    var max = _onboardingConfig.topics_per_user;
    var isUnlimited = (max === -1 || max === Infinity);

    var countEl = $('onboardingSelectedCount');
    if (countEl) countEl.textContent = selected;

    var counter = $('onboardingCounter');
    if (counter) {
        counter.classList.remove('ok', 'full');
        if (selected > 0) counter.classList.add('ok');
        if (!isUnlimited && selected >= max) counter.classList.add('full');

        var labelSpan = counter.querySelector('span');
        if (labelSpan) {
            if (isUnlimited) {
                labelSpan.innerHTML = 'Đã chọn <b id="onboardingSelectedCount">'
                    + selected + '</b> chủ đề (không giới hạn)';
            } else {
                labelSpan.innerHTML = 'Đã chọn <b id="onboardingSelectedCount">'
                    + selected + '</b> / <b id="onboardingMaxCount">'
                    + max + '</b>';
            }
        }
    }

    var startBtn = $('onboardingStartBtn');
    if (startBtn) startBtn.disabled = (selected === 0);
}

function onOnboardingStart() {
    var topics = Object.keys(_onboardingSelected);
    if (topics.length === 0) return;

    window.__onboardingAutoPicked = false;
    saveOnboardingSelection(topics, false);

    var modal = $('onboardingModal');
    if (modal) modal.classList.remove('show');

    applyOnboardingSelection(topics, true);
}

/* ═══════════════════════════════════════════════════════════ */
/* SỬA: ON ONBOARDING SKIP — GIỮ SELECTION CŨ NẾU CÓ            */
/* ═══════════════════════════════════════════════════════════ */
function onOnboardingSkip() {
    var modal = $('onboardingModal');
    if (modal) modal.classList.remove('show');

    var cfg = getOnboardingConfig();
    if (!cfg) return;

    var selectedCount = Object.keys(_onboardingSelected).length;

    // ═══════════════════════════════════════════════════════════
    // ĐÃ CHỌN → xóa hết chủ đề, banner hiện thông báo "chưa chọn"
    // CHƯA CHỌN → auto chọn (random cho demo/expired/trial, tất cả cho active/admin)
    // ═══════════════════════════════════════════════════════════
    if (selectedCount > 0) {
        // Đã chọn → xóa hết
        _onboardingSelected = {};
        window.__onboardingOverride = null;
        window.__onboardingAutoPicked = false;

        // Xóa selection đã lưu trong localStorage
        var key = getOnboardingStorageKey();
        if (key) {
            try {
                localStorage.setItem(key, JSON.stringify({
                    topics: [],
                    auto_picked: false,
                    savedAt: Date.now()
                }));
            } catch(e) {}
        }

        // Reload data đầy đủ theo tier (không bị giới hạn chủ đề nữa)
        state = { search:'', hsk:'', subject:'' };
        if ($('searchInput')) $('searchInput').value = '';
        if ($('hskFilter')) $('hskFilter').value = '';
        if ($('subjectFilter')) $('subjectFilter').value = '';
        if ($('clearSearchBtn')) $('clearSearchBtn').classList.remove('show');

        filtered = getLimitedData();
        renderedCount = 0;
        render(true);
        updateResultCount();

        // ⬇️ VẼ BANNER TRỐNG thay vì xóa banner
        showEmptyOnboardingBanner();

        showTagToast('Đã bỏ chọn tất cả chủ đề');
        return;
    }

    // Chưa chọn gì → auto chọn như cũ
    var allTopics = getAvailableTopicsForTier();
    if (allTopics.length === 0) return;

    var info = getTierInfo();
    var isLimitedTier = (info.tier === 'demo'
                      || info.tier === 'expired'
                      || info.tier === 'trial');

    var pickedTopics;
    var isUnlimited;

    if (isLimitedTier) {
        var max = (cfg.topics_per_user > 0) ? cfg.topics_per_user : 3;
        var pickCount = Math.min(max, allTopics.length);

        var shuffled = allTopics.slice();
        for (var i = shuffled.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var t = shuffled[i]; shuffled[i] = shuffled[j]; shuffled[j] = t;
        }
        pickedTopics = shuffled.slice(0, pickCount).map(function(t) { return t.name; });
        isUnlimited = false;
    } else {
        pickedTopics = allTopics.map(function(t) { return t.name; });
        isUnlimited = true;
    }

    window.__onboardingAutoPicked = true;
    saveOnboardingSelection(pickedTopics, true);
    applyOnboardingSelection(pickedTopics, true);

    if (isUnlimited) {
        showTagToast('Đã chọn tất cả ' + pickedTopics.length + ' chủ đề');
    } else {
        showTagToast('Đã gợi ý ' + pickedTopics.length + ' chủ đề phù hợp cho bạn');
    }
}
function showEmptyOnboardingBanner() {
    var old = $('onboardingActiveBanner');
    if (old) old.remove();

    var mainContent = $('mainContent');
    if (!mainContent) return;
    var container = mainContent.querySelector('.container');
    if (!container) return;
    if (mainContent.style.display === 'none') return;

    var banner = document.createElement('div');
    banner.id = 'onboardingActiveBanner';
    banner.className = 'onboarding-active-banner';

    var iconSpan = document.createElement('span');
    iconSpan.className = 'ob-icon';
    iconSpan.innerHTML = '<i class="fas fa-circle-info"></i>';
    banner.appendChild(iconSpan);

    var labelSpan = document.createElement('span');
    labelSpan.className = 'ob-label';
    labelSpan.textContent = 'Bạn chưa chọn chủ đề nào';
    banner.appendChild(labelSpan);

    var chipsWrap = document.createElement('span');
    chipsWrap.className = 'ob-chips';
    var hint = document.createElement('span');
    hint.className = 'ob-chip';
    hint.style.background = 'linear-gradient(135deg, #94a3b8, #64748b)';
    hint.textContent = 'Chọn chủ đề để được gợi ý câu phù hợp';
    chipsWrap.appendChild(hint);
    banner.appendChild(chipsWrap);

    var changeBtn = document.createElement('button');
    changeBtn.type = 'button';
    changeBtn.className = 'ob-change-btn';
    changeBtn.innerHTML = '<i class="fas fa-plus"></i> Chọn chủ đề';
    changeBtn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        // Xóa key để mở modal ở trạng thái "chưa chọn"
        var key = getOnboardingStorageKey();
        if (key) { try { localStorage.removeItem(key); } catch(e) {} }
        onChangeTopicsClick();
    });
    banner.appendChild(changeBtn);

    container.insertBefore(banner, container.firstChild);
}
/* ═══════════════════════════════════════════════════════════ */
/* SỬA: APPLY ONBOARDING SELECTION — GIỚI HẠN MỖI CHỦ ĐỀ       */
/* ═══════════════════════════════════════════════════════════ */
function applyOnboardingSelection(topics, scrollTop) {
    var cfg = getOnboardingConfig();
    if (!cfg) return;

    var maxQ = cfg.max_questions;
    var isUnlimitedQ = (maxQ === -1 || maxQ === Infinity);

    var allowedHsk;
    if (cfg.hsk_allowed && Array.isArray(cfg.hsk_allowed) && cfg.hsk_allowed.length > 0) {
        allowedHsk = cfg.hsk_allowed.map(function(n) { return 'HSK' + n; });
    } else {
        allowedHsk = getAllowedHskList();
    }

    // ⭐ Mở 50% số chủ đề (hardcode 0.5)
    var UNLOCK_RATIO = 0.5;

    // ⭐ Bước 1: Lấy TẤT CẢ chủ đề (theo HSK config) — DÙNG normalizeHsk
    var allTopicsFirstStt = {};
    RAW_DATA.forEach(function(r) {
        if (allowedHsk.indexOf(normalizeHsk(r.hsk)) === -1) return;   // ⭐
        var s = (r.subject || '').trim();
        if (!s) return;
        var stt = parseInt(r.stt);
        if (isNaN(stt)) stt = 999999;
        if (allTopicsFirstStt[s] === undefined || stt < allTopicsFirstStt[s]) {
            allTopicsFirstStt[s] = stt;
        }
    });
    var allTopicsList = Object.keys(allTopicsFirstStt);
    var totalTopicsCount = allTopicsList.length;

    // ⭐ Bước 2: Mở floor(N × 0.5) chủ đề (theo STT nhỏ nhất)
    var unlockedCount = Math.floor(totalTopicsCount * UNLOCK_RATIO);
    if (unlockedCount < 1 && totalTopicsCount > 0) unlockedCount = 1;

    var sortedAllTopics = allTopicsList.slice().sort(function(a, b) {
        return (allTopicsFirstStt[a] || 0) - (allTopicsFirstStt[b] || 0);
    });
    var unlockedTopics = sortedAllTopics.slice(0, unlockedCount);

    // ⭐ Bước 3: Lọc pool — DÙNG normalizeHsk
    var pool = RAW_DATA.filter(function(r) {
        if (allowedHsk.indexOf(normalizeHsk(r.hsk)) === -1) return false;   // ⭐
        var s = (r.subject || '').trim();
        if (topics.indexOf(s) === -1) return false;
        if (unlockedTopics.indexOf(s) === -1) return false;
        return true;
    });

    pool.sort(function(a, b) {
        return (parseInt(a.stt) || 0) - (parseInt(b.stt) || 0);
    });

    var final = [];
    if (isUnlimitedQ) {
        final = pool.slice();
    } else {
        var maxPerTopic = Math.max(1, Math.ceil(maxQ / Math.max(1, unlockedCount)));
        var perHsk = Math.ceil(maxQ / allowedHsk.length);

        var topicCount = {};
        var hskCount = {};
        allowedHsk.forEach(function(h) { hskCount[h] = 0; });

        for (var i = 0; i < pool.length && final.length < maxQ; i++) {
            var r = pool[i];
            var s = (r.subject || '').trim() || '__no_subject__';
            if ((topicCount[s] || 0) >= maxPerTopic) continue;

            var rHskNorm = normalizeHsk(r.hsk);   // ⭐
            if (rHskNorm && hskCount[rHskNorm] !== undefined && hskCount[rHskNorm] >= perHsk) continue;

            final.push(r);
            topicCount[s] = (topicCount[s] || 0) + 1;
            if (rHskNorm && hskCount[rHskNorm] !== undefined) hskCount[rHskNorm]++;
        }

        if (final.length < maxQ) {
            var usedIds = {};
            final.forEach(function(r) { usedIds[r.stt] = true; });
            for (var p = 0; p < pool.length && final.length < maxQ; p++) {
                var rp = pool[p];
                if (usedIds[rp.stt]) continue;
                var sp = (rp.subject || '').trim() || '__no_subject__';
                if ((topicCount[sp] || 0) >= maxPerTopic) continue;
                final.push(rp);
                usedIds[rp.stt] = true;
                topicCount[sp] = (topicCount[sp] || 0) + 1;
            }
        }

        if (final.length > maxQ) final = final.slice(0, maxQ);
    }

    final.sort(function(a, b) {
        return (parseInt(a.stt) || 0) - (parseInt(b.stt) || 0);
    });

    window.__onboardingOverride = final;
    window.__unlockedTopics = unlockedTopics;

    if (typeof state !== 'undefined' && state) {
        state.search = '';
        state.hsk = '';
        state.subject = '';
    }
    try {
        var si = document.getElementById('searchInput');
        if (si) si.value = '';
        var cb = document.getElementById('clearSearchBtn');
        if (cb) cb.classList.remove('show');
    } catch(e) {}

    if (typeof applyFilter === 'function') applyFilter();
    if (typeof updateResultCount === 'function') updateResultCount();

    if (typeof showOnboardingActiveBanner === 'function') {
        showOnboardingActiveBanner(topics, final.length);
    }

    if (scrollTop) {
        setTimeout(function() {
            var mainEl = document.getElementById('mainContent');
            if (mainEl) {
                var yOffset = mainEl.getBoundingClientRect().top + window.scrollY - 100;
                window.scrollTo({ top: yOffset, behavior: 'smooth' });
            }
        }, 200);
    }
}
/* ═══════════════════════════════════════════════════════════ */
/* SỬA: ON CHANGE TOPICS CLICK — KHÔNG XÓA STORAGE NGAY         */
/* ═══════════════════════════════════════════════════════════ */
function onChangeTopicsClick() {
    var cfg = getOnboardingConfig();

    if (!cfg) {
        showTagToast('Không thể đổi chủ đề ở chế độ này');
        return;
    }

    // FIX: KHÔNG xóa localStorage + override ngay.
    // Chỉ mở modal; user bấm "Bắt đầu" / "Bỏ qua" thì mới ghi đè.
    // Nếu user đóng modal (X) mà không chọn → giữ nguyên selection cũ.

    _onboardingConfig = cfg;

    // Load lại selection hiện tại vào _onboardingSelected để hiển thị đúng
    _onboardingSelected = {};
    var saved = loadOnboardingSelection();
    if (saved && Array.isArray(saved.topics)) {
        saved.topics.forEach(function(t) { _onboardingSelected[t] = true; });
    }

    var modal = $('onboardingModal');
    if (modal) modal.classList.remove('show');

    var titleEl = $('onboardingTitle');
    var subtitleEl = $('onboardingSubtitle');
    if (titleEl) titleEl.textContent = cfg.title || 'Bạn quan tâm chủ đề nào?';
    if (subtitleEl) subtitleEl.textContent = cfg.subtitle || '';

    renderOnboardingTopics();
    updateOnboardingUI();

    if (modal) {
        void modal.offsetWidth;
        modal.classList.add('show');
    }
}

/* ═══════════════════════════════════════════════════════════ */
/* SỬA: BANNER — ĐẦY ĐỦ THỐNG KÊ KHOÁ (5 STATS)                 */
/* ═══════════════════════════════════════════════════════════ */
function showOnboardingActiveBanner(topics, count) {
    var old = $('onboardingActiveBanner');
    if (old) old.remove();

    var mainContent = $('mainContent');
    if (!mainContent) return;
    var container = mainContent.querySelector('.container');
    if (!container) return;

    // FIX: Nếu mainContent đang ẩn (chưa init xong), thoát.
    if (mainContent.style.display === 'none') return;

    var info = getTierInfo();
    var totalAvailable = RAW_DATA.length;

    var cfg = getOnboardingConfig();
    var isUnlimitedTier = (info.tier === 'active')
                       || (cfg && (cfg.max_questions === -1 || cfg.max_questions === Infinity));

    var lockedCount = isUnlimitedTier ? 0 : Math.max(0, totalAvailable - count);
    var isLimited = (info.tier !== 'active');

    var lockedIndustryCount = 0;
    if (typeof DATASET_REGISTRY !== 'undefined' && DATASET_REGISTRY) {
        Object.keys(DATASET_REGISTRY).forEach(function(id) {
            if (id === 'tonghop') return;
            if (!canAccessChuyenNganh()) lockedIndustryCount++;
        });
    }

    var allowedHskForStats;
    if (cfg && cfg.hsk_allowed && Array.isArray(cfg.hsk_allowed) && cfg.hsk_allowed.length > 0) {
        allowedHskForStats = cfg.hsk_allowed.map(function(n) { return 'HSK' + n; });
    } else {
        allowedHskForStats = getAllowedHskList();
    }
    var maxQForStats = (cfg && cfg.max_questions > 0) ? cfg.max_questions : info.maxQuestions;
    var lockStats = computeLockStats(topics, allowedHskForStats, maxQForStats, isUnlimitedTier);

    var banner = document.createElement('div');
    banner.id = 'onboardingActiveBanner';
    banner.className = 'onboarding-active-banner';

    var isAuto = !!window.__onboardingAutoPicked;
    var iconHtml = isAuto ? '<i class="fas fa-magic"></i>' : '<i class="fas fa-star"></i>';
    var labelText = isAuto ? 'Chủ đề gợi ý cho bạn:' : 'Chủ đề của bạn:';

    var iconSpan = document.createElement('span');
    iconSpan.className = 'ob-icon';
    iconSpan.innerHTML = iconHtml;
    banner.appendChild(iconSpan);

    var labelSpan = document.createElement('span');
    labelSpan.className = 'ob-label';
    labelSpan.textContent = labelText;
    banner.appendChild(labelSpan);

    var MAX_VISIBLE_CHIPS = 5;
    var visibleTopics = topics.slice(0, MAX_VISIBLE_CHIPS);
    var hiddenCount = Math.max(0, topics.length - MAX_VISIBLE_CHIPS);

    var chipsWrap = document.createElement('span');
    chipsWrap.className = 'ob-chips';

    visibleTopics.forEach(function(t) {
        var chip = document.createElement('span');
        chip.className = 'ob-chip';
        chip.textContent = t.normalize ? t.normalize('NFC') : t;
        chipsWrap.appendChild(chip);
    });

    if (hiddenCount > 0) {
        var moreChip = document.createElement('span');
        moreChip.className = 'ob-chip ob-chip-more';
        moreChip.textContent = '+' + hiddenCount + ' chủ đề khác';
        moreChip.title = topics.join(' · ');
        moreChip.setAttribute('data-tooltip', topics.join(' · '));
        moreChip.style.cursor = 'help';
        chipsWrap.appendChild(moreChip);
    }

    banner.appendChild(chipsWrap);

    var countSpan = document.createElement('span');
    countSpan.className = 'ob-count';
    if (isUnlimitedTier) {
        countSpan.textContent = '(toàn bộ ' + count + ' câu)';
    } else {
        countSpan.textContent = '(' + count + ' câu)';
    }
    banner.appendChild(countSpan);

    var changeBtn = document.createElement('button');
    changeBtn.type = 'button';
    changeBtn.id = 'onboardingChangeBtn';
    changeBtn.className = 'ob-change-btn';
    changeBtn.innerHTML = '<i class="fas fa-sync-alt"></i> Đổi';
    changeBtn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        onChangeTopicsClick();
    });
    banner.appendChild(changeBtn);

    if (isLimited) {
        var statsBar = document.createElement('div');
        statsBar.className = 'ob-stats-bar ob-stats-inline';

        /* STAT 1: Số câu đang có / tổng */
        if (lockedCount > 0) {
            var stat1 = document.createElement('span');
            stat1.className = 'ob-stat-inline';
            stat1.innerHTML =
                '<i class="fas fa-database"></i>' +
                '<b>' + count + '</b>/' + totalAvailable + ' câu';
            statsBar.appendChild(stat1);
        }

        /* STAT 2: Số chủ đề chưa mở khoá */
        if (lockStats.lockedTopics > 0) {
            var stat2 = document.createElement('span');
            stat2.className = 'ob-stat-inline ob-stat-inline-topics';
            stat2.innerHTML =
                '<i class="fas fa-folder-minus"></i>' +
                '<b>' + lockStats.lockedTopics + '</b> chủ đề khoá';
            statsBar.appendChild(stat2);
        }

        /* STAT 3: Số chuyên ngành chưa mở */
        if (lockedIndustryCount > 0) {
            var stat3 = document.createElement('span');
            stat3.className = 'ob-stat-inline ob-stat-inline-industry';
            stat3.innerHTML =
                '<i class="fas fa-industry"></i>' +
                '<b>' + lockedIndustryCount + '</b> chuyên ngành khoá';
            statsBar.appendChild(stat3);
        }

        /* CTA */
        var shouldShowCta = false;
        var ctaLabel = '';
        var ctaIcon = '';
        var ctaAction = null;

        if (info.tier === 'trial') {
            var expiryEl = $('expiryBanner');
            var expiryVisible = false;
            if (expiryEl) {
                var displayStyle = window.getComputedStyle(expiryEl).display;
                expiryVisible = (expiryEl.style.display !== 'none' && displayStyle !== 'none');
            }
            if (!expiryVisible) {
                shouldShowCta = true;
                ctaLabel = 'Nâng cấp';
                ctaIcon = 'fas fa-gem';
                ctaAction = function() {
                    if (typeof openRenewalModal === 'function') openRenewalModal();
                };
            }
        }

        var hasAnyLock = (lockedCount > 0) || (lockedIndustryCount > 0) || (lockStats.lockedTopics > 0);

        if (hasAnyLock && shouldShowCta) {
            var ctaBtn = document.createElement('button');
            ctaBtn.type = 'button';
            ctaBtn.className = 'ob-cta-btn';
            ctaBtn.innerHTML = '<i class="' + ctaIcon + '"></i> ' + ctaLabel;
            ctaBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                if (typeof ctaAction === 'function') ctaAction();
            });
            statsBar.appendChild(ctaBtn);
        }

        if (statsBar.children.length > 0) {
            banner.appendChild(statsBar);
        }
    }

    container.insertBefore(banner, container.firstChild);
}

function initOnboarding() {
    var startBtn = $('onboardingStartBtn');
    var skipBtn = $('onboardingSkipBtn');
    var closeBtn = $('onboardingCloseBtn');

    if (startBtn) startBtn.addEventListener('click', onOnboardingStart);
    if (skipBtn)  skipBtn.addEventListener('click', onOnboardingSkip);

    if (closeBtn) {
        closeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            onOnboardingSkip();
        });
    }

    document.addEventListener('keydown', function(e) {
        if (e.key !== 'Escape') return;
        var modal = $('onboardingModal');
        if (modal && modal.classList.contains('show')) {
            onOnboardingSkip();
        }
    });

    var modal = $('onboardingModal');
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                onOnboardingSkip();
            }
        });
    }

    setTimeout(maybeShowOnboarding, 500);
}

window.maybeShowOnboarding = maybeShowOnboarding;
window.showOnboardingModal = showOnboardingModal;
window.applyOnboardingSelection = applyOnboardingSelection;
window.onChangeTopicsClick = onChangeTopicsClick;

/* ============================================================ */
/* TIKTOK BAR RESPONSIVE                                         */
/* ============================================================ */
function moveTikTokBarToHeader() {
    try {
        if (window.innerWidth < 769) return;
        var headerInner = document.querySelector('.header-inner');
        var headerActions = document.querySelector('.header-actions');
        var tiktokBar = document.querySelector('.sticky-top .container > .tiktok-bar');
        if (!headerInner || !headerActions || !tiktokBar) return;
        headerInner.insertBefore(tiktokBar, headerActions);
        setTimeout(function() { checkHeaderOverflow(); }, 100);
    } catch(e) {}
}

function moveTikTokBarBelowHeader() {
    try {
        var headerInner = document.querySelector('.header-inner');
        var tiktokBar = headerInner ? headerInner.querySelector('.tiktok-bar') : null;
        var container = document.querySelector('.sticky-top .container');
        var header = container ? container.querySelector('.header') : null;
        if (!tiktokBar || !container || !header) return;
        if (header.nextSibling) {
            container.insertBefore(tiktokBar, header.nextSibling);
        } else {
            container.appendChild(tiktokBar);
        }
    } catch(e) {}
}

function checkHeaderOverflow() {
    try {
        if (window.innerWidth < 769) return;
        var headerInner = document.querySelector('.header-inner');
        if (!headerInner) return;
        var tiktok = headerInner.querySelector('.tiktok-bar');
        if (!tiktok) return;
        tiktok.style.display = '';
    } catch(e) {}
}

var _lastWidthMode = null;
function handleResponsiveTikTok() {
    var currentMode = window.innerWidth >= 769 ? 'desktop' : 'mobile';
    if (currentMode === _lastWidthMode) return;
    _lastWidthMode = currentMode;
    if (currentMode === 'desktop') moveTikTokBarToHeader();
    else moveTikTokBarBelowHeader();
}

function populateTikTokFloat() {
    try {
        var pfTiktok = $('pfTiktokFloat');
        if (!pfTiktok) return;
        var tiktokUrl = (typeof TIKTOK_URL !== 'undefined' && TIKTOK_URL) ? TIKTOK_URL : '';
        if (!tiktokUrl) { pfTiktok.style.display = 'none'; return; }
        pfTiktok.href = tiktokUrl;
        var avatarUrl = (typeof TIKTOK_AVATAR !== 'undefined' && TIKTOK_AVATAR) ? TIKTOK_AVATAR : '';
        var avatarEl = $('pfTiktokAvatar');
        if (avatarEl) {
            if (avatarUrl) { avatarEl.src = avatarUrl; avatarEl.style.display = ''; }
            else { avatarEl.style.display = 'none'; }
        }
        var displayName = '';
        if (typeof TIKTOK_NICKNAME !== 'undefined' && TIKTOK_NICKNAME) displayName = TIKTOK_NICKNAME;
        else if (typeof TIKTOK_USERNAME !== 'undefined' && TIKTOK_USERNAME) displayName = TIKTOK_USERNAME;
        else displayName = 'TikTok';
        var nameEl = $('pfTiktokName');
        if (nameEl) nameEl.textContent = displayName;
        pfTiktok.title = 'Theo dõi TikTok: ' + displayName;
    } catch(e) {}
}
/* ═══════════════════════════════════════════════════════════ */
/* KHÓA Ô SEARCH KHI CHƯA ĐĂNG NHẬP (DEMO)                     */
/* Bao gồm: ô search chính + ô search trong practice full      */
/*          + nút toggle search nổi (quick_search)             */
/* ═══════════════════════════════════════════════════════════ */
function initSearchLockDemo() {
    function isDemo() {
        try {
            var info = getTierInfo();
            return info && info.tier === 'demo';
        } catch(e) {
            return false;
        }
    }

    function lockInput(inp) {
        if (!inp) return;
        if (inp.__searchLocked) return;
        inp.__searchLocked = true;

        inp.readOnly = true;
        inp.style.cursor = 'pointer';
        inp.style.background = 'linear-gradient(135deg,#fef3c7,#fde68a)';
        inp.style.borderColor = '#f59e0b';
        inp.style.color = '#92400e';
        inp.style.fontWeight = '600';
        inp.placeholder = 'Dang nhap de su dung tim kiem...';

        inp.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            if (typeof showLoginModal === 'function') showLoginModal();
            return false;
        }, true);
        inp.addEventListener('keydown', function(e) {
            e.preventDefault();
            e.stopPropagation();
            return false;
        }, true);
        inp.addEventListener('focus', function(e) {
            e.preventDefault();
            inp.blur();
            if (typeof showLoginModal === 'function') showLoginModal();
        }, true);
    }

    function unlockInput(inp) {
        if (!inp) return;
        if (!inp.__searchLocked) return;
        inp.__searchLocked = false;

        inp.readOnly = false;
        inp.style.cursor = '';
        inp.style.background = '';
        inp.style.borderColor = '';
        inp.style.color = '';
        inp.style.fontWeight = '';
        inp.placeholder = 'Tim kiem... (VD: hsk1 5)';
    }

    function lockQuickSearchToggle() {
        var root = document.getElementById('quickSearchRoot');
        if (!root) return;
        if (root.__searchLocked) return;
        root.__searchLocked = true;
        root.style.display = 'none';
    }

    function unlockQuickSearchToggle() {
        var root = document.getElementById('quickSearchRoot');
        if (!root) return;
        if (!root.__searchLocked) return;
        root.__searchLocked = false;
        root.style.display = '';
    }

    function applyLock() {
        var isD = isDemo();
        var si = document.getElementById('searchInput');
        var pfSi = document.getElementById('pfSearchInput');

        if (isD) {
            lockInput(si);
            lockInput(pfSi);
            lockQuickSearchToggle();
        } else {
            unlockInput(si);
            unlockInput(pfSi);
            unlockQuickSearchToggle();
        }
    }

    setTimeout(applyLock, 500);
    setInterval(applyLock, 2000);
}
/* ============================================================ */
/* INIT APP                                                      */
/* ============================================================ */
function initApp() {
    mobileWrapper = $('mobileWrapper');
    $('loadingScreen').classList.add('hidden');
    $('stickyTop').style.display = 'block';
    $('fabGroup').style.display = 'flex';
    $('mainContent').style.display = 'block';

    loadVoiceSettings();
    initDatasetSelector();

    if (typeof initSocial === 'function') initSocial();
    if (typeof updateFloatingLeftVisibility === 'function') updateFloatingLeftVisibility();
    if (typeof initAuthUI === 'function') initAuthUI();
    initScrollDetection();
    initFabGroup();
    initTheme();
    initDisplayState();
    initSpeech();
    initWriter();
    initPracticeFull();
    initVoiceSettings();
    initOnboarding();

    /* ❤️ Khởi tạo module Yêu thích */
    if (typeof initFavorites === 'function') initFavorites();

    /* ⭐ KHÓA Ô SEARCH KHI DEMO */
    initSearchLockDemo();

    _lastWidthMode = window.innerWidth >= 769 ? 'desktop' : 'mobile';
    if (_lastWidthMode === 'desktop') moveTikTokBarToHeader();
    populateTikTokFloat();

    var _resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(_resizeTimer);
        _resizeTimer = setTimeout(function() {
            handleResponsiveTikTok();
            checkHeaderOverflow();
        }, 200);
    });

    $('searchInput').addEventListener('input', applyFilter);
    $('resetBtn').addEventListener('click', function() {
        $('searchInput').value = '';
        $('hskFilter').value = '';
        $('subjectFilter').value = '';
        window.__onboardingOverride = null;

        /* ❤️ Nếu đang ở tab Yêu thích → về tổng hợp trước */
        if (typeof favState !== 'undefined' && favState.currentView) {
            favState.currentView = false;
            if (typeof switchDataset === 'function') switchDataset('tonghop');
            if (typeof markCurrentDatasetActive === 'function') markCurrentDatasetActive();
        }

        var obBanner = $('onboardingActiveBanner');
        if (obBanner) obBanner.remove();
        applyFilter();

        /* Khôi phục banner chủ đề sau khi reset filter */
        var saved = loadOnboardingSelection();
        if (saved && Array.isArray(saved.topics) && saved.topics.length > 0) {
            var cfg = getOnboardingConfig();
            if (cfg) {
                window.__onboardingAutoPicked = !!saved.auto_picked;
                applyOnboardingSelection(saved.topics, false);
            }
        }
    });
    $('clearSearchBtn').addEventListener('click', function() {
        $('searchInput').value = '';
        state.search = '';
        $('searchInput').focus();
        applyFilter();
        this.classList.remove('show');

        var saved = loadOnboardingSelection();
        if (saved && Array.isArray(saved.topics) && saved.topics.length > 0) {
            var cfg = getOnboardingConfig();
            if (cfg) {
                window.__onboardingAutoPicked = !!saved.auto_picked;
                applyOnboardingSelection(saved.topics, false);
            }
        }
    });
    $('hskFilter').addEventListener('change', function() {
        var val = this.value;
        var allowed = getAllowedHskList();
        if (val && allowed.indexOf(val) === -1) {
            var info = getTierInfo();
            var msg = info.tier === 'trial'
                ? 'Bản Trial chỉ cho phép lọc HSK1-' + info.maxHSK + '.'
                : 'Bản Demo chỉ cho phép lọc HSK1-' + info.maxHSK + '.';
            alert(msg);
            this.value = '';
            applyFilter();
            return;
        }
        applyFilter();
    });
    $('subjectFilter').addEventListener('change', function() {
        var val = this.value;
        var allowed = getAllowedSubjectList();
        if (val && allowed.indexOf(val) === -1) {
            var info = getTierInfo();
            var msg = info.tier === 'trial'
                ? 'Chủ đề này chưa có trong ' + info.maxQuestions + ' câu Trial.'
                : 'Chủ đề này chưa có trong ' + info.maxQuestions + ' câu Demo.';
            alert(msg);
            this.value = '';
            applyFilter();
            return;
        }
        applyFilter();
    });

    waitForData(function() {
        try { buildFilters(); applyFilter(); }
        catch(e) { console.error('Init error:', e); }
    });

    window.addEventListener('dataLoadError', function(e) {
        console.error('Data load error:', e.detail);
        mobileWrapper.innerHTML = '<div class="no-data">' +
            '<i class="fas fa-exclamation-triangle"></i>' +
            'Không tải được dữ liệu. Vui lòng thử lại sau.</div>';
    });
}
/* ═══════════════════════════════════════════════════════════ */
/* SỬA: REFRESH APP — VẼ LẠI BANNER SAU LOGIN/RELOAD            */
/* ═══════════════════════════════════════════════════════════ */
function refreshApp() {
    if (!window.__dataLoaded) {
        if (window.__dataLoadPromise) {
            window.__dataLoadPromise.then(function() { refreshApp(); });
        }
        return;
    }
    buildFilters();
    applyFilter();
    applyDisplayState();
    updateToggleButtons();
    updateResultCount();
    updateTierBadge();
    updateDemoBanner();

    /* ❤️ Cập nhật trạng thái Yêu thích khi tier đổi */
    if (typeof favUpdateLockState === 'function') favUpdateLockState();
    if (typeof favRefreshUI === 'function') favRefreshUI();

    /* FIX: Vẽ lại banner chủ đề nếu có selection */
    if (typeof maybeShowOnboarding === 'function') {
        setTimeout(maybeShowOnboarding, 0);
    }
}

function updateTierBadge() {
    var badge = $('trialBadge');
    if (!badge) return;
    var info = getTierInfo();
    if (info.tier === 'trial') {
        badge.classList.add('show');
        var daysLeft = null;
        if (typeof getDaysRemaining === 'function'
            && typeof currentUser !== 'undefined'
            && currentUser) {
            daysLeft = getDaysRemaining(currentUser);
        }
        var badgeText = $('trialBadgeText');
        if (badgeText) {
            if (daysLeft !== null && daysLeft > 0) {
                badgeText.textContent = 'Trial · ' + daysLeft + ' ngày';
            } else {
                badgeText.textContent = 'Trial';
            }
        }
    } else {
        badge.classList.remove('show');
    }
}

function updateDemoBanner() {
    var info = getTierInfo();
    var banner = $('demoBanner');
    if (!banner) return;

    /* ═══════════════════════════════════════════════════════════════
       ⭐ FIX: CHỈ HIỆN BANNER DEMO KHI USER CHƯA LOGIN (tier === 'demo')
       - tier 'demo'    → hiện banner vàng + nút "Đăng nhập"
       - tier 'expired' → ẩn (đã có banner Expiry riêng màu đỏ)
       - tier 'trial'   → ẩn
       - tier 'active'  → ẩn
       ═══════════════════════════════════════════════════════════════ */
    if (info.tier !== 'demo') {
        banner.style.display = 'none';
        return;
    }

    var titleEl = $('demoBannerTitle');
    var descEl  = $('demoBannerDesc');
    var btnEl   = $('demoBannerBtn');
    var btnText = $('demoBannerBtnText');
    var iconEl  = banner.querySelector('.demo-banner-icon');

    /* ⭐ Hiện banner */
    banner.style.display = 'flex';

    /* ═══════════════════════════════════════════════════════════════
       ⭐ DEMO (chưa login) → Nút "Đăng nhập bằng Gmail"
       ═══════════════════════════════════════════════════════════════ */
    if (titleEl) titleEl.innerHTML = 'Đăng nhập miễn phí để mở khóa toàn bộ';

    if (descEl) {
        descEl.innerHTML = 'Đăng nhập bằng <b>Gmail</b> để xem <b>toàn bộ kho câu</b>, ' +
            'không giới hạn nghe và luyện viết.<br>' +
            'Nghe + Luyện viết còn lại hôm nay: ' +
            '<b id="demoRemainingText" style="color:#16a34a">' + getDemoRemaining() + '</b> lượt.';
    }

    /* ⭐ XÓA HOÀN TOÀN attribute onclick cũ + gán property mới */
    if (btnEl) {
        btnEl.removeAttribute('onclick');
        btnEl.onclick = function(e) {
            if (e) { e.preventDefault(); e.stopPropagation(); }
            if (typeof showLoginModal === 'function') {
                showLoginModal();
            }
        };
    }

    if (btnText) btnText.textContent = 'Đăng nhập bằng Gmail';

    /* ⭐ Đổi icon trong nút thành icon đăng nhập */
    var btnIcon = btnEl ? btnEl.querySelector('i') : null;
    if (btnIcon) btnIcon.className = 'fas fa-sign-in-alt';

    /* ⭐ Icon tròn bên trái */
    if (iconEl) iconEl.innerHTML = '<i class="fas fa-gift"></i>';

    /* ⭐ Reset màu về mặc định (vàng) */
    banner.style.background = '';
    banner.style.borderColor = '';
}

    

/* ============================================================ */
/* SCROLL / FAB / THEME / DISPLAY                                */
/* ============================================================ */
function initScrollDetection() {
    var sticky = $('stickyTop');
    if (!sticky) return;
    var ticking = false;
    function update() {
        if (window.scrollY > 5) sticky.classList.add('scrolled');
        else sticky.classList.remove('scrolled');
        ticking = false;
    }
    window.addEventListener('scroll', function() {
        if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
}

function initFabGroup() {
    var fabGroup = $('fabGroup');
    var fabMainBtn = $('fabMainBtn');
    if (!fabGroup || !fabMainBtn) return;

    var closedFlag = null;
    try { closedFlag = sessionStorage.getItem('fabClosed'); } catch(_e) {}

    var fabOpen = (closedFlag !== '1');
    fabGroup.classList.toggle('open', fabOpen);

    fabMainBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        fabOpen = !fabOpen;
        fabGroup.classList.toggle('open', fabOpen);
        try { sessionStorage.setItem('fabClosed', fabOpen ? '0' : '1'); } catch(_e) {}
    });

    document.addEventListener('click', function(e) {
        if (!fabGroup.contains(e.target) && fabOpen && window.innerWidth > 768) {
            fabOpen = false;
            fabGroup.classList.remove('open');
            try { sessionStorage.setItem('fabClosed', '1'); } catch(_e) {}
        }
    });
}

function initTheme() {
    try {
        var saved = localStorage.getItem('theme');
        if (saved) document.documentElement.setAttribute('data-theme', saved);
        else document.documentElement.setAttribute('data-theme', 'light');
    } catch(e) {}
    updateThemeIcon();
    $('themeToggle').addEventListener('click', function() {
        var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        var newTheme = isDark ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
        try { localStorage.setItem('theme', newTheme); } catch(e) {}
        updateThemeIcon();
    });
}

function updateThemeIcon() {
    var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    var icon = $('themeToggle').querySelector('i');
    icon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
}

function initDisplayState() {
    try {
        var saved = localStorage.getItem('displayState');
        if (saved) {
            var parsed = JSON.parse(saved);
            displayState.vi = parsed.vi !== false;
            displayState.pinyin = !!parsed.pinyin;
            displayState.practice = !!parsed.practice;
        }
    } catch(e) {}
    var focusHidden = false;
    try { focusHidden = localStorage.getItem('focusHidden') === 'true'; } catch(e) {}
    if (focusHidden) document.body.classList.add('hide-floating');
    updateFocusBtnIcon();
    if (displayState.practice) { displayState.pinyin = false; displayState.vi = true; }
    applyDisplayState();
    updateToggleButtons();

    $('toggleViBtn').addEventListener('click', function(e) {
        e.stopPropagation();
        displayState.vi = !displayState.vi;
        applyDisplayState(); saveDisplayState(); updateToggleButtons();
    });
    $('togglePinyinBtn').addEventListener('click', function(e) {
        e.stopPropagation();
        displayState.pinyin = !displayState.pinyin;
        if (displayState.pinyin && displayState.practice) displayState.practice = false;
        applyDisplayState(); saveDisplayState(); updateToggleButtons();
    });
    $('togglePracticeBtn').addEventListener('click', function(e) {
        e.stopPropagation();
        displayState.practice = !displayState.practice;
        if (displayState.practice) { displayState.pinyin = false; displayState.vi = true; }
        applyDisplayState(); saveDisplayState(); updateToggleButtons();
    });
    var toggleFocusBtn = $('toggleFocusBtn');
    if (toggleFocusBtn) {
        toggleFocusBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            var isHidden = document.body.classList.toggle('hide-floating');
            try { localStorage.setItem('focusHidden', isHidden ? 'true' : 'false'); } catch(e) {}
            updateFocusBtnIcon();
        });
    }
}

function updateFocusBtnIcon() {
    var btn = $('toggleFocusBtn');
    if (!btn) return;
    var isHidden = document.body.classList.contains('hide-floating');
    var icon = btn.querySelector('i');
    if (isHidden) {
        icon.className = 'fas fa-bell-slash';
        btn.classList.remove('active');
    } else {
        icon.className = 'fas fa-bell';
        btn.classList.add('active');
    }
}

function applyDisplayState() {
    document.body.classList.toggle('show-vi', displayState.vi);
    document.body.classList.toggle('show-pinyin', displayState.pinyin);
    document.body.classList.toggle('show-practice', displayState.practice);
    if (displayState.practice) {
        document.querySelectorAll('.card-check').forEach(function(c) { c.innerHTML = ''; });
        document.querySelectorAll('.practice-input').forEach(function(i) {
            i.value = '';
            var answer = i.dataset.answer || '';
            updateInlinePreview(i, answer);
        });
    }
}

function saveDisplayState() {
    try { localStorage.setItem('displayState', JSON.stringify(displayState)); } catch(e) {}
}

function updateToggleButtons() {
    $('toggleViBtn').classList.toggle('active', displayState.vi);
    $('togglePinyinBtn').classList.toggle('active', displayState.pinyin);
    $('togglePracticeBtn').classList.toggle('active', displayState.practice);
    updateFocusBtnIcon();
}

window.toggleFocus = function(stt, element) {
    if (focusedStt === stt) { clearFocus(); return; }
    clearFocus();
    focusedStt = stt;
    element.classList.add('focused', 'tapped');
    setTimeout(function() { if (element) element.classList.remove('tapped'); }, 600);
};

window.clearFocus = function() {
    document.querySelectorAll('.focused').forEach(function(el) {
        el.classList.remove('focused', 'tapped');
    });
    focusedStt = null;
};

document.addEventListener('click', function(e) {
    if (e.target.closest('.card')) return;
    if (e.target.closest('.practice-input') || e.target.closest('.audio-btn') ||
        e.target.closest('.write-btn') || e.target.closest('.chip') ||
        e.target.closest('.fab-group') || e.target.closest('.icon-btn') ||
        e.target.closest('.search-bar') || e.target.closest('.filters') ||
        e.target.closest('.search-filter-row') ||
        e.target.closest('.writer-modal') || e.target.closest('.user-menu') ||
        e.target.closest('.login-modal') || e.target.closest('.admin-modal') ||
        e.target.closest('.practice-full-modal') || e.target.closest('.import-modal') ||
        e.target.closest('.edit-modal') || e.target.closest('.zalo-btn') ||
        e.target.closest('.tiktok-float-wrap') || e.target.closest('.tiktok-bar') ||
        e.target.closest('.renewal-modal') || e.target.closest('.voice-modal') ||
        e.target.closest('.dataset-selector') ||
        e.target.closest('.onboarding-modal') ||
        e.target.closest('.onboarding-active-banner') ||
        e.target.closest('.tag-clickable') ||
        e.target.closest('.toggle-check-btn')) return;
    clearFocus();
}, true);

/* ============================================================ */
/* SPEECH                                                        */
/* ============================================================ */
function initSpeech() {
    if ('speechSynthesis' in window) {
        speechSynthesis.getVoices();
        if (speechSynthesis.onvoiceschanged !== undefined) {
            speechSynthesis.onvoiceschanged = function(){
                populateVoiceSelect();
            };
        }
    }
}

window.speakText = function(text, btn, evt) {
    if (evt) evt.stopPropagation();
    if (!canUseFeature()) { showLimitMessage(); return; }
    if (!('speechSynthesis' in window)) { alert('Trình duyệt không hỗ trợ phát âm.'); return; }
    if (shouldCountUsage()) { incDemoUsage(); updateDemoRemaining(); }
    speechSynthesis.cancel();
    if (currentBtn) currentBtn.classList.remove('speaking');
    if (btn) { btn.classList.add('speaking'); currentBtn = btn; }
    var utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'zh-CN';
    applyVoiceSettings(utterance);
    utterance.onend = utterance.onerror = function() {
        if (currentBtn) { currentBtn.classList.remove('speaking'); currentBtn = null; }
    };
    setTimeout(function(){ speechSynthesis.speak(utterance); }, 50);
};

document.addEventListener('visibilitychange', function() {
    if (document.hidden && 'speechSynthesis' in window) {
        speechSynthesis.cancel();
        if (currentBtn) { currentBtn.classList.remove('speaking'); currentBtn = null; }
    }
});

function populateVoiceSelect() {
    if (!('speechSynthesis' in window)) return;
    var sel = $('voiceSelect');
    if (!sel) return;
    var voices = speechSynthesis.getVoices();
    var zhVoices = voices.filter(function(v) {
        return v.lang && v.lang.toLowerCase().indexOf('zh') === 0;
    });
    if (!zhVoices.length) {
        sel.innerHTML = '<option value="">-- Đang tải giọng đọc... --</option>';
        return;
    }
    sel.innerHTML = '';
    var defaultOpt = document.createElement('option');
    defaultOpt.value = '';
    defaultOpt.textContent = '-- Tự động (mặc định) --';
    sel.appendChild(defaultOpt);

    zhVoices.forEach(function(v) {
        var opt = document.createElement('option');
        opt.value = v.voiceURI;
        var label = v.name + ' (' + v.lang + ')' + (v.localService ? '' : ' - online');
        opt.textContent = label;
        sel.appendChild(opt);
    });
    sel.value = voiceState.voiceURI || '';
}

function updateVoiceUI() {
    var rateSlider = $('voiceRateSlider');
    var rateVal    = $('voiceRateValue');
    var pitchSlider = $('voicePitchSlider');
    var pitchVal   = $('voicePitchValue');
    var volSlider  = $('voiceVolumeSlider');
    var volVal     = $('voiceVolumeValue');
    if (rateSlider)  rateSlider.value  = voiceState.rate;
    if (rateVal)     rateVal.textContent = voiceState.rate.toFixed(2) + '×';
    if (pitchSlider) pitchSlider.value = voiceState.pitch;
    if (pitchVal)    pitchVal.textContent = voiceState.pitch.toFixed(2);
    if (volSlider)   volSlider.value   = voiceState.volume;
    if (volVal)      volVal.textContent = Math.round(voiceState.volume * 100) + '%';

    document.querySelectorAll('.voice-preset-btn').forEach(function(b) {
        var r = parseFloat(b.dataset.rate);
        b.classList.toggle('active', Math.abs(r - voiceState.rate) < 0.001);
    });
}

function voiceTestSpeak() {
    if (!('speechSynthesis' in window)) { alert('Trình duyệt không hỗ trợ phát âm.'); return; }
    speechSynthesis.cancel();
    var btn = $('voiceTestBtn');
    if (btn) {
        btn.classList.add('speaking');
        btn.innerHTML = '<i class="fas fa-stop"></i> Đang đọc...';
    }
    var u = new SpeechSynthesisUtterance('你好，欢迎学习中文。');
    u.lang = 'zh-CN';
    applyVoiceSettings(u);
    var finish = function() {
        if (btn) {
            btn.classList.remove('speaking');
            btn.innerHTML = '<i class="fas fa-play"></i> Nghe thử';
        }
    };
    u.onend = finish;
    u.onerror = finish;
    setTimeout(function(){ try { speechSynthesis.speak(u); } catch(e) { finish(); } }, 30);
}

function initVoiceSettings() {
    var modal = $('voiceModal');
    if (!modal) return;

    populateVoiceSelect();

    var rateSlider = $('voiceRateSlider');
    var pitchSlider = $('voicePitchSlider');
    var volSlider = $('voiceVolumeSlider');

    updateVoiceUI();

    if (rateSlider) rateSlider.addEventListener('input', function() {
        voiceState.rate = parseFloat(this.value);
        $('voiceRateValue').textContent = voiceState.rate.toFixed(2) + '×';
        document.querySelectorAll('.voice-preset-btn').forEach(function(b) {
            b.classList.toggle('active', Math.abs(parseFloat(b.dataset.rate) - voiceState.rate) < 0.001);
        });
        saveVoiceSettings();
    });
    if (pitchSlider) pitchSlider.addEventListener('input', function() {
        voiceState.pitch = parseFloat(this.value);
        $('voicePitchValue').textContent = voiceState.pitch.toFixed(2);
        saveVoiceSettings();
    });
    if (volSlider) volSlider.addEventListener('input', function() {
        voiceState.volume = parseFloat(this.value);
        $('voiceVolumeValue').textContent = Math.round(voiceState.volume * 100) + '%';
        saveVoiceSettings();
    });

    function adjust(key, delta, min, max) {
        voiceState[key] = Math.max(min, Math.min(max, +(voiceState[key] + delta).toFixed(2)));
        updateVoiceUI();
        saveVoiceSettings();
    }
    if ($('voiceRateMinus'))  $('voiceRateMinus').addEventListener('click',  function(){ adjust('rate',   -0.05, 0.5, 1.5); });
    if ($('voiceRatePlus'))   $('voiceRatePlus').addEventListener('click',   function(){ adjust('rate',    0.05, 0.5, 1.5); });
    if ($('voicePitchMinus')) $('voicePitchMinus').addEventListener('click', function(){ adjust('pitch',  -0.05, 0.5, 1.5); });
    if ($('voicePitchPlus'))  $('voicePitchPlus').addEventListener('click',  function(){ adjust('pitch',   0.05, 0.5, 1.5); });
    if ($('voiceVolumeMinus'))$('voiceVolumeMinus').addEventListener('click',function(){ adjust('volume', -0.05, 0, 1); });
    if ($('voiceVolumePlus')) $('voiceVolumePlus').addEventListener('click', function(){ adjust('volume',  0.05, 0, 1); });

    document.querySelectorAll('.voice-preset-btn').forEach(function(b) {
        b.addEventListener('click', function() {
            voiceState.rate = parseFloat(this.dataset.rate);
            updateVoiceUI();
            saveVoiceSettings();
        });
    });

    var sel = $('voiceSelect');
    if (sel) sel.addEventListener('change', function() {
        voiceState.voiceURI = this.value;
        saveVoiceSettings();
    });

    if ($('voiceTestBtn')) $('voiceTestBtn').addEventListener('click', voiceTestSpeak);

    if ($('voiceResetBtn')) $('voiceResetBtn').addEventListener('click', function() {
        voiceState.rate    = DEFAULT_VOICE.rate;
        voiceState.pitch   = DEFAULT_VOICE.pitch;
        voiceState.volume  = DEFAULT_VOICE.volume;
        voiceState.voiceURI = DEFAULT_VOICE.voiceURI;
        if ($('voiceSelect')) $('voiceSelect').value = '';
        updateVoiceUI();
        saveVoiceSettings();
    });

    if ($('pfVoiceBtn')) {
        $('pfVoiceBtn').addEventListener('click', function(e) {
            e.stopPropagation();
            e.preventDefault();
            populateVoiceSelect();
            updateVoiceUI();
            modal.classList.add('show');
        });
    }
    if ($('toggleVoiceBtn')) {
        $('toggleVoiceBtn').addEventListener('click', function(e) {
            e.stopPropagation();
            populateVoiceSelect();
            updateVoiceUI();
            modal.classList.add('show');
            if ($('fabGroup')) $('fabGroup').classList.remove('open');
        });
    }
    if ($('voiceClose')) $('voiceClose').addEventListener('click', function() { modal.classList.remove('show'); });
    modal.addEventListener('click', function(e) { if (e.target === this) modal.classList.remove('show'); });
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('show')) modal.classList.remove('show');
    });
}

/* ============================================================ */
/* BUILD FILTERS                                                 */
/* ============================================================ */
function buildFilters() {
    var hskSelect = $('hskFilter');
    var subjectSelect = $('subjectFilter');
    var info = getTierInfo();
    var isLimited = info.tier !== 'active';

    if (isLimited) {
        var allowedHsk = getAllowedHskList();
        var hskHtml = '<option value="">Tất cả (HSK1-' + info.maxHSK + ')</option>';
        allowedHsk.forEach(function(h) {
            hskHtml += '<option value="' + h + '">' + h + '</option>';
        });

        // ⭐ DANH SÁCH ĐẦY ĐỦ BAO GỒM HSK7-9
        var allHskList = ['HSK1','HSK2','HSK3','HSK4','HSK5','HSK6','HSK7-9'];
        allHskList.forEach(function(h) {
            if (allowedHsk.indexOf(h) === -1) {
                var lockLabel = info.tier === 'trial' ? '(gia hạn)' : '(đăng nhập)';
                hskHtml += '<option value="' + h + '" disabled>' + h + ' ' + lockLabel + '</option>';
            }
        });
        hskSelect.innerHTML = hskHtml;

        var allowedSubjects = getAllowedSubjectList();
        var allSubjectSet = {};
        RAW_DATA.forEach(function(r) { if (r.subject) allSubjectSet[r.subject] = 1; });
        var allSubjects = Object.keys(allSubjectSet).sort();
        var unlocked = [], locked = [];
        allSubjects.forEach(function(s) {
            if (allowedSubjects.indexOf(s) !== -1) unlocked.push(s);
            else locked.push(s);
        });
        var subjHtml = '<option value="">Tất cả chủ đề</option>';
        unlocked.forEach(function(s) {
            subjHtml += '<option value="' + escapeHtml(s) + '">' + escapeHtml(s) + '</option>';
        });
        locked.forEach(function(s) {
            var lockLabel = info.tier === 'trial' ? '(gia hạn)' : '(đăng nhập)';
            subjHtml += '<option value="' + escapeHtml(s) + '" disabled>' + escapeHtml(s) + ' ' + lockLabel + '</option>';
        });
        subjectSelect.innerHTML = subjHtml;
    } else {
        // ⭐ THÊM HSK7-9 VÀO DROPDOWN
        hskSelect.innerHTML =
            '<option value="">Tất cả</option>' +
            '<option value="HSK1">HSK1</option>' +
            '<option value="HSK2">HSK2</option>' +
            '<option value="HSK3">HSK3</option>' +
            '<option value="HSK4">HSK4</option>' +
            '<option value="HSK5">HSK5</option>' +
            '<option value="HSK6">HSK6</option>' +
            '<option value="HSK7-9">HSK7-9</option>';

        var allSubjectSet2 = {};
        RAW_DATA.forEach(function(r) { if (r.subject) allSubjectSet2[r.subject] = 1; });
        var allSubjects2 = Object.keys(allSubjectSet2).sort();
        subjectSelect.innerHTML = '<option value="">Tất cả chủ đề</option>' +
            allSubjects2.map(function(v){ return '<option value="'+escapeHtml(v)+'">'+escapeHtml(v)+'</option>'; }).join('');
    }
}

function updateFilterUI() {
    var hsk = $('hskFilter').value;
    var subject = $('subjectFilter').value;
    $('hskValue').textContent = hsk || 'Tất cả';
    $('subjectValue').textContent = subject || 'Tất cả';
    $('hskChip').classList.toggle('has-value', !!hsk);
    $('subjectChip').classList.toggle('has-value', !!subject);
    var info = getTierInfo();
    var limited = info.tier === 'demo' || info.tier === 'expired';
    $('hskChip').classList.toggle('demo-limited', limited);
    $('subjectChip').classList.toggle('demo-limited', limited);
    var count = 0;
    if (state.search) count++;
    if (hsk) count++;
    if (subject) count++;
    var resetBtn = $('resetBtn');
    var badge = $('resetBadge');
    if (count > 0) {
        resetBtn.classList.remove('hidden');
        resetBtn.classList.add('has-badge');
        badge.textContent = count;
    } else {
        resetBtn.classList.add('hidden');
    }
    updateResultCount();
}

function updateResultCount() {
    var el = $('resultCount');
    if (!el) return;
    var total = filtered ? filtered.length : 0;
    var hasFilter = !!(state.search || state.hsk || state.subject);
    if (!hasFilter) { el.classList.remove('show', 'empty'); return; }
    el.classList.add('show');
    el.classList.toggle('empty', total === 0);
    var spanEl = el.querySelector('span');
    if (spanEl) {
        if (total === 0) spanEl.innerHTML = 'Không tìm thấy kết quả nào';
        else spanEl.innerHTML = 'Tìm thấy <b>' + total + '</b> kết quả';
    }
}
/* ═══════════════════════════════════════════════════════════ */
/* PARSE SEARCH QUERY — Nhận diện cú pháp đặc biệt              */
/* Hỗ trợ:                                                       */
/*   "hsk1"      / "hsk1 5"    / "hsk1 5 10"                    */
/*   "hsk7" / "hsk8" / "hsk9" / "hsk7-9" / "hsk7-9 5"           */
/*   "HSK1"      / "HSK7-9"    (chữ hoa/thường đều OK)          */
/* ═══════════════════════════════════════════════════════════ */
function parseSearchQuery(rawQuery) {
    var q = (rawQuery || '').trim();
    if (!q) return null;

    var qLower = q.toLowerCase();

    // Hỗ trợ: 1-9 hoặc dải "7-9"
    var match = qLower.match(/^hsk\s*(7[-–\s]*9|[789]|\d+)\s*(?:(\d+)(?:\s+(\d+))?)?$/);
    if (!match) return null;

    var hskRaw = match[1].replace(/[\s–]/g, '');
    var hskValue;

    // ⭐ HSK 7, 8, 9 đều gộp về "HSK7-9"
    if (hskRaw === '7-9' || hskRaw === '7' || hskRaw === '8' || hskRaw === '9') {
        hskValue = 'HSK7-9';
    } else {
        var hskNum = parseInt(hskRaw, 10);
        if (isNaN(hskNum) || hskNum < 1 || hskNum > 6) return null;
        hskValue = 'HSK' + hskNum;
    }

    var startStt = match[2] ? parseInt(match[2]) : null;
    var endStt   = match[3] ? parseInt(match[3]) : startStt;

    if (startStt !== null && endStt !== null && endStt < startStt) {
        var tmp = startStt;
        startStt = endStt;
        endStt = tmp;
    }

    return {
        type: 'hsk_stt',
        hsk: hskValue,
        startStt: startStt,
        endStt: endStt,
        original: q
    };
}/* ============================================================ */
/* APPLY FILTER — Lọc câu theo search/HSK/subject                */
/* Đã tích hợp cú pháp đặc biệt: "hsk1 5", "hsk1", "hsk1 5 10"  */
/* ============================================================ */
function applyFilter() {
    /* ═══ 1. ĐỌC FILTER TỪ UI ═══ */
    var rawSearch = $('searchInput').value.trim();
    state.search  = rawSearch.toLowerCase();
    state.hsk     = $('hskFilter').value;
    state.subject = $('subjectFilter').value;
    updateFilterUI();

    var clearBtn = $('clearSearchBtn');
    if (state.search) clearBtn.classList.add('show');
    else              clearBtn.classList.remove('show');

    /* ═══ 2. TAB YÊU THÍCH → RENDER RIÊNG ═══ */
    if (typeof favState !== 'undefined'
        && favState
        && favState.currentView === true
        && typeof favRenderCurrentTab === 'function') {
        favRenderCurrentTab();
        return;
    }

    /* ═══ 3. LẤY TOÀN BỘ KHO — KHÔNG GIỚI HẠN TIER ═══ */
    var baseData = getLimitedData();

    var info = getTierInfo();
    var allowedHsk = getAllowedHskList();
    var isUnlimited = (info.tier === 'active');

    /* ═══ 4. KIỂM TRA CÚ PHÁP ĐẶC BIỆT ═══ */
    var parsed = parseSearchQuery(rawSearch);

    if (parsed && parsed.type === 'hsk_stt') {
        var targetHsk = normalizeHsk(parsed.hsk);   // ⭐ CHUẨN HOÁ

        /* ⭐ CHECK QUYỀN */
        if (!isUnlimited && allowedHsk.indexOf(targetHsk) === -1) {
            var lockMsg = info.tier === 'trial'
                ? '⚠️ ' + parsed.hsk + ' chưa mở khoá (cần gia hạn)'
                : '⚠️ ' + parsed.hsk + ' chưa mở khoá (cần đăng nhập)';
            showSearchToast(lockMsg);
            filtered = [];
            updateResultCount();
            render(true);
            return;
        }

        filtered = baseData.filter(function(r) {
            if (normalizeHsk(r.hsk) !== targetHsk) return false;   // ⭐
            if (parsed.startStt === null) return true;

            var sttNum = parseInt(String(r.stt).trim(), 10);
            if (isNaN(sttNum)) return false;

            return sttNum >= parsed.startStt && sttNum <= parsed.endStt;
        });

        updateResultCount();
        render(true);

        if (filtered.length === 0) {
            if (parsed.startStt === null) {
                showSearchToast('⚠️ Không có câu nào trong ' + parsed.hsk);
            } else if (parsed.startStt === parsed.endStt) {
                showSearchToast('⚠️ Không có câu số ' + parsed.startStt + ' trong ' + parsed.hsk);
            } else {
                showSearchToast('⚠️ Không có câu nào từ ' + parsed.startStt + ' → ' + parsed.endStt + ' trong ' + parsed.hsk);
            }
        } else {
            var foundMsg = parsed.startStt === null
                ? '✅ Tìm thấy ' + filtered.length + ' câu trong ' + parsed.hsk
                : (parsed.startStt === parsed.endStt
                    ? '✅ ' + parsed.hsk + ' câu số ' + parsed.startStt + ' (' + filtered.length + ' kết quả)'
                    : '✅ ' + parsed.hsk + ' câu ' + parsed.startStt + ' → ' + parsed.endStt + ' (' + filtered.length + ' kết quả)');
            showSearchToast(foundMsg);
        }

        setTimeout(function() {
            var mainEl = $('mainContent');
            if (mainEl) {
                var yOffset = mainEl.getBoundingClientRect().top + window.scrollY - 100;
                window.scrollTo({ top: yOffset, behavior: 'smooth' });
            }
        }, 100);

        return;
    }

    /* ═══ 5. LỌC TEXT THÔNG THƯỜNG ═══ */
    filtered = baseData.filter(function(r) {
        if (state.search) {
            var s = state.search;
            var inVi      = (r.vi      || '').toLowerCase().indexOf(s) !== -1;
            var inZh      = (r.zh      || '').toLowerCase().indexOf(s) !== -1;
            var inPinyin  = (r.pinyin  || '').toLowerCase().indexOf(s) !== -1;
            var inTopic   = (r.topic   || '').toLowerCase().indexOf(s) !== -1;
            var inSubject = (r.subject || '').toLowerCase().indexOf(s) !== -1;
            if (!inVi && !inZh && !inPinyin && !inTopic && !inSubject) return false;
        }
        if (state.hsk && normalizeHsk(r.hsk) !== normalizeHsk(state.hsk)) return false;   // ⭐
        if (state.subject && r.subject !== state.subject) return false;
        return true;
    });

    /* ⭐ LỌC LẦN 2: CHỈ GIỮ CÂU THUỘC QUYỀN USER */
    if (!isUnlimited && allowedHsk.length > 0) {
        filtered = filtered.filter(function(r) {
            return allowedHsk.indexOf(normalizeHsk(r.hsk)) !== -1;   // ⭐
        });
    }

    updateResultCount();
    render(true);

    if (state.hsk || state.subject) {
        setTimeout(function() {
            var mainEl = $('mainContent');
            if (mainEl) {
                var yOffset = mainEl.getBoundingClientRect().top + window.scrollY - 100;
                window.scrollTo({ top: yOffset, behavior: 'smooth' });
            }
        }, 150);
    }
}
/* ============================================================ */
/* RENDER CARDS                                                  */
/* ============================================================ */
function render(reset) {
    if (reset) { renderedCount = 0; focusedStt = null; }
    if (!filtered.length) {
        mobileWrapper.innerHTML = '<div class="no-data"><i class="fas fa-search"></i>Không tìm thấy câu nào</div>';
        return;
    }
    if (reset) mobileWrapper.innerHTML = '';
    var end = Math.min(renderedCount + PAGE_SIZE, filtered.length);
    var mobHtml = '';
    for (var i = renderedCount; i < end; i++) {
        var r = filtered[i];
        var zhJs = escapeJs(r.zh);
        var viJs = escapeJs(r.vi);
        var pinyinJs = escapeJs(r.pinyin);
        var zhHtml = escapeHtml(r.zh);
        var viHtml = escapeHtml(r.vi);
        var sttSafe = escapeHtml(r.stt);
        var sttJs = escapeJs(r.stt);

        var audio = r.zh ? '<button class="audio-btn" onclick="speakText(\'' + zhJs + '\', this, event)" title="Nghe"><i class="fas fa-volume-up"></i></button>' : '';
        var writeBtn = '';
        if (r.zh) {
            writeBtn = '<button class="write-btn" onclick="openWriter(\'' + zhJs + '\', \'' + viJs + '\', \'' + pinyinJs + '\', event)" title="Luyện viết"><i class="fas fa-pen-fancy"></i></button>';
        }
        var fullBtn = '';
        if (r.zh) {
            fullBtn = '<button class="practice-full-btn" onclick="openPracticeFull(\'' + sttJs + '\', event)" title="Luyện tập full màn hình"><i class="fas fa-expand"></i></button>';
        }
        var practiceInput = '<input type="text" class="practice-input" placeholder="Gõ tiếng Trung..." data-answer="' + zhHtml + '" data-vi-hint="' + viHtml + '" data-stt="' + sttSafe + '" oninput="checkInput(this)" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">';
        var toggleCheckBtn = '<button class="toggle-check-btn" onclick="toggleInlineCheck(this, event)" title="Ẩn/hiện kết quả kiểm tra" data-visible="0"><i class="fas fa-eye"></i></button>';

        var excelBadge = '';
        if (r.excelRow !== undefined && r.excelRow !== null && r.excelRow !== '') {
            excelBadge = '<span class="card-excel-row" title="Dòng ' + escapeHtml(r.excelRow) + ' trong file Excel">' +
                         '<i class="fas fa-file-excel"></i> ' + escapeHtml(r.excelRow) +
                         '</span>';
        }

        var topicTag = '';
        if (r.topic) {
            topicTag = '<span class="card-tag topic tag-clickable" ' +
                       'onclick="searchByTag(event, \'topic\', \'' + escapeJs(r.topic) + '\')" ' +
                       'title="Lọc theo chủ điểm này">' +
                       escapeHtml(r.topic) + '</span>';
        }
        var subjectTag = '';
        if (r.subject) {
            subjectTag = '<span class="card-tag subject tag-clickable" ' +
                         'onclick="searchByTag(event, \'subject\', \'' + escapeJs(r.subject) + '\')" ' +
                         'title="Lọc theo chủ đề này">' +
                         escapeHtml(r.subject) + '</span>';
        }

        /* ❤️ Nút Yêu thích */
        var favBtnHtml = (typeof favBuildFavButton === 'function')
            ? favBuildFavButton(r.stt)
            : '';

        mobHtml += '<div class="card" data-hsk="' + (r.hsk || '') + '" onclick="toggleFocus(\'' + sttJs + '\', this)" data-stt="' + sttSafe + '">' +
            '<div class="card-header">' +
                '<div class="card-stt">' + sttSafe + '</div>' +
                '<div class="card-meta">' +
                    (r.hsk ? '<span class="card-tag hsk">' + escapeHtml(r.hsk) + '</span>' : '') +
                    topicTag +
                    subjectTag +
                    excelBadge +
                '</div>' +
                '<div onclick="event.stopPropagation()" class="action-group">' +
                    audio + writeBtn + fullBtn + favBtnHtml +
                '</div>' +
            '</div>' +
            '<div class="card-body">' +
                (r.vi ? '<div class="card-vi">' + viHtml + '</div>' : '') +
                '<div class="card-zh">' + zhHtml + '</div>' +
                (r.pinyin ? '<div class="card-pinyin">' + escapeHtml(r.pinyin) + '</div>' : '') +
            '</div>' +
            '<div class="card-practice" onclick="event.stopPropagation()">' +
                practiceInput +
                toggleCheckBtn +
                '<div class="card-check" data-check-stt="' + sttSafe + '" style="display:none"></div>' +
            '</div>' +
            '</div>';
    }
    mobileWrapper.insertAdjacentHTML('beforeend', mobHtml);
    renderedCount = end;

    var oldMobileBtn = mobileWrapper.querySelector('.load-more');
    if (oldMobileBtn) oldMobileBtn.remove();
    var oldEndNote = mobileWrapper.querySelector('.end-note');
    if (oldEndNote) oldEndNote.remove();

    if (renderedCount < filtered.length) {
        var info = getTierInfo();
        var limited = info.tier !== 'active';
        var limitedDataLen = limited ? getLimitedData().length : RAW_DATA.length;
        var isTierLocked = limited && (renderedCount >= limitedDataLen) && (filtered.length >= limitedDataLen);

        if (!isTierLocked) {
            var btnMobile = document.createElement('button');
            btnMobile.className = 'load-more';
            btnMobile.innerHTML = '<i class="fas fa-chevron-down"></i> Xem thêm (' + renderedCount + '/' + filtered.length + ')';
            btnMobile.onclick = function() { render(false); };
            mobileWrapper.appendChild(btnMobile);
        } else {
            var lockedBtn = document.createElement('button');
            lockedBtn.className = 'load-more locked';
            if (info.tier === 'expired') {
                lockedBtn.classList.add('expired');
                lockedBtn.innerHTML = '<i class="fas fa-gem"></i> Gia hạn để xem toàn bộ ' + RAW_DATA.length + ' câu';
                lockedBtn.onclick = function() {
                    if (typeof openRenewalModal === 'function') openRenewalModal();
                };
            } else if (info.tier === 'trial') {
                lockedBtn.innerHTML = '<i class="fas fa-crown"></i> Gia hạn để xem toàn bộ ' + RAW_DATA.length + ' câu';
                lockedBtn.onclick = function() {
                    if (typeof openRenewalModal === 'function') openRenewalModal();
                };
            } else {
                lockedBtn.innerHTML = '<i class="fas fa-lock"></i> Đăng nhập để xem toàn bộ ' + RAW_DATA.length + ' câu';
                lockedBtn.onclick = function() {
                    if (typeof showLoginModal === 'function') showLoginModal();
                };
            }
            mobileWrapper.appendChild(lockedBtn);
        }
    } else if (filtered.length > PAGE_SIZE) {
        var endNote = document.createElement('div');
        endNote.className = 'end-note';
        endNote.innerHTML = '<i class="fas fa-check-circle"></i> Đã hiển thị tất cả ' + filtered.length + ' câu';
        mobileWrapper.appendChild(endNote);
    }
}
/* ============================================================ */
/* ANSWER CHECKING                                               */
/* ============================================================ */
function normalizeAnswer(str) {
    if (!str) return '';
    return String(str)
        .replace(/[。，！？、；：""''「」『』（）《》〈〉【】〔〕]/g, '')
        .replace(/[.,!?;:'"()\[\]{}\-~`@#$%^&*+=|\\/<>]/g, '')
        .replace(/\s+/g, '')
        .toLowerCase()
        .trim();
}

function removeTones(str) {
    if (!str) return '';
    var map = {
        'ā':'a','á':'a','ǎ':'a','à':'a','ē':'e','é':'e','ě':'e','è':'e',
        'ī':'i','í':'i','ǐ':'i','ì':'i','ō':'o','ó':'o','ǒ':'o','ò':'o',
        'ū':'u','ú':'u','ǔ':'u','ù':'u','ǖ':'v','ǘ':'v','ǚ':'v','ǜ':'v','ü':'v'
    };
    return str.replace(/[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]/g, function(c) { return map[c] || c; });
}

function removeFillers(str) {
    if (!str) return '';
    var result = str;
    FILLER_WORDS.forEach(function(w) { result = result.split(w).join(''); });
    return result;
}

function expandSynonyms(str) {
    var results = [str];
    var keys = Object.keys(SYNONYMS);
    for (var i = 0; i < keys.length; i++) {
        var key = keys[i];
        if (str.indexOf(key) !== -1) {
            var values = SYNONYMS[key];
            for (var j = 0; j < values.length; j++) results.push(str.split(key).join(values[j]));
        }
    }
    return results;
}

function levenshtein(a, b) {
    if (a === b) return 0;
    if (!a.length) return b.length;
    if (!b.length) return a.length;
    var matrix = [];
    for (var i = 0; i <= b.length; i++) matrix[i] = [i];
    for (var j = 0; j <= a.length; j++) matrix[0][j] = j;
    for (var i = 1; i <= b.length; i++) {
        for (var j = 1; j <= a.length; j++) {
            if (b.charAt(i-1) === a.charAt(j-1)) matrix[i][j] = matrix[i-1][j-1];
            else matrix[i][j] = Math.min(matrix[i-1][j-1] + 1, matrix[i][j-1] + 1, matrix[i-1][j] + 1);
        }
    }
    return matrix[b.length][a.length];
}

function similarity(a, b) {
    var maxLen = Math.max(a.length, b.length);
    if (maxLen === 0) return 1;
    return 1 - (levenshtein(a, b) / maxLen);
}

function smartCheck(userAnswer, correctAnswer) {
    var user = normalizeAnswer(userAnswer);
    var correct = normalizeAnswer(correctAnswer);
    if (!user) return { status: 'wrong', reason: '' };
    if (user === correct) return { status: 'correct', reason: 'Chính xác' };
    var userNoTone = removeTones(user);
    var correctNoTone = removeTones(correct);
    if (userNoTone === correctNoTone) return { status: 'correct', reason: 'Đúng (thiếu dấu thanh)' };
    var userNoFill = removeFillers(user);
    var correctNoFill = removeFillers(correct);
    if (userNoFill === correctNoFill) return { status: 'correct', reason: 'Đúng (bỏ qua từ phụ)' };
    var uNF = removeTones(userNoFill);
    var cNF = removeTones(correctNoFill);
    if (uNF === cNF) return { status: 'correct', reason: 'Đúng (từ phụ + dấu thanh)' };
    var userVariants = expandSynonyms(userNoFill);
    var correctVariants = expandSynonyms(correctNoFill);
    for (var i = 0; i < userVariants.length; i++) {
        for (var j = 0; j < correctVariants.length; j++) {
            if (userVariants[i] === correctVariants[j]) return { status: 'correct', reason: 'Đúng (từ đồng nghĩa)' };
        }
    }
    var maxSim = 0;
    for (var k = 0; k < correctVariants.length; k++) {
        var sim = similarity(userNoFill, correctVariants[k]);
        if (sim > maxSim) maxSim = sim;
    }
    for (var m = 0; m < userVariants.length; m++) {
        var sim2 = similarity(userVariants[m], correctNoFill);
        if (sim2 > maxSim) maxSim = sim2;
    }
    if (maxSim >= 0.85) return { status: 'partial', reason: 'Gần đúng (' + Math.round(maxSim * 100) + '%)' };
    if (user.indexOf(correct) !== -1 || correct.indexOf(user) !== -1) return { status: 'partial', reason: 'Thiếu/thừa từ' };
    return { status: 'wrong', reason: 'Không khớp' };
}

function countSyllables(pinyinWord) {
    if (!pinyinWord) return 0;
    var cleaned = pinyinWord
        .replace(/[.,!?;:'"()\[\]{}\-~`@#$%^&*+=|\\/<>。，！？、；：\s]/g, '')
        .toLowerCase();
    if (!cleaned) return 0;
    var map = {
        'ā':'a','á':'a','ǎ':'a','à':'a','ē':'e','é':'e','ě':'e','è':'e',
        'ī':'i','í':'i','ǐ':'i','ì':'i','ō':'o','ó':'o','ǒ':'o','ò':'o',
        'ū':'u','ú':'u','ǔ':'u','ù':'u','ǖ':'v','ǘ':'v','ǚ':'v','ǜ':'v','ü':'v'
    };
    cleaned = cleaned.replace(/[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]/g, function(c) { return map[c] || c; });
    var vowels = 'aeiouv';
    var count = 0;
    var i = 0;
    while (i < cleaned.length) {
        if (vowels.indexOf(cleaned[i]) !== -1) {
            count++;
            while (i < cleaned.length && vowels.indexOf(cleaned[i]) !== -1) {
                i++;
            }
        } else {
            i++;
        }
    }
    return count || 1;
}

function splitByPinyin(zh, pinyin) {
    if (!zh) return [];
    var hanziChars = [];
    for (var i = 0; i < zh.length; i++) {
        var c = zh[i];
        if (/[\u4e00-\u9fa5]/.test(c)) hanziChars.push(c);
    }
    if (hanziChars.length === 0) return [];

    if (!pinyin || !pinyin.trim()) {
        return hanziChars.map(function(c) { return { text: c, type: 'single', pinyin: '' }; });
    }

    var normalizedPinyin = pinyin
        .replace(/[.,!?;:'"()\[\]{}\-~`@#$%^&*+=|\\/<>。，！？、；：""'']/g, ' ')
        .replace(/\s+/g, ' ')
        .trim();

    var pinyinWords = normalizedPinyin.split(/\s+/).filter(function(w) { return w.length > 0; });
    var syllableCounts = pinyinWords.map(function(w) { return countSyllables(w); });
    var totalSyllables = syllableCounts.reduce(function(a, b) { return a + b; }, 0);

    if (totalSyllables === hanziChars.length) {
        var result = [];
        var charIdx = 0;
        for (var j = 0; j < syllableCounts.length; j++) {
            var cnt = syllableCounts[j];
            if (cnt <= 0) continue;
            var phrase = hanziChars.slice(charIdx, charIdx + cnt).join('');
            if (phrase) {
                result.push({
                    text: phrase,
                    type: 'phrase',
                    pinyin: pinyinWords[j] || ''
                });
            }
            charIdx += cnt;
        }
        if (charIdx < hanziChars.length) {
            var remaining = hanziChars.slice(charIdx).join('');
            if (result.length > 0) {
                result[result.length - 1].text += remaining;
                if (charIdx < pinyinWords.length) {
                    result[result.length - 1].pinyin += ' ' + pinyinWords.slice(charIdx).join(' ');
                }
            } else {
                result.push({ text: remaining, type: 'single', pinyin: '' });
            }
        }
        return result;
    }

    return hanziChars.map(function(c) { return { text: c, type: 'single', pinyin: '' }; });
}

function updateInlinePreview(input, answer) {
    var wrapper = input.parentElement;
    var preview = wrapper.querySelector('.inline-char-preview');
    if (!preview) {
        preview = document.createElement('div');
        preview.className = 'inline-char-preview';
        input.insertAdjacentElement('afterend', preview);
    }
    var userVal = input.value.replace(/\s+/g, '');
    var cleanAnswer = (answer || '').replace(/\s+/g, '');
    if (!cleanAnswer) { preview.innerHTML = ''; return; }
    var html = '';
    var maxLen = Math.max(userVal.length, cleanAnswer.length);
    for (var i = 0; i < maxLen; i++) {
        var userChar = userVal[i] || '';
        var answerChar = cleanAnswer[i] || '';
        var cls = 'char-slot';
        var display = '';
        var clickable = false;
        if (userChar && answerChar) {
            if (userChar === answerChar) {
                cls += ' correct';
                display = userChar;
            } else {
                cls += ' wrong';
                display = userChar;
                clickable = true;
            }
        } else if (!userChar && answerChar) {
            cls += ' ghost-missing';
            display = '·';
            clickable = true;
        } else if (userChar && !answerChar) {
            cls += ' extra';
            display = userChar;
            clickable = true;
        } else {
            continue;
        }
        if (clickable) {
            html += '<span class="' + cls + '" data-idx="' + i + '" onclick="fixInlineChar(this, event)">' + escapeHtml(display) + '</span>';
        } else {
            html += '<span class="' + cls + '">' + escapeHtml(display) + '</span>';
        }
    }
    preview.innerHTML = html;
}

window.fixInlineChar = function(el, evt) {
    evt.stopPropagation();
    if (evt.preventDefault) evt.preventDefault();
    var wrap = el.closest('.card-practice');
    var input = wrap ? wrap.querySelector('.practice-input') : null;
    if (!input) return;
    var strippedIdx = parseInt(el.dataset.idx);
    var rawVal = input.value;
    var rawIdx = -1;
    var strippedCount = -1;
    for (var i = 0; i < rawVal.length; i++) {
        if (!/\s/.test(rawVal[i])) {
            strippedCount++;
            if (strippedCount === strippedIdx) {
                rawIdx = i;
                break;
            }
        }
    }
    if (rawIdx === -1) rawIdx = rawVal.length;
    while (rawIdx < rawVal.length && /\s/.test(rawVal[rawIdx])) {
        rawIdx++;
    }
    input.focus();
    setTimeout(function() {
        try {
            var endIdx = Math.min(rawIdx + 1, rawVal.length);
            input.setSelectionRange(rawIdx, endIdx);
        } catch(e) {
            input.selectionStart = rawIdx;
            input.selectionEnd = Math.min(rawIdx + 1, rawVal.length);
        }
        el.classList.add('highlight');
        setTimeout(function() { el.classList.remove('highlight'); }, 1200);
    }, 10);
};

function showInlineCheckWithAnswer(input) {
    if (!input) return;
    var stt = input.dataset.stt;
    var answer = input.dataset.answer;
    var cells = document.querySelectorAll('[data-check-stt="' + stt + '"]');
    var val = input.value.trim();
    if (!answer) { cells.forEach(function(c) { c.innerHTML = ''; }); return; }
    var answerHtml = '<div class="answer-inline-display">' +
        '<span class="answer-inline-label"><i class="fas fa-check-circle"></i> Đáp án:</span>' +
        '<span class="answer-inline-text">' + escapeHtml(answer) + '</span>' +
        '</div>';
    var resultHtml = '';
    if (val) {
        var result = smartCheck(val, answer);
        if (result.status === 'correct') resultHtml = '<span class="ai-correct">ĐÚNG</span>';
        else if (result.status === 'partial') resultHtml = '<span class="ai-partial">GẦN ĐÚNG</span>';
        else resultHtml = '<span class="ai-wrong">SAI</span>';
        if (result.reason) resultHtml += '<span class="ai-reason">' + escapeHtml(result.reason) + '</span>';
    } else {
        resultHtml = '<span class="ai-reason">Chưa gõ gì cả</span>';
    }
    cells.forEach(function(c) { c.innerHTML = resultHtml + answerHtml; });
}

window.checkInput = function(input) {
    var stt = input.dataset.stt;
    var answer = input.dataset.answer;
    var cells = document.querySelectorAll('[data-check-stt="' + stt + '"]');
    var val = input.value.trim();
    updateInlinePreview(input, answer);
    var wrap = input.closest('.card-practice');
    var btn = wrap ? wrap.querySelector('.toggle-check-btn') : null;
    var isVisible = btn && btn.dataset.visible === '1';
    if (!isVisible) return;
    var answerHtml = '<div class="answer-inline-display">' +
        '<span class="answer-inline-label"><i class="fas fa-check-circle"></i> Đáp án:</span>' +
        '<span class="answer-inline-text">' + escapeHtml(answer) + '</span>' +
        '</div>';
    var resultHtml = '';
    if (val) {
        var result = smartCheck(val, answer);
        if (result.status === 'correct') resultHtml = '<span class="ai-correct">ĐÚNG</span>';
        else if (result.status === 'partial') resultHtml = '<span class="ai-partial">GẦN ĐÚNG</span>';
        else resultHtml = '<span class="ai-wrong">SAI</span>';
        if (result.reason) resultHtml += '<span class="ai-reason">' + escapeHtml(result.reason) + '</span>';
    } else {
        resultHtml = '<span class="ai-reason">Chưa gõ gì cả</span>';
    }
    cells.forEach(function(c) { c.innerHTML = resultHtml + answerHtml; });
};

window.toggleInlineCheck = function(btn, evt) {
    if (evt) { evt.stopPropagation(); if (evt.preventDefault) evt.preventDefault(); }
    var wrap = btn.closest('.card-practice');
    if (!wrap) return;
    var checkEl = wrap.querySelector('.card-check');
    var input = wrap.querySelector('.practice-input');
    if (!checkEl) return;
    var isVisible = btn.dataset.visible === '1';
    if (isVisible) {
        checkEl.style.display = 'none';
        btn.dataset.visible = '0';
        btn.innerHTML = '<i class="fas fa-eye"></i>';
        btn.classList.remove('active');
    } else {
        checkEl.style.display = 'block';
        btn.dataset.visible = '1';
        btn.innerHTML = '<i class="fas fa-eye-slash"></i>';
        btn.classList.add('active');
        showInlineCheckWithAnswer(input);
    }
};

/* ============================================================ */
/* PRACTICE FULL MODAL — expired dùng được như Demo              */
/* ============================================================ */
var pfCurrentStt = null;
var pfCurrentAnswer = '';
var pfCurrentVi = '';
var pfCurrentPinyin = '';
var pfHintEnabled = false;
var pfRandomMode = false;

window.openPracticeFull = function(stt, evt) {
    if (evt) { evt.stopPropagation(); if (evt.preventDefault) evt.preventDefault(); }

    if (!canUseFeature()) { showLimitMessage(); return; }

    if (typeof pfBuildDatasetSelect === 'function') pfBuildDatasetSelect();
    pfBuildFilterOptions();
    pfBuildQuickNav();
    var idx = -1;
    for (var i = 0; i < filtered.length; i++) {
        if (String(filtered[i].stt) === String(stt)) { idx = i; break; }
    }
    if (idx === -1) { alert('Không tìm thấy câu!'); return; }
    pfCurrentStt = stt;
    document.body.classList.add('practice-full-open');
    if (typeof updateFloatingLeftVisibility === 'function') updateFloatingLeftVisibility();
    document.body.style.overflow = 'hidden';
    $('practiceFullModal').classList.add('show');
    loadPracticeFull(stt);
};

window.closePracticeFull = function() {
    if (window._isSpeakingFull) stopSpeakFull();
    if (window._isQuickSpeaking) stopQuickSpeak();
    $('practiceFullModal').classList.remove('show');
    document.body.style.overflow = '';
    document.body.classList.remove('practice-full-open');
    if (typeof updateFloatingLeftVisibility === 'function') updateFloatingLeftVisibility();
    pfCurrentStt = null;
    if ('speechSynthesis' in window) speechSynthesis.cancel();
};

function loadPracticeFull(stt) {
    var idx = -1;
    for (var i = 0; i < filtered.length; i++) {
        if (String(filtered[i].stt) === String(stt)) { idx = i; break; }
    }
    if (idx === -1) return;
    if (!$('pfSearchInput').value && !$('pfHskFilter').value && !$('pfSubjectFilter').value) {
        $('pfSearchInput').value = $('searchInput').value;
        $('pfHskFilter').value = $('hskFilter').value;
        $('pfSubjectFilter').value = $('subjectFilter').value;
    }
    pfUpdateFilterUI();
    var r = filtered[idx];
    pfCurrentStt = stt;
    pfCurrentAnswer = r.zh || '';
    pfCurrentVi = r.vi || '';
    pfCurrentPinyin = r.pinyin || '';

    var sttRaw = (r.stt !== undefined && r.stt !== null && String(r.stt).trim() !== '')
                 ? String(r.stt).trim()
                 : '';
    var sttLabel = sttRaw ? '#' + sttRaw + '  ·  ' : '';
    $('pfCounter').textContent = sttLabel + 'Câu ' + (idx + 1) + ' / ' + filtered.length;

    var tagsHtml = '';
    if (r.hsk) tagsHtml += '<span class="card-tag hsk">' + escapeHtml(r.hsk) + '</span>';
    if (r.topic) {
        tagsHtml += '<span class="card-tag topic tag-clickable" ' +
                    'onclick="searchByTag(event, \'topic\', \'' + escapeJs(r.topic) + '\')" ' +
                    'title="Lọc theo chủ điểm này">' +
                    escapeHtml(r.topic) + '</span>';
    }
    if (r.subject) {
        tagsHtml += '<span class="card-tag tag-clickable" ' +
                    'onclick="searchByTag(event, \'subject\', \'' + escapeJs(r.subject) + '\')" ' +
                    'title="Lọc theo chủ đề này">' +
                    escapeHtml(r.subject) + '</span>';
    }
    if (r.excelRow !== undefined && r.excelRow !== null && r.excelRow !== '') {
        tagsHtml += '<span class="card-tag excel-tag" title="Dòng ' + escapeHtml(r.excelRow) + ' trong file Excel">' +
                    '<i class="fas fa-file-excel"></i> Excel: ' + escapeHtml(r.excelRow) +
                    '</span>';
    }
    $('pfTags').innerHTML = tagsHtml;
    $('pfVi').textContent = pfCurrentVi;
    $('pfInput').value = '';
    $('pfStatus').textContent = '';
    $('pfStatus').className = 'practice-full-status';
    $('pfAnswer').classList.remove('show');
    var revealBtn = $('pfRevealBtn');
    revealBtn.classList.remove('revealed', 'hidden');
    revealBtn.innerHTML = '<i class="fas fa-eye"></i> Xem đáp án';
    pfHintEnabled = false;
    $('pfHintBtn').classList.remove('active');
    updateCharPreview();
    $('pfPrevBtn').disabled = (idx === 0);
    $('pfNextBtn').disabled = (idx === filtered.length - 1);
    var quickNav = $('pfQuickNav');
    if (quickNav && quickNav.value !== stt) quickNav.value = stt;

    if (window._isSpeakingFull) {
        stopSpeakFull();
    } else {
        _setSpeakBtnState(false);
    }
    if (window._isQuickSpeaking) {
        stopQuickSpeak();
    } else {
        _setQuickSpeakBtnState(false);
    }

    setTimeout(function() {
        var active = document.activeElement;
        if (active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA' || active.tagName === 'SELECT')) return;
        $('pfInput').focus();
    }, 200);
}

window.pfNext = function() {
    if (!pfCurrentStt || filtered.length === 0) return;
    var idx = -1;
    for (var i = 0; i < filtered.length; i++) {
        if (String(filtered[i].stt) === String(pfCurrentStt)) { idx = i; break; }
    }
    if (idx === -1) return;

    if (pfRandomMode && filtered.length > 1) {
        var newIdx = idx;
        var tries = 0;
        while (newIdx === idx && tries < 20) {
            newIdx = Math.floor(Math.random() * filtered.length);
            tries++;
        }
        if (newIdx === idx) newIdx = (idx + 1) % filtered.length;

        var rndBtn = $('pfRandomToggleBtn');
        if (rndBtn) {
            var icon = rndBtn.querySelector('i');
            if (icon) {
                icon.style.animation = 'none';
                void icon.offsetWidth;
                icon.style.animation = 'diceShake 0.6s ease-in-out';
            }
        }
        loadPracticeFull(filtered[newIdx].stt);
        return;
    }

    if (idx >= filtered.length - 1) return;
    loadPracticeFull(filtered[idx + 1].stt);
};

window.pfToggleRandom = function() {
    pfRandomMode = !pfRandomMode;
    var btn = $('pfRandomToggleBtn');
    if (btn) {
        btn.classList.toggle('active', pfRandomMode);
        btn.title = pfRandomMode
            ? 'ĐANG BẬT: Nút Next sẽ nhảy câu ngẫu nhiên'
            : 'Bật/tắt chế độ nhảy câu ngẫu nhiên';
    }
    try { localStorage.setItem('pfRandomMode', pfRandomMode ? '1' : '0'); } catch(e) {}
};

window.pfPrev = function() {
    if (!pfCurrentStt) return;
    var idx = -1;
    for (var i = 0; i < filtered.length; i++) {
        if (String(filtered[i].stt) === String(pfCurrentStt)) { idx = i; break; }
    }
    if (idx <= 0) return;
    loadPracticeFull(filtered[idx - 1].stt);
};

function pfBuildQuickNav() {
    var sel = $('pfQuickNav');
    if (!sel) return;

    // ═══ NẾU BẬT "CHỈ CÂU YÊU THÍCH" → CHỈ HIỆN CÂU YÊU THÍCH ═══
    var sourceList = filtered;
    if (typeof favState !== 'undefined'
        && favState.pfOnlyFav
        && typeof favCanUse === 'function'
        && favCanUse()) {
        sourceList = filtered.filter(function(r) {
            return favHas(r.stt);
        });
    }

    var html = '<option value="">-- Chọn câu (' + sourceList.length + ') --</option>';
    sourceList.forEach(function(r, i) {
        var vi = (r.vi || '').substring(0, 45);
        var sttRaw = (r.stt !== undefined && r.stt !== null && String(r.stt).trim() !== '')
                     ? '#' + String(r.stt).trim() + ' · '
                     : '';
        var label = sttRaw + 'Câu ' + (i + 1) + ': ' + vi;
        html += '<option value="' + escapeHtml(r.stt) + '">' + escapeHtml(label) + '</option>';
    });
    sel.innerHTML = html;
    if (pfCurrentStt) sel.value = pfCurrentStt;
}
function pfQuickNavChange() {
    var sel = $('pfQuickNav');
    if (!sel) return;
    var stt = sel.value;
    if (!stt) return;
    loadPracticeFull(stt);
}

function pfBuildFilterOptions() {
    var hskSel = $('pfHskFilter');
    var subjSel = $('pfSubjectFilter');
    var info = getTierInfo();
    var isLimited = info.tier !== 'active';

    if (isLimited) {
        var allowedHsk = getAllowedHskList();
        var hskHtml = '<option value="">Tất cả</option>';
        allowedHsk.forEach(function(h) {
            hskHtml += '<option value="' + h + '">' + h + '</option>';
        });

        // ⭐ DANH SÁCH ĐẦY ĐỦ BAO GỒM HSK7-9
        var allHskList = ['HSK1','HSK2','HSK3','HSK4','HSK5','HSK6','HSK7-9'];
        allHskList.forEach(function(h) {
            if (allowedHsk.indexOf(h) === -1) {
                var lockLabel = info.tier === 'trial' ? '(gia hạn)' : '(đăng nhập)';
                hskHtml += '<option value="' + h + '" disabled>' + h + ' ' + lockLabel + '</option>';
            }
        });
        hskSel.innerHTML = hskHtml;

        var allowedSubjects = getAllowedSubjectList();
        var allSubjectSet = {};
        RAW_DATA.forEach(function(r) { if (r.subject) allSubjectSet[r.subject] = 1; });
        var allSubjects = Object.keys(allSubjectSet).sort();
        var unlocked = [], locked = [];
        allSubjects.forEach(function(s) {
            if (allowedSubjects.indexOf(s) !== -1) unlocked.push(s);
            else locked.push(s);
        });
        var subjHtml = '<option value="">Tất cả chủ đề</option>';
        unlocked.forEach(function(s) {
            subjHtml += '<option value="' + escapeHtml(s) + '">' + escapeHtml(s) + '</option>';
        });
        locked.forEach(function(s) {
            var lockLabel = info.tier === 'trial' ? '(gia hạn)' : '(đăng nhập)';
            subjHtml += '<option value="' + escapeHtml(s) + '" disabled>' + escapeHtml(s) + ' ' + lockLabel + '</option>';
        });
        subjSel.innerHTML = subjHtml;
    } else {
        // ⭐ THÊM HSK7-9 VÀO DROPDOWN
        hskSel.innerHTML =
            '<option value="">Tất cả</option>' +
            '<option value="HSK1">HSK1</option>' +
            '<option value="HSK2">HSK2</option>' +
            '<option value="HSK3">HSK3</option>' +
            '<option value="HSK4">HSK4</option>' +
            '<option value="HSK5">HSK5</option>' +
            '<option value="HSK6">HSK6</option>' +
            '<option value="HSK7-9">HSK7-9</option>';

        var allSubjectSet2 = {};
        RAW_DATA.forEach(function(r) { if (r.subject) allSubjectSet2[r.subject] = 1; });
        var allSubjects2 = Object.keys(allSubjectSet2).sort();
        subjSel.innerHTML = '<option value="">Tất cả chủ đề</option>' +
            allSubjects2.map(function(v) {
                return '<option value="' + escapeHtml(v) + '">' + escapeHtml(v) + '</option>';
            }).join('');
    }

    hskSel.value = $('hskFilter').value;
    subjSel.value = $('subjectFilter').value;
    $('pfSearchInput').value = $('searchInput').value;
    pfUpdateFilterUI();
}
function pfUpdateFilterUI() {
    var hsk = $('pfHskFilter').value;
    var subject = $('pfSubjectFilter').value;
    $('pfHskValue').textContent = hsk || 'Tất cả';
    $('pfSubjectValue').textContent = subject || 'Tất cả';
    $('pfHskChip').classList.toggle('has-value', !!hsk);
    $('pfSubjectChip').classList.toggle('has-value', !!subject);
    var search = $('pfSearchInput').value.trim();
    if (search) $('pfClearSearchBtn').classList.add('show');
    else $('pfClearSearchBtn').classList.remove('show');
}

/* ============================================================ */
/* PF APPLY FILTER — Lọc trong modal Practice Full               */
/* Đã tích hợp cú pháp đặc biệt: "hsk1 5", "hsk1", "hsk1 5 10"  */
/* ============================================================ */
function pfApplyFilter() {
    /* ═══ Đồng bộ filter ra ngoài ═══ */
    var rawSearch = $('pfSearchInput').value.trim();
    $('searchInput').value     = $('pfSearchInput').value;
    $('hskFilter').value       = $('pfHskFilter').value;
    $('subjectFilter').value   = $('pfSubjectFilter').value;

    state.search  = rawSearch.toLowerCase();
    state.hsk     = $('pfHskFilter').value;
    state.subject = $('pfSubjectFilter').value;

    var baseData = getLimitedData();

    var parsed = parseSearchQuery(rawSearch);

    var info = getTierInfo();
    var allowedHsk = getAllowedHskList();
    var isUnlimited = (info.tier === 'active');

    /* ═══ NHÁNH 1: CÚ PHÁP ĐẶC BIỆT ═══ */
    if (parsed && parsed.type === 'hsk_stt') {
        var targetHsk = normalizeHsk(parsed.hsk);   // ⭐ CHUẨN HOÁ

        if (!isUnlimited && allowedHsk.indexOf(targetHsk) === -1) {
            var lockMsg = info.tier === 'trial'
                ? '⚠️ ' + parsed.hsk + ' chưa mở khoá (cần gia hạn)'
                : '⚠️ ' + parsed.hsk + ' chưa mở khoá (cần đăng nhập)';
            showSearchToast(lockMsg);
            filtered = [];
        } else {
            filtered = baseData.filter(function(r) {
                if (normalizeHsk(r.hsk) !== targetHsk) return false;   // ⭐
                if (parsed.startStt === null) return true;

                var sttNum = parseInt(String(r.stt).trim(), 10);
                if (isNaN(sttNum)) return false;

                return sttNum >= parsed.startStt && sttNum <= parsed.endStt;
            });

            if (filtered.length === 0) {
                if (parsed.startStt === null) {
                    showSearchToast('⚠️ Không có câu nào trong ' + parsed.hsk);
                } else if (parsed.startStt === parsed.endStt) {
                    showSearchToast('⚠️ Không có câu số ' + parsed.startStt + ' trong ' + parsed.hsk);
                } else {
                    showSearchToast('⚠️ Không có câu nào từ ' + parsed.startStt + ' → ' + parsed.endStt + ' trong ' + parsed.hsk);
                }
            } else {
                var foundMsg = parsed.startStt === null
                    ? '✅ Tìm thấy ' + filtered.length + ' câu trong ' + parsed.hsk
                    : (parsed.startStt === parsed.endStt
                        ? '✅ ' + parsed.hsk + ' câu số ' + parsed.startStt
                        : '✅ ' + parsed.hsk + ' câu ' + parsed.startStt + ' → ' + parsed.endStt + ' (' + filtered.length + ' kết quả)');
                showSearchToast(foundMsg);
            }
        }
    }
    /* ═══ NHÁNH 2: TEXT THÔNG THƯỜNG ═══ */
    else {
        filtered = baseData.filter(function(r) {
            if (state.search) {
                var s = state.search;
                var inVi      = (r.vi      || '').toLowerCase().indexOf(s) !== -1;
                var inZh      = (r.zh      || '').toLowerCase().indexOf(s) !== -1;
                var inPinyin  = (r.pinyin  || '').toLowerCase().indexOf(s) !== -1;
                var inTopic   = (r.topic   || '').toLowerCase().indexOf(s) !== -1;
                var inSubject = (r.subject || '').toLowerCase().indexOf(s) !== -1;
                if (!inVi && !inZh && !inPinyin && !inTopic && !inSubject) return false;
            }
            if (state.hsk && normalizeHsk(r.hsk) !== normalizeHsk(state.hsk)) return false;   // ⭐
            if (state.subject && r.subject !== state.subject) return false;
            return true;
        });

        if (!isUnlimited && allowedHsk.length > 0) {
            filtered = filtered.filter(function(r) {
                return allowedHsk.indexOf(normalizeHsk(r.hsk)) !== -1;   // ⭐
            });
        }
    }

    /* ═══ Cập nhật UI ═══ */
    updateFilterUI();
    pfUpdateFilterUI();
    pfBuildQuickNav();
    render(true);

    if (state.hsk || state.subject || parsed) {
        setTimeout(function() {
            var bodyEl = document.querySelector('.practice-full-body');
            if (bodyEl) bodyEl.scrollTo({ top: 0, behavior: 'smooth' });
        }, 100);
    }

    /* ═══ Xử lý câu hiện tại ═══ */
    var activeEl = document.activeElement;
    var isTypingInSearch = activeEl && activeEl.id === 'pfSearchInput';
    var currentStillValid = false;

    if (pfCurrentStt) {
        for (var i = 0; i < filtered.length; i++) {
            if (String(filtered[i].stt) === String(pfCurrentStt)) {
                currentStillValid = true;
                break;
            }
        }
    }

    if (filtered.length > 0) {
        if (isTypingInSearch && currentStillValid) {
            var idx = -1;
            for (var j = 0; j < filtered.length; j++) {
                if (String(filtered[j].stt) === String(pfCurrentStt)) {
                    idx = j;
                    break;
                }
            }
            if (idx !== -1) {
                var rNow = filtered[idx];
                var sttNow = (rNow.stt !== undefined && rNow.stt !== null && String(rNow.stt).trim() !== '')
                             ? '#' + String(rNow.stt).trim() + '  ·  '
                             : '';
                $('pfCounter').textContent = sttNow + 'Câu ' + (idx + 1) + ' / ' + filtered.length;
            }
            return;
        }

        loadPracticeFull(filtered[0].stt);
    } else {
        pfCurrentStt = null;
        pfCurrentAnswer = '';
        pfCurrentVi = 'Không tìm thấy câu nào';
        pfCurrentPinyin = '';
        $('pfVi').textContent = 'Không tìm thấy câu nào';
        $('pfInput').value = '';
        $('pfCounter').textContent = 'Câu 0 / 0';
        $('pfTags').innerHTML = '';
        $('pfAnswer').classList.remove('show');
        $('pfPreview').innerHTML = '';
        $('pfStatus').textContent = '';
        $('pfPrevBtn').disabled = true;
        $('pfNextBtn').disabled = true;
    }
}
function updateCharPreview() {
    var input = $('pfInput');
    var preview = $('pfPreview');
    var userVal = input.value;
    var cleanUser = userVal.replace(/\s+/g, '');
    var cleanAnswer = pfCurrentAnswer.replace(/\s+/g, '');
    if (!cleanAnswer) { preview.innerHTML = ''; return; }
    var html = '';
    var maxLen = Math.max(cleanUser.length, cleanAnswer.length);
    for (var i = 0; i < maxLen; i++) {
        var userChar = cleanUser[i] || '';
        var answerChar = cleanAnswer[i] || '';
        var cls = 'char-slot';
        var display = '';
        var clickable = false;
        if (userChar && answerChar) {
            if (userChar === answerChar) { cls += ' correct'; display = userChar; }
            else { cls += ' wrong'; display = userChar; clickable = true; }
        } else if (!userChar && answerChar) {
            if (pfHintEnabled) { cls += ' ghost'; display = answerChar; }
            else { continue; }
        } else if (userChar && !answerChar) {
            cls += ' extra'; display = userChar; clickable = true;
        } else { continue; }
        if (clickable) {
            html += '<span class="' + cls + '" data-idx="' + i + '" onclick="fixCharAt(' + i + ', this)">' + escapeHtml(display) + '</span>';
        } else {
            html += '<span class="' + cls + '">' + escapeHtml(display) + '</span>';
        }
    }
    preview.innerHTML = html;
}

window.fixCharAt = function(idx, el) {
    var input = $('pfInput');
    if (!input) return;
    input.focus();
    setTimeout(function() {
        try { input.setSelectionRange(idx, idx + 1); }
        catch(e) { input.selectionStart = idx; input.selectionEnd = idx + 1; }
        if (el) {
            el.classList.add('highlight');
            setTimeout(function() { el.classList.remove('highlight'); }, 1200);
        }
    }, 10);
};

function toggleHint() {
    pfHintEnabled = !pfHintEnabled;
    var btn = $('pfHintBtn');
    if (pfHintEnabled) btn.classList.add('active');
    else btn.classList.remove('active');
    updateCharPreview();
}

function checkFullAnswer() {
    var input = $('pfInput');
    var statusEl = $('pfStatus');
    var val = input.value.trim();
    if (!val) {
        statusEl.textContent = '';
        statusEl.className = 'practice-full-status';
        return;
    }
    var result = smartCheck(val, pfCurrentAnswer);
    if (result.status === 'correct') {
        statusEl.textContent = 'ĐÚNG';
        statusEl.className = 'practice-full-status correct';
    } else if (result.status === 'partial') {
        statusEl.textContent = (result.reason || 'GẦN ĐÚNG');
        statusEl.className = 'practice-full-status partial';
    } else {
        statusEl.textContent = 'SAI';
        statusEl.className = 'practice-full-status wrong';
    }
}

var _activeTooltipWrap = null;

function togglePhraseTooltip(wrapEl) {
    if (!wrapEl) return;
    var tip = wrapEl.querySelector('.answer-phrase-tooltip');
    if (!tip) return;

    if (_activeTooltipWrap && _activeTooltipWrap !== wrapEl) {
        var oldTip = _activeTooltipWrap.querySelector('.answer-phrase-tooltip');
        if (oldTip) oldTip.classList.remove('show');
    }

    if (tip.classList.contains('show')) {
        tip.classList.remove('show');
        _activeTooltipWrap = null;
    } else {
        tip.classList.add('show');
        _activeTooltipWrap = wrapEl;
    }
}

document.addEventListener('click', function(e) {
    if (!e.target.closest('.answer-phrase-wrap')) {
        document.querySelectorAll('.answer-phrase-tooltip.show').forEach(function(t) {
            t.classList.remove('show');
        });
        _activeTooltipWrap = null;
    }
});

function revealFullAnswer() {
    var answerEl = $('pfAnswer');
    var revealBtn = $('pfRevealBtn');
    if (answerEl.classList.contains('show')) {
        answerEl.classList.remove('show');
        revealBtn.classList.remove('revealed');
        revealBtn.innerHTML = '<i class="fas fa-eye"></i> Xem đáp án';
        return;
    }
    var charsEl = $('pfAnswerChars');
    var pinyinEl = $('pfAnswerPinyin');
    charsEl.innerHTML = '';
    var phrases = splitByPinyin(pfCurrentAnswer, pfCurrentPinyin);
    if (phrases.length === 0) {
        pfCurrentAnswer.split('').forEach(function(c) {
            if (/[\u4e00-\u9fa5]/.test(c)) phrases.push({ text: c, type: 'single', pinyin: '' });
        });
    }
    window._pfPhrases = phrases;

    phrases.forEach(function(item, idx) {
        var wrap = document.createElement('span');
        wrap.className = 'answer-phrase-wrap';
        wrap.dataset.idx = idx;
        wrap.dataset.text = item.text;
        wrap.dataset.pinyin = item.pinyin || '';

        var btn = document.createElement('button');
        btn.className = 'answer-phrase-btn';
        btn.textContent = item.text;
        btn.title = item.pinyin ? (item.text + ' - ' + item.pinyin) : item.text;
        btn.onclick = (function(text, pinyin, el, wrapEl) {
            return function(e) {
                e.stopPropagation();
                el.classList.add('zoom-in');
                setTimeout(function() { el.classList.remove('zoom-in'); }, 700);
                togglePhraseTooltip(wrapEl);
                speakPhrase(text, el);
            };
        })(item.text, item.pinyin, btn, wrap);
        wrap.appendChild(btn);

        var tip = document.createElement('span');
        tip.className = 'answer-phrase-tooltip';
        tip.textContent = item.pinyin || item.text;
        wrap.appendChild(tip);

        if (item.pinyin) {
            wrap.addEventListener('mouseenter', function() {
                tip.classList.add('show');
            });
            wrap.addEventListener('mouseleave', function() {
                tip.classList.remove('show');
            });
        }

        charsEl.appendChild(wrap);
    });

    pinyinEl.textContent = pfCurrentPinyin;
    answerEl.classList.add('show');
    revealBtn.classList.add('revealed');
    revealBtn.innerHTML = '<i class="fas fa-eye-slash"></i> Ẩn đáp án';
}

window.speakPhrase = function(phrase, btn) {
    if (!canUseFeature()) { showLimitMessage(); return; }
    if (!('speechSynthesis' in window)) { alert('Trình duyệt không hỗ trợ phát âm.'); return; }
    if (shouldCountUsage()) { incDemoUsage(); updateDemoRemaining(); }
    speechSynthesis.cancel();
    document.querySelectorAll('.answer-phrase-btn.speaking').forEach(function(b) { b.classList.remove('speaking'); });
    btn.classList.add('speaking');
    var utterance = new SpeechSynthesisUtterance(phrase);
    utterance.lang = 'zh-CN';
    applyVoiceSettings(utterance);
    utterance.onend = utterance.onerror = function() { btn.classList.remove('speaking'); };
    setTimeout(function(){ speechSynthesis.speak(utterance); }, 30);
};

window._isSpeakingFull = false;
window._speakToken = 0;

function _setSpeakBtnState(speaking) {
    window._isSpeakingFull = speaking;
    var btn = $('pfSpeakBtn');
    if (!btn) return;
    if (speaking) {
        btn.classList.add('speaking');
        btn.setAttribute('title', 'Nhấn để dừng');
        btn.setAttribute('aria-label', 'Nhấn để dừng');
        var i = btn.querySelector('i');
        if (i) i.className = 'fas fa-stop';
    } else {
        btn.classList.remove('speaking');
        btn.setAttribute('title', 'Nghe câu này');
        btn.setAttribute('aria-label', 'Nghe câu này');
        var i2 = btn.querySelector('i');
        if (i2) i2.className = 'fas fa-volume-up';
    }
}

window.stopSpeakFull = function() {
    window._speakToken++;
    window._isSpeakingFull = false;
    if ('speechSynthesis' in window) {
        try { speechSynthesis.cancel(); } catch(e) {}
    }
    var charsContainer = $('pfAnswerChars');
    if (charsContainer) {
        charsContainer.querySelectorAll('.answer-phrase-btn.reading, .answer-phrase-btn.speaking').forEach(function(b) {
            b.classList.remove('reading', 'speaking');
        });
        charsContainer.querySelectorAll('.answer-phrase-tooltip.show').forEach(function(t) {
            t.classList.remove('show');
        });
        charsContainer.querySelectorAll('.answer-phrase-wrap.active-wrap').forEach(function(w) {
            w.classList.remove('active-wrap');
        });
    }
    _activeTooltipWrap = null;
    _setSpeakBtnState(false);
};

window.toggleSpeakFull = function() {
    if (!pfCurrentAnswer) return;
    if (window._isSpeakingFull) { stopSpeakFull(); return; }
    if (window._isQuickSpeaking) stopQuickSpeak();
    if (!canUseFeature()) { showLimitMessage(); return; }
    if (!('speechSynthesis' in window)) {
        alert('Trình duyệt không hỗ trợ phát âm.');
        return;
    }
    if (shouldCountUsage()) { incDemoUsage(); updateDemoRemaining(); }
    if ('speechSynthesis' in window) {
        try { speechSynthesis.cancel(); } catch(e) {}
    }
    var token = ++window._speakToken;
    _setSpeakBtnState(true);

    var answerVisible = $('pfAnswer').classList.contains('show');
    if (answerVisible) {
        _speakWithHighlightKaraoke(token);
    } else {
        _speakNormal(token);
    }
};

function _speakNormal(token) {
    var u = new SpeechSynthesisUtterance(pfCurrentAnswer);
    u.lang = 'zh-CN';
    applyVoiceSettings(u);
    var done = false;
    function finish() {
        if (done) return;
        done = true;
        if (token !== window._speakToken) return;
        _setSpeakBtnState(false);
    }
    u.onend = finish;
    u.onerror = finish;
    setTimeout(function() {
        if (token !== window._speakToken) return;
        try { speechSynthesis.speak(u); } catch(e) { finish(); }
    }, 30);
}

function _speakWithHighlightKaraoke(token) {
    var phrases = window._pfPhrases || [];
    var charsContainer = $('pfAnswerChars');
    if (!charsContainer) { _setSpeakBtnState(false); return; }
    var wraps = charsContainer.querySelectorAll('.answer-phrase-wrap');
    var buttons = charsContainer.querySelectorAll('.answer-phrase-btn');
    if (phrases.length === 0) { _speakNormal(token); return; }
    var idx = 0;

    function cleanupAll() {
        buttons.forEach(function(b) { b.classList.remove('reading'); });
        charsContainer.querySelectorAll('.answer-phrase-tooltip.show').forEach(function(t) {
            t.classList.remove('show');
        });
        charsContainer.querySelectorAll('.answer-phrase-wrap.active-wrap').forEach(function(w) {
            w.classList.remove('active-wrap');
        });
        _activeTooltipWrap = null;
    }

    function speakNext() {
        if (token !== window._speakToken) { cleanupAll(); return; }
        if (idx >= phrases.length) {
            cleanupAll();
            _setSpeakBtnState(false);
            return;
        }
        var phrase = phrases[idx];
        var btn = buttons[idx];
        var wrap = wraps[idx];

        if (btn) btn.classList.add('reading');
        if (wrap) {
            wrap.classList.add('active-wrap');
            charsContainer.querySelectorAll('.answer-phrase-tooltip.show').forEach(function(t) {
                t.classList.remove('show');
            });
            var tip = wrap.querySelector('.answer-phrase-tooltip');
            if (tip) {
                tip.classList.add('show');
                _activeTooltipWrap = wrap;
            }
        }

        var u = new SpeechSynthesisUtterance(phrase.text);
        u.lang = 'zh-CN';
        applyVoiceSettings(u);

        var handled = false;
        function next() {
            if (handled) return;
            handled = true;
            if (btn) btn.classList.remove('reading');
            if (wrap) wrap.classList.remove('active-wrap');
            if (token !== window._speakToken) { cleanupAll(); return; }
            idx++;
            setTimeout(speakNext, 120);
        }
        u.onend = next;
        u.onerror = next;
        setTimeout(function() {
            if (token !== window._speakToken) { next(); return; }
            try { speechSynthesis.speak(u); } catch(e) { next(); }
        }, 30);
    }

    setTimeout(speakNext, 100);
}

window._isQuickSpeaking = false;
window._quickSpeakToken = 0;

function _setQuickSpeakBtnState(speaking) {
    window._isQuickSpeaking = speaking;
    var btn = $('pfQuickSpeakBtn');
    if (!btn) return;
    if (speaking) {
        btn.classList.add('speaking');
        btn.setAttribute('title', 'Nhấn để dừng');
        btn.setAttribute('aria-label', 'Nhấn để dừng');
        var i = btn.querySelector('i');
        if (i) i.className = 'fas fa-stop';
    } else {
        btn.classList.remove('speaking');
        btn.setAttribute('title', 'Đọc cả câu');
        btn.setAttribute('aria-label', 'Đọc cả câu');
        var i2 = btn.querySelector('i');
        if (i2) i2.className = 'fas fa-volume-up';
    }
}

window.stopQuickSpeak = function() {
    window._quickSpeakToken++;
    window._isQuickSpeaking = false;
    if ('speechSynthesis' in window) {
        try { speechSynthesis.cancel(); } catch(e) {}
    }
    _setQuickSpeakBtnState(false);
};

window.toggleQuickSpeakFull = function() {
    if (!pfCurrentAnswer) return;
    if (window._isQuickSpeaking) { stopQuickSpeak(); return; }
    if (window._isSpeakingFull) stopSpeakFull();
    if (!canUseFeature()) { showLimitMessage(); return; }
    if (!('speechSynthesis' in window)) {
        alert('Trình duyệt không hỗ trợ phát âm.');
        return;
    }
    if (shouldCountUsage()) { incDemoUsage(); updateDemoRemaining(); }
    if ('speechSynthesis' in window) {
        try { speechSynthesis.cancel(); } catch(e) {}
    }
    var token = ++window._quickSpeakToken;
    _setQuickSpeakBtnState(true);
    _quickSpeakNormal(token);
};

function _quickSpeakNormal(token) {
    var u = new SpeechSynthesisUtterance(pfCurrentAnswer);
    u.lang = 'zh-CN';
    applyVoiceSettings(u);
    var done = false;
    function finish() {
        if (done) return;
        done = true;
        if (token !== window._quickSpeakToken) return;
        _setQuickSpeakBtnState(false);
    }
    u.onend = finish;
    u.onerror = finish;
    setTimeout(function() {
        if (token !== window._quickSpeakToken) return;
        try { speechSynthesis.speak(u); } catch(e) { finish(); }
    }, 30);
}

function initPracticeFull() {
    /* ═══════════════════════════════════════════════════════════
       ⬇️ AUTO-GROW TEXTAREA — Ô nhập tự giãn khi gõ câu dài
       ═══════════════════════════════════════════════════════════ */
    (function setupAutoGrow() {
        var inp = $('pfInput');
        if (!inp) return;

        function autoGrow() {
            if (!inp || inp.tagName !== 'TEXTAREA') return;
            inp.style.height = 'auto';
            var newH = inp.scrollHeight;
            var maxH = Math.floor(window.innerHeight * 0.4);
            if (newH > maxH) {
                inp.style.height = maxH + 'px';
                inp.style.overflowY = 'auto';
            } else {
                inp.style.height = newH + 'px';
                inp.style.overflowY = 'hidden';
            }
            var lineH = parseFloat(getComputedStyle(inp).lineHeight) || 20;
            var hasMultiline = newH > (lineH * 1.5 + 20);
            inp.classList.toggle('multiline', hasMultiline);
        }

        inp.addEventListener('input', autoGrow);
        inp.addEventListener('paste', function() { setTimeout(autoGrow, 0); });
        window.addEventListener('resize', autoGrow);

        var orig = window.loadPracticeFull;
        if (typeof orig === 'function' && !orig.__autoGrowPatched) {
            window.loadPracticeFull = function(stt) {
                var r = orig.apply(this, arguments);
                var i2 = $('pfInput');
                if (i2 && i2.tagName === 'TEXTAREA') {
                    i2.style.height = 'auto';
                    i2.style.overflowY = 'hidden';
                    i2.classList.remove('multiline');
                }
                return r;
            };
            window.loadPracticeFull.__autoGrowPatched = true;
        }

        autoGrow();
    })();

    /* ═══════════════════════════════════════════════════════════
       Random mode init
       ═══════════════════════════════════════════════════════════ */
    try {
        var savedRandom = localStorage.getItem('pfRandomMode') === '1';
        if (savedRandom) {
            pfRandomMode = true;
            var rBtnInit = $('pfRandomToggleBtn');
            if (rBtnInit) {
                rBtnInit.classList.add('active');
                rBtnInit.title = 'ĐANG BẬT: Nút Next sẽ nhảy câu ngẫu nhiên';
            }
        }
    } catch(e) {}

    /* Random toggle button */
    var randomToggleBtn = $('pfRandomToggleBtn');
    if (randomToggleBtn) {
        randomToggleBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            e.preventDefault();
            pfToggleRandom();
        });
    }

    /* Nút đóng modal */
    $('pfClose').addEventListener('click', closePracticeFull);

    /* Nút prev / next */
    $('pfPrevBtn').addEventListener('click', pfPrev);
    $('pfNextBtn').addEventListener('click', pfNext);

    /* Nút reveal / hint */
    $('pfRevealBtn').addEventListener('click', revealFullAnswer);
    $('pfHintBtn').addEventListener('click', toggleHint);

    /* Input — update preview + check */
    $('pfInput').addEventListener('input', function() {
        updateCharPreview();
        checkFullAnswer();
    });

    /* Quick nav */
    $('pfQuickNav').addEventListener('change', pfQuickNavChange);

    /* Search trong modal */
    $('pfSearchInput').addEventListener('input', function() { pfApplyFilter(); });
    $('pfClearSearchBtn').addEventListener('click', function() {
        $('pfSearchInput').value = '';
        $('pfSearchInput').focus();
        pfApplyFilter();
    });

    /* HSK filter trong modal */
    $('pfHskFilter').addEventListener('change', function() {
        var val = this.value;
        var allowed = getAllowedHskList();
        if (val && allowed.indexOf(val) === -1) {
            var info = getTierInfo();
            var msg = info.tier === 'trial'
                ? 'Bản Trial chỉ cho phép lọc HSK1-' + info.maxHSK + '.'
                : 'Bản Demo chỉ cho phép lọc HSK1-' + info.maxHSK + '.';
            alert(msg);
            this.value = '';
            return;
        }
        pfApplyFilter();
    });

    /* Subject filter trong modal */
    $('pfSubjectFilter').addEventListener('change', function() {
        var val = this.value;
        var allowed = getAllowedSubjectList();
        if (val && allowed.indexOf(val) === -1) {
            var info = getTierInfo();
            var msg = info.tier === 'trial'
                ? 'Chủ đề này chưa có trong ' + info.maxQuestions + ' câu Trial.'
                : 'Chủ đề này chưa có trong ' + info.maxQuestions + ' câu Demo.';
            alert(msg);
            this.value = '';
            return;
        }
        pfApplyFilter();
    });

    /* ═══════════════════════════════════════════════════════════
       KEYBOARD SHORTCUTS
       - Enter (không shift/ctrl): xuống dòng trong textarea
       - Ctrl + Arrow: prev / next
       - R: toggle random
       - Escape: đóng modal
       ═══════════════════════════════════════════════════════════ */
    document.addEventListener('keydown', function(e) {
        if (!$('practiceFullModal').classList.contains('show')) return;
        var active = document.activeElement;
        var isTyping = active && (
            active.tagName === 'INPUT' ||
            active.tagName === 'TEXTAREA' ||
            active.tagName === 'SELECT'
        );

        if (e.key === 'Escape') { closePracticeFull(); return; }

        /* Cho phép Enter xuống dòng bình thường trong textarea */
        if (e.key === 'Enter' && !e.shiftKey && !e.ctrlKey) return;

        if (isTyping) return;
        if (e.key === 'ArrowRight' && e.ctrlKey) pfNext();
        if (e.key === 'ArrowLeft' && e.ctrlKey) pfPrev();
        if (e.key === 'r' || e.key === 'R') pfToggleRandom();
    });

    /* ═══════════════════════════════════════════════════════════
       SWIPE GESTURE (mobile)
       ═══════════════════════════════════════════════════════════ */
    var modal = $('practiceFullModal');
    var touchStartX = 0;
    modal.addEventListener('touchstart', function(e) {
        touchStartX = e.touches[0].clientX;
    }, { passive: true });
    modal.addEventListener('touchend', function(e) {
        var dx = e.changedTouches[0].clientX - touchStartX;
        if (Math.abs(dx) > 100) {
            if (dx < 0) pfNext();
            else pfPrev();
        }
    }, { passive: true });

    /* ═══════════════════════════════════════════════════════════
       Nút loa trong ô nhập — toggle speak full
       ═══════════════════════════════════════════════════════════ */
    if (!window._pfSpeakBound) {
        window._pfSpeakBound = true;
        var speakBtn = $('pfSpeakBtn');
        if (speakBtn) {
            speakBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                toggleSpeakFull();
            });
        }
    }

    /* ═══════════════════════════════════════════════════════════
       Nút loa dưới nav — toggle quick speak
       ═══════════════════════════════════════════════════════════ */
    if (!window._pfQuickSpeakBound) {
        window._pfQuickSpeakBound = true;
        var quickBtn = $('pfQuickSpeakBtn');
        if (quickBtn) {
            quickBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                e.preventDefault();
                toggleQuickSpeakFull();
            });
        }
    }
}
function pfBuildDatasetSelect() {
    var sel = $('pfDatasetSelect');
    var row = $('pfDatasetRow');
    if (!sel) return;

    if (!window.__dataLoaded) {
        if (window.__dataLoadPromise) {
            window.__dataLoadPromise.then(function() { pfBuildDatasetSelect(); });
        }
        return;
    }

    var canAccessAll = canAccessChuyenNganh();
    var current = (typeof CURRENT_DATASET !== 'undefined') ? CURRENT_DATASET : 'tonghop';

    sel.innerHTML = '';

    // ═══════════════════════════════════════════════════════════
    //  BƯỚC 1: Thêm dataset từ DATASET_REGISTRY (tổng hợp + chuyên ngành)
    // ═══════════════════════════════════════════════════════════
    if (typeof DATASET_REGISTRY !== 'undefined' && DATASET_REGISTRY) {
        Object.keys(DATASET_REGISTRY).forEach(function(id) {
            var ds = DATASET_REGISTRY[id];
            var isTonghop = (id === 'tonghop');
            var isLocked = !isTonghop && !canAccessAll;

            var opt = document.createElement('option');
            opt.value = id;
            if (isLocked) {
                opt.dataset.locked = '1';
                opt.className = 'locked-opt';
            }

            var dsName = ds.name && ds.name.normalize
                         ? ds.name.normalize('NFC')
                         : ds.name;

            if (isTonghop) {
                opt.textContent = (ds.count || 0) + ' câu - Tổng hợp VPCX';
            } else {
                opt.textContent = (isLocked ? '[Khoá] ' : '') +
                                  dsName + ' (' + (ds.count || 0) + ' câu)';
            }

            sel.appendChild(opt);
        });
    }

    // ═══════════════════════════════════════════════════════════
    //  BƯỚC 2: Thêm dataset từ FIXPY_DATASETS (tab "1000 Câu giao tiếp")
    //  → KHÔNG có lock (giống tab Tổng hợp)
    // ═══════════════════════════════════════════════════════════
    if (window.FIXPY_DATASETS && typeof window.FIXPY_DATASETS === 'object') {
        Object.keys(window.FIXPY_DATASETS).forEach(function(id) {
            // Skip nếu trùng với DATASET_REGISTRY
            if (typeof DATASET_REGISTRY !== 'undefined' && DATASET_REGISTRY[id]) return;

            var ds = window.FIXPY_DATASETS[id];
            var opt = document.createElement('option');
            opt.value = id;

            var dsName = ds.name && ds.name.normalize
                         ? ds.name.normalize('NFC')
                         : ds.name;

            opt.textContent = dsName + ' (' + (ds.count || 0) + ' câu)';

            sel.appendChild(opt);
        });
    }

    // ═══════════════════════════════════════════════════════════
    //  BƯỚC 3: Set giá trị hiện tại
    // ═══════════════════════════════════════════════════════════
    var currentIsValid = false;
    for (var i = 0; i < sel.options.length; i++) {
        if (sel.options[i].value === current) {
            currentIsValid = true;
            break;
        }
    }

    if (currentIsValid) {
        sel.value = current;
    } else {
        // Fallback: nếu current không có trong options → về tonghop
        sel.value = 'tonghop';
    }

    // ═══════════════════════════════════════════════════════════
    //  BƯỚC 4: Đánh dấu row có locked options
    // ═══════════════════════════════════════════════════════════
    if (row) {
        var hasLock = !canAccessAll
                      && typeof DATASET_REGISTRY !== 'undefined'
                      && Object.keys(DATASET_REGISTRY).length > 1;
        row.classList.toggle('has-locked-options', hasLock);
    }
}

document.addEventListener('change', function(e) {
    if (!e.target || e.target.id !== 'pfDatasetSelect') return;

    var sel = e.target;
    var val = sel.value;
    var opt = sel.options[sel.selectedIndex];
    var currentDataset = (typeof CURRENT_DATASET !== 'undefined') ? CURRENT_DATASET : 'tonghop';

    if (opt && opt.dataset.locked === '1') {
        sel.value = currentDataset;
        showPracticeFullLockMessage();
        return;
    }

    if (val !== 'tonghop' && !canAccessChuyenNganh()) {
        sel.value = currentDataset;
        showPracticeFullLockMessage();
        return;
    }

    var ok = (typeof window.__switchRawData === 'function')
             ? window.__switchRawData(val)
             : false;
    if (!ok) {
        sel.value = currentDataset;
        return;
    }

    window.__onboardingOverride = null;
    var obBanner = $('onboardingActiveBanner');
    if (obBanner) obBanner.remove();

    state = { search:'', hsk:'', subject:'' };
    if ($('pfSearchInput')) $('pfSearchInput').value = '';
    if ($('pfHskFilter')) $('pfHskFilter').value = '';
    if ($('pfSubjectFilter')) $('pfSubjectFilter').value = '';
    if ($('searchInput')) $('searchInput').value = '';
    if ($('hskFilter')) $('hskFilter').value = '';
    if ($('subjectFilter')) $('subjectFilter').value = '';

    if (typeof pfBuildFilterOptions === 'function') pfBuildFilterOptions();

    if (typeof pfApplyFilter === 'function') {
        pfApplyFilter();
    } else if (typeof applyFilter === 'function') {
        applyFilter();
    }

    if (typeof filtered !== 'undefined' && filtered.length > 0) {
        if (typeof loadPracticeFull === 'function') {
            loadPracticeFull(filtered[0].stt);
        }
    }

    pfBuildDatasetSelect();
});

/* ============================================================ */
/* WRITER (Luyện viết chữ Hán) — expired dùng được như Demo      */
/* ============================================================ */
var writerInstance = null;
var currentWriteZh = '';
var currentWriteVi = '';
var currentWritePinyin = '';
var currentCharIndex = 0;

function initWriter() {
    $('writerAnimate').addEventListener('click', function() {
        if (!writerInstance) return;
        $('writerScore').textContent = '';
        $('writerScore').className = 'writer-score';
        writerInstance.cancelQuiz();
        writerInstance.animateCharacter();
    });
    $('writerQuiz').addEventListener('click', function() {
        if (!writerInstance) return;
        $('writerScore').textContent = 'Vẽ chữ bằng ngón tay...';
        $('writerScore').className = 'writer-score';
        writerInstance.quiz({
            onMistake: function(strokeData) {
                $('writerScore').textContent = 'Sai nét ' + (strokeData.strokeNum + 1) + ' - thử lại';
                $('writerScore').className = 'writer-score error';
            },
            onComplete: function(summary) {
                if (summary.totalMistakes === 0) {
                    $('writerScore').textContent = 'Tuyệt vời! Viết đúng tất cả các nét!';
                    $('writerScore').className = 'writer-score success';
                } else {
                    $('writerScore').textContent = 'Hoàn thành! Số nét sai: ' + summary.totalMistakes;
                    $('writerScore').className = 'writer-score';
                }
            }
        });
    });
    $('writerReset').addEventListener('click', function() {
        if (!writerInstance) return;
        $('writerScore').textContent = '';
        $('writerScore').className = 'writer-score';
        writerInstance.cancelQuiz();
        var chars = currentWriteZh.split('').filter(function(c) { return /[\u4e00-\u9fa5]/.test(c); });
        var currentChar = chars[currentCharIndex];
        if (currentChar) showWriterChar(currentChar);
    });
    $('writerClose').addEventListener('click', closeWriter);
    $('writerModal').addEventListener('click', function(e) {
        if (e.target === this) closeWriter();
    });
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeWriter();
    });
}

window.openWriter = function(zh, vi, pinyin, evt) {
    if (evt) { evt.stopPropagation(); if (evt.preventDefault) evt.preventDefault(); }
    if (!canUseFeature()) { showLimitMessage(); return; }
    if (typeof HanziWriter === 'undefined') { alert('Thư viện chưa tải xong.'); return; }
    if (shouldCountUsage()) { incDemoUsage(); updateDemoRemaining(); }
    currentWriteZh = zh || '';
    currentWriteVi = vi || '';
    currentWritePinyin = pinyin || '';
    currentCharIndex = 0;
    var chars = currentWriteZh.split('').filter(function(c) { return /[\u4e00-\u9fa5]/.test(c); });
    if (chars.length === 0) { alert('Câu này không có chữ Hán.'); return; }
    $('writerModal').classList.add('show');
    $('writerScore').textContent = '';
    $('writerScore').className = 'writer-score';
    $('writerViSmall').textContent = currentWriteVi;
    $('writerPinyinSmall').textContent = currentWritePinyin;
    renderWriterChars(chars);
    showWriterChar(chars[0]);
};

window.closeWriter = function() {
    $('writerModal').classList.remove('show');
    writerInstance = null;
};

function renderWriterChars(chars) {
    var container = $('writerChars');
    if (chars.length <= 1) { container.innerHTML = ''; return; }
    container.innerHTML = chars.map(function(c, i) {
        return '<button class="writer-char-btn' + (i === 0 ? ' active' : '') + '" data-idx="' + i + '" data-char="' + c + '">' + c + '</button>';
    }).join('');
    container.querySelectorAll('.writer-char-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var idx = parseInt(this.dataset.idx);
            var ch = this.dataset.char;
            container.querySelectorAll('.writer-char-btn').forEach(function(b) { b.classList.remove('active'); });
            this.classList.add('active');
            currentCharIndex = idx;
            $('writerScore').textContent = '';
            $('writerScore').className = 'writer-score';
            showWriterChar(ch);
        });
    });
}

function showWriterChar(char) {
    var target = $('writerTarget');
    target.innerHTML = '<div class="writer-loading"><i class="fas fa-spinner fa-pulse"></i>Đang tải...</div>';
    writerInstance = null;
    setTimeout(function() {
        try {
            target.innerHTML = '';
            var targetSize = target.offsetWidth || 280;
            var padSize = Math.round(targetSize * 0.06);
            var drawWidth = Math.round(targetSize * 0.07);
            writerInstance = HanziWriter.create('writerTarget', char, {
                width: targetSize, height: targetSize, padding: padSize,
                strokeColor: '#1e293b', radicalColor: '#7c3aed',
                highlightColor: '#f59e0b', outlineColor: '#cbd5e1',
                drawingColor: '#7c3aed', drawingWidth: drawWidth,
                showOutline: true, strokeAnimationSpeed: 1, delayBetweenStrokes: 250,
                charDataLoader: function(ch, onComplete, onError) {
                    fetch('https://cdn.jsdelivr.net/npm/hanzi-writer-data@2.0/' + encodeURIComponent(ch) + '.json')
                        .then(function(res) { if (!res.ok) throw new Error('Không có dữ liệu'); return res.json(); })
                        .then(onComplete)
                        .catch(function(err) {
                            if (onError) onError(err);
                            target.innerHTML = '<div class="writer-loading"><i class="fas fa-exclamation-triangle" style="color:#dc2626"></i>Không tải được dữ liệu.</div>';
                        });
                }
            });
        } catch(e) {
            target.innerHTML = '<div class="writer-loading"><i class="fas fa-exclamation-triangle"></i>Lỗi tạo khung vẽ</div>';
        }
    }, 100);
}
/* ═══════════════════════════════════════════════════════════════
   ❤️ FAVORITES BRIDGE — Build nút tim cho card
   ═══════════════════════════════════════════════════════════════ */
function favBuildFavButton(stt) {
    if (typeof favCanUse !== 'function') return '';

    var can = favCanUse();
    var currentDsId = (typeof CURRENT_DATASET !== 'undefined' && CURRENT_DATASET)
                      ? CURRENT_DATASET
                      : 'tonghop';

    var active = typeof favHas === 'function' ? favHas(stt, currentDsId) : false;

    var sttJs = escapeJs(stt);
    var sttSafe = escapeHtml(stt);
    var dsSafe = escapeHtml(currentDsId);

    var iconClass = !can ? 'fas fa-lock' : (active ? 'fas fa-heart' : 'far fa-heart');
    var title = !can
        ? 'Cần gia hạn để dùng Yêu thích'
        : (active ? 'Xoá khỏi yêu thích' : 'Thêm vào yêu thích');

    return '<button class="fav-btn' +
        (active ? ' active' : '') +
        (!can ? ' locked' : '') +
        '" data-stt="' + sttSafe + '" ' +
        'data-dataset-id="' + dsSafe + '" ' +
        'onclick="favOnCardBtnClick(event, \'' + sttJs + '\')" ' +
        'title="' + title + '">' +
        '<i class="' + iconClass + '"></i>' +
        '</button>';
}
window.pfApplyFilter = pfApplyFilter;
window.pfBuildQuickNav = pfBuildQuickNav;
window.pfUpdateFilterUI = pfUpdateFilterUI;
"""
