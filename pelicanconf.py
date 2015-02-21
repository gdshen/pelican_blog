#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '沈国栋'
SITENAME = '工具与思考'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'chs'

# configure of gdshen
THEME = "/home/gdshen/GithubBlog/bootlex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
RELATIVE_URLS = False
ARTICLE_URL = ('{slug}/')
ARTICLE_SAVE_AS = ('{slug}.html')
PAGE_URL = ('{slug}/')
PAGE_SAVE_AS = ('{slug}.html')
AUTHOR_URL = ('author/{name}/')
TAG_URL = ('tag/{name}/')
