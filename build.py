#!/usr/bin/env python3
# Générateur statique ISO+ : python3 build.py -> dist/
import os, json, shutil, datetime
D = "docs"
BASE = "/isoplus-facade"
SITE = "https://jiany-coder.github.io/isoplus-facade"
NOM = "ISO +"
TEL = "06 84 59 40 47"; TELI = "+33684594047"
MAIL = "isopluscontact1@gmail.com"
ADR = "62 Rue du Général Sarrail, 76360 Barentin"
CDN = "https://le-de.cdn-website.com/bea612ec7d6549328000bbc9921d1975/dms3rep/multi/opt/"
LOGO = CDN + "img_0002-fb5c36fe-1920w.jpeg"
RGE = CDN + "logo_qualibat-rge-hd-1920w.png"
P = [CDN + x for x in ["IMG_4330-1920w.jpeg", "a3b37b54_97cb_4489_bc5a_b8eaf0763536-1920w.jpeg",
     "ea238c2a_e323_400d_be69_c418081a6e56-1920w.jpeg", "IMG_6542-1920w.jpeg",
     "f317561b_fb0f_49fb_9043_7d4b114c21be-1920w.jpeg", "42200213_299605053957411_1372242197100888064_n-1920w.jpg"]]
TODAY = datetime.date.today().isoformat()
DESC = "ISO + est une entreprise de ravalement de façade, peinture extérieure et isolation thermique par l'extérieur basée à Barentin, qui intervient dans toute la Seine-Maritime, certifiée RGE Qualibat."

SERV = [
 dict(slug="ravalement-facade-rouen", nom="Ravalement de façade", kw="Ravalement de façade à Rouen", ic="🏠", img=P[0],
  court="Remise à neuf complète : réparation des fissures, enduit, traitement et finition.",
  defi="Le ravalement de façade est la remise en état complète des murs extérieurs d'un bâtiment : nettoyage, réparation des fissures, reprise de l'enduit et finition protectrice.",
  direct="ISO + réalise votre ravalement de façade à Rouen et dans la Métropole : diagnostic gratuit sur place, réparation des fissures et des enduits, traitement contre l'humidité et finition durable. Les travaux sont garantis 10 ans par notre assurance décennale et le devis écrit est gratuit.",
  etapes=["Diagnostic du support (fissures, humidité, adhérence)", "Protection des abords, échafaudage", "Nettoyage et traitement anti-mousse", "Rebouchage des fissures et reprise d'enduit", "Finition : enduit, peinture ou revêtement"],
  faq=[("Le ravalement est-il obligatoire à Rouen ?", "Dans certaines communes, le maire peut imposer un ravalement tous les 10 ans (article L132-1 du Code de la construction). Renseignez-vous auprès de votre mairie : nous vous aidons à monter le dossier."),
       ("Faut-il une autorisation pour un ravalement ?", "Une déclaration préalable de travaux est souvent demandée, notamment en secteur protégé ou si l'aspect de la façade change. Nous vous indiquons les démarches lors du devis."),
       ("Combien de temps durent les travaux ?", "Pour une maison individuelle, comptez en général une à trois semaines selon la surface, l'état du support et la météo."),
       ("Peut-on isoler en même temps que le ravalement ?", "Oui, c'est le meilleur moment : on parle d'isolation thermique par l'extérieur. L'échafaudage sert une seule fois et la façade est refaite à neuf.")]),
 dict(slug="peinture-exterieure-rouen", nom="Peinture extérieure", kw="Peinture de façade à Rouen", ic="🎨", img=P[1],
  court="Peinture de façade, pignons, murets et boiseries avec des produits adaptés au climat normand.",
  defi="La peinture de façade est l'application d'un revêtement coloré et protecteur sur les murs extérieurs, après préparation du support.",
  direct="ISO + repeint vos façades, pignons et murets à Rouen et alentours avec des peintures adaptées à l'humidité normande. Le support est d'abord nettoyé, réparé et traité ; la peinture est ensuite appliquée en deux couches pour une protection et une teinte qui durent.",
  etapes=["Choix de la teinte et vérification des règles locales (PLU)", "Nettoyage haute pression et traitement", "Réparation des fissures", "Sous-couche adaptée au support", "Deux couches de peinture façade"],
  faq=[("Quelle peinture choisir pour une façade en Normandie ?", "Une peinture façade microporeuse (pliolite, siloxane ou acrylique selon le support) laisse respirer le mur tout en le protégeant de la pluie."),
       ("Tous les combien faut-il repeindre une façade ?", "En général tous les 10 à 15 ans selon l'exposition, la qualité de la peinture et l'état du support."),
       ("Peut-on choisir n'importe quelle couleur ?", "Non, le PLU de votre commune peut imposer un nuancier. Nous vérifions avec vous avant le chantier."),
       ("Peut-on peindre par temps froid ?", "La plupart des peintures façade demandent une température supérieure à 5 °C et un temps sec. Nous planifions le chantier en conséquence.")]),
 dict(slug="isolation-thermique-exterieur-rouen", nom="Isolation thermique par l'extérieur", kw="Isolation par l'extérieur à Rouen", ic="🧱", img=P[2],
  court="ITE certifiée RGE : moins de déperditions, plus de confort et une façade neuve.",
  defi="L'isolation thermique par l'extérieur (ITE) consiste à poser un isolant sur les murs extérieurs, puis un enduit ou un bardage de finition, sans perdre de surface habitable.",
  direct="ISO + pose votre isolation thermique par l'extérieur à Rouen et dans l'agglomération. Certifiée RGE Qualibat, l'entreprise vous permet de demander les aides de l'État comme MaPrimeRénov' et les primes énergie. L'ITE supprime une grande partie des ponts thermiques et refait la façade en un seul chantier.",
  etapes=["Visite technique et étude des murs", "Aide au montage des dossiers d'aides", "Pose de l'isolant (polystyrène, laine de roche ou fibre de bois)", "Armature et sous-enduit", "Finition enduit ou bardage"],
  faq=[("Quelles aides pour isoler sa façade par l'extérieur ?", "Avec une entreprise RGE comme ISO +, vous pouvez prétendre selon vos revenus à MaPrimeRénov', aux primes CEE et à l'éco-prêt à taux zéro. Les conditions évoluent : vérifiez sur france-renov.gouv.fr."),
       ("ITE ou isolation par l'intérieur ?", "L'ITE ne réduit pas la surface habitable, traite mieux les ponts thermiques et refait la façade. L'isolation intérieure coûte souvent moins cher mais réduit les pièces. Voir notre article comparatif."),
       ("Quel isolant choisir ?", "Le polystyrène est économique, la laine de roche est incombustible et phonique, la fibre de bois apporte un bon confort d'été. Nous vous conseillons selon le mur et le budget."),
       ("Faut-il une autorisation ?", "Oui, une déclaration préalable de travaux est nécessaire car l'aspect extérieur change.")]),
 dict(slug="nettoyage-facade-rouen", nom="Nettoyage de façade", kw="Nettoyage de façade à Rouen", ic="💧", img=P[3],
  court="Démoussage, hydrogommage et traitement : une façade propre sans abîmer le support.",
  defi="Le nettoyage de façade retire mousses, lichens, pollution et salissures des murs extérieurs avec une méthode adaptée au matériau.",
  direct="ISO + nettoie vos façades à Rouen et alentours : haute pression, hydrogommage ou sablage selon le support (brique, pierre, enduit), puis traitement anti-mousse et hydrofuge pour garder une façade propre plus longtemps.",
  etapes=["Analyse du matériau", "Protection des menuiseries et abords", "Nettoyage adapté (haute pression, hydrogommage)", "Traitement anti-mousse", "Hydrofuge de protection"],
  faq=[("Quelle méthode pour une façade en brique ?", "L'hydrogommage à basse pression est souvent préféré car il nettoie sans éroder la brique ni les joints."),
       ("Un nettoyage suffit-il ou faut-il un ravalement ?", "Si l'enduit est sain et sans fissure, un nettoyage et un traitement suffisent. En cas de fissures ou de décollement, un ravalement est préférable."),
       ("Le traitement hydrofuge est-il utile ?", "Oui en Normandie : il limite la pénétration de l'eau et le retour des mousses tout en laissant le mur respirer."),
       ("Combien de temps dure un nettoyage ?", "Souvent de 1 à 3 jours pour une maison, selon la surface et l'accès.")]),
 dict(slug="bardage-rouen", nom="Bardage", kw="Pose de bardage à Rouen", ic="🪵", img=P[4],
  court="Bardage bois, composite, métal ou PVC pour isoler et moderniser la façade.",
  defi="Le bardage est un revêtement de façade fixé sur une ossature, en bois, composite, métal ou PVC, souvent associé à une isolation.",
  direct="ISO + pose votre bardage à Rouen et dans la Métropole : bois, composite, métal ou PVC, avec ou sans isolant derrière. Le bardage protège le mur, modernise l'aspect de la maison et peut faire partie d'une isolation par l'extérieur éligible aux aides.",
  etapes=["Choix du matériau et du coloris", "Pose de l'ossature", "Isolant si ITE", "Pare-pluie", "Pose des lames et finitions"],
  faq=[("Quel bardage choisir ?", "Le bois est chaleureux mais demande de l'entretien, le composite et le PVC en demandent peu, le métal donne un aspect contemporain."),
       ("Le bardage isole-t-il ?", "Seul, très peu. Avec un isolant posé dans l'ossature, il devient une vraie isolation par l'extérieur."),
       ("Faut-il une déclaration de travaux ?", "Oui, en général une déclaration préalable car l'aspect de la façade change."),
       ("Peut-on poser un bardage sur une partie seulement ?", "Oui, par exemple sur un pignon exposé à la pluie ou en habillage décoratif.")]),
 dict(slug="isolation-plancher-rouen", nom="Isolation de plancher", kw="Isolation de plancher à Rouen", ic="🔥", img=P[5],
  court="Isolation du plancher bas, du sous-sol ou du vide sanitaire contre le froid au sol.",
  defi="L'isolation du plancher bas consiste à poser un isolant sous le plancher du rez-de-chaussée, côté sous-sol, garage ou vide sanitaire.",
  direct="ISO + isole les planchers bas à Rouen et alentours : sous-sol, garage ou vide sanitaire. C'est un chantier rapide qui supprime la sensation de sol froid et réduit les pertes de chaleur, éligible aux aides avec une entreprise RGE.",
  etapes=["Visite du sous-sol ou vide sanitaire", "Choix de l'isolant", "Pose en plafond de sous-sol", "Traitement des points singuliers", "Contrôle de la continuité"],
  faq=[("Combien de temps pour isoler un plancher ?", "Souvent une journée à deux jours pour une maison individuelle."),
       ("Est-ce éligible aux aides ?", "Oui, avec une entreprise RGE, selon les dispositifs en vigueur. Vérifiez sur france-renov.gouv.fr."),
       ("Quel gain de confort ?", "La sensation de sol froid disparaît et les pertes de chaleur par le sol sont réduites."),
       ("Faut-il libérer le sous-sol ?", "Il faut dégager l'accès au plafond. Nous vous indiquons quoi déplacer avant le chantier.")]),
]

