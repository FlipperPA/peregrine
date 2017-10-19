# Peregrine

An opinionated blogging platform for Wagtail on the Django web framework.

## Get Started

### System

    mkvirtualenv my_blog
    pip install peregrine


### Settings

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

### URLs

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
