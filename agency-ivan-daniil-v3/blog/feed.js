(async()=>{
  const feed=document.querySelector('[data-published-posts]');
  if(!feed)return;

  const lang=feed.dataset.publishedPosts;
  const endpoint='https://idea-studio-blog-api.ivanromanenko.chatgpt.site/posts?';

  async function loadCover(link,query){
    try{
      const response=await fetch(endpoint+query);
      if(!response.ok)return;
      const {cover}=await response.json();
      if(!cover)return;

      const frame=document.createElement('div');
      frame.className='article-image';
      const image=document.createElement('img');
      image.alt='';
      image.decoding='async';
      image.addEventListener('load',()=>link.prepend(frame),{once:true});
      frame.append(image);
      image.src=cover;
    }catch{}
  }

  try{
    const response=await fetch(endpoint+new URLSearchParams({lang}));
    if(!response.ok)return;
    const posts=await response.json();
    if(!Array.isArray(posts)||!posts.length)return;

    const grid=document.createElement('div');
    grid.className='article-grid';
    const coverQueries=new WeakMap();
    const observer=typeof IntersectionObserver==='function' ? new IntersectionObserver(entries=>{
      for(const entry of entries){
        if(!entry.isIntersecting)continue;
        observer.unobserve(entry.target);
        void loadCover(entry.target,coverQueries.get(entry.target));
      }
    },{rootMargin:'200px'}) : null;

    for(const post of posts){
      const query=new URLSearchParams({lang,id:post.id});
      const card=document.createElement('article');
      card.className='article-card';
      const link=document.createElement('a');
      link.href=feed.dataset.postPage+'?'+query;
      const title=document.createElement('h3');
      title.textContent=post.title;
      link.append(title);
      card.append(link);
      grid.append(card);

      if(observer){
        coverQueries.set(link,query);
        observer.observe(link);
      }else{
        void loadCover(link,query);
      }
    }
    feed.append(grid);
    feed.hidden=false;
  }catch{}
})();
