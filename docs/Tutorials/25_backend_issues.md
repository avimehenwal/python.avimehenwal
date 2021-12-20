---
title: 25_backend_issues
tags:
  - orm
  - query
  - django
---

# 25_backend_issues

<TagLinks />

> Issues to be vary about

## N + 1 Problem

The N+1 Queries Problem is a perennial database performance issue. It affects many ORM’s and custom SQL code, and Django’s ORM is not immune either.

> Abusing the databse with large number of smaller queries insteead of one or two large queries.

Eg: Books and Authors DB Schema

To get a list of 10 books with author information N+1 queries are made to DB

### Django query optimization get results in a single query

For ForeignKey, you can use [selected_related()](https://docs.djangoproject.com/en/dev/ref/models/querysets/#select-related)

Comment.objects.select_related('video').all()

```
Bools.objects.select_related('author').prefetch_related('books')
```

- django debugger can show you how many queries were made to db

## References

- https://scoutapm.com/blog/django-and-the-n1-queries-problem
- https://stackoverflow.com/questions/31237042/whats-the-difference-between-select-related-and-prefetch-related-in-django-orm

## SQLite in S3 bucket?

[Low concurrency read+writes as it locks the entire DB file while querying](https://www.sqlite.org/whentouse.html)

<Footer />
