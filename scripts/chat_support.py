# -*- coding: utf-8 -*-
"""Chat Support + Quota Dashboard + User Online"""

import json


def build_chat_css():
    return r"""
.chat-float-btn{display:flex;align-items:center;gap:.5rem;padding:.7rem 1.1rem;border-radius:50px;background:linear-gradient(135deg, #4f46e5, #7c3aed, #a855f7);color:#fff;text-decoration:none;font-weight:700;font-size:.85rem;box-shadow:0 8px 24px rgba(124,58,237,.45);transition:all .35s cubic-bezier(.34,1.56,.64,1);-webkit-tap-highlight-color:transparent;white-space:nowrap;border:2px solid #fff;font-family:inherit;overflow:visible;position:relative;cursor:pointer;}
.chat-float-btn:hover,.chat-float-btn:active{transform:scale(1.05);box-shadow:0 12px 32px rgba(124,58,237,.65),0 0 0 6px rgba(139,92,246,.2);color:#fff;}
.chat-float-btn i.fa-comments{font-size:1.2rem;flex-shrink:0;line-height:1;position:relative;z-index:2;}
.chat-float-btn .chat-text{line-height:1.15;display:flex;flex-direction:column;position:relative;z-index:2;transition:opacity .2s, max-width .35s;max-width:200px;overflow:hidden;}
.chat-float-btn .chat-label{font-size:.65rem;opacity:.85;font-weight:500;white-space:nowrap}
.chat-float-btn .chat-name{font-size:.85rem;font-weight:700;white-space:nowrap}
.chat-float-btn::before{content:'';position:absolute;inset:0;border-radius:50px;background:linear-gradient(135deg, #4f46e5, #a855f7);opacity:0;z-index:1;pointer-events:none;transition:opacity .3s ease;}
.chat-float-btn.intro-glow{animation:chatIntroGlow 1.8s cubic-bezier(.4,0,.2,1) 1;}
@keyframes chatIntroGlow{
    0%{box-shadow:0 8px 24px rgba(124,58,237,.45),0 0 0 0 rgba(139,92,246,.6);}
    70%{box-shadow:0 8px 28px rgba(124,58,237,.7),0 0 0 16px rgba(139,92,246,0);}
    100%{box-shadow:0 8px 24px rgba(124,58,237,.45),0 0 0 0 rgba(139,92,246,0);}
}
.chat-float-btn.has-unread{background:linear-gradient(135deg, #dc2626, #b91c1c, #7f1d1d);animation:chatUrgentPulse 1.2s infinite;box-shadow:0 8px 24px rgba(220,38,38,.6);}
.chat-float-btn.has-unread::before{opacity:.5;background:linear-gradient(135deg, #dc2626, #7f1d1d);animation:chatUrgentPulse 1.2s infinite;}
.chat-float-btn.has-unread i.fa-comments{animation:chatBellShake 0.6s infinite;color:#fde68a;text-shadow:0 0 8px rgba(253,230,138,.9);}
@keyframes chatBellShake{0%,100%{transform:rotate(0deg);}15%{transform:rotate(-15deg);}30%{transform:rotate(15deg);}45%{transform:rotate(-12deg);}60%{transform:rotate(12deg);}75%{transform:rotate(-6deg);}}
@keyframes chatUrgentPulse{0%,100%{transform:scale(1);box-shadow:0 8px 24px rgba(220,38,38,.6),0 0 0 0 rgba(220,38,38,.7);}50%{transform:scale(1.08);box-shadow:0 12px 32px rgba(220,38,38,.8),0 0 0 14px rgba(220,38,38,0);}}
.chat-float-btn .chat-badge{position:absolute;top:-6px;right:-6px;min-width:24px;height:24px;padding:0 .45rem;border-radius:50px;background:linear-gradient(135deg,#fbbf24,#f59e0b);color:#1e1b4b;font-size:.72rem;font-weight:900;display:none;align-items:center;justify-content:center;border:2.5px solid #fff;line-height:1;box-shadow:0 3px 10px rgba(251,191,36,.7);animation:chatBadgeBounce 0.8s infinite;z-index:5;}
.chat-float-btn.has-unread .chat-badge{background:linear-gradient(135deg,#fff,#fef3c7);color:#dc2626;box-shadow:0 3px 12px rgba(255,255,255,.8),0 0 0 2px #dc2626;}
.chat-float-btn .chat-badge.show{display:flex}
@keyframes chatBadgeBounce{0%,100%{transform:scale(1);}50%{transform:scale(1.18);}}
.chat-float-btn.hidden{display:none}
@media (max-width:768px){
    .chat-float-btn{width:46px;height:46px;padding:0;border-radius:50%;justify-content:center;gap:0;}
    .chat-float-btn i.fa-comments{font-size:1.25rem;}
    .chat-float-btn .chat-text{opacity:0;max-width:0;overflow:hidden;}
    .chat-float-btn::before{border-radius:50%;}
    .chat-float-btn .chat-badge{top:-4px;right:-4px;min-width:20px;height:20px;font-size:.65rem;border-width:2px;}
    .chat-float-btn:hover,.chat-float-btn:active{transform:scale(1.08);}
}
@media (max-width:400px){
    .chat-float-btn{width:42px;height:42px;}
    .chat-float-btn i.fa-comments{font-size:1.1rem;}
}

#chatFloatWrap{position:fixed;right:50px;bottom:calc(16px + env(safe-area-inset-bottom));left:auto;top:auto;z-index:9998;display:flex;flex-direction:column;align-items:flex-end;gap:.55rem;pointer-events:none;transition:opacity .3s ease, transform .3s ease;opacity:1;transform:translateY(0);}
#chatFloatWrap > *{pointer-events:auto;}
#chatFloatWrap.hidden{display:flex;opacity:0;transform:translateY(12px);pointer-events:none;}
body.chat-is-open #chatFloatWrap{z-index:3999;}
body.has-floating-group #chatFloatWrap{bottom:calc(16px + env(safe-area-inset-bottom));}

#chatFloatBtn{position:relative;width:56px;height:56px;border-radius:50%;padding:0;justify-content:center;gap:0;transition:transform .3s cubic-bezier(.34,1.56,.64,1), box-shadow .3s, background .3s;}
#chatFloatBtn .chat-text{display:none !important;}
#chatFloatBtn i.fa-comments{font-size:1.35rem;}
#chatFloatBtn.menu-open{transform:rotate(45deg) scale(1.05);}

#chatFloatMenu{display:flex;flex-direction:column;align-items:flex-end;gap:.55rem;opacity:0;transform:translateY(20px) scale(0.8);pointer-events:none;transition:opacity .25s ease, transform .3s cubic-bezier(.34,1.56,.64,1);transform-origin:bottom right;margin-bottom:.55rem;}
#chatFloatMenu.show{opacity:1;transform:translateY(0) scale(1);pointer-events:auto;}

.chat-float-sub{width:50px;height:50px;border-radius:50%;border:2px solid #fff;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1.15rem;padding:0;position:relative;transition:transform .25s cubic-bezier(.34,1.56,.64,1), box-shadow .25s;font-family:inherit;-webkit-tap-highlight-color:transparent;box-shadow:0 6px 18px rgba(0,0,0,.25);}
.chat-float-sub:hover,.chat-float-sub:active{transform:scale(1.12);}
.chat-float-sub.chat-sub{background:linear-gradient(135deg, #4f46e5, #7c3aed);box-shadow:0 6px 18px rgba(124,58,237,.5);}
.chat-float-sub.chat-sub:hover{box-shadow:0 10px 26px rgba(124,58,237,.7);}
.chat-float-sub.manager-sub{background:linear-gradient(135deg, #059669, #10b981);box-shadow:0 6px 18px rgba(16,185,129,.5);}
.chat-float-sub.manager-sub:hover{box-shadow:0 10px 26px rgba(16,185,129,.7);}
.chat-float-sub .sub-badge{position:absolute;top:-5px;right:-5px;min-width:20px;height:20px;padding:0 .35rem;border-radius:50px;background:#dc2626;color:#fff;font-size:.62rem;font-weight:900;display:none;align-items:center;justify-content:center;border:2px solid #fff;line-height:1;animation:chatBadgeBounce 0.8s infinite;}
.chat-float-sub .sub-badge.show{display:flex;}

@media (max-width:768px){
    #chatFloatWrap{right:40px;bottom:calc(14px + env(safe-area-inset-bottom));}
    #chatFloatBtn{width:50px;height:50px;}
    #chatFloatBtn i.fa-comments{font-size:1.2rem;}
    .chat-float-sub{width:44px;height:44px;font-size:1rem;}
}
@media (max-width:400px){
    #chatFloatWrap{right:36px;bottom:calc(12px + env(safe-area-inset-bottom));}
}

.chat-modal{position:fixed;inset:0;background:transparent;z-index:4000;display:none;padding:0;pointer-events:none;}
.chat-modal.show{display:block;pointer-events:auto;}
.chat-box{position:fixed;right:20px;top:80px;left:auto;bottom:auto;background:#fff;border-radius:18px;width:360px;height:30vh;min-height:260px;max-height:calc(100vh - 120px);box-shadow:0 16px 48px rgba(0,0,0,.28),0 0 0 1px rgba(0,0,0,.05);display:flex;flex-direction:column;overflow:hidden;transform-origin:bottom right;animation:chatPopIn .28s cubic-bezier(.34,1.56,.64,1);transition:width .3s cubic-bezier(.4,0,.2,1), height .3s cubic-bezier(.4,0,.2,1), right .35s cubic-bezier(.34,1.56,.64,1), top .35s cubic-bezier(.34,1.56,.64,1), border-radius .3s;pointer-events:auto;z-index:4001;}
@keyframes chatPopIn{from{opacity:0;transform:scale(.85) translateY(20px);}to{opacity:1;transform:scale(1) translateY(0);}}
[data-theme="dark"] .chat-box{background:#1e293b;box-shadow:0 16px 48px rgba(0,0,0,.7),0 0 0 1px rgba(255,255,255,.08);}
.chat-box::before{content:'';position:absolute;bottom:-14px;left:var(--arrow-left,22px);width:0;height:0;border-left:14px solid transparent;border-right:14px solid transparent;border-top:14px solid #fff;filter:drop-shadow(0 2px 3px rgba(0,0,0,.08));pointer-events:none;z-index:1;transition:left .35s cubic-bezier(.34,1.56,.64,1);}
[data-theme="dark"] .chat-box::before{border-top-color:#1e293b;}
.chat-box::after{content:'';position:absolute;bottom:-10px;left:calc(var(--arrow-left,22px) + 2px);width:0;height:0;border-left:12px solid transparent;border-right:12px solid transparent;border-top:12px solid #4f46e5;pointer-events:none;z-index:2;transition:left .35s cubic-bezier(.34,1.56,.64,1);}
.chat-box.admin-thread-open{height:55vh;min-height:420px;max-height:calc(100vh - 80px);}
@media (max-width:600px){
    .chat-box{width:calc(100vw - 24px);height:30vh;min-height:240px;max-height:calc(100vh - 90px);border-radius:18px;}
    .chat-box::before,.chat-box::after{display:none;}
    .chat-box.admin-thread-open{height:55vh;min-height:400px;max-height:calc(100vh - 70px);}
}
@media (max-width:400px){
    .chat-box{width:calc(100vw - 16px);height:30vh;min-height:220px;}
    .chat-box.admin-thread-open{height:60vh;min-height:380px;}
}

.chat-header{padding:1rem 1.25rem;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;display:flex;align-items:center;gap:.75rem;flex-shrink:0;}
.chat-header-back{width:34px;height:34px;border-radius:50%;border:none;background:rgba(255,255,255,.15);color:#fff;cursor:pointer;display:none;align-items:center;justify-content:center;font-size:.95rem;flex-shrink:0;}
.chat-header-back.show{display:flex}
.chat-header-info{flex:1;min-width:0}
.chat-header-info .name{font-weight:800;font-size:.95rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.chat-header-info .status{font-size:.72rem;opacity:.9;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.chat-header .chat-counter{font-size:.65rem;opacity:.85;padding:.15rem .5rem;border-radius:50px;background:rgba(255,255,255,.2);white-space:nowrap;flex-shrink:0;display:none;}
.chat-header .chat-counter.show{display:inline-block}
.chat-header .chat-counter.warn{background:rgba(251,191,36,.35);color:#fef3c7;font-weight:800;}
.chat-header .chat-counter.danger{background:rgba(220,38,38,.5);color:#fff;font-weight:800;animation:chatLimitPulse 1.5s infinite;}
.chat-header-close{width:34px;height:34px;border-radius:50%;border:none;background:rgba(255,255,255,.2);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;}
.chat-header-close:hover{background:rgba(255,255,255,.35)}

.chat-body{flex:1;min-height:0;overflow-y:auto;padding:1rem 1.25rem;background:#f8fafc;display:flex;flex-direction:column;gap:.45rem;}
[data-theme="dark"] .chat-body{background:#0f172a;}
.chat-msg{display:flex;gap:.4rem;max-width:85%;align-items:flex-end;}
.chat-msg.from-user{align-self:flex-end;flex-direction:row-reverse}
.chat-msg.from-admin{align-self:flex-start}
.chat-msg .bubble{padding:.6rem .85rem;border-radius:16px;font-size:.85rem;line-height:1.45;word-break:break-word;white-space:pre-wrap;}
.chat-msg.from-user .bubble{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;border-bottom-right-radius:4px;}
.chat-msg.from-admin .bubble{background:#fff;color:#0f172a;border:1px solid #e2e8f0;border-bottom-left-radius:4px;}
[data-theme="dark"] .chat-msg.from-admin .bubble{background:#334155;color:#f1f5f9;border-color:#475569;}
.chat-msg .msg-time{font-size:.62rem;color:#94a3b8;padding:0 .3rem;white-space:nowrap;align-self:flex-end;margin-bottom:.15rem;}
.chat-system{align-self:center;font-size:.7rem;color:#64748b;background:#e2e8f0;padding:.25rem .75rem;border-radius:50px;text-align:center;margin:.3rem 0;}
.chat-empty{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;text-align:center;color:#94a3b8;padding:1.5rem;gap:.75rem;}
.chat-empty i{font-size:2.5rem;opacity:.35}
.chat-empty .title{font-size:.92rem;font-weight:700;color:#475569;}
.chat-empty .desc{font-size:.78rem;line-height:1.5;max-width:280px;}

.chat-footer{padding:.75rem 1rem;border-top:1px solid #e2e8f0;background:#fff;flex-shrink:0;display:flex;flex-direction:column;gap:.5rem;}
[data-theme="dark"] .chat-footer{background:#1e293b;border-color:#334155;}
.chat-footer-row{display:flex;gap:.5rem;align-items:flex-end;}
.chat-footer textarea{flex:1;min-width:0;min-height:42px;max-height:130px;padding:.65rem .9rem;border-radius:22px;border:1.5px solid #e2e8f0;background:#f8fafc;color:#0f172a;font-size:.85rem;font-family:inherit;outline:none;resize:none;overflow-y:hidden;line-height:1.4;}
[data-theme="dark"] .chat-footer textarea{background:#0f172a;color:#f1f5f9;border-color:#334155;}
.chat-footer textarea:focus{border-color:#4f46e5;}
.chat-footer textarea:disabled{opacity:.6;cursor:not-allowed;background:#f1f5f9;border-color:#cbd5e1;}
[data-theme="dark"] .chat-footer textarea:disabled{background:#0f172a;border-color:#475569;}
.chat-send-btn{width:44px;height:44px;border-radius:50%;border:none;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1.05rem;flex-shrink:0;}
.chat-send-btn:disabled{opacity:.4;cursor:not-allowed;}
.chat-quick-replies{display:flex;gap:.35rem;flex-wrap:wrap;padding:.5rem 0;border-bottom:1px dashed #e2e8f0;margin-bottom:.1rem;}
.chat-quick-replies.hidden{display:none}
.chat-quick-btn{padding:.3rem .7rem;border-radius:50px;border:1.5px solid rgba(37,99,235,.3);background:rgba(37,99,235,.08);color:#1e40af;font-size:.72rem;font-weight:700;cursor:pointer;font-family:inherit;}
.chat-quick-btn:hover{background:#2563eb;color:#fff;}

.chat-limit-banner{display:none;margin:0 0 .5rem;padding:.65rem .85rem;background:linear-gradient(135deg,#fef3c7,#fde68a);border:1.5px solid #f59e0b;border-radius:10px;font-size:.78rem;color:#78350f;line-height:1.45;animation:chatLimitSlide .3s cubic-bezier(.34,1.56,.64,1);flex-shrink:0;align-items:flex-start;gap:.5rem;}
.chat-limit-banner.show{display:flex}
.chat-limit-banner.danger{background:linear-gradient(135deg,#fecaca,#fca5a5);border-color:#dc2626;color:#7f1d1d;}
.chat-limit-banner .clb-icon{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#f59e0b,#d97706);color:#fff;display:flex;align-items:center;justify-content:center;font-size:.85rem;flex-shrink:0;animation:chatLimitPulse 1.5s infinite;}
.chat-limit-banner.danger .clb-icon{background:linear-gradient(135deg,#dc2626,#991b1b);}
@keyframes chatLimitPulse{0%,100%{transform:scale(1);}50%{transform:scale(1.1);}}
.chat-limit-banner .clb-text{flex:1;min-width:0;}
.chat-limit-banner .clb-text b{color:#dc2626;font-weight:900;}
.chat-limit-banner .clb-actions{display:flex;gap:.35rem;flex-wrap:wrap;margin-top:.4rem;}
.chat-limit-banner .clb-btn{padding:.35rem .7rem;border-radius:50px;border:none;font-size:.72rem;font-weight:800;cursor:pointer;font-family:inherit;text-decoration:none;display:inline-flex;align-items:center;gap:.3rem;transition:.15s;white-space:nowrap;}
.chat-limit-banner .clb-btn.zalo{background:linear-gradient(135deg,#0068ff,#0052cc);color:#fff;box-shadow:0 3px 10px rgba(0,104,255,.35);}
.chat-limit-banner .clb-btn.zalo:hover{transform:translateY(-1px);box-shadow:0 5px 14px rgba(0,104,255,.5);color:#fff;}
.chat-limit-banner .clb-btn.dismiss{background:rgba(120,53,15,.15);color:#78350f;}
.chat-limit-banner .clb-btn.dismiss:hover{background:rgba(120,53,15,.25);}
@keyframes chatLimitSlide{from{opacity:0;transform:translateY(-8px);}to{opacity:1;transform:translateY(0);}}

.admin-chat-thread{display:flex;align-items:center;gap:.75rem;padding:.75rem .85rem;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;margin-bottom:.5rem;cursor:pointer;position:relative;}
[data-theme="dark"] .admin-chat-thread{background:#334155;border-color:#475569;}
.admin-chat-thread:hover{border-color:#4f46e5;}
.admin-chat-thread.unread{border-color:#dc2626;background:rgba(220,38,38,.05);}
.admin-chat-thread .t-avatar{width:42px;height:42px;border-radius:50%;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1rem;flex-shrink:0;}
.admin-chat-thread .t-info{flex:1;min-width:0}
.admin-chat-thread .t-name{font-weight:800;font-size:.88rem;margin-bottom:.15rem;}
.admin-chat-thread .t-preview{font-size:.75rem;color:#64748b;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.admin-chat-thread .t-time{font-size:.68rem;color:#94a3b8;flex-shrink:0;}
.admin-chat-thread .t-badge{position:absolute;top:-4px;right:-4px;min-width:22px;height:22px;padding:0 .4rem;border-radius:50px;background:#dc2626;color:#fff;font-size:.65rem;font-weight:900;display:flex;align-items:center;justify-content:center;}

.chat-typing{display:none;align-self:flex-start;padding:.5rem .85rem;background:#fff;border:1px solid #e2e8f0;border-radius:16px;border-bottom-left-radius:4px;font-size:.8rem;color:#64748b;gap:.35rem;align-items:center;max-width:140px;margin-top:.2rem;}
.chat-typing.show{display:inline-flex}
.chat-typing .dots{display:inline-flex;gap:3px;}
.chat-typing .dots span{width:6px;height:6px;border-radius:50%;background:#94a3b8;animation:chatDotBounce 1.4s infinite;}
.chat-typing .dots span:nth-child(2){animation-delay:.2s}
.chat-typing .dots span:nth-child(3){animation-delay:.4s}
@keyframes chatDotBounce{0%,60%,100%{transform:translateY(0);opacity:.5}30%{transform:translateY(-5px);opacity:1}}
[data-theme="dark"] .chat-typing{background:#334155;border-color:#475569;color:#cbd5e1;}
[data-theme="dark"] .chat-typing .dots span{background:#94a3b8;}

.dropdown-chat-preview{display:none;margin:.4rem .5rem;padding:.65rem .75rem;background:linear-gradient(135deg, rgba(79,70,229,.06), rgba(124,58,237,.06));border:1px solid rgba(124,58,237,.2);border-radius:10px;cursor:pointer;transition:.15s;}
.dropdown-chat-preview:hover{border-color:#7c3aed;background:linear-gradient(135deg, rgba(79,70,229,.12), rgba(124,58,237,.12));}
.dropdown-chat-preview.show{display:block}
.dropdown-chat-preview .dcp-head{display:flex;align-items:center;justify-content:space-between;gap:.4rem;margin-bottom:.25rem;}
.dropdown-chat-preview .dcp-title{font-size:.68rem;font-weight:800;color:#7c3aed;text-transform:uppercase;letter-spacing:.4px;display:flex;align-items:center;gap:.3rem;}
.dropdown-chat-preview .dcp-time{font-size:.62rem;color:#94a3b8;font-weight:600;}
.dropdown-chat-preview .dcp-msg{font-size:.78rem;color:#0f172a;line-height:1.35;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;word-break:break-word;}
.dropdown-chat-preview .dcp-msg b{color:#4f46e5;}
.dropdown-chat-preview .dcp-badge{display:inline-block;background:#dc2626;color:#fff;font-size:.58rem;font-weight:900;padding:.1rem .35rem;border-radius:50px;margin-left:.35rem;vertical-align:middle;}
[data-theme="dark"] .dropdown-chat-preview{background:linear-gradient(135deg, rgba(79,70,229,.15), rgba(124,58,237,.15));border-color:rgba(165,180,252,.35);}
[data-theme="dark"] .dropdown-chat-preview .dcp-msg{color:#f1f5f9;}
[data-theme="dark"] .dropdown-chat-preview .dcp-msg b{color:#a5b4fc;}

.quota-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.75rem;margin-bottom:1rem;}
.quota-card{padding:1rem;border-radius:12px;background:var(--surface-2);border:1px solid var(--border);position:relative;overflow:hidden;}
.quota-card.warn{background:linear-gradient(135deg,rgba(245,158,11,.12),rgba(251,191,36,.06));border-color:#f59e0b;}
.quota-card.danger{background:linear-gradient(135deg,rgba(220,38,38,.12),rgba(220,38,38,.05));border-color:#dc2626;}
.quota-card .qc-label{font-size:.7rem;text-transform:uppercase;letter-spacing:.4px;font-weight:700;color:var(--text-3);margin-bottom:.35rem;display:flex;align-items:center;gap:.35rem;}
.quota-card .qc-value{font-size:1.6rem;font-weight:900;line-height:1;color:var(--text);margin-bottom:.25rem;}
.quota-card.warn .qc-value{color:#d97706;}
.quota-card.danger .qc-value{color:#dc2626;}
.quota-card .qc-sub{font-size:.7rem;color:var(--text-3);line-height:1.3;}
.quota-card .qc-bar{height:5px;background:var(--surface);border-radius:50px;overflow:hidden;margin-top:.5rem;border:1px solid var(--border);}
.quota-card .qc-bar-fill{height:100%;border-radius:50px;transition:width .4s ease,background .3s ease;background:linear-gradient(90deg,#16a34a,#22c55e);}
.quota-card.warn .qc-bar-fill{background:linear-gradient(90deg,#f59e0b,#fbbf24);}
.quota-card.danger .qc-bar-fill{background:linear-gradient(90deg,#dc2626,#ef4444);}
.quota-card .qc-icon{position:absolute;top:.75rem;right:.75rem;font-size:1.5rem;opacity:.15;color:var(--text);}
.quota-actions{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1rem;}
.quota-actions .btn{padding:.45rem .85rem;font-size:.78rem;}
.quota-info{padding:.75rem 1rem;border-radius:10px;background:var(--primary-light);color:var(--primary-dark);font-size:.78rem;line-height:1.5;display:flex;align-items:flex-start;gap:.5rem;margin-top:1rem;}
.quota-info i{margin-top:.15rem;flex-shrink:0;}
.quota-history-table{width:100%;border-collapse:collapse;font-size:.78rem;margin-top:.5rem;}
.quota-history-table th{padding:.4rem .6rem;text-align:left;background:var(--surface-2);color:var(--text-2);font-size:.68rem;text-transform:uppercase;border-bottom:1px solid var(--border);}
.quota-history-table td{padding:.4rem .6rem;border-bottom:1px solid var(--border);color:var(--text);}
.quota-history-table tr:last-child td{border-bottom:none;}
.quota-history-table .qht-ok{color:#16a34a;font-weight:700;}
.quota-history-table .qht-warn{color:#d97706;font-weight:700;}
.quota-history-table .qht-danger{color:#dc2626;font-weight:700;}

.online-user-row{display:flex;align-items:center;gap:.6rem;padding:.6rem .75rem;border-radius:10px;background:var(--surface-2);margin-bottom:.4rem;transition:.15s;}
.online-user-row:hover{background:var(--surface);box-shadow:0 2px 8px rgba(0,0,0,.06);}
.ou-dot{width:10px;height:10px;border-radius:50%;background:#16a34a;box-shadow:0 0 0 3px rgba(22,163,74,.2);animation:onlinePulse 2s infinite;flex-shrink:0;}
@keyframes onlinePulse{0%,100%{box-shadow:0 0 0 3px rgba(22,163,74,.2);}50%{box-shadow:0 0 0 6px rgba(22,163,74,.1);}}
.ou-info{flex:1;min-width:0;}
.ou-name{font-weight:700;font-size:.85rem;color:var(--text);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.ou-sub{font-size:.7rem;color:var(--text-3);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.ou-chat-btn{width:32px;height:32px;border-radius:8px;border:none;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.8rem;flex-shrink:0;transition:.15s;}
.ou-chat-btn:hover{transform:scale(1.08);box-shadow:0 4px 12px rgba(124,58,237,.4);}

.chat-toast{position:fixed;bottom:120px;left:50%;transform:translateX(-50%) translateY(20px);background:linear-gradient(135deg,#dc2626,#b91c1c);color:#fff;padding:.85rem 1.3rem;border-radius:12px;font-size:.85rem;font-weight:700;z-index:99999;opacity:0;transition:opacity .3s, transform .3s;pointer-events:none;box-shadow:0 12px 32px rgba(220,38,38,.4);max-width:80vw;text-align:center;line-height:1.4;}
.chat-toast.show{opacity:1;transform:translateX(-50%) translateY(0);}
@media (max-width:768px){
    .chat-toast{bottom:100px;font-size:.8rem;padding:.75rem 1.1rem;max-width:90vw;}
}
"""


