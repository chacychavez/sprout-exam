from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "contractualemployee" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(20) NOT NULL UNIQUE,
    "last_name" VARCHAR(128),
    "email" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "contract_end_date" TIMESTAMPTZ,
    "projects" VARCHAR(128)
);;
        CREATE TABLE IF NOT EXISTS "employee" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(20) NOT NULL UNIQUE,
    "last_name" VARCHAR(128),
    "email" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
        CREATE TABLE IF NOT EXISTS "regularemployee" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(20) NOT NULL UNIQUE,
    "last_name" VARCHAR(128),
    "email" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "number_of_leaves" INT,
    "benefits" VARCHAR(128)
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "contractualemployee";
        DROP TABLE IF EXISTS "employee";
        DROP TABLE IF EXISTS "regularemployee";"""
