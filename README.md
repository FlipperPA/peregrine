# Peregrine

Peregrine is an opinionated blogging platform which uses [the Wagtail CMS](https://wagtail.io) on the [Django web framework](https://www.djangoproject.com). It uses Wagtail's fantastic [StreamField feature](http://docs.wagtail.io/en/v1.13/topics/streamfield.html) to provide fully structured content body element blocks, completely separating content from the presentation layer (CSS, JS, and HTML).

*This is very much pre-alpha software, in heavy active development!*

## Getting Started: the Five Minute Install

There instructions will be fleshed out, but if you want to give it a try, here are the basics.

### System

```shell
mkvirtualenv my_blog
# pip install peregrine # Coming soon! We've opened a ticket with PyPI to get the peregrine namespace.
pip install git+https://github.com/FlipperPA/peregrine.git
django-admin startproject my_blog
cd my_blog
```

### Settings

Your settings file will be located in `my_blog/settings.py` if you're using the default Django project layout created by the `startproject` command above. You'll need to add the sections beneath `INSTALLED_APPS` and `MIDDLEWARE` in your settings to look like this.

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

    'peregrine',
    'bootstrap4',
    'wagtailcodeblock',
    'wagtailcontentstream',
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

### Fire it up!

After you've set up your settings, we need to create your database and a superuser. Issue the following commands from your project root directory.

*Only run the command `peregrine_initial_site` if you are running on a new project, as it loads database fixtures!*


```shell
python manage.py migrate
python manage.py peregrine_initial_site
python manage.py createsuperuser
python manage.py runserver 0:8000
```

You should then be able to navigate to http://localhost:8000/cms/ and log in, and start creating!


## Contributors

* Timothy Allen (https://github.com/FlipperPA/)
* Jon Banafato (https://github.com/jonafato/)
* Jeff Triplett (https://github.com/jefftriplett/)
