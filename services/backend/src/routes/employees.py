from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist
from src.auth.jwthandler import get_current_user

import src.crud.employees as crud
from src.schemas.employees import (
    RegularEmployeeOutSchema,
    RegularEmployeeInSchema,
    UpdateRegularEmployee,
    ContractualEmployeeOutSchema,
    ContractualEmployeeInSchema,
    UpdateContractualEmployee,
)
from src.schemas.token import Status


router = APIRouter()


@router.get(
    "/employees/regular",
    response_model=List[RegularEmployeeOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_employees():
    return await crud.get_regular_employees()


@router.get(
    "/employees/regular/{employee_id}",
    response_model=RegularEmployeeOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_regular_employee(employee_id: int) -> RegularEmployeeOutSchema:
    try:
        return await crud.get_regular_employee(employee_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Employee does not exist",
        )


@router.post(
    "/employees/regular",
    response_model=RegularEmployeeOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def create_regular_employee(
    employee: RegularEmployeeInSchema,
) -> RegularEmployeeOutSchema:
    return await crud.create_regular_employee(employee)


@router.patch(
    "/employees/regular/{employee_id}",
    response_model=RegularEmployeeOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def update_regular_employee(
    employee_id: int,
    employee: UpdateRegularEmployee,
) -> RegularEmployeeOutSchema:
    return await crud.update_regular_employee(employee_id, employee)


@router.delete(
    "/employees/regular/{employee_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_regular_employee(employee_id: int):
    return await crud.delete_regular_employee(employee_id)


@router.get(
    "/employees/contractual",
    response_model=List[ContractualEmployeeOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_employees():
    return await crud.get_contractual_employees()


@router.get(
    "/employees/contractual/{employee_id}",
    response_model=ContractualEmployeeOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_contractual_employee(employee_id: int) -> ContractualEmployeeOutSchema:
    try:
        return await crud.get_contractual_employee(employee_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Employee does not exist",
        )


@router.post(
    "/employees/contractual",
    response_model=ContractualEmployeeOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def create_contractual_employee(
    employee: ContractualEmployeeInSchema,
) -> ContractualEmployeeOutSchema:
    return await crud.create_contractual_employee(employee)


@router.patch(
    "/employees/contractual/{employee_id}",
    response_model=ContractualEmployeeOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def update_contractual_employee(
    employee_id: int,
    employee: UpdateContractualEmployee,
) -> ContractualEmployeeOutSchema:
    return await crud.update_contractual_employee(employee_id, employee)


@router.delete(
    "/employees/contractual/{employee_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_contractual_employee(employee_id: int):
    return await crud.delete_contractual_employee(employee_id)