def build_chat_html():
    return r"""
<div class="chat-modal" id="chatModal">
    <div class="chat-box">
        <div class="chat-header">
            <button class="chat-header-back" id="chatBack" type="button"><i class="fas fa-arrow-left"></i></button>
            <div class="chat-header-info" id="chatHeaderInfo">
                <div class="name">Hỗ trợ Admin</div>
                <div class="status">Thường trả lời trong 5-10 phút</div>
            </div>
            <span class="chat-counter" id="chatCounter">0/50</span>
            <button class="chat-header-close" id="chatClose" type="button"><i class="fas fa-times"></i></button>
        </div>
        <div class="chat-body" id="chatBody">
            <div class="chat-empty"><i class="fas fa-comments"></i><div class="title">Đang tải...</div></div>
        </div>
        <div class="chat-footer">
            <div class="chat-limit-banner" id="chatLimitBanner">
                <div class="clb-icon"><i class="fas fa-exclamation-triangle"></i></div>
                <div class="clb-text">
                    <div id="chatLimitText">Bạn sắp đạt giới hạn tin nhắn.</div>
                    <div class="clb-actions">
                        <a class="clb-btn zalo" id="chatLimitZaloBtn" href="#" target="_blank" rel="noopener"><i class="fas fa-comment-dots"></i> Chat Zalo</a>
                        <button class="clb-btn dismiss" type="button" id="chatLimitDismiss"><i class="fas fa-times"></i> Để sau</button>
                    </div>
                </div>
            </div>
          <div class="chat-quick-replies hidden" id="chatQuickReplies">
    <button class="chat-quick-btn" type="button" data-reply="Chào bạn, chúc bạn ngày mới học vui!">Chào hỏi</button>
    <button class="chat-quick-btn" type="button" data-reply="Tài khoản sắp hết hạn, gia hạn để học tiếp nhé bạn!">Nhắc hết hạn</button>
    <button class="chat-quick-btn" type="button" data-reply="Đã gia hạn cho bạn rồi, học vui nha!">Đã gia hạn</button>
    <button class="chat-quick-btn" type="button" data-reply="Nhớ luyện viết mỗi ngày nhé bạn!">Nhắc luyện viết</button>
    <button class="chat-quick-btn" type="button" data-reply="Mỗi ngày 10 từ, bạn sẽ giỏi nhanh thôi!">Mẹo học</button>
    <button class="chat-quick-btn" type="button" data-reply="Bạn học chăm quá, cố lên nhé!">Động viên</button>
    <button class="chat-quick-btn" type="button" data-reply="Cảm ơn bạn đã đồng hành cùng mình!">Cảm ơn</button>
    <button class="chat-quick-btn" type="button" data-reply="Cần gì cứ nhắn mình nhé bạn!">Hỗ trợ</button>
</div>
            <div class="chat-footer-row">
                <textarea id="chatInput" placeholder="Nhập tin nhắn..." rows="1" maxlength="1000"></textarea>
                <button class="chat-send-btn" id="chatSendBtn" type="button" disabled><i class="fas fa-paper-plane"></i></button>
            </div>
        </div>
    </div>
</div>
"""


