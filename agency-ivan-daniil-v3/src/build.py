from pathlib import Path
import json, html, hashlib
ROOT=Path(__file__).resolve().parent.parent
DATA=json.loads((ROOT/'src/content.json').read_text())
BASE='https://ivanromanenko78.github.io/agency-ivan-daniil-v3/'
PHONE='351967901942'
CSS_REV=hashlib.sha256((ROOT/'assets/style.css').read_bytes()).hexdigest()[:10]
JS_REV=hashlib.sha256((ROOT/'assets/app.js').read_bytes()).hexdigest()[:10]
esc=lambda s:html.escape(str(s),quote=True)

def path(lang,key):
    prefix='' if lang=='pt' else lang+'/'
    d=DATA[lang]
    if key=='home': return prefix+'index.html'
    if key in d['services']: return prefix+d['services'][key]['slug']+'.html'
    if key.startswith('article-'): return prefix+'blog/'+d['articles'][int(key.split('-')[1])]['slug']+'.html'
    return prefix+{'blog':'blog/index.html','contact':'contacto.html','credits':'creditos.html'}[key]

def rel(src,target):
    import posixpath
    return posixpath.relpath(target,posixpath.dirname(src) or '.')

def link(lang,key,current,anchor=''):
    return rel(current,path(lang,key))+anchor

def asset(current,name): return rel(current,'assets/'+name)
def aurl(lang,key):return BASE+path(lang,key)
def btn(text,url,outline=False): return f'<a class="button {"button-outline" if outline else ""}" href="{esc(url)}">{text}<span aria-hidden="true">↗</span></a>'
def arrow():return '<span aria-hidden="true">↗</span>'

def motion(d):
    return '<div class="motion-art" aria-hidden="true"><div class="motion-ring"></div><div class="motion-type">'+''.join(f'<span>{x}</span>' for x in d['motionWords'])+'</div><div class="motion-grid"></div><span class="motion-id">IDea Studio / MOTION STUDY 001</span></div>'

def media(lang,cur,kind='coffee',hero=False):
    d=DATA[lang];label=d['mediaLabels'][kind]
    if kind in ['content','reels']:
        return f'''<figure class="media-frame still {kind}"><img src="{asset(cur,kind+'.webp')}" width="900" height="1350" alt="{esc(label)}" fetchpriority="high"><div class="film-grain" aria-hidden="true"></div><figcaption class="film-bottom">{label}</figcaption></figure>'''
    return f'''<figure class="media-frame {'hero-film' if hero else ''} {kind}"><video muted playsinline loop preload="none" poster="{asset(cur,kind+'.webp')}" data-video data-src="{asset(cur,kind+'.mp4')}" aria-label="{esc(label)}"></video><div class="film-grain" aria-hidden="true"></div><div class="film-top"><span><i></i> FILM / EDIT / MOTION</span><span>PLAY / LOOP</span></div><div class="film-bottom"><span>{label}</span><button class="video-toggle" type="button" data-play="{d['play']}" data-pause="{d['pause']}" aria-label="{d['play']}">▶</button></div></figure>'''

def services(lang,cur):
 d=DATA[lang]
 cards=''
 for i,(key,s) in enumerate(d['services'].items()):
    cards+=f'''<a class="service-row reveal" href="{link(lang,key,cur)}"><span class="mono">0{i+1}</span><h3>{s['name']}</h3><p>{s['intro']}</p><span class="round-arrow" aria-hidden="true">↗</span></a>'''
 return f'<section id="services" class="section paper"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">IDea Studio / {d["nav"][0]}</p><h2>{d["servicesH"]}</h2></div><p>{d["servicesLead"]}</p></div><div class="service-list">{cards}</div></div></section>'

