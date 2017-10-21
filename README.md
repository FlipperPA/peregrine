# Peregrine

Peregrine is an opinionated blogging platform which uses [the Wagtail CMS](https://wagtail.io) on the [Django web framework](https://www.djangoproject.com). It uses Wagtail's fantastic [StreamField feature](http://docs.wagtail.io/en/v1.13/topics/streamfield.html) to provide fully structured content body element blocks, completely separating content from the presentation layer (CSS, JS, and HTML).

*This is very much pre-alpha software, in heavy active development!*

## Get Started

There instructions will be fleshed out, but if you want to give it a try, here's the basic gist of it if you know what you're doing in Django.

### System

```shell
mkvirtualenv my_blog
pip install peregrine
```

### Settings

```python
INSTALLED_APPS = [
    ...
]

PEREGRINE_APPS = [
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailsites',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.contrib.table_block',

    'bootstrap4',
    'wagtailcodeblock',
    'wagtailcontentstream',
    'peregrine',
    'taggit',
    'modelcluster',
]

INSTALLED_APPS += PEREGRINE_APPS

MIDDLEWARE = [
    ...
]

PEREGRINE_MIDDLEWARE = [
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

MIDDLEWARE += PEREGRINE_MIDDLEWARE

WAGTAIL_SITE_NAME = 'My Blog'
```

### URLs

```python
from django.conf.urls import url, include
from django.contrib import admin

from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Peregrine URLs for Wagtail
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'', include(wagtail_urls)),
]
```

## Contributors

* Timothy Allen (https://github.com/FlipperPA/)
* Jon Banafato (https://github.com/jonafato/)
* Jeff Triplett (https://github.com/jefftriplett/)
