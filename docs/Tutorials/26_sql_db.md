---
title: SQL DB
tags:
  - managed
  - cloud
  - hosted
  - sql
  - db
---

# SQL DB

<TagLinks />

::: tip cloudSQL is expensive
I've been running a small Cloud SQL Postgres DB for about a week and the charges are up to 80\$ for just over a week. This is way to high for me as the DB isn't accessed most days anyway.
:::

## PlanetScale SQL DB

- best serverless SQL DB, scalable
- git like database branches, concept just like git-flow, push/pull
  - entirely new playground to play with new data/schema
  - see diff with other db branches, schema-wise
  - test staging with exact copy from production, byte-for-byte ecactly same data

```
pscale branch create vercel add-table
```

## with django ORM

PlanetScale uses [vitess](https://vitess.io/) (Horizontal scaling for mySQL).

- scale beyond clouds, with RDS you are stick to a cloud
- vitess handles sudden DB spikes (biggest nightmares of DB)
- https://www.koyeb.com/tutorials/how-to-deploy-a-django-application-using-planetscale-and-koyeb
- https://vitess.io/blog/2020-11-30-how-to-deploy-django/
- https://github.com/vitessio/vitess/blob/d234083743d1cc9757ef673bf89be1a4a299b0b0/support/django/README.md

### Serverless Hosting koyeb

> 10 core location 55 Edge locations

- https://www.koyeb.com/
- No devops from our end
- [x] TLS encryption
- [ ] Global load balancing
- [ ] Auto healing
- [ ] Auto cron/work task

<Footer />