def package(lang,cur):
 d=DATA[lang];cards=''
 for plan in d['plans']:
  recommended=plan['key']=='business'
  badge=f'<span class="tier-badge">{d["recommended"]}</span>' if recommended else '<span class="tier-badge tier-badge-empty" aria-hidden="true">&nbsp;</span>'
  rows=''.join(f'<div><dt>{label}</dt><dd>{value}</dd></div>' for label,value in zip(d['planLabels'],plan['values']))
  prefix=f'<span class="tier-from">{d["from"]}</span>' if plan['key']=='premium' else ''
  price=f"{int(plan['price']):,}".replace(',', ' ')
  bonus=''
  if plan.get('bonus'):
   label, description=plan['bonus']
   bonus=f'<p class="tier-bonus"><strong>{esc(label)}</strong><span>{esc(description)}</span></p>'
  cards+=f'''<article class="tier-card {'tier-recommended' if recommended else ''}">{badge}<h3>{plan['name']}</h3><p class="tier-subtitle">{plan['subtitle']}</p><div class="tier-price">{prefix}<strong>{price} €</strong><span>{d['month']}</span></div><dl class="tier-features">{rows}</dl>{bonus}{btn(d['choosePlan'],link(lang,'contact',cur)+'?service=content&plan='+plan['key'])}</article>'''
 shared=''.join(f'<div><h4>{h}</h4><p>{p}</p></div>' for h,p in d['sharedFeatures'])
 return f'''<section id="package" class="section"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">INSTAGRAM + FACEBOOK</p><h2>{d['packageH']}</h2></div><p>{d['packageLead']}</p></div><div class="tier-grid">{cards}</div><div class="package-common"><h3>{d['sharedTitle']}</h3><div class="package-shared">{shared}</div><p class="package-counting">{d['countingNote']}</p><p class="fineprint">{d['trial']}</p></div><aside class="ad-budget"><span aria-hidden="true">↗</span><div><h3>{d['adBudgetTitle']}</h3><p>{d['adBudgetNote']}</p></div></aside><p class="fineprint">{d['terms']}</p></div></section>'''

def process(lang,cur):
 d=DATA[lang]
 items=''.join(f'<li class="reveal"><span class="step-number">0{i+1}</span><h3>{h}</h3><p>{p}</p></li>' for i,(h,p) in enumerate(d['steps']))
 return f'<section class="section process-section"><div class="wrap"><p class="eyebrow">IDea Studio / PROCESS</p><h2>{d["processH"]}</h2><ol class="steps">{items}</ol></div></section>'

def ideas(lang,cur):
 d=DATA[lang]; contents=[media(lang,cur),media(lang,cur,'barber'),motion(d)]
 cards=''.join(f'<article class="idea-card reveal">{m}<div class="idea-caption"><span class="eyebrow">{tag}</span><h3>{h}</h3><p>{p}</p></div></article>' for (tag,h,p),m in zip(d['ideas'],contents))
 return f'<section class="section"><div class="wrap"><div class="section-heading"><h2>{d["ideasH"]}</h2><p>{d["demoNote"]}</p></div><div class="ideas-grid">{cards}</div></div></section>'

def team(lang,cur):
 d=DATA[lang]
 return f'''<section id="studio" class="section paper"><div class="wrap team-layout"><div><p class="eyebrow">IDea Studio</p><h2>{d['teamH']}</h2><p class="team-note">{d['teamNote']}</p></div><div class="team-people"><article class="person reveal"><span class="person-initial" aria-hidden="true">IR</span><div><h3>Ivan Romanenko</h3><span class="role">{d['ivanRole']}</span><p>{d['ivanText']}</p></div></article><article class="person reveal"><span class="person-initial" aria-hidden="true">D</span><div><h3>Daniil</h3><span class="role">{d['daniilRole']}</span><p>{d['daniilText']}</p></div></article></div></div></section>'''

