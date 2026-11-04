'use strict';
const locale=JSON.parse(document.getElementById('locale').textContent);
const reduce=matchMedia('(prefers-reduced-motion: reduce)');
const menu=document.getElementById('mobile-menu'), toggle=document.getElementById('menu-toggle');
function closeMenu(){menu.hidden=true;toggle.setAttribute('aria-expanded','false');toggle.innerHTML=locale.menu+' <span>+</span>';}
toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')==='true';if(open)closeMenu();else{menu.hidden=false;toggle.setAttribute('aria-expanded','true');toggle.innerHTML=locale.close+' <span>−</span>';}});
menu.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeMenu();toggle.focus();}});
if('IntersectionObserver' in window){const reveal=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');reveal.unobserve(e.target);}}),{threshold:.08});document.querySelectorAll('.reveal').forEach(el=>reveal.observe(el));}
const videos=[...document.querySelectorAll('[data-video]')];
function loadVideo(v){if(!v.getAttribute('src')){v.src=v.dataset.src;v.load();}}
function setState(v){const b=v.closest('figure').querySelector('.video-toggle');b.textContent=v.paused?'▶':'Ⅱ';b.setAttribute('aria-label',v.paused?b.dataset.play:b.dataset.pause);b.setAttribute('aria-pressed',String(!v.paused));}
videos.forEach(v=>{const b=v.closest('figure').querySelector('.video-toggle');b.addEventListener('click',()=>{if(v.paused){v.dataset.manual='play';loadVideo(v);v.play().catch(()=>{});}else{v.dataset.manual='pause';v.pause();}});v.addEventListener('play',()=>setState(v));v.addEventListener('pause',()=>setState(v));v.addEventListener('error',()=>{b.disabled=true;b.textContent='—';});});
const connection=navigator.connection;
if('IntersectionObserver' in window){const io=new IntersectionObserver(entries=>entries.forEach(({target:v,isIntersecting})=>{v.dataset.visible=isIntersecting?'1':'0';if(isIntersecting&&!document.hidden&&v.dataset.manual!=='pause'&&!reduce.matches&&!connection?.saveData){loadVideo(v);v.play().catch(()=>{});}else if(!isIntersecting)v.pause();}),{threshold:.2});videos.forEach(v=>io.observe(v));}
document.addEventListener('visibilitychange',()=>videos.forEach(v=>{if(document.hidden)v.pause();else if(v.dataset.visible==='1'&&v.dataset.manual!=='pause'&&!reduce.matches&&!connection?.saveData){loadVideo(v);v.play().catch(()=>{});}}));
reduce.addEventListener('change',()=>{if(reduce.matches)videos.forEach(v=>v.pause());});
const form=document.getElementById('brief-form');
if(form){
 const choice=new URLSearchParams(location.search).get('service');
 const service=Object.hasOwn(locale.serviceNames,choice)?locale.serviceNames[choice]:null;
 const requestedPlan=new URLSearchParams(location.search).get('plan');
 const plan=Object.hasOwn(locale.planNames,requestedPlan)?locale.planNames[requestedPlan]:null;
 form.addEventListener('submit',()=>{
  const fields=[[locale.name,document.getElementById('brief-name').value.trim()]];
  const business=document.getElementById('brief-business').value.trim();
  if(business)fields.push([locale.business,business]);
  if(service)fields.push([locale.service,service]);
  if(plan)fields.push([locale.planLabel,plan]);
  fields.push([locale.brief,document.getElementById('brief-task').value.trim()]);
  form.elements.text.value=locale.message+'\n\n'+fields.map(([label,value])=>label+': '+value).join('\n');
 });
}