def build_quota_html():
    return r"""
<div class="admin-section collapsed" id="adminQuotaSection">
    <div class="admin-section-head">
        <div class="ash-left">
            <div class="ash-icon violet"><i class="fas fa-chart-line"></i></div>
            <div class="ash-text">
                <div class="ash-title"><span>Quota Firestore</span></div>
                <div class="ash-subtitle">
                    <span class="chip primary"><i class="fas fa-database"></i> <span id="quotaStatusChip">Đang tải...</span></span>
                </div>
            </div>
        </div>
        <div class="ash-actions">
            <button class="btn" id="refreshQuotaBtn" style="padding:.4rem .7rem;font-size:.75rem" title="Làm mới"><i class="fas fa-sync-alt"></i></button>
            <button class="admin-toggle-btn" id="toggleQuotaBtn" title="Hiện Quota"><i class="fas fa-eye-slash"></i></button>
        </div>
    </div>
    <div class="admin-section-body">
        <div class="admin-section-inner">
            <div class="quota-actions">
                <button class="btn primary" id="quotaResetBtn"><i class="fas fa-redo"></i> Reset đếm hôm nay</button>
                <button class="btn" id="quotaExportBtn"><i class="fas fa-file-export"></i> Xuất CSV</button>
                <button class="btn" id="quotaSimBtn"><i class="fas fa-flask"></i> Test cảnh báo</button>
            </div>
            <div class="quota-grid" id="quotaGrid">
                <div class="quota-card">
                    <i class="fas fa-eye qc-icon"></i>
                    <div class="qc-label"><i class="fas fa-book-reader"></i> Reads hôm nay</div>
                    <div class="qc-value" id="quotaReads">0</div>
                    <div class="qc-sub">Giới hạn: 50.000</div>
                    <div class="qc-bar"><div class="qc-bar-fill" id="quotaReadsBar" style="width:0%"></div></div>
                </div>
                <div class="quota-card">
                    <i class="fas fa-pen qc-icon"></i>
                    <div class="qc-label"><i class="fas fa-pen"></i> Writes hôm nay</div>
                    <div class="qc-value" id="quotaWrites">0</div>
                    <div class="qc-sub">Giới hạn: 20.000</div>
                    <div class="qc-bar"><div class="qc-bar-fill" id="quotaWritesBar" style="width:0%"></div></div>
                </div>
                <div class="quota-card">
                    <i class="fas fa-trash qc-icon"></i>
                    <div class="qc-label"><i class="fas fa-trash"></i> Deletes hôm nay</div>
                    <div class="qc-value" id="quotaDeletes">0</div>
                    <div class="qc-sub">Giới hạn: 20.000</div>
                    <div class="qc-bar"><div class="qc-bar-fill" id="quotaDeletesBar" style="width:0%"></div></div>
                </div>
                <div class="quota-card">
                    <i class="fas fa-users qc-icon"></i>
                    <div class="qc-label"><i class="fas fa-users"></i> User đang hoạt động</div>
                    <div class="qc-value" id="quotaOnlineUsers">0</div>
                    <div class="qc-sub">Tab đang mở (localStorage)</div>
                </div>
                <div class="quota-card">
                    <i class="fas fa-clock qc-icon"></i>
                    <div class="qc-label"><i class="fas fa-clock"></i> Reset sau</div>
                    <div class="qc-value" id="quotaResetTime">--:--:--</div>
                    <div class="qc-sub">Giờ UTC (Firebase)</div>
                </div>
                <div class="quota-card">
                    <i class="fas fa-tachometer-alt qc-icon"></i>
                    <div class="qc-label"><i class="fas fa-tachometer-alt"></i> Reads/phút</div>
                    <div class="qc-value" id="quotaReadRate">0</div>
                    <div class="qc-sub">Tốc độ hiện tại</div>
                </div>
            </div>
            <div class="quota-info">
                <i class="fas fa-info-circle"></i>
                <div>
                    <b>Lưu ý:</b> Số liệu đếm từ client (localStorage), KHÔNG phải số liệu chính thức từ Firebase.
                    Để xem quota chính thức, vào <b>Firebase Console → Usage</b>.
                    <br>Reset tự động vào <b>00:00 UTC</b> (07:00 giờ VN).
                </div>
            </div>
            <div style="margin-top:1rem;">
                <div style="padding:.5rem 0;"><strong style="font-size:.82rem;"><i class="fas fa-history"></i> Lịch sử 7 ngày</strong></div>
                <table class="quota-history-table">
                    <thead><tr><th>Ngày</th><th>Reads</th><th>Writes</th><th>Deletes</th><th>Trạng thái</th></tr></thead>
                    <tbody id="quotaHistoryBody"><tr><td colspan="5" style="text-align:center;color:var(--text-3);padding:1rem;">Chưa có dữ liệu</td></tr></tbody>
                </table>
            </div>
        </div>
    </div>
</div>
"""


