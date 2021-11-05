from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="peregrine",
    description="Peregrine is an opinioned blog system for the Wagtail content "
    "management system on the Django Web Framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tim Allen",
    author_email="tallen@wharton.upenn.edu",
    url="https://github.com/FlipperPA/peregrine",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    install_requires=[
        "wagtail>=2.15",
        "wagtailcontentstream>=0.4.0",
        "django-bootstrap4>=2",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
