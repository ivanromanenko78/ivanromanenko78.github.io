(async()=>{
  const feed=document.querySelector('[data-published-posts]');
  const lang=feed.dataset.publishedPosts;
  try{
    const response=await fetch('https://idea-studio-blog-api.ivanromanenko.chatgpt.site/posts?'+new URLSearchParams({lang}));
    if(!response.ok)return;
    const posts=await response.json();
    if(!Array.isArray(posts)||!posts.length)return;
    const list=document.createElement('ul');
    for(const post of posts){
      const link=document.createElement('a');
      link.href=feed.dataset.postPage+'?'+new URLSearchParams({lang,id:post.id});
      link.textContent=post.title;
      const row=document.createElement('li');
      row.append(link);
      list.append(row);
    }
    feed.append(list);
    feed.hidden=false;
  }catch{}
})();