def journal(lang,cur,full=False):
 d=DATA[lang]
 cards=''
 for i,ar in enumerate(d['articles']):
  if cur==path(lang,'article-'+str(i)): continue
  image=['journal-social.webp','journal-shoot.webp','journal-edit.webp'][i]
  visual=f'<img src="{asset(cur,image)}" width="1200" height="750" loading="lazy" alt="{esc(d["journalAlt"][i])}">' 
  cards+=f'<article class="article-card reveal"><a href="{link(lang,"article-"+str(i),cur)}"><div class="article-image">{visual}<span class="article-index mono">0{i+1}</span></div><div class="article-meta mono">{ar["category"]} / 04.11.2026</div><h3>{ar["title"]}</h3><p>{ar["excerpt"]}</p><span class="text-link">{d["read"]} ↗</span></a></article>'
 return f'<section class="section journal-section {"paper" if full else ""}"><div class="wrap">'+('' if full else f'<div class="section-heading"><h2>{d["journalH"]}</h2><a class="text-link" href="{link(lang,"blog",cur)}">{d["allArticles"]} ↗</a></div>')+f'<div class="article-grid {"two-articles" if cur.startswith(("blog/", "en/blog/", "ru/blog/")) and not cur.endswith("/index.html") else ""}">{cards}</div></div></section>'

def faq(lang,items):
 d=DATA[lang]; bits=''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in items)
 return f'<section class="section"><div class="wrap faq-layout"><div><p class="eyebrow">FAQ</p><h2>{d["faq"]}</h2></div><div class="faq-list">{bits}</div></div></section>'

def cta(lang,cur):
 d=DATA[lang]
 return f'<section class="contact-band"><div class="wrap"><p class="eyebrow">IDea Studio / NEXT FRAME</p><div><h2>{d["contactH"]}</h2>{btn(d["talk"],link(lang,"contact",cur))}</div></div></section>'

HOME_SERVICE_COPY={
 "pt": [
  "Escolher serviço",
  "Ver preços",
  "Ajudamos empresas em Lisboa com produção de vídeo, conteúdo para redes sociais, publicidade digital e criação de sites.",
  [
   [
    "Vídeo e conteúdo",
    "Filmagem, Reels e publicações para redes sociais."
   ],
   [
    "Publicidade",
    "Configuração e gestão de campanhas digitais."
   ],
   [
    "Criação de sites",
    "Landing pages e sites para empresas."
   ]
  ]
 ],
 "en": [
  "Choose a service",
  "View prices",
  "We help Lisbon businesses with video production, social content, digital advertising and web design.",
  [
   [
    "Video and content",
    "Filming, Reels and posts for social media."
   ],
   [
    "Advertising",
    "Digital campaign setup and management."
   ],
   [
    "Web design",
    "Landing pages and business websites."
   ]
  ]
 ],
 "ru": [
  "Выбрать услугу",
  "Смотреть цены",
  "Помогаем бизнесу в Лиссабоне с видео, контентом для соцсетей, рекламой и созданием сайтов.",
  [
   [
    "Видео и контент",
    "Съёмка, Reels и публикации для соцсетей."
   ],
   [
    "Реклама",
    "Настройка и ведение рекламных кампаний."
   ],
   [
    "Создание сайтов",
    "Лендинги и сайты для бизнеса."
   ]
  ]
 ]
}

def home(lang,cur):
 d=DATA[lang]
 label,price_label,lead,cards=HOME_SERVICE_COPY[lang]
 urls=('#package',rel(cur,'publicidade')+'/?lang='+lang+'#ads','sites/#packages')
 cards_html=''.join(f'<a class="hero-service" href="{url}"><strong>{name}</strong><span>{description}</span><span class="hero-service-prices">{price_label} ↗</span></a>' for (name,description),url in zip(cards,urls))
 service_nav=f'<nav class="hero-services" aria-label="{label}">{cards_html}</nav>'
 return f'''<section class="hero wrap"><div class="hero-heading"><div><p class="eyebrow"><i></i>{d['eyebrow']}</p><h1>{d['homeH']}</h1></div><div class="hero-aside"><p class="lead">{lead}</p><div class="hero-actions">{btn(d['cta'],link(lang,'contact',cur))}<a class="text-link" href="#package">{d["plans"][0]["price"]} € {d['month']} ↓</a></div></div></div>{service_nav}{media(lang,cur,'hero',True)}<div class="hero-caption mono"><span>{d['homeTitle']}</span><span>FILM / EDIT / MOTION / SOCIAL</span></div></section>'''+services(lang,cur)+package(lang,cur)+ideas(lang,cur)+process(lang,cur)+team(lang,cur)+journal(lang,cur)+faq(lang,d['services']['content']['faqs'])+cta(lang,cur)