def build_online_section_html():
    return r"""
<div class="admin-section" id="adminOnlineSection">
    <div class="admin-section-head">
        <div class="ash-left">
            <div class="ash-icon" style="background:rgba(22,163,74,.15);color:#16a34a;">
                <i class="fas fa-circle"></i>
            </div>
            <div class="ash-text">
                <div class="ash-title"><span>User đang online</span></div>
                <div class="ash-subtitle">
                    <span class="chip ok">
                        <i class="fas fa-circle" style="color:#16a34a;font-size:.5rem"></i>
                        <span id="onlineCount">0</span> user
                    </span>
                    <span class="chip" style="font-size:.62rem;">
                        <i class="fas fa-bolt" style="color:#f59e0b;"></i> Realtime
                    </span>
                </div>
            </div>
        </div>
        <div class="ash-actions">
            <button class="admin-toggle-btn active" id="toggleOnlineBtn" title="Ẩn">
                <i class="fas fa-eye"></i>
            </button>
        </div>
    </div>
    <div class="admin-section-body">
        <div class="admin-section-inner">
            <div id="onlineUserList">
                <div class="no-data"><i class="fas fa-spinner fa-pulse"></i><span>Đang tải...</span></div>
            </div>
        </div>
    </div>
</div>
"""


def build_config_js(config):
    def esc_js(s):
        if s is None:
            return ''
        return (str(s)
                .replace('\\', '\\\\')
                .replace('"', '\\"')
                .replace('\n', '\\n')
                .replace('\r', '\\r'))

    zalo_phone = esc_js(config.get("zalo_phone", ""))
    tg_token = esc_js(config.get("telegram_bot_token", ""))
    tg_chat = esc_js(config.get("telegram_chat_id", ""))
    site_name = esc_js(config.get("tiktok_nickname", "Website"))

    return (
        '<script>\n'
        '  window.ZALO_PHONE = "' + zalo_phone + '";\n'
        '  window.TELEGRAM_BOT_TOKEN = "' + tg_token + '";\n'
        '  window.TELEGRAM_CHAT_ID = "' + tg_chat + '";\n'
        '  window.SITE_NAME = "' + site_name + '";\n'
        '</script>\n'
    )


def build_telegram_notify_js():
    return r"""
(function() {
    'use strict';

    var _tgLastSent = 0;
    var TG_MIN_INTERVAL = 2000;

    function escapeMarkdown(s) {
        if (s == null) return '';
        return String(s).replace(/([_*\[\]()~`>#+\-=|{}.!\\])/g, '\\$1');
    }

    window.__sendTelegramNotify = function(userEmail, userName, messageText, from) {
        var token = window.TELEGRAM_BOT_TOKEN;
        var chatId = window.TELEGRAM_CHAT_ID;

        if (!token) return;
        if (!chatId || chatId === '-0' || chatId === '0') return;

        var now = Date.now();
        if (now - _tgLastSent < TG_MIN_INTERVAL) return;
        _tgLastSent = now;

        var siteName = window.SITE_NAME || document.title || 'Website';
        var isAdmin = (from === 'admin');
        var header = isAdmin ? '*Admin vừa trả lời*' : '*Tin nhắn mới từ*';

        var siteUrl = window.location.origin + window.location.pathname;
        var adminUrl = siteUrl + '?admin_chat=' + encodeURIComponent(userEmail || '');

        var text =
            header + ' ' + escapeMarkdown(siteName) + '\n' +
            'Tên: ' + escapeMarkdown(userName || 'User') + '\n' +
            'Email: ' + escapeMarkdown(userEmail || '') + '\n' +
            '---------------\n' +
            escapeMarkdown(messageText || '') + '\n' +
            '---------------\n' +
            new Date().toLocaleString('vi-VN') + '\n\n' +
            'Copy link de tra loi:\n' +
            adminUrl;

        var url = 'https://api.telegram.org/bot' + token + '/sendMessage';
        var payload = {
            chat_id: chatId,
            text: text,
            disable_web_page_preview: true
        };

        fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        }).catch(function() {});
    };
})();
"""


