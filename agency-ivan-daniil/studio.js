const STUDIO_BASE=new URL('.',import.meta.url);window.__STUDIO_BASE__=STUDIO_BASE.pathname;
const language=document.documentElement.dataset.lang||'pt';
const heroWords={"ru": "ВАШ БИЗНЕС.<br>В КАДРЕ.", "en": "YOUR BUSINESS.<br>IN THE FRAME.", "pt": "O SEU NEGÓCIO.<br>EM IMAGEM."};

const $=s=>document.querySelector(s);
const preview=$('#studio-preview'),video=$('#studio-preview-video');
function openPreview(){preview.showModal();video.play().catch(()=>{});}
function closePreview(){video.pause();preview.close();}
$('#studio-preview-close').addEventListener('click',closePreview);
preview.addEventListener('cancel',()=>video.pause());
preview.addEventListener('click',e=>{if(e.target===preview)closePreview();});
const wa='https://wa.me/351967901942';
// Capture prototype navigation before the reference engine attempts remote routes.
document.addEventListener('click',e=>{
 if(e.target.closest('.language-switch a')){e.stopImmediatePropagation();return;}
 const demo=e.target.closest('[data-studio-preview],#home-reel-video-watch-btn');
 if(demo){e.preventDefault();e.stopImmediatePropagation();openPreview();return;}
 const link=e.target.closest('[data-studio-target]');
 if(link){e.preventDefault();e.stopImmediatePropagation();document.documentElement.classList.remove('menu-open');$('#header-right-menu-btn').setAttribute('aria-expanded','false');const target=document.getElementById(link.dataset.studioTarget);if(window.studioNavigate)window.studioNavigate(target.id);else target.scrollIntoView({behavior:'smooth'});return;}
 if(e.target.closest('#header-logo')){e.preventDefault();e.stopImmediatePropagation();if(window.studioNavigate)window.studioNavigate('home-hero');else window.scrollTo({top:0,behavior:'smooth'});return;}
 if(e.target.closest('#end-section-title-link')){e.preventDefault();e.stopImmediatePropagation();window.open(wa,'_blank','noopener');}
},true);
document.querySelectorAll('[data-studio-contact]').forEach(form=>form.addEventListener('submit',e=>{e.preventDefault();e.stopImmediatePropagation();const name=form.querySelector('input').value;window.open(wa+'?text='+encodeURIComponent((language==='ru'?'Здравствуйте! '+(name?'Меня зовут '+name+'. ':'')+'Хочу узнать подробнее о пакете контента.':language==='en'?'Hello! '+(name?'My name is '+name+'. ':'')+'I would like to know more about your content package.':'Olá! '+(name?'Sou '+name+'. ':'')+'Gostaria de saber mais sobre o pacote de conteúdo.')),'_blank','noopener');},true));
let webgl=false;try{const c=document.createElement('canvas');webgl=!!(c.getContext('webgl2')||c.getContext('webgl'));}catch{}
function fallback(){
 document.documentElement.classList.add('no-webgl');
 const hero=$('#home-hero-visual-container'),heroActions=$('#hero-actions');hero.innerHTML=`<video class="fallback-hero-video" autoplay muted playsinline loop preload="auto" src="./assets/textures/reel/desktop.mp4"></video><div class="fallback-wordmark">${heroWords[language]||heroWords.pt}</div><span class="fallback-cross">+</span><span class="fallback-cross">+</span><span class="fallback-cross">+</span><span class="fallback-cross">+</span>`;
 if(heroActions)hero.append(heroActions);
 const reel=document.createElement('video');reel.className='fallback-reel';reel.src=new URL('assets/textures/reel/desktop.mp4',STUDIO_BASE).href;reel.autoplay=true;reel.loop=true;reel.muted=true;reel.playsInline=true;$('#home-reel-video-container').prepend(reel);
 document.querySelectorAll('.project-item').forEach(item=>{item.querySelector('.project-item-image').style.backgroundImage=`url('${new URL('assets/projects/'+item.dataset.id+'/home.webp',STUDIO_BASE).href}')`;});
 $('#header-right-menu-btn').addEventListener('click',()=>{const open=document.documentElement.classList.toggle('menu-open');$('#header-right-menu-btn').setAttribute('aria-expanded',String(open));});
 $('#header-right-talk-btn').addEventListener('click',()=>window.open(wa,'_blank','noopener'));
 $('#header-menu-talk').addEventListener('click',()=>window.open(wa,'_blank','noopener'));
 $('#footer-bottom-up').addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
 // Pointer motion keeps the fallback responsive without relying on a graphics context.
 hero.addEventListener('pointermove',e=>{const r=hero.getBoundingClientRect();const x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;hero.querySelector('.fallback-wordmark').style.transform=`translate(${x*12}px,${y*12}px)`;});
 document.querySelectorAll('video[autoplay]').forEach(v=>v.play().catch(()=>{}));
 const observer=new IntersectionObserver(entries=>entries.forEach(({target,isIntersecting})=>{if(isIntersecting)target.play().catch(()=>{});else target.pause();}),{rootMargin:'200px'});document.querySelectorAll('video[autoplay]').forEach(v=>observer.observe(v));
}
if(webgl){
 try{await import(new URL('engine/hoisted.CUO_IjfL.js',STUDIO_BASE));}
 catch(e){console.warn('3D unavailable; showing video version.',e);fallback();}
}else fallback();