def service_page(lang,key,cur):
 d=DATA[lang];s=d['services'][key]
 visual=motion(d) if key=='motion' else media(lang,cur,{'content':'content','reels':'reels','video':'camera'}[key])
 advertising_link=''
 if key=='video':
  ads_label={"pt":"Publicidade e gestão de redes sociais","en":"Advertising and social media management","ru":"Реклама и ведение соцсетей"}[lang]
  ads_url=rel(cur,'publicidade')+'/?lang='+lang
  advertising_link=f'<p><a class="text-link" href="{ads_url}">{ads_label} ↗</a></p>'
 who=''.join(f'<li>{x}</li>' for x in s['who']); out=''.join(f'<li>{x}</li>' for x in s['out'])
 return f'''<section class="service-hero wrap"><div><p class="eyebrow">{s['tag']} · LISBOA</p><h1>{s['h']}</h1><p class="lead">{s['lead']}</p>{btn(d['talk'],link(lang,'contact',cur)+'?service='+key)}{advertising_link}<p class="service-seo-label mono">{s['title']}</p></div><div class="service-visual">{visual}</div></section><section class="section paper"><div class="wrap"><div class="section-heading"><h2>{d['forWho']}</h2><p>{s['intro']}</p></div><ul class="who-grid">{who}</ul></div></section><section class="section"><div class="wrap delivery-layout"><div><p class="eyebrow">IDea Studio / OUTPUT</p><h2>{d['deliver']}</h2><ul class="check-list">{out}</ul></div><aside class="scope-panel"><p class="eyebrow">{d['scope']}</p><h3>{s['price']}</h3><p>{s['priceText']}</p>{btn(d['talk'],link(lang,'contact',cur)+'?service='+key)}<p class="fineprint">{d['terms']}</p></aside></div></section>'''+(package(lang,cur) if key=='content' else '')+process(lang,cur)+faq(lang,s['faqs'])+f'<section class="section paper"><div class="wrap"><p class="eyebrow">{d["related"]}</p><div class="related-services">'+''.join(f'<a href="{link(lang,k,cur)}">{ss["name"]} ↗</a>' for k,ss in d['services'].items() if k!=key)+'</div></div></section>'+cta(lang,cur)

def contact(lang,cur):
 d=DATA[lang]
 return f'''<section class="section wrap contact-layout"><div><p class="eyebrow">IDea Studio / CONTACT</p><h1>{d['contactH']}</h1><p class="lead">{d['contactLead']}</p><a class="contact-phone" href="tel:+{PHONE}">+351 967 901 942</a><a class="text-link" href="https://wa.me/{PHONE}">WhatsApp ↗</a><p class="fineprint">Lisboa, Portugal · PT / EN / RU</p></div><div class="form-panel"><form id="brief-form" action="https://wa.me/{PHONE}" method="get"><label for="brief-name">{d['name']}</label><input id="brief-name" autocomplete="name" maxlength="120" placeholder="{esc(d['namePlaceholder'])}" required><label for="brief-business">{d['businessLabel']}</label><input id="brief-business" autocomplete="organization" maxlength="160" placeholder="{esc(d['businessPlaceholder'])}"><label for="brief-task">{d['brief']}</label><textarea id="brief-task" rows="5" maxlength="1800" placeholder="{esc(d['briefPlaceholder'])}" required></textarea><input type="hidden" name="text" id="whatsapp-text" value="{esc(d['message'])}"><button class="button" type="submit">{d['send']} <span aria-hidden="true">↗</span></button><p class="fineprint">{d['formNote']}</p></form></div></section>'''

