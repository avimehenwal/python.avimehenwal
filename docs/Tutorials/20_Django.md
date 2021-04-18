---
title: Django
tags:
  - django
  - framework
---

# Django

<TagLinks />

## Features?

> build a website with database attached to it

- high level web framework with **batteries included** started in 2003
- [instagram](https://instagram-engineering.com/web-service-efficiency-at-instagram-with-python-4976d078e366), pinterest, dropbox
- creating Django Data Models and then rendering them into Views. Full MVC pattern compliant
- Free admin UI out of the box
- [single request/response model like PHP at a time, single threaded](https://www.reddit.com/r/django/comments/99lu1k/how_do_you_make_django_handle_multiple_requests/)
- Security against SQL injection, cross-site scripting, cross-site request forgery and clickjacking.
- WSGI successor (PEP 333 & PEP 3333) => [ASGI Asynchronous Server Gateway Interface](https://asgi.readthedocs.io/en/latest/specs/index.html)
  - Django Channels, Queue implementation
  - CGI, run C code from HTTP requests
  - before request/response now we are talking about **connection and events**
- Can ctearte and mount multiple apps under various urls paths, use `include()`

```
# startup commands
python -m venv venv && source ./venv/bin/activate
pip install django && django-admin startproject dj2021 && cd dj2021
# create local sqlite DB, run it anytime after to make new, change django models
python manage.py migrate
python manage.py runserver
```

::: warning django migrations
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

start development server`python manage.py migrate && python manage.py runserver`

Django tracks which ones are applied using a special table in your database called **django_migrations**) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.
:::

## New App

```
python manage.py startapp polls
python manage.py shell
python manage.py createsuperuser
```

- Let django know about your new app model, wire up new app into django

### How to write views?

- How to add App namespace?

### How to add new models?

```
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001

```

- Register your app models to admin `admin.site.register(Question)`
- How to raise 404 ? when model doesnt exist? `get_object_or_404`

[what is refential CASCADE in django models?](https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models)

: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.

## How is it different?

Ruby of rails

- twitter, shopify 14 years ago

### Django | node.js | ruby on rails

#### production web-server | database

#### postgresSQL vs mySQL

## How to work with django?

<Footer />