# communes : nom, secteur, distance approx. depuis Barentin (km), particularité
COM = [
 ("Rouen","Rouen centre",18,"Le centre historique, les quartiers rive gauche et les hauteurs mêlent maisons à pans de bois, immeubles en pierre et pavillons. Nous travaillons aussi bien sur maisons que sur petites copropriétés."),
 ("Mont-Saint-Aignan","Plateau Ouest",15,"Commune résidentielle du plateau nord-ouest, avec beaucoup de pavillons des années 60 à 80 dont les murs gagnent beaucoup à une isolation par l'extérieur."),
 ("Bois-Guillaume","Plateau Nord",17,"Maisons bourgeoises et pavillons en brique ou enduit : ravalements soignés et ITE sont les demandes les plus fréquentes."),
 ("Isneauville","Plateau Nord",18,"Commune pavillonnaire en développement, avec des maisons récentes à repeindre et d'autres plus anciennes à isoler."),
 ("Quincampoix","Plateau Nord",22,"Maisons individuelles exposées au vent du plateau : l'isolation des murs et un enduit protecteur font une vraie différence."),
 ("Houppeville","Plateau Ouest",12,"Commune proche de Barentin, avec des pavillons et des maisons anciennes à rénover."),
 ("Bihorel","Plateau Nord",19,"Pavillons et petites résidences : nettoyage, peinture et ravalement de façade."),
 ("Darnétal","Plateau Est",22,"Maisons de ville en brique et anciennes maisons ouvrières : nettoyage doux de la brique et ravalement."),
 ("Le Mesnil-Esnard","Plateau Est",25,"Commune résidentielle du plateau Est, beaucoup de maisons individuelles où l'ITE est très demandée."),
 ("Franqueville-Saint-Pierre","Plateau Est",27,"Pavillons des années 70 à 2000 : isolation par l'extérieur, bardage et peinture de façade."),
 ("Bonsecours","Plateau Est",24,"Maisons anciennes et pavillons sur les hauteurs de Rouen : ravalement et traitement contre l'humidité."),
 ("Belbeuf","Plateau Est",28,"Maisons individuelles avec terrain : ravalement, peinture et bardage."),
 ("Boos","Plateau Est",30,"Commune du plateau Est en croissance, avec des maisons récentes et anciennes à isoler et repeindre."),
 ("Maromme","Vallée du Cailly",13,"Maisons de ville et pavillons de la vallée du Cailly : nettoyage, ravalement et isolation."),
 ("Déville-lès-Rouen","Vallée du Cailly",14,"Maisons mitoyennes et pavillons : peinture et ravalement de façade."),
 ("Malaunay","Vallée du Cailly",9,"Commune voisine de Barentin : délai d'intervention court pour vos devis."),
 ("Canteleu","Rive droite Ouest",16,"Maisons et pavillons des hauteurs de Canteleu : isolation et ravalement."),
 ("Sotteville-lès-Rouen","Rive gauche",21,"Maisons de ville en brique typiques : nettoyage et rénovation de façade."),
 ("Le Grand-Quevilly","Rive gauche",21,"Pavillons et maisons de ville : peinture, ravalement et ITE."),
 ("Le Petit-Quevilly","Rive gauche",20,"Maisons mitoyennes en brique : nettoyage doux, rejointoiement et peinture."),
 ("Barentin","Siège de l'entreprise",0,"Notre siège est à Barentin : c'est ici que nous intervenons le plus vite."),
]
def slugc(n):
    import unicodedata
    s = unicodedata.normalize("NFD", n).encode("ascii","ignore").decode().lower()
    return "".join(c if c.isalnum() else "-" for c in s).strip("-").replace("--","-")