def build_chat_js():
    return r"""
(function() {
    'use strict';

    var DAILY_LIMIT = 50;
    var LIMIT_WARN_AT = 40;
    var MAX_MESSAGES = 100;

    var COOLDOWN_MS = 3000;
    var RATE_LIMIT_PER_MIN = 10;
    var DUPLICATE_WINDOW = 30000;
    var MIN_MESSAGE_LENGTH = 1;
    var MAX_MESSAGE_LENGTH = 1000;

    var CHAT = {
        inited: false,
        threadUnsub: null,
        adminListUnsub: null,
        adminThreadUnsub: null,
        adminCurrentEmail: null,
        isOpen: false,
        lastThreadData: null,
        lastSeenAt: 0,
        typingTimer: null,
        onlineUnsub: null
    };

    var SPAM = {
        lastSentAt: 0,
        minuteLog: [],
        lastText: '',
        lastTextAt: 0,
        isSending: false
    };

    function $id(id) { return document.getElementById(id); }
    function esc(s) {
        if (s == null) return '';
        return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
                        .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    }
    function jsStr(s) {
        if (s == null) return '';
        return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/"/g,'\\"');
    }
    function timeAgo(ms) {
        if (ms < 60000) return 'Vừa xong';
        if (ms < 3600000) return Math.floor(ms/60000) + ' phút trước';
        if (ms < 86400000) return Math.floor(ms/3600000) + ' giờ trước';
        if (ms < 2592000000) return Math.floor(ms/86400000) + ' ngày trước';
        return Math.floor(ms/2592000000) + ' tháng trước';
    }
    function getDb() { return window.db || null; }
    function getCu() { return window.currentUser || null; }
    function isAdmin() { var u = getCu(); return u && u.role === 'admin'; }

    function todayKey() {
        var d = new Date();
        return d.getFullYear() + '-' + String(d.getMonth()+1).padStart(2,'0') + '-' + String(d.getDate()).padStart(2,'0');
    }
    function getDailyCount() {
        var u = getCu();
        if (!u || !u.email) return 0;
        try { return parseInt(localStorage.getItem('chat_count_' + u.email + '_' + todayKey()) || '0', 10) || 0; }
        catch(e) { return 0; }
    }
    function incDailyCount() {
        var u = getCu();
        if (!u || !u.email) return 0;
        var c = getDailyCount() + 1;
        try { localStorage.setItem('chat_count_' + u.email + '_' + todayKey(), String(c)); } catch(e) {}
        return c;
    }
    function updateCounterUI() {
        var u = getCu();
        var counterEl = $id('chatCounter');
        var banner = $id('chatLimitBanner');
        var textEl = $id('chatLimitText');
        if (!counterEl) return;
        if (isAdmin() || !u || !u.email) {
            counterEl.classList.remove('show', 'warn', 'danger');
            if (banner) banner.classList.remove('show');
            return;
        }
        var count = getDailyCount();
        counterEl.classList.add('show');
        counterEl.textContent = count + '/' + DAILY_LIMIT;
        counterEl.classList.remove('warn', 'danger');
        if (count >= DAILY_LIMIT) counterEl.classList.add('danger');
        else if (count >= LIMIT_WARN_AT) counterEl.classList.add('warn');
        if (banner && textEl) {
            if (count >= DAILY_LIMIT) {
                banner.classList.add('show', 'danger');
                textEl.innerHTML = 'Đã đạt giới hạn ' + DAILY_LIMIT + ' tin/ngày. Chuyển sang Zalo để tiếp tục.';
                var ic = banner.querySelector('.clb-icon');
                if (ic) ic.innerHTML = '<i class="fas fa-ban"></i>';
            } else if (count >= LIMIT_WARN_AT) {
                banner.classList.add('show');
                banner.classList.remove('danger');
                textEl.innerHTML = 'Đã gửi ' + count + '/' + DAILY_LIMIT + ' tin hôm nay. Còn ' + (DAILY_LIMIT - count) + ' tin.';
                var ic2 = banner.querySelector('.clb-icon');
                if (ic2) ic2.innerHTML = '<i class="fas fa-exclamation-triangle"></i>';
            } else {
                banner.classList.remove('show');
            }
        }
    }
    function canSend() {
        if (isAdmin()) return true;
        if (getDailyCount() >= DAILY_LIMIT) { updateCounterUI(); return false; }
        return true;
    }
    function initLimitBanner() {
        var banner = $id('chatLimitBanner');
        var dismiss = $id('chatLimitDismiss');
        var zaloBtn = $id('chatLimitZaloBtn');
        if (!banner) return;
        if (zaloBtn) {
            var phone = (window.ZALO_PHONE || '').replace(/\D/g, '');
            if (phone) zaloBtn.href = 'https://zalo.me/' + phone;
            else { zaloBtn.href = '#'; zaloBtn.onclick = function(e){ e.preventDefault(); alert('Chưa cấu hình Zalo.'); }; }
        }
        if (dismiss) dismiss.addEventListener('click', function() {
            banner.classList.remove('show');
            try { sessionStorage.setItem('chatLimitDismissed', String(Date.now())); } catch(e) {}
        });
        updateCounterUI();
    }

    function checkSpam(text) {
        var now = Date.now();
        if (isAdmin()) return { allowed: true };

        if (SPAM.lastSentAt > 0) {
            var elapsed = now - SPAM.lastSentAt;
            if (elapsed < COOLDOWN_MS) {
                var wait = Math.ceil((COOLDOWN_MS - elapsed) / 1000);
                return {
                    allowed: false,
                    reason: 'Vui lòng đợi ' + wait + ' giây trước khi gửi tin tiếp theo.',
                    waitMs: COOLDOWN_MS - elapsed
                };
            }
        }

        if (SPAM.isSending) {
            return { allowed: false, reason: 'Đang gửi tin nhắn, vui lòng đợi...', waitMs: 500 };
        }

        SPAM.minuteLog = SPAM.minuteLog.filter(function(t) { return now - t < 60000; });
        if (SPAM.minuteLog.length >= RATE_LIMIT_PER_MIN) {
            var oldest = SPAM.minuteLog[0];
            var waitMs = 60000 - (now - oldest);
            return {
                allowed: false,
                reason: 'Bạn đã gửi quá ' + RATE_LIMIT_PER_MIN + ' tin/phút. Đợi ' + Math.ceil(waitMs / 1000) + ' giây.',
                waitMs: waitMs
            };
        }

        var normalized = text.trim().toLowerCase();
        if (normalized === SPAM.lastText && now - SPAM.lastTextAt < DUPLICATE_WINDOW) {
            return { allowed: false, reason: 'Bạn vừa gửi tin nhắn giống hệt. Vui lòng thay đổi nội dung.', waitMs: 2000 };
        }

        if (text.trim().length < MIN_MESSAGE_LENGTH) {
            return { allowed: false, reason: 'Tin nhắn quá ngắn.', waitMs: 0 };
        }
        if (text.length > MAX_MESSAGE_LENGTH) {
            return { allowed: false, reason: 'Tin nhắn quá dài (tối đa ' + MAX_MESSAGE_LENGTH + ' ký tự).', waitMs: 0 };
        }

        var cleanText = text.replace(/[^a-zA-Z0-9À-ỹ\u4e00-\u9fff]/g, '');
        if (cleanText.length < 1 && text.length > 5) {
            return { allowed: false, reason: 'Tin nhắn không hợp lệ.', waitMs: 0 };
        }

        return { allowed: true };
    }

    function updateSpamState(text) {
        var now = Date.now();
        SPAM.lastSentAt = now;
        SPAM.lastText = text.trim().toLowerCase();
        SPAM.lastTextAt = now;
        SPAM.minuteLog.push(now);
        SPAM.isSending = false;
    }

    function resetSpamState() { SPAM.isSending = false; }

    function showSpamError(reason, waitMs) {
        var input = $id('chatInput');
        if (!input) return;
        input.style.animation = 'chatBellShake 0.5s';
        setTimeout(function() { input.style.animation = ''; }, 600);

        if (waitMs && waitMs > 1000) {
            input.disabled = true;
            var btn = $id('chatSendBtn');
            var originalPlaceholder = input.placeholder;
            var remaining = Math.ceil(waitMs / 1000);
            input.placeholder = 'Vui lòng đợi ' + remaining + ' giây...';

            var timer = setInterval(function() {
                remaining--;
                if (remaining <= 0) {
                    clearInterval(timer);
                    input.disabled = false;
                    input.placeholder = originalPlaceholder;
                    if (btn) btn.disabled = !input.value.trim();
                } else {
                    input.placeholder = 'Vui lòng đợi ' + remaining + ' giây...';
                }
            }, 1000);
        }

        showToast(reason);
    }

    function showToast(msg) {
        var toast = document.getElementById('chatToast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'chatToast';
            toast.className = 'chat-toast';
            document.body.appendChild(toast);
        }
        toast.textContent = msg;
        toast.classList.add('show');
        clearTimeout(toast._timer);
        toast._timer = setTimeout(function() { toast.classList.remove('show'); }, 3000);
    }

    function mountChatButton(retries) {
        retries = retries || 0;
        if (document.getElementById('chatFloatBtn')) return;
        if (retries > 20) return;
        if (!document.body) {
            setTimeout(function(){ mountChatButton(retries + 1); }, 300);
            return;
        }

        var wrap = document.getElementById('chatFloatWrap');
        if (!wrap) {
            wrap = document.createElement('div');
            wrap.id = 'chatFloatWrap';
            wrap.className = 'hidden';
            document.body.appendChild(wrap);
        }

        var menu = document.createElement('div');
        menu.id = 'chatFloatMenu';
        menu.className = 'chat-float-menu';
        menu.innerHTML =
            '<button type="button" class="chat-float-sub chat-sub" id="chatSubBtn" title="Chat với Admin">' +
                '<i class="fas fa-comments"></i>' +
                '<span class="sub-badge" id="chatSubBadge">0</span>' +
            '</button>' +
            '<button type="button" class="chat-float-sub manager-sub" id="managerSubBtn" title="Quản lý Chat (Admin)">' +
                '<i class="fas fa-users-cog"></i>' +
                '<span class="sub-badge" id="managerSubBadge">0</span>' +
            '</button>';

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'chat-float-btn hidden';
        btn.id = 'chatFloatBtn';
        btn.title = 'Hỗ trợ';
        btn.innerHTML = '<i class="fas fa-comments"></i>' +
            '<span class="chat-badge" id="chatFabBadge">0</span>';

        wrap.appendChild(menu);
        wrap.appendChild(btn);

        btn.addEventListener('click', function() {
            var isAdminUser = isAdmin();
            if (isAdminUser) {
                var isOpen = menu.classList.contains('show');
                if (isOpen) closeFloatMenu();
                else openFloatMenu();
            } else {
                btn.classList.remove('has-unread');
                if (CHAT.isOpen) closeChat();
                else openChat();
            }
        });

        var chatSub = document.getElementById('chatSubBtn');
        if (chatSub) {
            chatSub.addEventListener('click', function(e) {
                e.stopPropagation();
                closeFloatMenu();
                btn.classList.remove('has-unread');
                if (CHAT.isOpen) closeChat();
                else openChat();
            });
        }

        var managerSub = document.getElementById('managerSubBtn');
        if (managerSub) {
            managerSub.addEventListener('click', function(e) {
                e.stopPropagation();
                closeFloatMenu();
                if (typeof window.__acmToggleModal === 'function') {
                    window.__acmToggleModal();
                } else if (typeof window.__acmOpenModal === 'function') {
                    window.__acmOpenModal();
                }
            });
        }

        document.addEventListener('click', function(e) {
            if (!menu.classList.contains('show')) return;
            if (wrap.contains(e.target)) return;
            closeFloatMenu();
        }, true);

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && menu.classList.contains('show')) {
                closeFloatMenu();
            }
        });

        setTimeout(function() {
            if (!btn.classList.contains('has-unread')) {
                btn.classList.add('intro-glow');
                setTimeout(function() { btn.classList.remove('intro-glow'); }, 2000);
            }
        }, 800);
    }

    function openFloatMenu() {
        var menu = document.getElementById('chatFloatMenu');
        var btn = document.getElementById('chatFloatBtn');
        if (!menu) return;
        if (!isAdmin()) return;
        menu.classList.add('show');
        if (btn) btn.classList.add('menu-open');
        syncSubBadges();
    }

    function closeFloatMenu() {
        var menu = document.getElementById('chatFloatMenu');
        var btn = document.getElementById('chatFloatBtn');
        if (menu) menu.classList.remove('show');
        if (btn) btn.classList.remove('menu-open');
    }

    function syncSubBadges() {
        var chatFabBadge = document.getElementById('chatFabBadge');
        var chatSubBadge = document.getElementById('chatSubBadge');
        var managerSubBadge = document.getElementById('managerSubBadge');
        var acmFabBadge = document.getElementById('acmFabBadge');

        if (chatFabBadge && chatSubBadge) {
            var chatCount = parseInt(chatFabBadge.textContent) || 0;
            if (chatCount > 0) {
                chatSubBadge.textContent = chatCount > 99 ? '99+' : chatCount;
                chatSubBadge.classList.add('show');
            } else {
                chatSubBadge.classList.remove('show');
            }
        }

        if (acmFabBadge && managerSubBadge) {
            var mgrCount = parseInt(acmFabBadge.textContent) || 0;
            if (mgrCount > 0) {
                managerSubBadge.textContent = mgrCount > 99 ? '99+' : mgrCount;
                managerSubBadge.classList.add('show');
            } else {
                managerSubBadge.classList.remove('show');
            }
        }
    }

    window.__syncChatSubBadges = syncSubBadges;
    window.__openFloatMenu = openFloatMenu;
    window.__closeFloatMenu = closeFloatMenu;

    function updateFabVisibility() {
        var fab = $id('chatFloatBtn');
        var wrap = $id('chatFloatWrap');
        if (!fab || !wrap) return;
        var u = getCu();
        if (u && u.email) {
            wrap.classList.remove('hidden');
            fab.classList.remove('hidden');
        } else {
            wrap.classList.add('hidden');
            fab.classList.add('hidden');
        }
    }

    function setFabBadge(n) {
        var el = $id('chatFabBadge');
        var btn = $id('chatFloatBtn');
        if (!el) return;
        if (n > 0) {
            el.textContent = n > 99 ? '99+' : n;
            el.classList.add('show');
            if (btn) btn.classList.add('has-unread');
        } else {
            el.classList.remove('show');
            if (btn) btn.classList.remove('has-unread');
        }
        syncSubBadges();
    }

    function positionChatBox() {
        var fab = $id('chatFloatBtn');
        var box = document.querySelector('.chat-box');
        if (!fab || !box) return;

        var fabRect = fab.getBoundingClientRect();
        var boxRect = box.getBoundingClientRect();
        var isMobile = window.innerWidth <= 600;

        var boxWidth = boxRect.width || (isMobile ? (window.innerWidth - 24) : 360);

        var right = window.innerWidth - fabRect.right;
        if (right < 8) right = 8;
        if (right + boxWidth > window.innerWidth - 8) {
            right = Math.max(8, window.innerWidth - boxWidth - 8);
        }

        var gap = 16;
        var boxHeight = boxRect.height || 260;
        var top = fabRect.top - boxHeight - gap;
        if (top < 8) top = 8;
        var maxTop = window.innerHeight - boxHeight - 8;
        if (top > maxTop) top = maxTop;

        box.style.right = right + 'px';
        box.style.left = 'auto';
        box.style.top = top + 'px';
        box.style.bottom = 'auto';

        var fabCenterX = fabRect.left + fabRect.width / 2;
        var boxLeft = window.innerWidth - right - boxWidth;
        var arrowLeft = fabCenterX - boxLeft - 14;
        arrowLeft = Math.max(16, Math.min(arrowLeft, boxWidth - 32));
        box.style.setProperty('--arrow-left', arrowLeft + 'px');
    }

    function syncFloatingGroupState() {
        var group = document.getElementById('floatingLeftGroup');
        var isVisible = false;
        if (group) {
            var style = window.getComputedStyle(group);
            isVisible = (style.display !== 'none') &&
                        (style.visibility !== 'hidden') &&
                        (parseFloat(style.opacity || '1') > 0.05);
        }
        var changed = document.body.classList.contains('has-floating-group') !== isVisible;
        document.body.classList.toggle('has-floating-group', isVisible);
        if (changed && CHAT.isOpen) {
            setTimeout(positionChatBox, 60);
            setTimeout(positionChatBox, 380);
        }
    }

    function startUserThreadWatch() {
        stopUserThreadWatch();
        var u = getCu(), db = getDb();
        if (!u || !u.email || !db || isAdmin()) return;
        var email = u.email;
        var threadRef = db.collection('chat_threads').doc(email);
        var initKey = 'chat_init_' + email + '_' + todayKey();
        try {
            if (!sessionStorage.getItem(initKey)) {
                threadRef.get().then(function(doc) {
                    if (!doc.exists) {
                        threadRef.set({
                            userEmail: email, userName: u.name || email.split('@')[0],
                            messages: [], lastMessage: '',
                            lastMessageAt: firebase.firestore.FieldValue.serverTimestamp(),
                            lastMessageFrom: 'user', unreadByAdmin: 0, unreadByUser: 0,
                            userTypingAt: null, adminTypingAt: null,
                            createdAt: firebase.firestore.FieldValue.serverTimestamp()
                        }).then(function() {
                            try { sessionStorage.setItem(initKey, '1'); } catch(e) {}
                        }).catch(function(){});
                    } else { try { sessionStorage.setItem(initKey, '1'); } catch(e) {} }
                }).catch(function(){});
            }
        } catch(e) {}

        CHAT.threadUnsub = threadRef.onSnapshot(function(doc) {
            if (!doc.exists) return;
            var d = doc.data();
            CHAT.lastThreadData = d;
            var unread = d.unreadByUser || 0;
            setFabBadge(unread);
            var lastAt = d.lastMessageAt ? d.lastMessageAt.toMillis() : 0;
            var fromAdmin = (d.lastMessageFrom === 'admin');
            if (fromAdmin && lastAt > (CHAT.lastSeenAt || 0) && unread > 0) {
                CHAT.lastSeenAt = lastAt;
                if (!CHAT.isOpen) setTimeout(function() { if (!CHAT.isOpen) openChat(); }, 400);
            }
            if (CHAT.isOpen && !isAdmin()) {
                renderUserMessages(d);
                if ((d.unreadByUser || 0) > 0) threadRef.update({ unreadByUser: 0 }).catch(function(){});
            }
            var adminTyping = d.adminTypingAt;
            var showTyping = false;
            if (adminTyping) {
                var ms = adminTyping.toMillis ? adminTyping.toMillis() : 0;
                if (ms && (Date.now() - ms) < 5000) showTyping = true;
            }
            var tEl = $id('chatTypingIndicator');
            if (tEl) tEl.classList.toggle('show', showTyping);
            updateDropdownPreviewFromData(d);
        }, function(err) {
            console.error('Chat watch error:', err);
            var body = $id('chatBody');
            if (body) body.innerHTML = '<div class="chat-empty">' +
                '<i class="fas fa-exclamation-triangle" style="color:#dc2626"></i>' +
                '<div class="title">Không tải được chat</div>' +
                '<div class="desc">' + esc(err.message) + '</div></div>';
        });
    }
    function stopUserThreadWatch() {
        if (CHAT.threadUnsub) { try { CHAT.threadUnsub(); } catch(e){} CHAT.threadUnsub = null; }
    }

    function updateDropdownPreviewFromData(d) {
        var el = document.getElementById('dropdownChatPreview');
        if (!el) return;
        if (isAdmin()) { el.classList.remove('show'); return; }
        el.classList.add('show');
        var dcpMsg = document.getElementById('dcpMsg');
        var dcpTime = document.getElementById('dcpTime');
        var dcpBadge = document.getElementById('dcpBadge');
        if (!dcpMsg) return;
        if (!d || !d.lastMessage) {
            dcpMsg.textContent = 'Chưa có tin nhắn. Bấm để bắt đầu chat với Admin.';
            if (dcpTime) dcpTime.textContent = '';
            if (dcpBadge) dcpBadge.style.display = 'none';
            return;
        }
        var fromMe = (d.lastMessageFrom === 'user');
        dcpMsg.innerHTML = (fromMe ? '<b>Bạn:</b> ' : '<b>Admin:</b> ') + esc(d.lastMessage);
        if (dcpTime) {
            var at = d.lastMessageAt ? d.lastMessageAt.toDate() : null;
            dcpTime.textContent = at ? timeAgo(Date.now() - at.getTime()) : '';
        }
        var unread = d.unreadByUser || 0;
        if (dcpBadge) {
            if (unread > 0) { dcpBadge.textContent = unread > 99 ? '99+' : unread; dcpBadge.style.display = 'inline-block'; }
            else dcpBadge.style.display = 'none';
        }
    }

    function renderUserMessages(d) {
        var body = $id('chatBody');
        if (!body) return;
        var msgs = d.messages || [];
        if (msgs.length === 0) {
            body.innerHTML = '<div class="chat-empty"><i class="fas fa-comments"></i>' +
                '<div class="title">Bắt đầu cuộc trò chuyện</div>' +
                '<div class="desc">Gửi tin nhắn cho admin nếu bạn cần hỗ trợ.</div></div>' +
                '<div class="chat-typing" id="chatTypingIndicator"><span>Đang trả lời</span><span class="dots"><span></span><span></span><span></span></span></div>';
            if (CHAT.isOpen) { setTimeout(positionChatBox, 30); setTimeout(positionChatBox, 300); }
            return;
        }
        var html = '', lastDate = null;
        msgs.forEach(function(m) {
            var at = m.at ? (m.at.toDate ? m.at.toDate() : new Date((m.at.seconds||0)*1000)) : new Date();
            var dateStr = at.toLocaleDateString('vi-VN');
            if (dateStr !== lastDate) { html += '<div class="chat-system">' + dateStr + '</div>'; lastDate = dateStr; }
            var time = at.toLocaleTimeString('vi-VN', {hour:'2-digit',minute:'2-digit'});
            var isMe = (m.from === 'user');
            html += '<div class="chat-msg ' + (isMe?'from-user':'from-admin') + '">' +
                '<div class="bubble">' + esc(m.text||'').replace(/\n/g,'<br>') + '</div>' +
                '<span class="msg-time">' + time + '</span></div>';
        });
        html += '<div class="chat-typing" id="chatTypingIndicator"><span>Đang trả lời</span><span class="dots"><span></span><span></span><span></span></span></div>';
        body.innerHTML = html;
        var nearBottom = body.scrollHeight - body.scrollTop - body.clientHeight < 150;
        if (nearBottom) setTimeout(function(){ body.scrollTop = body.scrollHeight; }, 30);
        if (CHAT.isOpen) { setTimeout(positionChatBox, 30); setTimeout(positionChatBox, 300); }
    }

    function startOnlineWatch() {
        if (!isAdmin()) return;
        if (typeof firebase === 'undefined' || typeof firebase.database !== 'function') return;
        if (CHAT.onlineUnsub) return;

        try {
            var ref = firebase.database().ref('presence');
            var handler = ref.on('value', function(snap) {
                var val = snap.val() || {};
                var now = Date.now();
                var cutoff = now - 3 * 60 * 1000;
                var users = [];

                Object.keys(val).forEach(function(k) {
                    var u = val[k];
                    if (u && u.at && u.at > cutoff) {
                        users.push({
                            email: u.email || decodeURIComponent(k),
                            name: u.name || 'User',
                            at: u.at
                        });
                    }
                });

                users.sort(function(a, b) { return b.at - a.at; });
                renderOnlineList(users);
            });

            CHAT.onlineUnsub = function() {
                try { ref.off('value', handler); } catch(e) {}
            };
        } catch(e) {}
    }

    function stopOnlineWatch() {
        if (CHAT.onlineUnsub) {
            try { CHAT.onlineUnsub(); } catch(e) {}
            CHAT.onlineUnsub = null;
        }
    }

    function renderOnlineList(users) {
        var el = document.getElementById('onlineUserList');
        var countEl = document.getElementById('onlineCount');
        if (!el) return;

        if (countEl) countEl.textContent = users.length;

        if (users.length === 0) {
            el.innerHTML = '<div class="no-data"><i class="fas fa-user-slash"></i><span>Không có user nào online</span></div>';
            return;
        }

        var html = '';
        users.forEach(function(u) {
            var diff = Date.now() - u.at;
            var status;
            if (diff < 60000) status = 'Vừa xong';
            else if (diff < 120000) status = Math.floor(diff / 60000) + ' phút trước';
            else status = Math.floor(diff / 60000) + ' phút trước';

            html += '<div class="online-user-row">' +
                '<div class="ou-dot"></div>' +
                '<div class="ou-info">' +
                    '<div class="ou-name">' + esc(u.name) + '</div>' +
                    '<div class="ou-sub">' + esc(u.email) + ' - ' + status + '</div>' +
                '</div>' +
                '<button class="ou-chat-btn" type="button" ' +
                    'onclick="if(window.__chatOpenThread){window.__chatOpenThread(\'' + jsStr(u.email) + '\');}" ' +
                    'title="Chat với user">' +
                    '<i class="fas fa-comments"></i>' +
                '</button>' +
            '</div>';
        });
        el.innerHTML = html;
    }

    function startAdminListWatch() {
        stopAdminListWatch();
        var db = getDb();
        if (!db || !isAdmin()) return;
        var body = $id('chatBody');
        if (body) body.innerHTML = '<div class="chat-empty"><i class="fas fa-spinner fa-pulse"></i><div class="title">Đang tải...</div></div>';
        CHAT.adminListUnsub = db.collection('chat_threads')
            .orderBy('lastMessageAt', 'desc').limit(30)
            .onSnapshot(function(snap) {
                if (snap.empty) {
                    if (body) body.innerHTML = '<div class="chat-empty"><i class="fas fa-comments"></i><div class="title">Chưa có hội thoại</div></div>';
                    setFabBadge(0);
                    if (CHAT.isOpen) setTimeout(positionChatBox, 30);
                    return;
                }
                var html = '', totalUnread = 0;
                snap.forEach(function(doc) {
                    var d = doc.data();
                    var email = d.userEmail || doc.id;
                    var name = d.userName || email.split('@')[0];
                    var unread = d.unreadByAdmin || 0;
                    totalUnread += unread;
                    var lastAt = d.lastMessageAt ? d.lastMessageAt.toDate() : new Date();
                    var preview = d.lastMessage || '(chưa có tin nhắn)';
                    if (d.lastMessageFrom === 'admin') preview = 'Bạn: ' + preview;
                    var initial = (name.charAt(0) || '?').toUpperCase();
                    html += '<div class="admin-chat-thread' + (unread>0?' unread':'') + '" onclick="window.__chatOpenThread(\'' + jsStr(email) + '\')">' +
                        '<div class="t-avatar">' + esc(initial) + '</div>' +
                        '<div class="t-info"><div class="t-name">' + esc(name) + '</div>' +
                        '<div class="t-preview">' + esc(preview) + '</div></div>' +
                        '<div class="t-time">' + timeAgo(Date.now() - lastAt.getTime()) + '</div>' +
                        (unread>0 ? '<div class="t-badge">' + (unread>99?'99+':unread) + '</div>' : '') +
                    '</div>';
                });
                if (body) body.innerHTML = html;
                setFabBadge(totalUnread);
                if (CHAT.isOpen) { setTimeout(positionChatBox, 30); setTimeout(positionChatBox, 300); }
            }, function(err) { console.error('Admin list watch error:', err); });
    }
    function stopAdminListWatch() {
        if (CHAT.adminListUnsub) { try { CHAT.adminListUnsub(); } catch(e){} CHAT.adminListUnsub = null; }
    }
    function startAdminThreadWatch(email) {
        stopAdminThreadWatch();
        var db = getDb();
        if (!db || !isAdmin()) return;
        CHAT.adminCurrentEmail = email;
        var threadRef = db.collection('chat_threads').doc(email);
        threadRef.get().then(function(doc) {
            var d = doc.exists ? doc.data() : {};
            var name = d.userName || email.split('@')[0];
            $id('chatHeaderInfo').innerHTML = '<div class="name">' + esc(name) + '</div><div class="status">' + esc(email) + '</div>';
        }).catch(function(){});
        CHAT.adminThreadUnsub = threadRef.onSnapshot(function(doc) {
            if (!doc.exists) return;
            var d = doc.data();
            if (CHAT.isOpen && CHAT.adminCurrentEmail === email) {
                renderAdminMessages(d);
                if ((d.unreadByAdmin || 0) > 0) threadRef.update({ unreadByAdmin: 0 }).catch(function(){});
            }
            var userTyping = d.userTypingAt;
            var show = false;
            if (userTyping) {
                var ms = userTyping.toMillis ? userTyping.toMillis() : 0;
                if (ms && (Date.now() - ms) < 5000) show = true;
            }
            var tEl = $id('chatTypingIndicator');
            if (tEl) tEl.classList.toggle('show', show);
        }, function(err) { console.error('Admin thread watch error:', err); });
    }
    function stopAdminThreadWatch() {
        if (CHAT.adminThreadUnsub) { try { CHAT.adminThreadUnsub(); } catch(e){} CHAT.adminThreadUnsub = null; }
    }
    function renderAdminMessages(d) {
        var body = $id('chatBody');
        if (!body) return;
        var msgs = d.messages || [];
        if (msgs.length === 0) {
            body.innerHTML = '<div class="chat-empty"><i class="fas fa-comments"></i>' +
                '<div class="title">Chưa có tin nhắn</div>' +
                '<div class="desc">Gửi tin nhắn chào user để bắt đầu.</div></div>' +
                '<div class="chat-typing" id="chatTypingIndicator"><span>Đang trả lời</span><span class="dots"><span></span><span></span><span></span></span></div>';
            if (CHAT.isOpen) { setTimeout(positionChatBox, 30); setTimeout(positionChatBox, 300); }
            return;
        }
        var html = '', lastDate = null;
        msgs.forEach(function(m) {
            var at = m.at ? (m.at.toDate ? m.at.toDate() : new Date((m.at.seconds||0)*1000)) : new Date();
            var dateStr = at.toLocaleDateString('vi-VN');
            if (dateStr !== lastDate) { html += '<div class="chat-system">' + dateStr + '</div>'; lastDate = dateStr; }
            var time = at.toLocaleTimeString('vi-VN', {hour:'2-digit',minute:'2-digit'});
            var isAdminMsg = (m.from === 'admin');
            html += '<div class="chat-msg ' + (isAdminMsg?'from-user':'from-admin') + '">' +
                '<div class="bubble">' + esc(m.text||'').replace(/\n/g,'<br>') + '</div>' +
                '<span class="msg-time">' + time + '</span></div>';
        });
        html += '<div class="chat-typing" id="chatTypingIndicator"><span>Đang trả lời</span><span class="dots"><span></span><span></span><span></span></span></div>';
        body.innerHTML = html;
        var nearBottom = body.scrollHeight - body.scrollTop - body.clientHeight < 150;
        if (nearBottom) setTimeout(function(){ body.scrollTop = body.scrollHeight; }, 30);
        if (CHAT.isOpen) { setTimeout(positionChatBox, 30); setTimeout(positionChatBox, 300); }
    }

    function openChat() {
        var u = getCu();
        if (!u) { if (typeof window.showLoginModal === 'function') window.showLoginModal(); return; }
        CHAT.isOpen = true;
        $id('chatModal').classList.add('show');
        document.body.classList.add('chat-is-open');
        positionChatBox();
        var dd = $id('userDropdown');
        if (dd) dd.classList.remove('show');
        if (isAdmin()) {
            openAdminListView();
            startOnlineWatch();
        } else {
            openUserView();
            updateCounterUI();
        }
        setTimeout(positionChatBox, 30);
        setTimeout(positionChatBox, 320);
    }

    function closeChat() {
        CHAT.isOpen = false;
        $id('chatModal').classList.remove('show');
        document.body.classList.remove('chat-is-open');
        var box = document.querySelector('.chat-box');
        if (box) box.classList.remove('admin-thread-open');
        stopAdminThreadWatch();
        stopOnlineWatch();
        CHAT.adminCurrentEmail = null;
        CHAT.lastSeenAt = Date.now();
        resetSpamState();
    }

    function openUserView() {
        $id('chatHeaderInfo').innerHTML = '<div class="name">Hỗ trợ Admin</div><div class="status">Thường trả lời trong 5-10 phút</div>';
        $id('chatBack').classList.remove('show');
        $id('chatClose').style.display = 'flex';
        $id('chatQuickReplies').classList.add('hidden');
        var box = document.querySelector('.chat-box');
        if (box) box.classList.remove('admin-thread-open');
        if (CHAT.lastThreadData) renderUserMessages(CHAT.lastThreadData);
        setTimeout(positionChatBox, 30);
        setTimeout(positionChatBox, 320);
    }

    function openAdminListView() {
        $id('chatHeaderInfo').innerHTML = '<div class="name">Chat hỗ trợ</div><div class="status">Chọn user để trả lời</div>';
        $id('chatBack').classList.remove('show');
        $id('chatClose').style.display = 'flex';
        $id('chatQuickReplies').classList.add('hidden');
        var box = document.querySelector('.chat-box');
        if (box) box.classList.remove('admin-thread-open');
        stopAdminThreadWatch();
        CHAT.adminCurrentEmail = null;
        startAdminListWatch();
        setTimeout(positionChatBox, 30);
        setTimeout(positionChatBox, 320);
    }

    function openAdminThread(email) {
        if (!isAdmin()) return;
        stopAdminListWatch();
        $id('chatHeaderInfo').innerHTML = '<div class="name">Đang tải...</div><div class="status">' + esc(email) + '</div>';
        $id('chatBack').classList.add('show');
        $id('chatClose').style.display = 'none';
        $id('chatQuickReplies').classList.remove('hidden');
        var box = document.querySelector('.chat-box');
        if (box) box.classList.add('admin-thread-open');
        startAdminThreadWatch(email);
        setTimeout(positionChatBox, 30);
        setTimeout(positionChatBox, 320);
    }

    function sendMessage() {
        var input = $id('chatInput');
        var text = input.value.trim();
        if (!text) return;
        var u = getCu(), db = getDb();
        if (!u || !db) return;
        var targetEmail, from;
        if (CHAT.adminCurrentEmail) { targetEmail = CHAT.adminCurrentEmail; from = 'admin'; }
        else if (!isAdmin()) {
            targetEmail = u.email; from = 'user';
            if (!canSend()) {
                var banner = $id('chatLimitBanner');
                if (banner) banner.classList.add('show', 'danger');
                input.style.animation = 'chatBellShake 0.4s';
                setTimeout(function() { input.style.animation = ''; }, 500);
                return;
            }
            var spamCheck = checkSpam(text);
            if (!spamCheck.allowed) {
                showSpamError(spamCheck.reason, spamCheck.waitMs);
                return;
            }
        } else return;

        SPAM.isSending = true;
        var btn = $id('chatSendBtn');
        btn.disabled = true;
        input.value = '';
        autoResize();
        var threadRef = db.collection('chat_threads').doc(targetEmail);
        var newMsg = {
            from: from, fromEmail: u.email, fromName: u.name || 'User',
            text: text, at: firebase.firestore.Timestamp.now()
        };
        threadRef.get().then(function(doc) {
            var data = doc.exists ? doc.data() : {};
            var msgs = data.messages || [];
            msgs.push(newMsg);
            if (msgs.length > MAX_MESSAGES) msgs = msgs.slice(-MAX_MESSAGES);
            var update = {
                messages: msgs, lastMessage: text.substring(0, 100),
                lastMessageAt: firebase.firestore.FieldValue.serverTimestamp(),
                lastMessageFrom: from,
                userEmail: targetEmail,
                userName: data.userName || u.name || targetEmail.split('@')[0]
            };
            if (from === 'user') {
                update.unreadByAdmin = (data.unreadByAdmin || 0) + 1;
                update.unreadByUser = 0;
                update.userTypingAt = null;
            } else {
                update.unreadByUser = (data.unreadByUser || 0) + 1;
                update.unreadByAdmin = 0;
                update.adminTypingAt = null;
            }
            return threadRef.set(update, { merge: true });
        }).then(function() {
            if (from === 'user') {
                incDailyCount();
                updateCounterUI();
                updateSpamState(text);
                if (typeof window.__sendTelegramNotify === 'function') {
                    window.__sendTelegramNotify(targetEmail, u.name || u.email.split('@')[0], text, 'user');
                }
                try {
                    db.collection('activity_logs').add({
                        email: u.email,
                        type: 'chat',
                        title: 'Gửi tin nhắn cho Admin',
                        detail: text.substring(0, 100),
                        at: firebase.firestore.FieldValue.serverTimestamp()
                    });
                } catch(e) {}
            } else {
                SPAM.isSending = false;
            }
        }).catch(function(err) {
            alert('Lỗi gửi tin: ' + err.message);
            SPAM.isSending = false;
        }).finally(function() {
            btn.disabled = !input.value.trim();
        });
    }
    function autoResize() {
        var inp = $id('chatInput');
        if (!inp) return;
        inp.style.height = 'auto';
        inp.style.height = Math.min(inp.scrollHeight, 130) + 'px';
    }
    function markTyping() {
        var u = getCu(), db = getDb();
        if (!u || !db || CHAT.typingTimer) return;
        var threadEmail, field;
        if (CHAT.adminCurrentEmail) { threadEmail = CHAT.adminCurrentEmail; field = 'adminTypingAt'; }
        else if (!isAdmin()) { threadEmail = u.email; field = 'userTypingAt'; }
        else return;
        var data = {};
        data[field] = firebase.firestore.FieldValue.serverTimestamp();
        db.collection('chat_threads').doc(threadEmail).set(data, { merge: true }).catch(function(){});
        CHAT.typingTimer = setTimeout(function() { CHAT.typingTimer = null; }, 3000);
    }

    function init() {
        if (CHAT.inited) return;
        CHAT.inited = true;
        mountChatButton();
        initLimitBanner();
        var closeBtn = $id('chatClose');
        if (closeBtn) closeBtn.addEventListener('click', closeChat);
        var backBtn = $id('chatBack');
        if (backBtn) backBtn.addEventListener('click', function() { if (isAdmin()) openAdminListView(); });
        var modal = $id('chatModal');
        if (modal) modal.addEventListener('click', function(e) { if (e.target === this) closeChat(); });
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && CHAT.isOpen) closeChat();
        });
        var input = $id('chatInput');
        if (input) {
            input.addEventListener('input', function() {
                autoResize();
                $id('chatSendBtn').disabled = !this.value.trim();
                if (this.value.trim()) markTyping();
            });
            input.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    if (!this.value.trim()) return;
                    sendMessage();
                }
            });
        }
        var sendBtn = $id('chatSendBtn');
        if (sendBtn) sendBtn.addEventListener('click', sendMessage);
        document.querySelectorAll('.chat-quick-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var inp = $id('chatInput');
                inp.value = this.dataset.reply || this.textContent.trim();
                autoResize();
                $id('chatSendBtn').disabled = false;
                inp.focus();
            });
        });

        var toggleOnlineBtn = $id('toggleOnlineBtn');
        var onlineSection = $id('adminOnlineSection');
        if (toggleOnlineBtn && onlineSection) {
            toggleOnlineBtn.addEventListener('click', function() {
                onlineSection.classList.toggle('collapsed');
                var isVisible = !onlineSection.classList.contains('collapsed');
                var icon = this.querySelector('i');
                if (icon) icon.className = isVisible ? 'fas fa-eye' : 'fas fa-eye-slash';
                this.classList.toggle('active', isVisible);
                this.title = isVisible ? 'Ẩn' : 'Hiện';
            });
        }

        syncFloatingGroupState();
        setInterval(syncFloatingGroupState, 1000);

        window.addEventListener('resize', function() {
            if (CHAT.isOpen) positionChatBox();
        });

        window.addEventListener('scroll', function() {
            if (CHAT.isOpen) positionChatBox();
        }, { passive: true });

        window.__chatOpenThread = openAdminThread;
        window.__chatOpen = openChat;
        window.__chatPosition = positionChatBox;
    }

    var _lastEmail = null;
    function watchAuth() {
        setInterval(function() {
            var u = getCu();
            var email = u ? u.email : null;
            if (email === _lastEmail) return;
            _lastEmail = email;
            updateFabVisibility();
            stopUserThreadWatch();
            stopAdminListWatch();
            stopAdminThreadWatch();
            if (email) {
                if (isAdmin()) startAdminListWatch();
                else { startUserThreadWatch(); updateCounterUI(); }
            } else {
                setFabBadge(0);
                if (CHAT.isOpen) closeChat();
            }
            if (CHAT.isOpen) setTimeout(positionChatBox, 100);
        }, 2000);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() { init(); updateFabVisibility(); watchAuth(); });
    } else {
        init(); updateFabVisibility(); watchAuth();
    }
})();
"""


