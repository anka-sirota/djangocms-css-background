# CSS Background

## Description

Fork of https://github.com/WnP/djangocms-css-background.

Allows does the same thing that the djangocms-css-background does, but also allows nesting.


## Depends

- Django==1.7
- [django-cms](https://github.com/divio/django-cms)
- [djangocms-placeholder-attr](https://github.com/WnP/cms_placeholder_attr)
- [django-filer](https://github.com/stefanfoulis/django-filer)


## Installation

* pip install git+git://github.com/anka-sirota/djangocms-css-background.git#egg=djangocms-css-background;
* Syncronize the models: `python manage.py syncdb` (with south or django 1.7 use migrations)
* Put in your INSTALLED_APPS: `INSTALLED_APPS += ('djangocms-css-background', )`


## Usage

Select "CSS Background" from the list of available plugins, choose background, and then nest more plugins inside it.
