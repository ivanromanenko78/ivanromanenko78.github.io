const locale=JSON.parse(document.getElementById('locale').textContent);
const form=document.getElementById('brief-form');
form.addEventListener('submit',event=>{
 event.preventDefault();
 const data=new FormData(form);
 const values=['name','business','contact','brief'].map(key=>String(data.get(key)||'').trim());
 const lines=values.map((value,index)=>value?locale.msg_fields[index]+': '+value:'').filter(Boolean);
 const message=locale.message+'\n\n'+lines.join('\n');
 document.getElementById('prepared-text').value=message;
 document.getElementById('send-message').href='https://wa.me/351967901942?text='+encodeURIComponent(message);
 const ready=document.getElementById('message-ready');ready.hidden=false;ready.scrollIntoView({behavior:'smooth',block:'nearest'});
});
document.getElementById('copy-message').addEventListener('click',async()=>{
 const message=document.getElementById('prepared-text');
 try{await navigator.clipboard.writeText(message.value);document.getElementById('copy-status').textContent=locale.copied;}
 catch{message.focus();message.select();document.getElementById('copy-status').textContent=locale.copyfail;}
});
