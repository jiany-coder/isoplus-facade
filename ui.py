# Couche design premium ISO + (importée par build.py)
I = {
 "shield": '<path d="M20 13c0 5-3.5 7.5-7.7 8.9a1 1 0 0 1-.6 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.6 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "award": '<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/>',
 "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "home": '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 "brush": '<path d="m9.1 11 7.5-7.5a2.1 2.1 0 0 1 3 3L12 14"/><path d="M7 14a3 3 0 0 0-3 3c0 1.3-2 2-2 2s3 2 6 0a3 3 0 0 0-1-5z"/>',
 "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10Z"/><path d="M2 21c0-3 1.9-5.4 5.2-6"/>',
 "drop": '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5S5 13 5 15a7 7 0 0 0 7 7z"/>',
 "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>',
 "grid": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/>',
 "building": '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18zM6 12H4a2 2 0 0 0-2 2v8h4M18 9h2a2 2 0 0 1 2 2v11h-4M10 6h4M10 10h4M10 14h4M10 18h4"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "arrow": '<path d="M5 12h14M13 5l7 7-7 7"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "euro": '<path d="M4 10h12M4 14h9M19 6a7.7 7.7 0 0 0-5.2-2A7.9 7.9 0 0 0 6 12c0 4.4 3.5 8 7.8 8 2 0 3.8-.8 5.2-2"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "camera": '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3z"/><circle cx="12" cy="13" r="3"/>',
}
def ic(k, s=22, c=""):
    return f'<svg class="i {c}" viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[k]}</svg>'

SICON = {"ravalement-facade-rouen":"home","peinture-exterieure-rouen":"brush","isolation-thermique-exterieur-rouen":"leaf","nettoyage-facade-rouen":"drop","bardage-rouen":"layers","isolation-plancher-rouen":"grid","facade-isolation-professionnels-rouen":"building"}
SBEN = {"ravalement-facade-rouen":"Fissures traitées, murs protégés de l'humidité et valeur de votre bien préservée.",
 "peinture-exterieure-rouen":"Une façade comme neuve, une teinte qui tient et un mur protégé de la pluie.",
 "isolation-thermique-exterieur-rouen":"Moins de chauffage, plus de confort, aides de l'État possibles grâce au label RGE.",
 "nettoyage-facade-rouen":"Mousses et salissures retirées sans abîmer la brique, la pierre ou l'enduit.",
 "bardage-rouen":"Une maison modernisée et un mur protégé, avec isolation possible derrière.",
 "isolation-plancher-rouen":"Fini le sol froid : un chantier rapide, souvent en une à deux journées.",
 "facade-isolation-professionnels-rouen":"Bureaux, collectivités et copropriétés : chantier phasé, locaux ouverts."}
SCTA = {"isolation-thermique-exterieur-rouen":"Étudier mon isolation","facade-isolation-professionnels-rouen":"Obtenir une étude","peinture-exterieure-rouen":"Estimer ma peinture"}

