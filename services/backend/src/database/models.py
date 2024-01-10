from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Employee(models.Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=20, unique=True)
    last_name = fields.CharField(max_length=128, null=True)
    email = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class RegularEmployee(Employee):
    number_of_leaves = fields.IntField(max_length=128, null=True)
    benefits = fields.CharField(max_length=128, null=True)


class ContractualEmployee(Employee):
    contract_end_date = fields.DatetimeField(null=True)
    projects = fields.CharField(max_length=128, null=True)
