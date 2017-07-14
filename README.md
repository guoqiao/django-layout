# django-layout
a generic modern django project layout to bootstrap new project.

## Stack

- ubuntu
- nginx
- postgresql
- uwsgi
- supervisor
- celery

## django project structure

    django-layout
    ├── apps
    │   ├── accounts
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── __init__.py
    │   │   ├── migrations
    │   │   │   └── __init__.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── views.py
    │   └── main
    │       ├── admin.py
    │       ├── apps.py
    │       ├── __init__.py
    │       ├── migrations
    │       │   └── __init__.py
    │       ├── models.py
    │       ├── tests.py
    │       └── views.py
    ├── fixtures
    │   ├── init_sites.json
    │   ├── prod_sites.json
    │   ├── test_profiles.json
    │   └── test_users.json
    ├── layout
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── local.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── LICENSE
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── static
    │   ├── css
    │   │   └── main.css
    │   ├── img
    │   └── js
    │       └── main.js
    └── templates
        ├── base.html
        └── home.html

## Questions and Answers

### why we need another `layout` dir inside the repo root?
Django changes its default layout since 1.4 and introduce this new dir:

    https://docs.djangoproject.com/en/1.10/releases/1.4/#updated-default-project-layout-and-manage-py

These fix some issues with the previous manage.py handling of Python
import paths that caused double imports, trouble moving from development
to deployment, and other difficult-to-debug path issues.

### why we need the `apps` dir?
Group apps into this dir, make file list shorter.
Also, this distinct django apps from other dirs.

### why is the `apps` dir in repo root other then django project root?
1. I hate deep dirs.
2. This structure make it easier to add another django project based on same set of apps.

### why don't put tempaltes/static/fixtures inside each app and make them self-contained?
Self-contained seems like a good idea, make it much easier to package
the app and reuse it. If your app is very independent, then make it
self-contained or make a package, no problem. But normally that's not
true. You either need a lot of extra effert to make it really
self-contained, or you end up depend on files in other apps, like base
template, static files, or models. After struggling for many years,
I've to accept the fact that these stuff are global and common files
which need to share by whole project. And put these global files all
together make it way easier to have a glace what we have in project.

Also, this help you get ride of stupid duplicated dir structure like
`accounts/templates/accounts/profile.html`. Flat is always better
than nested.

### what is the strange prefix for fixtures naming?
Normally we have 2 kinds of fixtures:
1. initial: required for all envs
2. test: used for test/dev

The prefix make it easy to distinct different fixtures. And you can load fixtures in bulk:

    python manage.py loaddata fixtures/test_*

And, I didn't put different related data together, because that only
make sense at beginning, it will become a mess later, make it painful to
figure out what data we have.
By creating fixtures on a per models basis, I make it very clear what we have
and where to add new data.

