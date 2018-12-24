# Peregrine

## Note: Please Read Before Using

**Peregrine will be joining forces with CodeRedCMS. We have similar philosophies: a plug and play system on top of Wagtail using Bootstrap 4. It doesn't make sense to duplicate our efforts.**

We will keep this repository and PyPI package present for our (very few) users.

**Please see [CodeRedCMS here](https://github.com/coderedcorp/coderedcms).**

Peregrine is an opinionated blogging platform which uses [the Wagtail CMS](https://wagtail.io) on the [Django web framework](https://www.djangoproject.com). It uses Wagtail's fantastic [StreamField feature](http://docs.wagtail.io/en/v1.13/topics/streamfield.html) to provide fully structured content body element blocks, completely separating content from the presentation layer (CSS, JS, and HTML).

*This is alpha software, in active development!*

Peregrine requires at least Wagtail 2.0 and Django 2.0.

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
    'peregrine',
    'bootstrap4',
    'wagtailcodeblock',
    'wagtailcontentstream',
    'taggit',
    'modelcluster',

    'wagtail.core',
    'wagtail.admin',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail.images',
    'wagtail.embeds',
    'wagtail.search',
    'wagtail.sites',
    'wagtail.contrib.settings',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block',
]

INSTALLED_APPS += PEREGRINE_APPS

MIDDLEWARE = [
    ...
]

PEREGRINE_MIDDLEWARE = [
    'wagtail.core.middleware.SiteMiddleware',
]

MIDDLEWARE += PEREGRINE_MIDDLEWARE

WAGTAIL_SITE_NAME = 'My Blog'


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

## Release Notes

### 0.2.2

* Switch the menus to pull any non-post pages tagged for inclusion in menus, rather than just pages of type `SitePage`.

### 0.2.1

* Add a `VACUUM` command if running SQLite on S3 as the default database engine to keep the SQLite DB size as small as possible.

### 0.2.0

* Add new setting to only keep recent revisions. If not set, will keep all revisions.

## Maintainer

* Timothy Allen (https://github.com/FlipperPA/)

## Contributors

* Jon Banafato (https://github.com/jonafato/)
* Rana Fayez (https://github.com/meetRanaFayez/)
* Jeff Triplett (https://github.com/jefftriplett/)