CSS2 = r"""
:root{--b:#0582DB;--bl:#2fa4f0;--bd:#046bb5;--gr:#3fae22;--k:#0f1115;--k2:#181b21;--g:#f3f6f9;--t:#525862;--line:#e4e8ee;--r:22px;--sh:0 30px 60px -20px rgba(15,17,21,.25)}
body{font-size:16.5px;padding-bottom:0}
h1{font-size:clamp(2.3rem,6vw,4.7rem);letter-spacing:-.035em;line-height:1}
h2{font-size:clamp(1.9rem,4vw,3.2rem);letter-spacing:-.03em}
section>.w>h2:before,.prose>h2:first-child:before{display:none}
.eb{display:inline-flex;align-items:center;gap:8px;font:700 .74rem Inter;letter-spacing:.2em;text-transform:uppercase;color:var(--b);margin-bottom:14px}.eb:before{content:"";width:26px;height:2px;background:var(--b);border-radius:2px}
.dark .eb,.hero .eb{color:var(--bl)}.dark .eb:before,.hero .eb:before{background:var(--bl)}
.sh{display:flex;justify-content:space-between;align-items:end;gap:30px;margin-bottom:44px;flex-wrap:wrap}.sh p{margin:0;max-width:52ch}.sh h2{margin:0;max-width:18ch}
.i{flex:none}
/* boutons */
.btn{border-radius:14px;padding:16px 26px;font-weight:700;letter-spacing:-.01em;position:relative;overflow:hidden;color:#fff!important;background:linear-gradient(180deg,#1b95ea,#0476c7);box-shadow:0 10px 24px -6px rgba(5,130,219,.55),inset 0 1px 0 rgba(255,255,255,.25)}
.btn:hover{background:linear-gradient(180deg,#24a0f5,#0582DB);box-shadow:0 16px 30px -8px rgba(5,130,219,.65);transform:translateY(-2px)}
.btn .i{transition:transform .25s}.btn:hover .i{transform:translateX(3px)}
.btn.o{background:linear-gradient(180deg,#58cc35,#3a9f1f);box-shadow:0 10px 24px -6px rgba(63,174,34,.55),inset 0 1px 0 rgba(255,255,255,.3)}.btn.o:hover{background:linear-gradient(180deg,#66d943,#3fae22)}.btn.o:hover .i{transform:rotate(-12deg)}
.btn.w2{background:#fff;color:var(--k)!important;box-shadow:0 10px 24px -8px rgba(0,0,0,.35)}
.btn.ghost{background:transparent;color:var(--k)!important;box-shadow:inset 0 0 0 1.5px var(--line)}.btn.ghost:hover{box-shadow:inset 0 0 0 1.5px var(--b);color:var(--b)!important;background:transparent}
.lnk{display:inline-flex;align-items:center;gap:6px;font-weight:700;color:var(--b);text-decoration:none}.lnk:hover .i{transform:translateX(3px)}.lnk .i{transition:.25s}
/* header */
header .w{gap:18px}.hcta{display:flex;gap:10px;align-items:center}.hcta .btn{padding:13px 20px;font-size:.95rem}
.call{background:linear-gradient(180deg,#58cc35,#3a9f1f);box-shadow:0 8px 20px -6px rgba(63,174,34,.55),inset 0 1px 0 rgba(255,255,255,.3);border-radius:12px;padding:13px 18px}
.call:hover{box-shadow:0 12px 26px -8px rgba(63,174,34,.65)}
nav a{position:relative}nav>a:after{content:"";position:absolute;left:0;right:0;bottom:-6px;height:2px;background:var(--b);transform:scaleX(0);transition:.25s;border-radius:2px}nav>a:hover:after{transform:scaleX(1)}
/* hero premium */
.hx{position:relative;min-height:100vh;min-height:100svh;display:flex;align-items:flex-end;padding:170px 0 0;color:#fff;overflow:hidden;background:#1a1d22}
.hx>img.bgi{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;animation:kb 18s ease-out both}
@keyframes kb{from{transform:scale(1.08)}to{transform:scale(1)}}
.hx:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,12,15,.78) 0%,rgba(10,12,15,.45) 45%,rgba(10,12,15,0) 75%),linear-gradient(0deg,rgba(10,12,15,.55),transparent 40%)}
.hx .w{position:relative;z-index:2;width:100%;display:grid;grid-template-columns:1.25fr .75fr;gap:30px;align-items:end;padding-bottom:40px}
.hx h1{color:#fff;margin-bottom:20px}.hx h1 span{color:var(--bl)}
.hx .lead{font-size:1.18rem;color:rgba(255,255,255,.9);max-width:56ch;margin-bottom:30px}
.hx .cta .btn{padding:18px 28px;font-size:1.02rem}
.chips2{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px;list-style:none}.chips2 li{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);backdrop-filter:blur(8px);padding:9px 14px;border-radius:999px;font-size:.88rem;font-weight:600}.chips2 .i{color:#7fd65f}
.hx .mwrap{margin-bottom:-6px}
/* bandeau réassurance */
.trustbar{position:relative;z-index:3;margin-top:-1px;background:#fff;border-bottom:1px solid var(--line)}
.trustbar .w{display:grid;grid-template-columns:repeat(4,1fr)}
.tb{display:flex;gap:14px;align-items:center;padding:28px 18px}.tb+.tb{border-left:1px solid var(--line)}
.tb .ib{width:50px;height:50px;border-radius:14px;background:rgba(5,130,219,.09);color:var(--b);display:grid;place-items:center}
.tb b{display:block;color:var(--k);font:800 1.05rem Barlow}.tb span{font-size:.86rem;line-height:1.4;display:block}
/* cartes prestations */
.sgrid{display:grid;grid-template-columns:repeat(12,1fr);gap:20px}
.sc{grid-column:span 4;position:relative;border-radius:var(--r);overflow:hidden;background:#fff;border:1px solid var(--line);display:flex;flex-direction:column;transition:transform .35s,box-shadow .35s;text-decoration:none;color:inherit}
.sc.big{grid-column:span 6}
.sc:hover{transform:translateY(-6px);box-shadow:var(--sh)}
.sc .im{position:relative;aspect-ratio:16/10;overflow:hidden}.sc .im img{width:100%;height:100%;object-fit:cover;transition:transform .7s}.sc:hover .im img{transform:scale(1.06)}
.sc .bad{position:absolute;top:14px;left:14px;width:46px;height:46px;border-radius:13px;background:#fff;color:var(--b);display:grid;place-items:center;box-shadow:0 8px 20px rgba(0,0,0,.18)}
.sc .num{position:absolute;top:16px;right:16px;font:800 .78rem Inter;letter-spacing:.12em;color:#fff;background:rgba(15,17,21,.55);backdrop-filter:blur(6px);padding:6px 10px;border-radius:999px}
.sc .bd{padding:24px 26px 26px;display:flex;flex-direction:column;gap:10px;flex:1}.sc h3{margin:0;font-size:1.35rem}.sc p{margin:0;font-size:.95rem}
.sc .lnk{margin-top:auto;padding-top:8px}
/* réalisations */
.gal2{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:220px;gap:14px}
.gal2 figure{position:relative;border-radius:18px;overflow:hidden;margin:0}.gal2 figure:nth-child(1){grid-column:span 2;grid-row:span 2}
.gal2 img{width:100%;height:100%;object-fit:cover;transition:transform .7s}.gal2 figure:hover img{transform:scale(1.06)}
.gal2 figcaption{position:absolute;left:12px;bottom:12px;background:rgba(255,255,255,.92);color:var(--k);font:700 .8rem Inter;padding:7px 12px;border-radius:999px}
.ba{position:relative;border-radius:22px;overflow:hidden;aspect-ratio:16/9;background:#222;user-select:none}
.ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.ba .af{clip-path:inset(0 0 0 50%)}
.ba input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.ba .hd{position:absolute;top:0;bottom:0;left:50%;width:3px;background:#fff;transform:translateX(-50%);pointer-events:none}.ba .hd:after{content:"⟷";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:46px;height:46px;border-radius:50%;background:#fff;color:var(--k);display:grid;place-items:center;font-weight:800;box-shadow:0 6px 20px rgba(0,0,0,.3)}
.ba .lb{position:absolute;top:14px;background:rgba(15,17,21,.7);color:#fff;font:700 .75rem Inter;letter-spacing:.12em;padding:6px 10px;border-radius:999px}.ba .l1{left:14px}.ba .l2{right:14px}
.soon{border:2px dashed #cdd6e0;border-radius:22px;padding:34px;display:flex;gap:20px;align-items:center;background:#fff;margin-top:20px}.soon .ib{width:56px;height:56px;border-radius:16px;background:rgba(5,130,219,.09);color:var(--b);display:grid;place-items:center;flex:none}.soon p{margin:0}
/* pourquoi */
.why{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.wc{background:var(--k2);border:1px solid rgba(255,255,255,.07);border-radius:var(--r);padding:30px;transition:.3s}.wc:hover{border-color:rgba(47,164,240,.6);transform:translateY(-4px)}
.wc .ib{width:52px;height:52px;border-radius:14px;background:rgba(47,164,240,.14);color:var(--bl);display:grid;place-items:center;margin-bottom:18px}
.wc h3{color:#fff;font-size:1.25rem}.wc p{margin:0;font-size:.95rem}
/* méthode */
.steps2{display:grid;grid-template-columns:repeat(4,1fr);gap:0;counter-reset:s;position:relative}
.steps2:before{content:"";position:absolute;top:27px;left:12%;right:12%;height:2px;background:repeating-linear-gradient(90deg,var(--b) 0 8px,transparent 8px 16px);opacity:.4}
.st{padding:0 18px;text-align:center;position:relative}.st .n{width:56px;height:56px;border-radius:50%;background:var(--b);color:#fff;display:grid;place-items:center;font:800 1.2rem Barlow;margin:0 auto 18px;box-shadow:0 0 0 8px #fff,0 12px 24px -6px rgba(5,130,219,.6)}
.st p{margin:0 auto;font-size:.95rem}
/* focus */
.focus{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.fc{text-decoration:none;position:relative;border-radius:26px;overflow:hidden;min-height:440px;display:flex;align-items:flex-end;color:#fff}
.fc img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .8s}.fc:hover img{transform:scale(1.05)}
.fc:after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,12,15,.88) 10%,rgba(10,12,15,.1) 70%)}
.fc .eb{color:#fff}.fc .ct{position:relative;z-index:1;padding:34px}.fc h3{color:#fff;font-size:clamp(1.5rem,2.6vw,2.1rem)}.fc ul{list-style:none;margin:14px 0 22px;display:grid;gap:6px}.fc li{display:flex;gap:8px;align-items:center;font-size:.95rem}.fc li .i{color:#7fd65f}
/* zone */
.zone{display:grid;grid-template-columns:.9fr 1.1fr;gap:50px;align-items:center}
.zmap{position:relative;aspect-ratio:1;border-radius:28px;background:radial-gradient(circle at 50% 50%,rgba(5,130,219,.14),rgba(5,130,219,.02) 60%),#fff;border:1px solid var(--line);overflow:hidden}
.zmap .ring{position:absolute;left:50%;top:50%;border:1.5px dashed rgba(5,130,219,.35);border-radius:50%;transform:translate(-50%,-50%)}
.zmap .dot{position:absolute;transform:translate(-50%,-50%);font:700 .74rem Inter;color:var(--k);display:flex;align-items:center;gap:5px;white-space:nowrap}.zmap .dot:before{content:"";width:9px;height:9px;border-radius:50%;background:var(--b);box-shadow:0 0 0 4px rgba(5,130,219,.18)}
.zmap .hq{font-size:.86rem}.zmap .hq:before{width:14px;height:14px;background:var(--gr);box-shadow:0 0 0 6px rgba(63,174,34,.2)}
.tags a{border-radius:12px}
/* faq */
.faq details{transition:.25s}.faq details[open]{box-shadow:0 18px 40px -20px rgba(15,17,21,.25);border-color:transparent}
.faq details p{animation:fd .35s ease}@keyframes fd{from{opacity:0;transform:translateY(-4px)}}
/* devis */
.dv{background:var(--k);color:#c3c8cf;position:relative;overflow:hidden}.dv:before{content:"";position:absolute;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(5,130,219,.35),transparent 65%);top:-300px;right:-200px}
.dv .w{position:relative;display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:start}.dv h2{color:#fff}
.dv ul.pl{list-style:none;display:grid;gap:14px;margin:26px 0}.dv ul.pl li{display:flex;gap:12px;align-items:center;color:#fff;font-weight:600}.dv ul.pl .ib{width:40px;height:40px;border-radius:12px;background:rgba(47,164,240,.15);color:var(--bl);display:grid;place-items:center}
.fcard{background:#fff;border-radius:26px;padding:34px;color:var(--t);box-shadow:0 40px 80px -30px rgba(0,0,0,.6)}
.fcard h3{font-size:1.5rem;margin-bottom:4px}.fcard .sub{font-size:.9rem;margin-bottom:22px}
.f2{display:grid;grid-template-columns:1fr 1fr;gap:14px}.f2 .full{grid-column:1/-1}
.fld label{display:block;font:600 .82rem Inter;color:var(--k);margin-bottom:6px}.fld input,.fld select,.fld textarea{border:1.5px solid var(--line);border-radius:12px;padding:14px;font-size:.98rem;transition:.2s;background:#fbfcfd}
.fld input:focus,.fld select:focus,.fld textarea:focus{outline:0;border-color:var(--b);box-shadow:0 0 0 4px rgba(5,130,219,.12);background:#fff}
.fld.err input,.fld.err select{border-color:#d93636}.fld .em{display:none;color:#d93636;font-size:.8rem;margin-top:5px}.fld.err .em{display:block}
.pills{display:flex;flex-wrap:wrap;gap:8px}.pills label{margin:0;cursor:pointer}.pills input{position:absolute;opacity:0;width:1px;height:1px}.pills span{display:inline-block;border:1.5px solid var(--line);border-radius:999px;padding:9px 14px;font:600 .86rem Inter;color:var(--k);transition:.2s;background:#fbfcfd}.pills input:checked+span{background:var(--b);border-color:var(--b);color:#fff}.pills input:focus-visible+span{box-shadow:0 0 0 4px rgba(5,130,219,.2)}
.fcard .btn{width:100%;justify-content:center;padding:19px;font-size:1.05rem;margin-top:6px}
.note{font-size:.8rem;margin-top:12px;line-height:1.5}.note a{color:var(--b)}
.ok{display:none;text-align:center;padding:20px 0}.ok .ib{width:70px;height:70px;border-radius:50%;background:rgba(63,174,34,.12);color:var(--gr);display:grid;place-items:center;margin:0 auto 16px}
.sent .ok{display:block}.sent form{display:none}
/* footer & barre mobile */
.bar{gap:0;box-shadow:0 -10px 30px rgba(0,0,0,.15)}.bar a{display:flex;align-items:center;justify-content:center;gap:8px}.bar a:first-child{background:linear-gradient(180deg,#58cc35,#3a9f1f)}.bar a:last-child{background:linear-gradient(180deg,#1b95ea,#0476c7);color:#fff}
.fin .btn.d{background:#fff;color:var(--k)!important}
nav a,.btn,.call{white-space:nowrap}nav{gap:22px}.hx .eb{color:#fff}.hx .eb:before{background:var(--bl)}
.ddt{display:inline-flex!important;align-items:center;gap:4px}.chev{transition:transform .25s}.dd:hover .chev{transform:rotate(180deg)}
.dd>div{padding:10px;min-width:320px;border:1px solid var(--line);top:calc(100% + 14px)}.dd>div:before{content:"";position:absolute;top:-16px;left:0;right:0;height:16px}.dd>div a{font-weight:600;font-size:.93rem;padding:10px 14px}.dd>div a:hover{background:rgba(5,130,219,.07);color:var(--b)}
.hcta{gap:16px}.hph{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--k)}.hpi{width:42px;height:42px;border-radius:12px;background:rgba(63,174,34,.12);color:var(--gr);display:grid;place-items:center;transition:.25s}.hph:hover .hpi{background:var(--gr);color:#fff}
.hph small{display:block;font-size:.72rem;color:var(--t);line-height:1.1}.hph b{display:block;font:800 1.02rem Inter;letter-spacing:-.01em;line-height:1.25}
.hbtn{padding:13px 20px!important;font-size:.95rem!important;border-radius:12px!important}
@media(max-width:1280px){nav{gap:18px}nav a{font-size:.9rem}.hph span:last-child{display:none}}
@media(max-width:960px){.hcta{display:none}}
@media(max-width:960px){
 body{padding-bottom:62px}
 .hx{padding:120px 0 0;min-height:auto}.hx .w{grid-template-columns:1fr;padding-bottom:30px}.hx .mwrap{display:none}
 .hx:after{background:linear-gradient(0deg,rgba(10,12,15,.92) 30%,rgba(10,12,15,.35) 100%)}
 .hx .lead{font-size:1.04rem}.hx .cta{flex-direction:column}.hx .cta .btn{justify-content:center;width:100%}
 .chips2 li{font-size:.8rem;padding:8px 12px}
 .trustbar .w{grid-template-columns:1fr 1fr;padding:0}.tb{padding:18px 14px;flex-direction:column;align-items:flex-start;gap:10px}.tb:nth-child(3){border-left:0}.tb:nth-child(n+3){border-top:1px solid var(--line)}
 .sc,.sc.big{grid-column:1/-1}.sgrid{gap:16px}
 .gal2{grid-template-columns:1fr 1fr;grid-auto-rows:160px}.gal2 figure:nth-child(1){grid-column:span 2}
 .why,.focus,.zone,.dv .w,.f2{grid-template-columns:1fr}.f2 .full{grid-column:auto}
 .steps2{grid-template-columns:1fr;gap:26px}.steps2:before{display:none}.st{text-align:left;display:grid;grid-template-columns:56px 1fr;gap:4px 16px}.st .n{margin:0;grid-row:span 2}.st h3{margin:0;align-self:end}.st p{margin:0}
 .fc{min-height:380px}.fc .eb{color:#fff}.fc .ct{padding:24px}.fcard{padding:24px}.zmap{max-width:420px}
 .sh{margin-bottom:28px}.soon{flex-direction:column;align-items:flex-start}
}
@media(max-width:400px){h1{font-size:2.05rem}.lgs{height:40px!important}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}.rv{opacity:1!important;transform:none!important}}
"""