def article(lang,idx,cur):
 d=DATA[lang]; ar=d['articles'][idx]
 toc=''.join(f'<a href="#part-{i}"><span>0{i+1}</span>{h}</a>' for i,(h,p) in enumerate(ar['sections']))
 body=''.join(f'<section id="part-{i}"><h2>{h}</h2><p>{p}</p></section>' for i,(h,p) in enumerate(ar['sections']))
 return f'''<header class="article-heading wrap"><a class="text-link" href="{link(lang,'blog',cur)}">← {d['back']}</a><p class="eyebrow">{ar['category']} / JOURNAL</p><h1>{ar['title']}</h1><p class="lead">{ar['excerpt']}</p><p class="mono">{d['author']} · 04.11.2026 · 3 {d['minutes']}</p></header><figure class="article-cover wrap"><img src="{asset(cur,['journal-social.webp','journal-shoot.webp','journal-edit.webp'][idx])}" width="1200" height="750" alt="{esc(d['journalAlt'][idx])}"></figure><div class="article-body wrap"><nav class="toc" aria-label="{d['nav'][3]}">{toc}</nav><article class="prose">{body}<aside class="article-offer"><h2>{d['monthly']}</h2><p>{d["plans"][0]["price"]} € {d['month']} · {d['trial']}</p>{btn(d['talk'],link(lang,'contact',cur)+'?service=content')}</aside><p><a class="text-link" href="{link(lang,'content',cur)}">{d['services']['content']['name']} ↗</a><br><a class="text-link" href="{link(lang,'video',cur)}">{d['services']['video']['name']} ↗</a></p></article></div>'''+journal(lang,cur)+cta(lang,cur)

def credits(lang,cur):
 d=DATA[lang]
 sources=[('Mixkit', 'Film production — 44069', 'https://mixkit.co/free-stock-video/young-man-recording-with-a-camera-on-a-set-44069/'), ('Mixkit', 'Barber — 43241', 'https://mixkit.co/free-stock-video/barber-begins-to-cut-the-hair-of-his-client-43241/'), ('Mixkit', 'Coffee — 41860', 'https://mixkit.co/free-stock-video/employee-serving-a-cup-of-coffee-from-a-machine-41860/'), ('Pexels / Amar Preciado', 'Product shoot — 7112246', 'https://www.pexels.com/video/a-videographer-holding-a-camera-7112246/'), ('Pexels / cottonbro studio', 'Social media — 5081926', 'https://www.pexels.com/photo/person-using-a-smartphone-5081926/'), ('Pexels / The Lazy Artist Gallery', 'Camera equipment — 4164088', 'https://www.pexels.com/photo/digital-camera-with-different-lenses-on-table-4164088/'), ('Pexels / Amar Preciado', 'Editing — 11025648', 'https://www.pexels.com/photo/a-laptop-near-the-computer-set-on-the-table-11025648/'), ('Pexels / Hanna Pad', 'Brand content — 12433033', 'https://www.pexels.com/photo/a-woman-being-recorded-on-a-camera-12433033/'), ('Pexels / Alan Quirván', 'Recording — 14540964', 'https://www.pexels.com/photo/woman-during-recording-14540964/')]
 items=''.join(f'<li><a href="{url}">{label} ↗</a><br><small>{author}</small></li>' for author,label,url in sources)
 return f'''<section class="section wrap legal"><p class="eyebrow">IDea Studio / INFO</p><h1>{d['creditTitle']}</h1><p class="lead">{d['creditText']}</p><ul class="media-credits">{items}</ul><p><a href="https://mixkit.co/license/#videoFree">Mixkit License ↗</a> · <a href="https://www.pexels.com/license/">Pexels License ↗</a></p><h2>{d['credits']}</h2><p>{d['privacyText']}</p><a href="tel:+{PHONE}">+351 967 901 942</a></section>'''

