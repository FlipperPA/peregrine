# Peregrine

An opinionated blogging platform for Wagtail on the Django web framework.

## Get Started

    mkvirtualenv my_blog
    pip install peregrine

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
