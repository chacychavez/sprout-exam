from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist
import datetime

from src.database.models import RegularEmployee, ContractualEmployee
from src.schemas.employees import RegularEmployeeOutSchema, ContractualEmployeeOutSchema
from src.schemas.token import Status  # NEW


async def get_regular_employees():
    return await RegularEmployeeOutSchema.from_queryset(RegularEmployee.all())


async def get_regular_employee(employee_id) -> RegularEmployeeOutSchema:
    return await RegularEmployeeOutSchema.from_queryset_single(
        RegularEmployee.get(id=employee_id)
    )


async def create_regular_employee(employee) -> RegularEmployeeOutSchema:
    employee_dict = employee.dict(exclude_unset=True)
    employee_obj = await RegularEmployee.create(**employee_dict)
    return await RegularEmployeeOutSchema.from_tortoise_orm(employee_obj)


async def update_regular_employee(employee_id, employee) -> RegularEmployeeOutSchema:
    try:
        await RegularEmployeeOutSchema.from_queryset_single(
            RegularEmployee.get(id=employee_id)
        )
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {employee_id} not found")

    await RegularEmployee.filter(id=employee_id).update(
        **employee.dict(exclude_unset=True)
    )
    return await RegularEmployeeOutSchema.from_queryset_single(
        RegularEmployee.get(id=employee_id)
    )


async def delete_regular_employee(employee_id) -> Status:  # UPDATED
    try:
        await RegularEmployeeOutSchema.from_queryset_single(
            RegularEmployee.get(id=employee_id)
        )
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {employee_id} not found")

    deleted_count = await RegularEmployee.filter(id=employee_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Note {employee_id} not found")
    return Status(message=f"Deleted RegularEmployee {employee_id}")  # UPDATED


async def get_contractual_employees():
    return await ContractualEmployeeOutSchema.from_queryset(ContractualEmployee.all())


async def get_contractual_employee(employee_id) -> ContractualEmployeeOutSchema:
    return await ContractualEmployeeOutSchema.from_queryset_single(
        ContractualEmployee.get(id=employee_id)
    )


async def create_contractual_employee(employee) -> ContractualEmployeeOutSchema:
    employee_dict = employee.dict(exclude_unset=True)
    print(type(employee_dict["contract_end_date"]), employee_dict["contract_end_date"])
    employee_obj = await ContractualEmployee.create(**employee_dict)
    return await ContractualEmployeeOutSchema.from_tortoise_orm(employee_obj)


async def update_contractual_employee(
    employee_id, employee
) -> ContractualEmployeeOutSchema:
    try:
        await ContractualEmployeeOutSchema.from_queryset_single(
            ContractualEmployee.get(id=employee_id)
        )
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {employee_id} not found")

    employee_dict = employee.dict(exclude_unset=True)
    employee_dict["contract_end_date"] = datetime.datetime.fromtimestamp(
        employee_dict["contract_end_date"]
    )

    await ContractualEmployee.filter(id=employee_id).update(**employee_dict)
    return await ContractualEmployeeOutSchema.from_queryset_single(
        ContractualEmployee.get(id=employee_id)
    )


async def delete_contractual_employee(employee_id) -> Status:  # UPDATED
    try:
        await ContractualEmployeeOutSchema.from_queryset_single(
            ContractualEmployee.get(id=employee_id)
        )
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {employee_id} not found")

    deleted_count = await ContractualEmployee.filter(id=employee_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Note {employee_id} not found")
    return Status(message=f"Deleted ContractualEmployee {employee_id}")  # UPDATED