BLOG = [
 dict(slug="prix-ravalement-facade-rouen", t="Ravalement de façade à Rouen : de quoi dépend le prix ?", s="ravalement-facade-rouen",
  intro="Le prix d'un ravalement de façade dépend surtout de quatre choses : la surface, l'état du support, la finition choisie et l'accès (échafaudage). Un devis sérieux se fait donc toujours après une visite sur place, gratuite chez ISO +.",
  secs=[("Quels éléments font varier le prix ?", "La surface à traiter, le nombre de fissures, la présence d'humidité, la hauteur et l'accès au mur, ainsi que la finition (simple peinture, enduit, ou isolation par l'extérieur)."),
        ("Un nettoyage peut-il suffire ?", "Oui si l'enduit est sain. Un nettoyage avec traitement anti-mousse et hydrofuge coûte bien moins qu'un ravalement complet."),
        ("Peut-on obtenir des aides ?", "Un ravalement seul n'est pas aidé. En revanche, s'il est couplé à une isolation par l'extérieur réalisée par une entreprise RGE, les aides comme MaPrimeRénov' peuvent s'appliquer selon vos revenus."),
        ("Comment comparer deux devis ?", "Vérifiez que chaque devis détaille la préparation, le traitement des fissures, les produits utilisés, l'échafaudage et la garantie décennale.")],
  tab=[("Élément","Influence sur le prix"),("Surface","Forte"),("État du support et fissures","Forte"),("Accès et échafaudage","Moyenne"),("Type de finition","Forte")]),
 dict(slug="ite-ou-isolation-interieur", t="Isolation par l'extérieur ou par l'intérieur : que choisir ?", s="isolation-thermique-exterieur-rouen",
  intro="L'isolation par l'extérieur (ITE) est en général la meilleure solution thermique pour une maison : elle ne réduit pas la surface habitable et traite mieux les ponts thermiques. L'isolation par l'intérieur reste pertinente quand la façade ne peut pas être modifiée.",
  secs=[("Quels sont les avantages de l'ITE ?", "Pas de perte de surface, pas de travaux dans les pièces, suppression d'une grande partie des ponts thermiques et façade refaite à neuf."),
        ("Quand préférer l'isolation intérieure ?", "En secteur protégé où l'aspect extérieur ne peut pas changer, ou pour isoler pièce par pièce avec un budget plus serré."),
        ("Quelles aides en 2026 ?", "MaPrimeRénov', primes CEE et éco-PTZ sont accessibles avec une entreprise RGE comme ISO +. Les montants dépendent de vos revenus : consultez france-renov.gouv.fr."),
        ("Combien de temps dure une ITE ?", "Pour une maison individuelle, comptez généralement deux à quatre semaines selon la surface et la météo.")],
  tab=[("Critère","Extérieur (ITE)","Intérieur"),("Surface habitable","Conservée","Réduite"),("Ponts thermiques","Bien traités","Partiellement"),("Travaux dans la maison","Non","Oui"),("Façade refaite","Oui","Non")]),
 dict(slug="quand-repeindre-facade-normandie", t="Quand repeindre sa façade en Normandie ?", s="peinture-exterieure-rouen",
  intro="En Normandie, le meilleur moment pour repeindre une façade va de fin avril à septembre : il faut un mur sec, plus de 5 °C et pas de pluie annoncée. Une façade se repeint en général tous les 10 à 15 ans.",
  secs=[("Quels signes montrent qu'il faut repeindre ?", "Peinture qui farine au toucher, écailles, traces vertes de mousse, fissures fines ou couleur ternie."),
        ("Pourquoi éviter l'hiver ?", "Le froid et l'humidité empêchent la peinture de sécher et d'adhérer correctement, ce qui réduit sa durée de vie."),
        ("Faut-il une autorisation ?", "Souvent une déclaration préalable si la couleur change, et le PLU peut imposer un nuancier."),
        ("Quelle préparation avant la peinture ?", "Nettoyage, traitement anti-mousse, réparation des fissures puis sous-couche : c'est la préparation qui fait durer la peinture.")],
  tab=[("Saison","Conditions","Conseil"),("Printemps","Variable","Possible fin avril à juin"),("Été","Idéal","Éviter les fortes chaleurs"),("Automne","Possible en septembre","Surveiller la pluie"),("Hiver","Défavorable","À éviter")]),
]

GFAQ = [("Quelles zones couvrez-vous ?", "ISO + intervient dans toute la Seine-Maritime, en priorité à Rouen et dans la Métropole : plateau Est (Le Mesnil-Esnard, Franqueville-Saint-Pierre, Bonsecours, Belbeuf, Boos), plateau Nord et Ouest (Mont-Saint-Aignan, Bois-Guillaume, Isneauville, Quincampoix, Houppeville), vallée du Cailly et rive gauche, depuis notre siège de Barentin."),
        ("Le devis est-il gratuit ?", "Oui, la visite et le devis écrit sont gratuits et sans engagement."),
        ("Êtes-vous certifiés RGE ?", "Oui, ISO + est certifiée RGE Qualibat, ce qui ouvre droit aux aides de l'État pour l'isolation."),
        ("Vos travaux sont-ils garantis ?", "Oui, nos travaux sont couverts par la garantie décennale (10 ans)."),
        ("Quels sont vos horaires ?", "Du lundi au samedi, de 9 h à 18 h."),
        ("Pouvez-vous m'aider pour les aides MaPrimeRénov' ?", "Oui, nous vous accompagnons dans le montage des dossiers d'aides pour votre isolation par l'extérieur.")]