JS = r"""(function(){
var e=document.querySelectorAll('.rv');if('IntersectionObserver' in window){var o=new IntersectionObserver(function(n){n.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');o.unobserve(x.target)}})},{threshold:.08});e.forEach(function(x){o.observe(x)})}else e.forEach(function(x){x.classList.add('in')});
document.querySelectorAll('.ba input').forEach(function(r){r.addEventListener('input',function(){var b=r.closest('.ba');b.querySelector('.af').style.clipPath='inset(0 0 0 '+r.value+'%)';b.querySelector('.hd').style.left=r.value+'%'})});
var f=document.getElementById('devis');if(!f)return;
function err(n,on){var d=f.querySelector('[data-f="'+n+'"]');if(d)d.classList.toggle('err',on);return !on}
f.addEventListener('submit',function(ev){ev.preventDefault();
 var v=function(n){var el=f.elements[n];return el?(el.value||'').trim():''};
 var p=(f.querySelector('input[name=p]:checked')||{}).value||'';
 var ok=err('n',v('n').length<2)&err('t',!/^(\+33|0)[1-9](\s?\d{2}){4}$/.test(v('t').replace(/[.\-]/g,' ').replace(/\s+/g,' ')))&err('e',v('e')&&!/^\S+@\S+\.\S+$/.test(v('e')))&err('v',v('v').length<2)&err('p',!p);
 if(!ok){var x=f.querySelector('.err input,.err');if(x&&x.scrollIntoView)x.scrollIntoView({block:'center',behavior:'smooth'});return}
 var body='Nom : '+v('n')+'\nTéléphone : '+v('t')+'\nE-mail : '+v('e')+'\nCommune du projet : '+v('v')+'\nPrestation : '+p+'\n\nProjet :\n'+v('m')+'\n\n(Photos jointes à ce message si disponibles)';
 window.location.href='mailto:'+f.dataset.to+'?subject='+encodeURIComponent('Demande de devis '+p+' - '+v('v'))+'&body='+encodeURIComponent(body);
 f.parentNode.classList.add('sent');});
})();"""

