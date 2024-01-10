# Sprout Exam

Quick example of FastAPI with Tortoise and Aerich (for migration support).

## Quick Start

Build the image and spin up the `web` (FastAPI + Uvicorn) and `web-db` (Postgres) containers:

```sh
$ docker-compose up -d --build
```

Init Aerich:

```sh
$ docker-compose exec web aerich init -t db.TORTOISE_ORM
```

Create the first migration and apply it to the database:

```sh
$ docker-compose exec web aerich init-db
```

## Create Migration

Make a change to the model. Then, run:

```
$ docker-compose exec web aerich migrate
$ docker-compose exec web aerich upgrade
```

## Setup admin

- Go to https://localhost:5050/docs
- Register an admin user

## Postgres

Want to access the database via psql?

```sh
$ docker-compose exec web-db psql -U postgres

```

## Frontend

- Go to http://localhost:8080/
