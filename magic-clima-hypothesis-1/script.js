'use strict';
const slides=[...document.querySelectorAll('.slide')];
const previous=document.querySelector('#previous'),next=document.querySelector('#next'),counter=document.querySelector('#counter'),progress=document.querySelector('#progress');
let active=0;
function update(i){active=i;counter.textContent=`${i+1} / ${slides.length}`;progress.value=i+1;previous.disabled=i===0;next.disabled=i===slides.length-1;}
function go(i){i=Math.max(0,Math.min(slides.length-1,i));slides[i].scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'});update(i);history.replaceState(null,'',`#${slides[i].id}`);}
previous.addEventListener('click',()=>go(active-1));next.addEventListener('click',()=>go(active+1));
document.querySelector('#print').addEventListener('click',()=>window.print());
document.querySelector('#larger').addEventListener('click',e=>{const pressed=e.currentTarget.getAttribute('aria-pressed')!=='true';e.currentTarget.setAttribute('aria-pressed',String(pressed));document.documentElement.style.setProperty('--scale',pressed?'1.2':'1');});
const full=document.querySelector('#fullscreen');if(!document.fullscreenEnabled){full.hidden=true;}else{full.addEventListener('click',async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen();}catch{full.textContent='Полный экран недоступен';}});document.addEventListener('fullscreenchange',()=>full.textContent=document.fullscreenElement?'Выйти из экрана':'На весь экран');}
document.addEventListener('keydown',e=>{if(/INPUT|TEXTAREA|SELECT|BUTTON/.test(e.target.tagName)||e.target.isContentEditable)return;if(e.key==='ArrowRight'){e.preventDefault();go(active+1);}if(e.key==='ArrowLeft'){e.preventDefault();go(active-1);}});
let queued=false;function track(){if(queued)return;queued=true;requestAnimationFrame(()=>{let best=0,distance=Infinity;slides.forEach((slide,i)=>{const d=Math.abs(slide.getBoundingClientRect().top-90);if(d<distance){distance=d;best=i;}});update(best);queued=false;});}window.addEventListener('scroll',track,{passive:true});window.addEventListener('resize',track);window.addEventListener('hashchange',track);track();