def form(SERV, MAIL, TEL, TELI, title="Votre devis gratuit"):
    pills = "".join(f'<label><input type="radio" name="p" value="{s["nom"]}"><span>{s["nom"]}</span></label>' for s in SERV)
    return f'''<div class="fcard"><h3>{title}</h3><p class="sub">2 minutes pour décrire votre projet. Visite et devis écrit gratuits.</p>
<form id="devis" data-to="{MAIL}" novalidate><div class="f2">
<div class="fld" data-f="n"><label for="fn">Nom et prénom *</label><input id="fn" name="n" autocomplete="name" required><span class="em">Indiquez votre nom.</span></div>
<div class="fld" data-f="t"><label for="ft">Téléphone *</label><input id="ft" name="t" type="tel" inputmode="tel" autocomplete="tel" placeholder="06 00 00 00 00" required><span class="em">Numéro français à 10 chiffres.</span></div>
<div class="fld" data-f="e"><label for="fe">E-mail</label><input id="fe" name="e" type="email" autocomplete="email" placeholder="facultatif"><span class="em">Adresse e-mail invalide.</span></div>
<div class="fld" data-f="v"><label for="fv">Commune du projet *</label><input id="fv" name="v" autocomplete="address-level2" placeholder="Ex. Bois-Guillaume" required><span class="em">Indiquez la commune.</span></div>
<div class="fld full" data-f="p"><label>Prestation recherchée *</label><div class="pills">{pills}</div><span class="em">Choisissez une prestation.</span></div>
<div class="fld full"><label for="fm">Votre projet</label><textarea id="fm" name="m" rows="4" placeholder="Surface approximative, état de la façade, délai souhaité..."></textarea></div>
</div><button class="btn" type="submit">Recevoir mon devis gratuit {ic("arrow",20)}</button>
<p class="note">{ic("camera",14)} Le bouton ouvre votre messagerie avec la demande déjà rédigée : il reste à cliquer sur Envoyer, et vous pouvez y joindre des photos de votre façade. Pressé ? Appelez le <a href="tel:{TELI}">{TEL}</a>.</p></form>
<div class="ok"><div class="ib">{ic("check",34)}</div><h3>Votre demande est prête</h3><p>Votre messagerie s'est ouverte avec le message rédigé. Pensez à cliquer sur <b>Envoyer</b> et à joindre vos photos. Rien ne s'est ouvert ? Écrivez à <a href="mailto:{MAIL}">{MAIL}</a> ou appelez le <a href="tel:{TELI}">{TEL}</a>.</p></div></div>'''