def build_quota_js():
    return r"""
(function() {
    'use strict';

    var QUOTA = {
        inited: false,
        reads: 0, writes: 0, deletes: 0,
        lastMinuteReads: 0,
        lastMinuteTs: Date.now(),
        history: {}
    };

    var LIMIT_READS = 50000;
    var LIMIT_WRITES = 20000;
    var LIMIT_DELETES = 20000;
    var WARN_PCT = 70;
    var DANGER_PCT = 90;

    function $id(id) { return document.getElementById(id); }
    function todayKey() {
        var d = new Date();
        return d.getFullYear() + '-' + String(d.getMonth()+1).padStart(2,'0') + '-' + String(d.getDate()).padStart(2,'0');
    }
    function getQuotaKey() { return 'quota_' + todayKey(); }

    function loadQuota() {
        try {
            var raw = localStorage.getItem(getQuotaKey());
            if (raw) {
                var q = JSON.parse(raw);
                QUOTA.reads = q.reads || 0;
                QUOTA.writes = q.writes || 0;
                QUOTA.deletes = q.deletes || 0;
            }
            var h = localStorage.getItem('quota_history');
            if (h) QUOTA.history = JSON.parse(h);
        } catch(e) {}
    }
    function saveQuota() {
        try {
            localStorage.setItem(getQuotaKey(), JSON.stringify({
                reads: QUOTA.reads, writes: QUOTA.writes, deletes: QUOTA.deletes
            }));
            var keys = Object.keys(QUOTA.history).sort().slice(-7);
            var newH = {};
            keys.forEach(function(k) { newH[k] = QUOTA.history[k]; });
            QUOTA.history = newH;
            localStorage.setItem('quota_history', JSON.stringify(QUOTA.history));
        } catch(e) {}
    }

    window.__quotaTrack = function(type, n) {
        n = n || 1;
        if (type === 'read') QUOTA.reads += n;
        else if (type === 'write') QUOTA.writes += n;
        else if (type === 'delete') QUOTA.deletes += n;
        saveQuota();
        updateQuotaUI();
    };

    function wrapFirestore() {
        if (!window.firebase || !window.firebase.firestore) return false;
        if (window.__quotaWrapped) return true;
        window.__quotaWrapped = true;

        var docProto = firebase.firestore.DocumentReference.prototype;
        var colProto = firebase.firestore.CollectionReference.prototype;

        var origDocGet = docProto.get;
        docProto.get = function() {
            return origDocGet.apply(this, arguments).then(function(r) {
                window.__quotaTrack('read', 1);
                return r;
            });
        };

        var origColGet = colProto.get;
        colProto.get = function() {
            return origColGet.apply(this, arguments).then(function(snap) {
                window.__quotaTrack('read', snap.size || 1);
                return snap;
            });
        };

        var origSet = docProto.set;
        docProto.set = function() {
            window.__quotaTrack('write', 1);
            return origSet.apply(this, arguments);
        };

        var origUpdate = docProto.update;
        docProto.update = function() {
            window.__quotaTrack('write', 1);
            return origUpdate.apply(this, arguments);
        };

        var origDelete = docProto.delete;
        docProto.delete = function() {
            window.__quotaTrack('delete', 1);
            return origDelete.apply(this, arguments);
        };

        var origAdd = colProto.add;
        colProto.add = function() {
            window.__quotaTrack('write', 1);
            return origAdd.apply(this, arguments);
        };

        return true;
    }

    function pct(v, max) { return Math.min(100, (v / max) * 100); }
    function setCardStatus(card, p) {
        if (!card) return;
        card.classList.remove('warn', 'danger');
        if (p >= DANGER_PCT) card.classList.add('danger');
        else if (p >= WARN_PCT) card.classList.add('warn');
    }

    function updateQuotaUI() {
        var elR = $id('quotaReads');
        var barR = $id('quotaReadsBar');
        var pR = pct(QUOTA.reads, LIMIT_READS);
        if (elR) elR.textContent = QUOTA.reads.toLocaleString('vi-VN');
        if (barR) barR.style.width = pR + '%';
        if (elR) setCardStatus(elR.closest('.quota-card'), pR);

        var elW = $id('quotaWrites');
        var barW = $id('quotaWritesBar');
        var pW = pct(QUOTA.writes, LIMIT_WRITES);
        if (elW) elW.textContent = QUOTA.writes.toLocaleString('vi-VN');
        if (barW) barW.style.width = pW + '%';
        if (elW) setCardStatus(elW.closest('.quota-card'), pW);

        var elD = $id('quotaDeletes');
        var barD = $id('quotaDeletesBar');
        var pD = pct(QUOTA.deletes, LIMIT_DELETES);
        if (elD) elD.textContent = QUOTA.deletes.toLocaleString('vi-VN');
        if (barD) barD.style.width = pD + '%';
        if (elD) setCardStatus(elD.closest('.quota-card'), pD);

        var chip = $id('quotaStatusChip');
        if (chip) {
            var maxPct = Math.max(pR, pW, pD);
            if (maxPct >= DANGER_PCT) { chip.textContent = 'Nguy hiểm (' + Math.round(maxPct) + '%)'; chip.style.color = '#dc2626'; }
            else if (maxPct >= WARN_PCT) { chip.textContent = 'Cảnh báo (' + Math.round(maxPct) + '%)'; chip.style.color = '#d97706'; }
            else { chip.textContent = 'OK (' + Math.round(maxPct) + '%)'; chip.style.color = ''; }
        }

        var elTime = $id('quotaResetTime');
        if (elTime) {
            var now = new Date();
            var utc = new Date(now.getTime() + now.getTimezoneOffset() * 60000);
            var tomorrow = new Date(Date.UTC(utc.getUTCFullYear(), utc.getUTCMonth(), utc.getUTCDate() + 1));
            var diff = tomorrow.getTime() - now.getTime();
            var h = Math.floor(diff / 3600000);
            var m = Math.floor((diff % 3600000) / 60000);
            var s = Math.floor((diff % 60000) / 1000);
            elTime.textContent = String(h).padStart(2,'0') + ':' + String(m).padStart(2,'0') + ':' + String(s).padStart(2,'0');
        }

        var now2 = Date.now();
        if (now2 - QUOTA.lastMinuteTs >= 60000) {
            QUOTA.lastMinuteReads = QUOTA.reads;
            QUOTA.lastMinuteTs = now2;
        }
        var elRate = $id('quotaReadRate');
        if (elRate) elRate.textContent = QUOTA.lastMinuteReads.toLocaleString('vi-VN');

        var elOnline = $id('quotaOnlineUsers');
        if (elOnline) {
            var count = 0;
            try {
                for (var i = 0; i < localStorage.length; i++) {
                    var k = localStorage.key(i);
                    if (k && k.indexOf('chat_init_') === 0) count++;
                }
            } catch(e) {}
            elOnline.textContent = count.toLocaleString('vi-VN');
        }

        var histBody = $id('quotaHistoryBody');
        if (histBody) {
            var keys = Object.keys(QUOTA.history).sort().reverse();
            if (keys.length === 0) {
                histBody.innerHTML = '<tr><td colspan="5" style="text-align:center;color:var(--text-3);padding:1rem;">Chưa có dữ liệu</td></tr>';
            } else {
                var html = '';
                keys.forEach(function(k) {
                    var h = QUOTA.history[k];
                    var pR2 = pct(h.reads || 0, LIMIT_READS);
                    var pW2 = pct(h.writes || 0, LIMIT_WRITES);
                    var maxP = Math.max(pR2, pW2);
                    var cls = 'qht-ok', txt = 'OK';
                    if (maxP >= DANGER_PCT) { cls = 'qht-danger'; txt = 'Nguy hiểm'; }
                    else if (maxP >= WARN_PCT) { cls = 'qht-warn'; txt = 'Cảnh báo'; }
                    html += '<tr>' +
                        '<td>' + k + '</td>' +
                        '<td>' + (h.reads || 0).toLocaleString('vi-VN') + '</td>' +
                        '<td>' + (h.writes || 0).toLocaleString('vi-VN') + '</td>' +
                        '<td>' + (h.deletes || 0).toLocaleString('vi-VN') + '</td>' +
                        '<td class="' + cls + '">' + txt + '</td>' +
                    '</tr>';
                });
                histBody.innerHTML = html;
            }
        }
    }

    function saveToHistory() {
        var k = todayKey();
        QUOTA.history[k] = {
            reads: QUOTA.reads,
            writes: QUOTA.writes,
            deletes: QUOTA.deletes
        };
        saveQuota();
    }
    setInterval(saveToHistory, 60000);

    function init() {
        if (QUOTA.inited) return;
        QUOTA.inited = true;
        loadQuota();
        var tries = 0;
        var timer = setInterval(function() {
            tries++;
            if (wrapFirestore() || tries > 20) clearInterval(timer);
        }, 500);
        updateQuotaUI();
        setInterval(updateQuotaUI, 5000);
        setTimeout(saveToHistory, 3000);
    }

    window.__quotaReset = function() {
        if (!confirm('Reset đếm quota hôm nay?')) return;
        QUOTA.reads = 0; QUOTA.writes = 0; QUOTA.deletes = 0;
        saveQuota();
        updateQuotaUI();
    };
    window.__quotaExport = function() {
        var rows = [['Date', 'Reads', 'Writes', 'Deletes']];
        Object.keys(QUOTA.history).sort().forEach(function(k) {
            var h = QUOTA.history[k];
            rows.push([k, h.reads || 0, h.writes || 0, h.deletes || 0]);
        });
        var csv = rows.map(function(r) { return r.join(','); }).join('\n');
        var blob = new Blob([csv], { type: 'text/csv' });
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'quota_' + todayKey() + '.csv';
        a.click();
        URL.revokeObjectURL(url);
    };
    window.__quotaSimulate = function() {
        QUOTA.reads += 5000;
        QUOTA.writes += 2000;
        saveQuota();
        updateQuotaUI();
        alert('Đã thêm 5.000 reads + 2.000 writes để test cảnh báo.');
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
"""


