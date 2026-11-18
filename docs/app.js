(function(){
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
})();