def render(lang,key):
 d=DATA[lang];cur=path(lang,key)
 title={"pt":"Vídeo, publicidade e criação de sites em Lisboa","en":"Video, advertising and web design in Lisbon","ru":"Видео, реклама и создание сайтов в Лиссабоне"}[lang] if key=='home' else d['services'][key]['title'] if key in d['services'] else d['articles'][int(key.split('-')[1])]['title'] if key.startswith('article-') else {'blog':d['nav'][3]+' — '+d['journalH'].replace('<br>',' '),'contact':d['contactTitle'],'credits':d['creditTitle']}[key]
 desc={"pt":"Produção de vídeo, conteúdos para redes sociais, campanhas digitais e criação de sites para empresas em Lisboa. Veja os serviços e preços da IDea Studio.","en":"Video production, social media content, digital advertising and web design for Lisbon businesses. Explore IDea Studio’s services and prices.","ru":"Видеосъёмка, контент для соцсетей, настройка рекламы и создание сайтов для бизнеса в Лиссабоне. Услуги и цены IDea Studio."}[lang] if key=='home' else d['services'][key]['lead'] if key in d['services'] else d['articles'][int(key.split('-')[1])]['excerpt'] if key.startswith('article-') else d['contactLead'] if key=='contact' else d['homeLead']
 canonical=BASE+cur
 is_article=key.startswith('article-')
 share_image=BASE+'assets/'+(['journal-social.webp','journal-shoot.webp','journal-edit.webp'][int(key.split('-')[1])] if is_article else 'social.jpg')
 share_type='image/webp' if is_article else 'image/jpeg'
 share_height='750' if is_article else '630' 
 head=f'''<!doctype html><html lang="{d['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} | IDea Studio</title><meta name="description" content="{esc(desc)}"><meta name="theme-color" content="#111411"><link rel="canonical" href="{canonical}"><link rel="icon" href="{asset(cur,'icon.svg')}" type="image/svg+xml"><link rel="stylesheet" href="{asset(cur,'style.css')}?v={CSS_REV}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="{'article' if key.startswith('article-') else 'website'}"><meta property="og:url" content="{canonical}"><meta property="og:site_name" content="IDea Studio"><meta property="og:image" content="{share_image}"><meta name="twitter:card" content="summary_large_image">'''
 locales={'pt':'pt_PT','en':'en_GB','ru':'ru_RU'}
 head+=f'<meta property="og:locale" content="{locales[lang]}"><meta property="og:image:type" content="{share_type}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="{share_height}"><meta property="og:image:alt" content="{esc(d['homeTitle'])}"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{share_image}"><meta name="twitter:image:alt" content="{esc(d['homeTitle'])}">'
 for lng in DATA:
  head+=f'<link rel="alternate" hreflang="{DATA[lng]["lang"]}" href="{aurl(lng,key)}">'
  if lng!=lang: head+=f'<meta property="og:locale:alternate" content="{locales[lng]}">'

 head+=f'<link rel="alternate" hreflang="x-default" href="{aurl("pt",key)}">'
 org={'@type':'Organization','@id':BASE+'#studio','name':'IDea Studio','url':BASE,'telephone':'+351967901942','areaServed':{'@type':'City','name':'Lisboa'}}
 graph=[org,{'@type':('ContactPage' if key=='contact' else 'CollectionPage' if key=='blog' else 'WebPage'),'@id':canonical+'#page','url':canonical,'name':title,'description':desc,'inLanguage':d['lang'],'isPartOf':{'@id':BASE+'#website'}},{'@type':'WebSite','@id':BASE+'#website','name':'IDea Studio','url':BASE}]
 if key in d['services']: graph.append({'@type':'Service','name':title,'description':desc,'url':canonical,'provider':{'@id':BASE+'#studio'},'areaServed':{'@type':'City','name':'Lisboa'}})
 if key in ['home','content']:
  offers=[]
  for plan in d['plans']:
   offer={'@type':'Offer','url':aurl(lang,'content')+'#package','name':plan['name'],'priceCurrency':'EUR','itemOffered':{'@type':'Service','name':plan['name']+' — '+d['services']['content']['name'],'provider':{'@id':BASE+'#studio'}}}
   if plan['key']=='premium':offer['priceSpecification']={'@type':'UnitPriceSpecification','minPrice':plan['price'],'priceCurrency':'EUR','unitText':d['month']}
   else:offer['priceSpecification']={'@type':'UnitPriceSpecification','price':plan['price'],'priceCurrency':'EUR','unitText':d['month']}
   offers.append(offer)
  graph.append({'@type':'OfferCatalog','@id':aurl(lang,'content')+'#packages','name':d['monthly'],'itemListElement':offers})
 if key.startswith('article-'):graph.append({'@type':'BlogPosting','headline':title,'description':desc,'datePublished':'2026-11-04','dateModified':'2026-11-04','author':{'@id':BASE+'#studio'},'publisher':{'@id':BASE+'#studio'},'mainEntityOfPage':canonical,'image':share_image,'inLanguage':d['lang']})
 if key!='home':graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'IDea Studio','item':aurl(lang,'home')},{'@type':'ListItem','position':2,'name':title,'item':canonical}]})
 head+='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('</',r'<\/')+'</script></head>'
 nav=f'''<a href="{link(lang,'home',cur,'#services')}">{d['nav'][0]}</a><a href="{link(lang,'content',cur,'#package')}">{d['nav'][1]}</a><a href="{link(lang,'home',cur,'#studio')}">{d['nav'][2]}</a><a href="{link(lang,'blog',cur)}">{d['nav'][3]}</a>'''
 language_names={'pt':'Português','en':'English','ru':'Русский'}
 language_label={'pt':'Idioma','en':'Language','ru':'Язык'}[lang]
 langs=''.join(f'<a href="{rel(cur,path(lng,key))}" lang="{DATA[lng]["lang"]}" hreflang="{DATA[lng]["lang"]}" aria-label="{language_names[lng]}" {"aria-current=page" if lng==lang else ""}>{language_names[lng]}</a>' for lng in DATA)
 ads_label={'pt':'Publicidade','en':'Advertising','ru':'Реклама'}[lang]
 ads_url=rel(cur,'publicidade')+'/?lang='+lang
 ads_nav=f'<a href="{ads_url}">{ads_label}</a>'
 sites_label={"pt":"Criação de sites","en":"Web design","ru":"Создание сайтов"}[lang]
 sites_url=rel(cur,path(lang,'home')).removesuffix('index.html')+'sites/'
 nav+=f'<a href="{sites_url}">{sites_label}</a>'
 desktop_nav=nav if key=='video' else nav+ads_nav
 header_ads=f'<a class="text-link" href="{ads_url}">{ads_label}</a>' if key=='video' else ''
 nav+=ads_nav
 header=f'''<body><a href="#main" class="skip-link">{d['skip']}</a><header class="site-header"><div class="wrap header-inner"><a href="{link(lang,'home',cur)}" class="brand"><img class="studio-logo" src="{asset(cur,'idea-studio-logo.png')}" alt="IDea Studio — Agência Criativa" lang="pt-PT" width="600" height="157"></a><nav class="desktop-nav" aria-label="{d['menu']}">{desktop_nav}</nav><div class="header-actions">{header_ads}<nav class="languages" aria-label="{language_label}">{langs}</nav><a class="header-contact" href="{link(lang,'contact',cur)}">{d['talk']} ↗</a><button id="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu">{d['menu']} <span>+</span></button></div></div><div class="mobile-language-bar wrap"><span class="language-label">{language_label}</span><nav class="languages" aria-label="{language_label}">{langs}</nav></div><nav id="mobile-menu" class="mobile-menu wrap" aria-label="{d['menu']}" hidden>{nav}<a href="{link(lang,'contact',cur)}">{d['talk']} ↗</a></nav></header>'''
 if key=='home': body=home(lang,cur)
 elif key in d['services']: body=service_page(lang,key,cur)
 elif key=='blog': body=f'<section class="journal-hero wrap"><p class="eyebrow">IDea Studio / JOURNAL</p><h1>{d["journalH"]}</h1><p class="lead">{d["articles"][0]["excerpt"]}</p></section>'+journal(lang,cur,True)+cta(lang,cur)
 elif key=='contact': body=contact(lang,cur)
 elif key=='credits':body=credits(lang,cur)
 else:body=article(lang,int(key.split('-')[1]),cur)
 editor_label={'pt':'Área de edição','en':'Blog editor','ru':'Редактор блога'}[lang]
 editor_link=f'<a href="https://idea-studio-editor.ivanromanenko.chatgpt.site/admin/">{editor_label}</a>' if key=='blog' else ''
 footer=f'''<footer class="site-footer"><div class="wrap"><div class="footer-top"><a class="footer-wordmark" href="{link(lang,'home',cur)}"><img class="studio-logo" src="{asset(cur,'idea-studio-logo.png')}" alt="IDea Studio — Agência Criativa" lang="pt-PT" width="600" height="157"></a><p>{d['footerLine']}<br>Lisboa, Portugal</p></div><div class="footer-links">{''.join(f'<a href="{link(lang,k,cur)}">{s["name"]}</a>' for k,s in d['services'].items())}<a href="{link(lang,'blog',cur)}">{d['nav'][3]}</a></div><div class="footer-bottom"><span>© 2026 IDea Studio</span><a href="tel:+{PHONE}">+351 967 901 942</a><a href="{link(lang,'credits',cur)}">{d['credits']}</a>{editor_link}<a href="#main" aria-label="Top">↑</a></div></div></footer>'''
 locale={k:d[k] for k in ['message','name','business','service','brief','menu','close','planLabel']}
 locale['serviceNames']={k:v['name'] for k,v in d['services'].items()}
 locale['planNames']={v['key']:v['name'] for v in d['plans']}
 if key=='home':
  head=head.removesuffix('</head>')+"<style>.hero-services{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:0 0 24px}.hero-service{display:grid;align-content:start;gap:5px;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--dark)}.hero-service strong{font-size:17px}.hero-service span{font-size:13px;color:var(--muted)}.hero-service .hero-service-prices{color:var(--lime);font-weight:bold}.hero-service:hover{border-color:var(--lime)}@media(max-width:600px){.hero-services{grid-template-columns:1fr;gap:8px}.hero-service{grid-template-columns:1fr auto;align-items:center;padding:10px 12px}.hero-service strong{font-size:15px}.hero-service .hero-service-prices{grid-column:2;grid-row:1 / span 2;max-width:100px;text-align:right}}</style>"+'</head>'
 result=head+header+'<main id="main">'+body+'</main>'+footer+'<script id="locale" type="application/json">'+json.dumps(locale,ensure_ascii=False)+'</script>'+f'<script defer src="{asset(cur,"app.js")}?v={JS_REV}"></script></body></html>'
 target=ROOT/cur;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(result)
 return canonical

keys=['home','content','reels','video','motion','blog','contact','credits']+['article-'+str(i) for i in range(3)]
urls=[render(lng,k) for lng in DATA for k in keys]
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{u}</loc><lastmod>2026-11-04</lastmod></url>' for u in urls)+f'<url><loc>{BASE}publicidade/</loc></url>'+''.join(f'<url><loc>{BASE}{folder}sites/</loc></url>' for folder in ('','en/','ru/'))+'</urlset>'
(ROOT/'sitemap.xml').write_text(xml)
print(f'Built {len(urls)} pages in PT / EN / RU')
