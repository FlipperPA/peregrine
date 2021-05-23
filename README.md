# Peregrine

Peregrine is an opinionated blogging platform which uses [the Wagtail CMS](https://wagtail.io) on the [Django web framework](https://www.djangoproject.com). It uses Wagtail's fantastic [StreamField feature](http://docs.wagtail.io/en/v1.13/topics/streamfield.html) to provide fully structured content body element blocks, completely separating content from the presentation layer (CSS, JS, and HTML).

Peregrine requires at least Wagtail 2.0 and Django 2.0.

**Are you looking for a more robust system, for example, creating a marketing site? The maintainer of Peregrine also contributes to [CodeRedCMS](https://github.com/coderedcorp/coderedcms), which offers a lot more bells and whistles. Peregrine will remain a basic blogging system.**

## Getting Started: the Five Minute Install

These instructions will be fleshed out, but if you want to give it a try, here are the basics.

### System

```shell
mkvirtualenv my_blog
pip install peregrine
django-admin startproject my_blog
cd my_blog
```

### Settings

Your settings file will be located in `my_blog/settings.py` if you're using the default Django project layout created by the `startproject` command above. You'll need to add the sections beneath `INSTALLED_APPS` and `MIDDLEWARE`, and add `'wagtail.contrib.settings.context_processors.settings',` to your `TEMPLATES` context processors in your settings to look like this.

```python
INSTALLED_APPS = [
    ...
]

PEREGRINE_APPS = [
    "peregrine",
    "bootstrap4",
    "wagtailcodeblock",
    "wagtailcontentstream",

    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "taggit",
    "modelcluster",

    "wagtail.contrib.settings",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.table_block",
]


INSTALLED_APPS += PEREGRINE_APPS

MIDDLEWARE = [
    ...
]

PEREGRINE_MIDDLEWARE = [
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

MIDDLEWARE += PEREGRINE_MIDDLEWARE

# WAGTAIL_SITE_NAME is used by Wagtail; others are used by OpenGraph.
WAGTAIL_SITE_NAME = "PyPhilly: Home of FlipperPA"
WAGTAIL_SITE_DESCRIPTION = "PyPhilly is the website of Tim Allen, a web developer living in Philadelphia. Tim has a wide range of interests, but mostly writes about Python, Django, and virtual reality."
WAGTAIL_SITE_URL = "https://PyPhilly.org/"

TEMPLATES = [
    {
        ...

        'OPTIONS': {
            'context_processors': [
                ...

                'wagtail.contrib.settings.context_processors.settings',
            ]
        }
    }
]

```

### URLs

```python
from django.contrib import admin
from django.urls import include, path, re_path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # Wagtail / Peregrine URLs
    path('documents/', include(wagtaildocs_urls)),
    path('cms/', include(wagtailadmin_urls)),
    re_path(r'^', include('peregrine.urls')),
]
```

### Fire it up!

After you've set up your settings, we need to create your database and a superuser. Issue the following commands from your project root directory.

*Only run the command `peregrine_initial_site` if you are running on a new project, as it loads database fixtures!*


```shell
python manage.py migrate
# ** Be sure to see the note above before running this next command. It isn't necessary if you don't want to. **
python manage.py peregrine_initial_site
python manage.py createsuperuser
python manage.py runserver 0:8000
```

You should then be able to navigate to http://localhost:8000/cms/ and log in, and start creating!

## Maintainer

* Timothy Allen (https://github.com/FlipperPA/)

## Contributors

* Jon Banafato (https://github.com/jonafato/)
* Dave Bauer (https://github.com/tdxdave)
* Rana Fayez (https://github.com/Tagine/)
* Jeff Triplett (https://github.com/jefftriplett/)