def build_quota_init_js():
    return r"""
(function() {
    'use strict';
    function $id(id) { return document.getElementById(id); }

    function bindQuotaButtons() {
        var resetBtn = $id('quotaResetBtn');
        if (resetBtn && !resetBtn._bound) {
            resetBtn._bound = true;
            resetBtn.addEventListener('click', function() {
                if (typeof window.__quotaReset === 'function') window.__quotaReset();
            });
        }
        var expBtn = $id('quotaExportBtn');
        if (expBtn && !expBtn._bound) {
            expBtn._bound = true;
            expBtn.addEventListener('click', function() {
                if (typeof window.__quotaExport === 'function') window.__quotaExport();
            });
        }
        var simBtn = $id('quotaSimBtn');
        if (simBtn && !simBtn._bound) {
            simBtn._bound = true;
            simBtn.addEventListener('click', function() {
                if (typeof window.__quotaSimulate === 'function') window.__quotaSimulate();
            });
        }
        var refBtn = $id('refreshQuotaBtn');
        if (refBtn && !refBtn._bound) {
            refBtn._bound = true;
            refBtn.addEventListener('click', function() {
                window.dispatchEvent(new Event('quota-refresh'));
                if (window.__quotaTrack) window.__quotaTrack('read', 0);
            });
        }
        var toggleQuotaBtn = $id('toggleQuotaBtn');
        var quotaSection = $id('adminQuotaSection');
        if (toggleQuotaBtn && quotaSection && !toggleQuotaBtn._bound) {
            toggleQuotaBtn._bound = true;
            toggleQuotaBtn.addEventListener('click', function() {
                quotaSection.classList.toggle('collapsed');
                var isVisible = !quotaSection.classList.contains('collapsed');
                var icon = this.querySelector('i');
                if (icon) icon.className = isVisible ? 'fas fa-eye' : 'fas fa-eye-slash';
                this.classList.toggle('active', isVisible);
                this.title = isVisible ? 'Ẩn' : 'Hiện';
            });
        }
    }

    bindQuotaButtons();
    setTimeout(bindQuotaButtons, 1000);
    setTimeout(bindQuotaButtons, 3000);
})();
"""