CSS = """:root{--b:#30AFFF;--bd:#0a8fe0;--k:#111214;--k2:#1b1c1f;--g:#F5F6F7;--t:#55585e;--line:#e7e9ec;--r:24px}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{font-family:Inter,system-ui,sans-serif;color:var(--t);line-height:1.7;background:#fff;font-size:17px;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:Barlow,sans-serif;color:var(--k);line-height:1.05;font-weight:800;letter-spacing:-.02em}h1{font-size:clamp(2.4rem,5.4vw,4.4rem)}h2{font-size:clamp(1.9rem,3.6vw,3.1rem);margin-bottom:.5em}h3{font-size:1.3rem;margin-bottom:.4em}
a{color:var(--k)}img{max-width:100%;display:block}.w{max-width:1240px;margin:auto;padding:0 24px}section{padding:100px 0}p{max-width:70ch}
section>.w>h2:before,.prose>h2:first-child:before,.kick{content:"ISO + · FAÇADE & ISOLATION";display:inline-block;font:800 .7rem Inter;letter-spacing:.22em;color:var(--k);background:rgba(48,175,255,.16);padding:8px 14px;border-radius:999px;margin-bottom:18px}
.dark section>.w>h2:before,.dark>.w>h2:before{background:rgba(48,175,255,.18);color:var(--b)}
.top{background:var(--k);color:#c9ccd1;font-size:.82rem;padding:9px 0;letter-spacing:.02em}.top .w{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}.top a{color:#fff;font-weight:700;text-decoration:none}.top b{color:var(--b)}
header{position:sticky;top:10px;z-index:50;height:0}header .w{display:flex;align-items:center;justify-content:space-between;height:70px;background:#fff;border-radius:999px;box-shadow:0 18px 50px rgba(0,0,0,.18);padding:0 10px 0 22px;margin-top:10px;max-width:1240px;width:calc(100% - 24px)}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none}.lg{height:44px;width:auto}
nav{display:flex;gap:26px;align-items:center}nav a{color:var(--k);text-decoration:none;font-weight:600;font-size:.95rem}nav a:hover{color:var(--bd)}
.dd{position:relative}.dd>div{display:none;position:absolute;top:100%;left:-14px;background:#fff;box-shadow:0 20px 40px rgba(0,0,0,.14);border-radius:18px;padding:12px;min-width:300px}.dd:hover>div{display:block}.dd>div a{display:block;padding:9px 12px;border-radius:10px}.dd>div a:hover{background:var(--g)}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--b);color:var(--k)!important;font-weight:800;padding:15px 26px;border-radius:999px;text-decoration:none;border:0;cursor:pointer;font-size:1rem;transition:.25s;font-family:Inter}.btn:hover{background:#fff;box-shadow:0 0 0 2px var(--b) inset;transform:translateY(-2px)}
.btn.a{background:var(--b)}.btn.o{background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.55);color:#fff!important;backdrop-filter:blur(6px)}.btn.o:hover{background:#fff;color:var(--k)!important}.btn.d{background:var(--k);color:#fff!important}
header .btn{padding:12px 20px}.burger{display:none;background:none;border:0;font-size:1.7rem;padding:0 12px}
.hero{position:relative;color:#fff;padding:190px 0 90px;min-height:92vh;display:flex;align-items:flex-end;background:#222 center/cover no-repeat}
.hero:after{content:"";position:absolute;inset:auto 0 0 0;height:55%;background:linear-gradient(to top,rgba(0,0,0,.55),transparent)}
.hero .w{position:relative;z-index:1;width:100%;display:grid;grid-template-columns:1.3fr .7fr;gap:40px;align-items:end}
.hero .glass{background:rgba(17,18,20,.62);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.14);border-radius:28px;padding:38px 40px;max-width:720px}
.hero h1{color:#fff}.hero h1 span{color:var(--b)}.hero p.l{font-size:1.12rem;margin:16px 0;color:#eef0f2}
.hero ul{list-style:none;margin:16px 0 26px;display:flex;flex-wrap:wrap;gap:8px 22px}.hero li{font-weight:700;font-size:.92rem}.hero li:before{content:"✓";color:var(--b);font-weight:900;margin-right:8px}.cta{display:flex;gap:12px;flex-wrap:wrap}
.seal{justify-self:end;width:210px;height:210px;position:relative;filter:drop-shadow(0 16px 40px rgba(0,0,0,.4))}.seal svg.ring{width:100%;height:100%;animation:spin 22s linear infinite}.seal .mid{position:absolute;inset:46px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:var(--k);font:800 1.05rem Barlow;line-height:1.05}.seal .mid img{width:64px;margin-bottom:4px}@keyframes spin{to{transform:rotate(360deg)}}
.crumb{font-size:.85rem;color:#d7dade;margin-bottom:14px}.crumb a{color:#fff}
.stats{background:var(--k);padding:0}.stats .w{display:grid;grid-template-columns:repeat(5,1fr)}.stats .w>div{padding:34px 14px;color:#c9ccd1;font-size:.88rem;border-left:1px solid rgba(255,255,255,.08)}.stats b{display:block;font:800 2rem Barlow;color:#fff}.stats b:first-letter{color:var(--b)}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.g2{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;transition:.35s;display:flex;flex-direction:column}.card:hover{transform:translateY(-6px);box-shadow:0 28px 60px rgba(0,0,0,.12);border-color:transparent}
.card img{height:220px;object-fit:cover;width:100%;transition:.6s}.card:hover img{transform:scale(1.05)}.card .in{padding:26px;flex:1;display:flex;flex-direction:column;background:#fff;position:relative}.card .n{font:800 .8rem Inter;letter-spacing:.15em;color:var(--bd);margin-bottom:6px}.card a.m{margin-top:auto;font-weight:800;text-decoration:none;color:var(--k)}.card a.m:hover{color:var(--bd)}
.bg{background:var(--g)}.dark{background:var(--k);color:#b9bdc3;position:relative;overflow:hidden}.dark h2,.dark h3{color:#fff}
.urg{background:var(--k);color:#c9ccd1;border-radius:28px;padding:48px}.urg h2{color:#fff}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;counter-reset:s}.steps div{background:var(--k2);padding:30px;border-radius:var(--r);border:1px solid rgba(255,255,255,.07);transition:.3s}.steps div:hover{border-color:var(--b)}.steps div:before{counter-increment:s;content:"0" counter(s);font:800 2.6rem Barlow;color:var(--b);display:block;margin-bottom:10px}
.tags{display:flex;flex-wrap:wrap;gap:10px}.tags a{background:#fff;border:1px solid var(--line);padding:11px 18px;border-radius:16px;text-decoration:none;color:var(--k);font-weight:700;font-size:.92rem;transition:.2s}.tags a:hover{background:var(--k);color:#fff}
.faq details{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px 24px;margin-bottom:12px}.faq summary{font:800 1.15rem Barlow;color:var(--k);cursor:pointer;list-style:none;display:flex;justify-content:space-between}.faq summary:after{content:"+";color:var(--bd);font-size:1.5rem;line-height:1}.faq details[open] summary:after{content:"−"}.faq p{margin-top:10px}
table{width:100%;border-collapse:collapse;margin:20px 0;background:#fff;border-radius:18px;overflow:hidden;border:1px solid var(--line)}th{background:var(--k);color:#fff;text-align:left}th,td{padding:14px 16px;border-bottom:1px solid var(--line)}
.prose{max-width:820px}.prose h2{margin-top:1.4em;font-size:clamp(1.5rem,2.4vw,2rem)}.prose p,.prose ul,.prose ol{margin:.8em 0}.prose li{margin-left:1.2em}
.box{background:var(--g);border-left:4px solid var(--b);padding:20px 24px;border-radius:14px;margin:20px 0}
.ph{border-radius:28px;width:100%;height:100%;max-height:560px;object-fit:cover}
.trust{display:flex;gap:24px;align-items:center;flex-wrap:wrap;margin-top:20px}.trust img{height:70px;background:#fff;padding:6px;border-radius:10px}
form{display:grid;gap:12px}input,textarea,select{width:100%;padding:15px;border:1px solid #d5d8dc;border-radius:14px;font:inherit;background:#fff}
.fin{background:var(--k);color:#c9ccd1;text-align:center;border-top:3px solid var(--b)}.fin h2{color:#fff}.fin p{margin:auto}.fin .cta{justify-content:center;margin-top:26px}
footer{background:#0a0b0c;color:#8f949b;padding:80px 0 110px;font-size:.92rem}footer .w{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:40px}footer h3{color:#fff;font:800 .72rem Inter;letter-spacing:.2em;text-transform:uppercase;margin-bottom:16px}footer a{color:#c9ccd1;text-decoration:none;display:block;margin:5px 0}footer a:hover{color:var(--b)}
.bar{position:fixed;bottom:0;left:0;right:0;z-index:60;display:none;grid-template-columns:1fr 1fr}.bar a{padding:17px;text-align:center;font-weight:800;text-decoration:none}.bar a:first-child{background:var(--k);color:#fff}.bar a:last-child{background:var(--b);color:var(--k)}
.rv{opacity:0;transform:translateY(24px);transition:.7s}.rv.in{opacity:1;transform:none}
.mwrap{justify-self:end;position:relative;width:300px}.masc{width:300px;height:auto;animation:bob 4s ease-in-out infinite}.mwrap .seal{position:absolute;left:-90px;bottom:10px;width:150px;height:150px}.mwrap .seal .mid{inset:32px;font-size:.8rem}.mwrap .seal .mid img{width:40px}@keyframes bob{50%{transform:translateY(-10px)}}.fm{width:130px;margin:0 auto 10px;animation:bob 4s ease-in-out infinite}
@media(max-width:960px){.mwrap{justify-self:center;width:220px}.masc{width:220px}.mwrap .seal{left:-60px;width:120px;height:120px}nav{display:none;position:absolute;top:80px;left:0;right:0;background:#fff;flex-direction:column;padding:24px;align-items:flex-start;border-radius:24px;box-shadow:0 20px 40px rgba(0,0,0,.15)}nav.on{display:flex}.dd>div{position:static;display:block;box-shadow:none;padding:0 0 0 10px}.burger{display:block}header .btn{display:none}
.grid,.steps,.g2,footer .w,.hero .w{grid-template-columns:1fr}.seal{justify-self:start;width:150px;height:150px}.seal .mid{inset:32px;font-size:.8rem}.seal .mid img{width:40px}.hero{padding:130px 0 60px}.hero .glass{padding:26px}.stats .w{grid-template-columns:repeat(2,1fr)}section{padding:64px 0}.bar{display:grid}.top .z{display:none}}
"""