def home(g):
    P, SERV, COM, TEL, TELI, MAIL, LOGO, RGE, SEAL, GFAQ, BLOG = (g[k] for k in "P SERV COM TEL TELI MAIL LOGO RGE SEAL GFAQ BLOG".split())
    slugc, faqhtml = g["slugc"], g["faqhtml"]
    b = f'''<section class="hx"><img class="bgi" src="{P[0]}" alt="Maison rénovée par ISO + : façade enduite blanche et soubassement près de Rouen" fetchpriority="high"><div class="w"><div>
<p class="eb">Façadier RGE en Seine-Maritime</p><h1>Ravalement de façade et isolation <span>à Rouen</span></h1>
<p class="lead">ISO + rénove, repeint et isole les façades des maisons, des bâtiments professionnels et des collectivités à Rouen et dans toute la Seine-Maritime. Un interlocuteur unique, du diagnostic à la réception.</p>
<div class="cta"><a class="btn" href="#devis-form">Demander mon devis gratuit {ic("arrow",20)}</a><a class="btn o" href="tel:{TELI}">{ic("phone",19)} {TEL}</a></div>
<ul class="chips2"><li>{ic("award",17)} Certifié RGE Qualibat</li><li>{ic("shield",17)} Garantie décennale</li><li>{ic("file",17)} Devis gratuit</li></ul></div>
<div class="mwrap"><img class="masc" src="/mascotte.svg?v=8" alt="Mascotte ISO + avec casque et gilet au logo ISO +" width="300" height="380"><img class="vlogo" src="{LOGO}" alt="">{SEAL}</div></div></section>'''
    b += f'''<section class="trustbar" style="padding:0"><div class="w">
<div class="tb"><div class="ib">{ic("award",24)}</div><div><b>RGE Qualibat</b><span>Aides à l'isolation possibles</span></div></div>
<div class="tb"><div class="ib">{ic("shield",24)}</div><div><b>Garantie décennale</b><span>Travaux couverts 10 ans</span></div></div>
<div class="tb"><div class="ib">{ic("file",24)}</div><div><b>Devis gratuit</b><span>Visite et diagnostic offerts</span></div></div>
<div class="tb"><div class="ib">{ic("pin",24)}</div><div><b>Seine-Maritime</b><span>Basés à Barentin, près de Rouen</span></div></div></div></section>'''
    cards = ""
    for i, s in enumerate(SERV):
        big = " big" if i in (0, 1, 5, 6) else ""
        cards += f'''<a class="sc rv{big}" href="/{s["slug"]}/"><div class="im"><img src="{s["img"]}" alt="{s["nom"]} réalisé par ISO + en Seine-Maritime" loading="lazy"><span class="bad">{ic(SICON[s["slug"]],22)}</span><span class="num">0{i+1}</span></div><div class="bd"><h3>{s["nom"]}</h3><p>{SBEN[s["slug"]]}</p><span class="lnk">{SCTA.get(s["slug"],"Faire estimer mes travaux")} {ic("arrow",18)}</span></div></a>'''
    # 7 cartes : 6+6 / 4+4+4 / 6 ... -> rangées équilibrées
    b += f'''<section id="services"><div class="w"><div class="sh"><div><p class="eb">Nos prestations</p><h2>Tout pour votre façade, en un seul artisan</h2></div><p>Maisons individuelles, bâtiments tertiaires, collectivités et copropriétés : ISO + traite la façade de A à Z, avec des produits adaptés au climat normand.</p></div>
<div class="sgrid">{cards}</div></div></section>'''
    figs = [(P[0],"Façade enduite et soubassement"),(P[1],"Peinture de façade"),(P[2],"Isolation par l'extérieur"),(P[4],"Rénovation de façade"),(P[3],"Ravalement")]
    b += f'''<section class="bg"><div class="w"><div class="sh"><div><p class="eb">Réalisations</p><h2>Donnez une nouvelle vie à votre façade</h2></div><p>Quelques chantiers réalisés par ISO +. Chaque façade est différente : la visite gratuite permet de choisir la bonne solution.</p></div>
<div class="gal2">{"".join(f'<figure class="rv"><img src="{u}" alt="{c} réalisée par ISO + en Seine-Maritime" loading="lazy"><figcaption>{c}</figcaption></figure>' for u,c in figs)}</div>
<div class="soon rv"><div class="ib">{ic("camera",26)}</div><div><h3 style="margin-bottom:4px">Avant / après : la galerie s'enrichit</h3><p>Les comparatifs avant / après de nos prochains chantiers seront publiés ici, avec la commune et le type de travaux.</p></div><a class="btn ghost" href="#devis-form" style="margin-left:auto">Faire estimer ma façade</a></div></div></section>'''
    whys = [("award","Certifié RGE Qualibat","Le label qui vous ouvre droit aux aides de l'État pour l'isolation, comme MaPrimeRénov' et les primes énergie."),
            ("shield","Garantie décennale","Vos travaux de façade et d'isolation sont couverts pendant 10 ans par notre assurance."),
            ("file","Devis écrit et gratuit","Visite, diagnostic et devis détaillé offerts, sans engagement : vous savez exactement ce qui est prévu."),
            ("users","Un seul interlocuteur","Le même contact du premier appel à la réception du chantier. Pas de sous-traitance cachée."),
            ("home","Spécialiste de la façade","Ravalement, peinture, nettoyage, bardage et ITE : un métier, maîtrisé de bout en bout."),
            ("pin","Artisan de proximité","Basés à Barentin, nous intervenons vite à Rouen et dans toute la Seine-Maritime.")]
    b += f'''<section class="dark"><div class="w"><div class="sh"><div><p class="eb">Pourquoi ISO +</p><h2>Des garanties réelles, pas des promesses</h2></div><a class="btn o" href="tel:{TELI}">{ic("phone",19)} Parler à un conseiller</a></div>
<div class="why">{"".join(f'<div class="wc rv"><div class="ib">{ic(k,26)}</div><h3>{t}</h3><p>{d}</p></div>' for k,t,d in whys)}</div></div></section>'''
    steps = [("Vous nous contactez","Par téléphone ou formulaire, en 2 minutes."),("Visite gratuite","Diagnostic de la façade et des murs, sur place."),("Devis détaillé","Travaux, produits, délais et aides possibles, par écrit."),("Chantier soigné","Protection, travaux, nettoyage et réception avec vous.")]
    b += f'''<section><div class="w"><div class="sh" style="justify-content:center;text-align:center"><div><p class="eb">Notre méthode</p><h2 style="max-width:none">Votre projet en 4 étapes claires</h2></div></div>
<div class="steps2">{"".join(f'<div class="st rv"><span class="n">{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(steps))}</div>
<p style="text-align:center;margin:44px auto 0"><a class="btn" href="#devis-form">Obtenir une étude de mon projet {ic("arrow",20)}</a></p></div></section>'''
    ite, rav = SERV[2], SERV[0]
    b += f'''<section class="bg"><div class="w"><div class="sh"><div><p class="eb">Prestations phares</p><h2>Isoler et rénover en un seul chantier</h2></div><p>L'échafaudage est monté une seule fois : coupler ravalement et isolation par l'extérieur, c'est moins de frais et une façade neuve.</p></div>
<div class="focus"><a class="fc rv" href="/{ite["slug"]}/"><img src="{ite["img"]}" alt="Isolation thermique par l'extérieur ISO + à Rouen" loading="lazy"><div class="ct"><p class="eb">Éligible aux aides</p><h3>Isolation thermique par l'extérieur</h3><ul><li>{ic("check",17)} Moins de déperditions, plus de confort</li><li>{ic("check",17)} Aucune perte de surface habitable</li><li>{ic("check",17)} MaPrimeRénov' et primes CEE avec une entreprise RGE</li></ul><span class="btn">Étudier mon isolation {ic("arrow",18)}</span></div></a>
<a class="fc rv" href="/{rav["slug"]}/"><img src="{rav["img"]}" alt="Ravalement de façade ISO + près de Rouen" loading="lazy"><div class="ct"><p class="eb">Façade neuve</p><h3>Ravalement de façade</h3><ul><li>{ic("check",17)} Fissures et enduits réparés</li><li>{ic("check",17)} Traitement contre l'humidité et les mousses</li><li>{ic("check",17)} Finition enduit, peinture ou bardage</li></ul><span class="btn">Faire estimer mon ravalement {ic("arrow",18)}</span></div></a></div></div></section>'''
    pos = [("Barentin",50,50,1),("Rouen",72,64,0),("Mont-Saint-Aignan",64,52,0),("Bois-Guillaume",74,48,0),("Isneauville",80,38,0),("Quincampoix",78,26,0),("Le Mesnil-Esnard",84,74,0),("Franqueville-St-Pierre",80,84,0),("Maromme",60,60,0),("Canteleu",56,70,0),("Le Grand-Quevilly",64,80,0),("Malaunay",58,40,0),("Darnétal",88,60,0)]
    dots = "".join(f'<span class="dot{" hq" if h else ""}" style="left:{x}%;top:{y}%">{n}</span>' for n,x,y,h in pos)
    b += f'''<section><div class="w zone"><div class="zmap rv" role="img" aria-label="Zone d'intervention d'ISO + autour de Barentin et Rouen"><span class="ring" style="width:40%;height:40%"></span><span class="ring" style="width:70%;height:70%"></span><span class="ring" style="width:98%;height:98%"></span>{dots}</div>
<div><p class="eb">Zone d'intervention</p><h2>Toute la Seine-Maritime, depuis Barentin</h2><p>Rouen et sa Métropole en priorité : plateau Est, plateau Nord, vallée du Cailly et rive gauche. Votre commune n'est pas listée ? Nous intervenons dans tout le département.</p>
<div class="tags" style="margin:24px 0">{"".join(f'<a href="/{slugc(c[0])}/">{c[0]}</a>' for c in COM)}</div><a class="lnk" href="/communes/">Voir toutes nos zones {ic("arrow",18)}</a></div></div></section>'''
    b += faqhtml(GFAQ).replace('<h2>Questions fréquentes</h2>','<p class="eb">FAQ</p><h2>Vos questions, nos réponses</h2>')
    b += f'''<section class="dv" id="devis-form"><div class="w"><div><p class="eb">Devis gratuit</p><h2>Parlons de votre façade</h2><p>Décrivez votre projet : nous vous rappelons pour fixer la visite. Le diagnostic et le devis sont gratuits et sans engagement.</p>
<ul class="pl"><li><span class="ib">{ic("file",20)}</span>Devis écrit et détaillé</li><li><span class="ib">{ic("award",20)}</span>Entreprise RGE Qualibat</li><li><span class="ib">{ic("shield",20)}</span>Garantie décennale 10 ans</li><li><span class="ib">{ic("clock",20)}</span>Du lundi au samedi, 9 h - 18 h</li></ul>
<a class="btn o" href="tel:{TELI}">{ic("phone",19)} Appeler le {TEL}</a></div>{form(SERV, MAIL, TEL, TELI)}</div></section>'''
    return b
