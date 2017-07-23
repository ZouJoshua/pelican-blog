#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joshua Zou'
SITENAME = "Joshua's Blog"
SITEURL = 'https://ZouJoshua.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese (Simplified)'
# Formatting for date
DEFAULT_DATE_FORMAT = ('%Y-%m-%d %a')


# Do not publish articles set in the future
#WITH_FUTURE_DATES = False
#TEMPLATE_PAGES = {'blog.html':'blog.html'}

#EXTRA_PATH_METADATA = {'extra/CNAME':{'path':'CNAME'}}




# Feed generation is usually not desired when developing
FEED_RSS = "feed/index.html"
FEED_ATOM = "feed/atom/index.html"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('魏畅的Blog', 'https://weichangit.github.io/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('weibo','http://www.weibo.com/233499456'),
		  ('envelope','mailto:joshua_zou@163.com'),
          ('twitter', 'https://twitter.com/joshua_zou'),
          ('facebook','https://www.facebook.com/joshua.zou.127'),
          ('linkedin', 'https://www.linkedin.com/in/%E5%B8%85-%E9%82%B9-736390135/'),
          ('github','https://github.com/ZouJoshua'))

DEFAULT_PAGINATION = True
PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
DIRECT_TEMPLATES = ('categories','index','blog')

POST_LIMIT = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Formatting for urls
ARTICLE_URL = "articles/{slug}/"
ARTICLE_SAVE_AS = "articles/{slug}/index.html"

# THEME
THEME = './pelican-themes/BT3-Flat'
BLOGDESCRIBE= '心安即行 \t 自在欢喜'

# HEADER_IMAGE
STATIC_PATHS = ['images','extra','articles']
HEADER_IMAGE = 'header_image.png'

# BACKGROUND_IMAGE
BACKGROUND_IMAGE = 'background_image.png'

# descripe
SITE_THUMBNATL = 'logo.png'
SITE_THUMBNATL_TEXT = 'Joshua zzzzz'
SITESUBTITLE = '一生所求  爱与自由  你与温柔'

FAVICON = 'logo.png'
ICON = 'logo.png'
SHORTCUT_IMAGE = 'logo.png'



# ABOUT_ME
PERSONAL_PHOTO = 'PERSONAL_PHOTO.png'
PERSONAL_INFO = "My name is Joshua Zou, a data mining / data analysis engineer who is working & living in Beijing, China.Currently working on ACMR.I've been working in this position for more than two years and the future career direction is to be a data scientist. I completed my work under linux and Windows.I learnt some languages, like Python,R, SAS, I use some analysis software, such as SPSS , SPSS Modeler, but also understand Eviews. But Python has been my favorite since I knew it for the first time in 2016. In the database, I used MySQL, Oracle, now also use Mongodb, Redis.At the same time, I understand a lot of data mining algorithms, and I think this is my core skills."


# pluginss
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'neighbors', 'related_posts']
# PLUGINS = ['sitemap', 'neighbors', 'related_posts','disqus_static']
# MARKUP = ('md', 'ipynb')




# sitemap

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# RELATED_POSTS
RELATED_POSTS_MAX = 3



# blog search
SWIFTYPE = 'MCHm_v2z1KZJynsU4VKN'


# disqus
DISQUS_SITENAME = 'joshuazou'

# JIATHIS
JIATHIS = True



# WORK
# WORK_DESCRIPTION = ''
# items to descripe a work "type","cover-image link","title","descption","link"
# WORK_LIST = {('link','https://xxx.png','workname','work descption','http://xxxxx')}