def page(path, title, desc, body, schema=None, crumbs=None):
    url = SITE + "/" + (path.replace("index.html","") if path.endswith("index.html") else path)
    sch = [LB]
    if crumbs:
        sch.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+u} for i,(n,u) in enumerate(crumbs)]})
    if schema: sch += schema
    servs = "".join(f'<a href="/{s["slug"]}/">{s["nom"]}</a>' for s in SERV)
    html = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{P[0]}"><meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Barlow:wght@600;800&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v=5"><link rel="icon" href="{LOGO}">
{''.join('<script type="application/ld+json">'+json.dumps(s,ensure_ascii=False)+'</script>' for s in sch)}</head><body>
<div class="top"><div class="w"><span class="z">📍 Intervention dans <b>toute la Seine-Maritime (76)</b> · Devis gratuit et sans engagement</span><span>Lun-Sam 9h-18h · <a href="tel:{TELI}">📞 {TEL}</a></span></div></div>
<header><div class="w"><a class="logo" href="/"><svg class="lg" viewBox="0 0 210 56" width="170" height="46" role="img" aria-label="ISO + façade et isolation"><rect x="2" y="6" width="44" height="44" rx="12" fill="#30AFFF"/><path d="M12 30 24 19l12 11v12H12z" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/><path d="M19 42v-8h10v8" fill="#fff"/><text x="56" y="34" font-family="Manrope,Arial" font-weight="800" font-size="26" fill="#111214">ISO</text><text x="106" y="34" font-family="Manrope,Arial" font-weight="800" font-size="30" fill="#30AFFF">+</text><text x="57" y="49" font-family="Inter,Arial" font-weight="600" font-size="10" letter-spacing="2.2" fill="#4a4a52">FAÇADE · ISOLATION</text></svg></a>
<nav id="nav"><a href="/">Accueil</a><div class="dd"><a href="/#services">Prestations ▾</a><div>{servs}</div></div><a href="/communes/">Communes</a><a href="/blog/">Conseils</a><a href="/faq/">FAQ</a><a href="/contact/">Contact</a></nav>
<a class="btn" href="tel:{TELI}">📞 {TEL}</a><button class="burger" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('on')">☰</button></div></header>
<main>{body}</main>
<section class="fin"><div class="w"><img class="fm" src="/mascotte.svg" alt="Mascotte ISO +" width="150" height="190" loading="lazy"><h2>Votre façade mérite le meilleur</h2><p>Visite, diagnostic et devis écrit gratuits. Travaux garantis 10 ans.</p><div class="cta"><a class="btn d" href="/contact/">Demander mon devis gratuit</a><a class="btn o" href="tel:{TELI}">📞 {TEL}</a></div></div></section>
<footer><div class="w"><div><a class="logo" href="/"><svg class="lg" viewBox="0 0 210 56" width="170" height="46" role="img" aria-label="ISO + façade et isolation"><rect x="2" y="6" width="44" height="44" rx="12" fill="#30AFFF"/><path d="M12 30 24 19l12 11v12H12z" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/><path d="M19 42v-8h10v8" fill="#fff"/><text x="56" y="34" font-family="Manrope,Arial" font-weight="800" font-size="26" fill="#fff">ISO</text><text x="106" y="34" font-family="Manrope,Arial" font-weight="800" font-size="30" fill="#30AFFF">+</text><text x="57" y="49" font-family="Inter,Arial" font-weight="600" font-size="10" letter-spacing="2.2" fill="#9aa4ae">FAÇADE · ISOLATION</text></svg></a><p style="margin-top:12px">{DESC}</p><div class="trust"><img src="{RGE}" alt="Certification RGE Qualibat"></div></div>
<div><h3>Prestations</h3>{servs}</div><div><h3>Communes</h3>{''.join(f'<a href="/{slugc(c[0])}/">Façade {c[0]}</a>' for c in COM[:8])}<a href="/communes/">Toutes les communes →</a></div>
<div><h3>Contact</h3><a href="tel:{TELI}">📞 {TEL}</a><a href="mailto:{MAIL}">✉️ {MAIL}</a><p>{ADR}</p><p>Lun-Sam : 9h-18h</p><a href="/contact/">Formulaire de devis</a><a href="/mentions-legales/">Mentions légales</a></div></div></footer>
<script src="/app.js?v=4" defer></script><div class="bar"><a href="tel:{TELI}">📞 Appeler</a><a href="/contact/">Devis gratuit</a></div></body></html>"""
    html = html.replace('href="/', 'href="'+BASE+'/').replace('src="/', 'src="'+BASE+'/').replace(BASE+'//', '//'); f = os.path.join(D, path); os.makedirs(os.path.dirname(f), exist_ok=True); open(f,"w").write(html)
    PAGES.append(url)

LB = {"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","@id":SITE+"/#entreprise","name":NOM,"description":DESC,"url":SITE+"/","telephone":TELI,"email":MAIL,"image":P[0],"logo":LOGO,
 "address":{"@type":"PostalAddress","streetAddress":"62 Rue du Général Sarrail","postalCode":"76360","addressLocality":"Barentin","addressCountry":"FR"},
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"09:00","closes":"18:00"}],
 "areaServed":[{"@type":"AdministrativeArea","name":"Seine-Maritime"}]+[{"@type":"City","name":c[0]} for c in COM],"hasCredential":{"@type":"EducationalOccupationalCredential","name":"RGE Qualibat"},
 "sameAs":["https://instagram.com/isoplusfacade","https://www.pagesjaunes.fr/pros/62536500"]}

def faqhtml(fq, t="Questions fréquentes"):
    return f'<section class="bg faq"><div class="w prose" style="margin:auto"><h2>{t}</h2>' + "".join(f"<details open><summary>{q}</summary><p>{a}</p></details>" for q,a in fq) + "</div></section>"
def faqschema(fq): return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in fq]}
SEAL = f'<div class="seal"><svg class="ring" viewBox="0 0 200 200"><defs><path id="c" d="M100 100m-82 0a82 82 0 1 1 164 0a82 82 0 1 1-164 0"/></defs><circle cx="100" cy="100" r="98" fill="#111214"/><text font-family="Inter" font-weight="800" font-size="15" letter-spacing="4.2" fill="#fff"><textPath href="#c">CERTIFIÉ RGE QUALIBAT · GARANTIE DÉCENNALE · </textPath></text></svg><div class="mid"><img src="{RGE}" alt="Logo RGE Qualibat">10 ANS</div></div>'
def hero(img, h1, lead, pts, crumb="", masc=False):
    return f'<section class="hero" style="background-image:url({img})"><div class="w"><div class="glass">{crumb}<h1>{h1}</h1><p class="l">{lead}</p><ul>{"".join(f"<li>{p}</li>" for p in pts)}</ul><div class="cta"><a class="btn" href="/contact/">Devis gratuit ↗</a><a class="btn o" href="tel:{TELI}">📞 {TEL}</a></div></div>{('<div class="mwrap"><img class="masc" src="/mascotte.svg" alt="Mascotte ISO + avec casque et gilet au logo ISO +" width="300" height="380">'+SEAL+'</div>') if masc else SEAL}</div></section>'
STATS = '<section class="stats"><div class="w"><div><b>Gratuit</b>Visite et devis</div><div><b>RGE</b>Qualibat</div><div><b>10 ans</b>Garantie décennale</div><div><b>76</b>Toute la Seine-Maritime</div><div><b>1</b>Seul interlocuteur</div></div></section>'
def cards():
    return '<div class="grid">' + "".join(f'<article class="card rv"><img src="{s["img"]}" alt="{s["nom"]} réalisé par ISO + près de Rouen" loading="lazy"><div class="in"><span class="n">0{i+1}</span><h3>{s["ic"]} {s["nom"]}</h3><p>{s["court"]}</p><a class="m" href="/{s["slug"]}/">Voir la prestation →</a></div></article>' for i,s in enumerate(SERV)) + "</div>"
def tags(): return '<div class="tags">' + "".join(f'<a href="/{slugc(c[0])}/">{c[0]}</a>' for c in COM) + "</div>"
STEPS = '<div class="steps"><div><h3>Appel ou formulaire</h3><p>Vous décrivez votre projet, nous fixons un rendez-vous rapide.</p></div><div><h3>Visite gratuite</h3><p>Diagnostic de la façade et des murs sur place.</p></div><div><h3>Devis écrit détaillé</h3><p>Prestations, produits, délais et aides possibles.</p></div><div><h3>Chantier soigné</h3><p>Protection, travaux, nettoyage et réception avec vous.</p></div></div>'

def build():
    global PAGES; PAGES = []
    shutil.rmtree(D, ignore_errors=True); os.makedirs(D)
    open(f"{D}/style.css","w").write(CSS); open(f"{D}/mascotte.svg","w").write(open("mascot.svg").read().replace("LOGO",LOGO)); open(f"{D}/app.js","w").write('(function(){var e=document.querySelectorAll(".rv");if(!("IntersectionObserver"in window)){e.forEach(function(x){x.classList.add("in")});return}var o=new IntersectionObserver(function(n){n.forEach(function(x){if(x.isIntersecting){x.target.classList.add("in");o.unobserve(x.target)}})},{threshold:.1});e.forEach(function(x){o.observe(x)})})()')
    # accueil
    b = hero(P[0], "Ravalement de façade et isolation <span>à Rouen</span>", "ISO + rénove, repeint et isole les façades des maisons de Rouen et de toute la Seine-Maritime. Entreprise certifiée RGE Qualibat, basée à Barentin.",
             ["Ravalement, peinture extérieure, nettoyage, bardage", "Isolation thermique par l'extérieur éligible aux aides", "Visite et devis écrit gratuits, garantie décennale"], masc=True) + STATS
    b += f'<section id="services"><div class="w"><h2>Nos prestations façade et isolation</h2><p style="margin-bottom:30px">Un seul interlocuteur du diagnostic à la réception du chantier, pour toute la Métropole rouennaise.</p>{cards()}</div></section>'
    b += f'<section class="bg"><div class="w g2"><div><h2>Pourquoi isoler par l\'extérieur pendant votre ravalement ?</h2><p>{SERV[2]["direct"]}</p><div class="box"><b>Bon à savoir :</b> l\'échafaudage est monté une seule fois. Ravalement et isolation dans le même chantier, c\'est moins de frais et une façade neuve.</div><a class="btn" href="/isolation-thermique-exterieur-rouen/">Découvrir l\'ITE</a></div><img class="ph" src="{P[2]}" alt="Isolation thermique par l\'extérieur d\'une maison près de Rouen" loading="lazy"></div></section>'
    b += f'<section class="dark"><div class="w"><h2>Comment se passe votre projet ?</h2><p style="margin-bottom:30px">Quatre étapes simples, sans surprise.</p>{STEPS}</div></section>'
    b += '<section><div class="w g2"><div class="urg"><h2>Le climat normand use vos façades</h2><p>Pluie fréquente, humidité, mousses et vent sur les plateaux : un enduit fissuré laisse entrer l\'eau, et un mur humide isole mal. Un diagnostic gratuit permet de savoir s\'il faut nettoyer, repeindre, ravaler ou isoler.</p></div><div><h3>💧 Humidité et infiltrations</h3><p>Fissures et enduits poreux laissent passer l\'eau.</p><h3>🌿 Mousses et lichens</h3><p>Ils noircissent la façade et dégradent le support.</p><h3>🌬️ Vent des plateaux</h3><p>Il refroidit les murs mal isolés et augmente le chauffage.</p></div></div></section>'
    b += f'<section class="bg"><div class="w"><h2>Zones d\'intervention : Rouen et la Métropole</h2><p style="margin-bottom:20px">Depuis Barentin, ISO + intervient dans toute la Seine-Maritime : Rouen, le plateau Est, le plateau Nord, la vallée du Cailly et la rive gauche.</p>{tags()}</div></section>'
    b += '<section><div class="w"><h2>Nos conseils façade et isolation</h2><div class="grid">' + "".join(f'<article class="card rv"><img src="{P[i+3]}" alt="{a["t"]}" loading="lazy"><div class="in"><h3>{a["t"]}</h3><p>{a["intro"][:130]}…</p><a class="m" href="/blog/{a["slug"]}/">Lire le conseil →</a></div></article>' for i,a in enumerate(BLOG)) + '</div></div></section>'
    b += faqhtml(GFAQ)
    page("index.html", "Ravalement de façade et isolation à Rouen | ISO +", "ISO +, ravalement de façade, peinture extérieure et isolation par l'extérieur à Rouen et dans la Métropole. RGE Qualibat. Devis gratuit.", b, [faqschema(GFAQ)])
    # services
    for s in SERV:
        cr = f'<div class="crumb"><a href="/">Accueil</a> › {s["nom"]}</div>'
        b = hero(s["img"], s["kw"], s["direct"], ["Diagnostic et devis écrit gratuits", "Entreprise RGE Qualibat", "Garantie décennale 10 ans"], cr)
        b += f'<section><div class="w g2"><div class="prose"><h2>Qu\'est-ce que : {s["nom"].lower()} ?</h2><p>{s["defi"]}</p><h2>Comment se déroule le chantier ?</h2><ol>{"".join(f"<li>{e}</li>" for e in s["etapes"])}</ol><h2>Quel prix ?</h2><p>Le prix dépend de la surface, de l\'état du support, de l\'accès et de la finition choisie. ISO + établit un devis écrit gratuit après visite sur place.</p></div><img src="{s["img"]}" alt="{s["nom"]} par ISO + à Rouen" class="ph" loading="lazy"></div></section>'
        b += f'<section class="bg"><div class="w"><h2>{s["nom"]} : repères</h2><table><tr><th>Point</th><th>Chez ISO +</th></tr><tr><td>Visite et diagnostic</td><td>Gratuits</td></tr><tr><td>Devis</td><td>Écrit et détaillé, sans engagement</td></tr><tr><td>Certification</td><td>RGE Qualibat</td></tr><tr><td>Garantie</td><td>Décennale 10 ans</td></tr><tr><td>Zone</td><td>Rouen et Métropole</td></tr></table><h3 style="margin-top:30px">{s["nom"]} près de chez vous</h3>' + '<div class="tags">' + "".join(f'<a href="/{slugc(c[0])}/">{s["nom"]} {c[0]}</a>' for c in COM[:12]) + '</div></div></section>'
        b += faqhtml(s["faq"], f'Questions sur : {s["nom"].lower()}')
        sv = {"@context":"https://schema.org","@type":"Service","name":s["kw"],"description":s["defi"],"provider":{"@id":SITE+"/#entreprise"},"areaServed":"Rouen"}
        page(f'{s["slug"]}/index.html', (s["kw"]+" | ISO + RGE")[:62], s["direct"][:155], b, [sv, faqschema(s["faq"])], [("Accueil","/"),(s["nom"],f'/{s["slug"]}/')])
    # communes
    for n, sec, km, txt in COM:
        sl = slugc(n); cr = f'<div class="crumb"><a href="/">Accueil</a> › <a href="/communes/">Communes</a> › {n}</div>'
        dist = "Siège de l'entreprise" if km == 0 else f"Environ {km} km de notre siège de Barentin"
        b = hero(P[COM.index((n,sec,km,txt)) % 6], f"Ravalement de façade et isolation à {n}", f"ISO + rénove, repeint et isole les façades à {n} ({sec}). {txt}", ["Visite et devis gratuits à " + n, "Isolation par l'extérieur RGE, éligible aux aides", "Garantie décennale"], cr)
        b += f'<section><div class="w g2"><div class="prose"><h2>Quels travaux de façade à {n} ?</h2><p>À {n}, ISO + réalise le ravalement de façade, la peinture extérieure, le nettoyage, le bardage et l\'isolation thermique par l\'extérieur. {txt}</p><h2>Repères pour {n}</h2><table><tr><th>Point</th><th>Détail</th></tr><tr><td>Secteur</td><td>{sec}</td></tr><tr><td>Distance</td><td>{dist}</td></tr><tr><td>Diagnostic</td><td>Gratuit, sur place</td></tr><tr><td>Devis</td><td>Écrit, sans engagement</td></tr><tr><td>Aides isolation</td><td>Possibles (entreprise RGE)</td></tr></table><h2>Faut-il une autorisation à {n} ?</h2><p>Un ravalement ou une isolation par l\'extérieur demandent souvent une déclaration préalable en mairie de {n}, et le PLU peut encadrer les couleurs. Nous vous aidons à préparer le dossier.</p></div><div>' + "".join(f'<p><a href="/{s["slug"]}/"><b>{s["ic"]} {s["nom"]} à {n}</b></a><br>{s["court"]}</p><br>' for s in SERV) + '</div></div></section>'
        voisins = [c for c in COM if c[1] == sec and c[0] != n][:6] or COM[:6]
        b += '<section class="bg"><div class="w"><h2>Communes voisines</h2><div class="tags">' + "".join(f'<a href="/{slugc(c[0])}/">{c[0]}</a>' for c in voisins) + '</div></div></section>'
        fq = [(f"Intervenez-vous à {n} ?", f"Oui, ISO + intervient à {n} pour tous les travaux de façade et d'isolation. {dist}."),
              (f"Le devis est-il gratuit à {n} ?", "Oui, la visite, le diagnostic et le devis écrit sont gratuits et sans engagement."),
              ("Pouvez-vous m'aider pour les aides à l'isolation ?", "Oui, ISO + est certifiée RGE Qualibat et vous accompagne pour MaPrimeRénov' et les primes énergie.")]
        b += faqhtml(fq)
        page(f"{sl}/index.html", f"Façade et isolation à {n} | ISO +"[:62], f"Ravalement de façade, peinture extérieure et isolation par l'extérieur à {n}. Entreprise RGE, devis gratuit. ISO + au {TEL}.", b, [faqschema(fq)], [("Accueil","/"),("Communes","/communes/"),(n,f"/{sl}/")])
    b = hero(P[1], "Nos zones d'intervention autour de Rouen", "ISO + intervient dans toute la Métropole Rouen Normandie depuis Barentin.", ["Plateau Est et plateau Nord", "Vallée du Cailly et rive gauche", "Rouen centre"])
    secs = {}
    for c in COM: secs.setdefault(c[1], []).append(c[0])
    b += '<section><div class="w">' + "".join(f'<h2>{k}</h2><div class="tags" style="margin-bottom:30px">' + "".join(f'<a href="/{slugc(x)}/">{x}</a>' for x in v) + "</div>" for k,v in secs.items()) + "</div></section>"
    page("communes/index.html", "Zones d'intervention façade et isolation Rouen | ISO +", "Toutes les communes où ISO + réalise ravalement, peinture extérieure et isolation : Rouen, plateau Est, plateau Nord, rive gauche.", b, None, [("Accueil","/"),("Communes","/communes/")])
    # blog
    for i, a in enumerate(BLOG):
        s = next(x for x in SERV if x["slug"] == a["s"]); cr = f'<div class="crumb"><a href="/">Accueil</a> › <a href="/blog/">Conseils</a></div>'
        t = a["tab"]; tab = "<table><tr>" + "".join(f"<th>{c}</th>" for c in t[0]) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in t[1:]) + "</table>"
        b = f'<section class="hero" style="background-image:url({P[i+3]});padding:80px 0"><div class="w">{cr}<h1>{a["t"]}</h1><p class="l">Publié le {TODAY} · Mis à jour le {TODAY} · Par l\'équipe ISO +</p></div></section>'
        b += f'<section><div class="w prose"><p class="box">{a["intro"]}</p>' + "".join(f"<h2>{q}</h2><p>{r}</p>" for q,r in a["secs"]) + f'<h2>En résumé</h2>{tab}<p>Sources officielles : <a href="https://france-renov.gouv.fr" rel="noopener">France Rénov\'</a>, <a href="https://www.service-public.fr/particuliers/vosdroits/F17578" rel="noopener">Service-Public.fr (déclaration préalable)</a>.</p><p>Pour aller plus loin : <a href="/{s["slug"]}/">{s["kw"]}</a> · <a href="/rouen/">Façade à Rouen</a> · <a href="/le-mesnil-esnard/">Façade au Mesnil-Esnard</a></p></div></section>'
        art = {"@context":"https://schema.org","@type":"Article","headline":a["t"],"datePublished":TODAY,"dateModified":TODAY,"author":{"@type":"Organization","name":NOM},"publisher":{"@id":SITE+"/#entreprise"},"image":P[i+3]}
        page(f'blog/{a["slug"]}/index.html', (a["t"]+" | ISO +")[:62], a["intro"][:155], b, [art], [("Accueil","/"),("Conseils","/blog/"),(a["t"],f'/blog/{a["slug"]}/')])
    b = hero(P[4], "Conseils façade et isolation", "Nos guides pour bien préparer vos travaux à Rouen et en Normandie.", ["Prix et devis", "Aides à l'isolation", "Bonnes périodes de travaux"])
    b += '<section><div class="w grid">' + "".join(f'<article class="card rv"><img src="{P[i+3]}" alt="{a["t"]}" loading="lazy"><div class="in"><h3>{a["t"]}</h3><p>{a["intro"][:140]}…</p><a class="m" href="/blog/{a["slug"]}/">Lire →</a></div></article>' for i,a in enumerate(BLOG)) + "</div></section>"
    page("blog/index.html", "Conseils ravalement et isolation de façade | ISO +", "Guides ISO + : prix d'un ravalement, ITE ou isolation intérieure, quand repeindre sa façade en Normandie.", b, None, [("Accueil","/"),("Conseils","/blog/")])
    # faq
    allf = GFAQ + [q for s in SERV for q in s["faq"][:2]]
    b = hero(P[5], "Foire aux questions", "Toutes les réponses sur le ravalement, la peinture extérieure et l'isolation par l'extérieur à Rouen.", ["Devis et délais", "Aides et autorisations", "Garanties"]) + faqhtml(allf, "Vos questions, nos réponses")
    page("faq/index.html", "FAQ ravalement, peinture et isolation Rouen | ISO +", "Questions fréquentes sur le ravalement de façade, la peinture extérieure, l'ITE et les aides à Rouen.", b, [faqschema(allf)], [("Accueil","/"),("FAQ","/faq/")])
    # contact
    opts = "".join(f"<option>{s['nom']}</option>" for s in SERV)
    b = hero(P[0], "Demandez votre devis gratuit", "Réponse rapide, visite et diagnostic gratuits sur place.", [f"Téléphone : {TEL}", f"Email : {MAIL}", ADR])
    b += f'''<section><div class="w g2"><div><h2>Votre projet</h2><form onsubmit="event.preventDefault();var f=this;location.href='mailto:{MAIL}?subject='+encodeURIComponent('Demande de devis '+f.p.value+' - '+f.v.value)+'&body='+encodeURIComponent('Nom : '+f.n.value+'\\nTéléphone : '+f.t.value+'\\nCommune : '+f.v.value+'\\nProjet : '+f.p.value+'\\n\\n'+f.m.value)">
<input name="n" placeholder="Nom et prénom" required><input name="t" type="tel" placeholder="Téléphone" required><input name="v" placeholder="Commune" required><select name="p">{opts}</select><textarea name="m" rows="5" placeholder="Décrivez votre projet (surface, état de la façade...)"></textarea><button class="btn">Envoyer ma demande</button><p style="font-size:.85rem">Un souci d'envoi ? Appelez le <a href="tel:{TELI}">{TEL}</a>.</p></form></div>
<div><h2>Coordonnées</h2><p><b>ISO +</b><br>{ADR}<br>📞 <a href="tel:{TELI}">{TEL}</a><br>✉️ <a href="mailto:{MAIL}">{MAIL}</a><br>Du lundi au samedi, 9h-18h</p><iframe title="Carte ISO + Barentin" src="https://www.google.com/maps?q=62+Rue+du+G%C3%A9n%C3%A9ral+Sarrail+76360+Barentin&output=embed" style="width:100%;height:320px;border:0;border-radius:16px;margin-top:20px" loading="lazy"></iframe></div></div></section>'''
    page("contact/index.html", "Devis gratuit façade et isolation Rouen | ISO +", f"Contactez ISO + pour un devis gratuit de ravalement, peinture ou isolation à Rouen. {TEL}.", b, None, [("Accueil","/"),("Contact","/contact/")])
    page("mentions-legales/index.html", "Mentions légales | ISO +", "Mentions légales du site ISO +.", f'<section><div class="w prose"><h1>Mentions légales</h1><p>Éditeur : ISO +, {ADR}. Téléphone : {TEL}. Email : {MAIL}. SIRET : [À COMPLÉTER].</p><p>Hébergement : Cloudflare, Inc.</p><p>Aucun cookie publicitaire n\'est déposé.</p></div></section>')
    open(f"{D}/robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(f"{D}/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in PAGES) + "</urlset>")
    open(f"{D}/llms.txt","w").write(f"# ISO +\n> {DESC}\n\n" + "".join(f"- [{s['kw']}]({SITE}/{s['slug']}/)\n" for s in SERV) + f"\nContact : {TEL} · {MAIL}\n")
    print(len(PAGES), "pages")
build()
