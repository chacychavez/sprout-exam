from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import RegularEmployee, ContractualEmployee


class UpdateEmployee(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]


RegularEmployeeInSchema = pydantic_model_creator(
    RegularEmployee, name="RegularEmployeeIn", exclude_readonly=True
)
RegularEmployeeOutSchema = pydantic_model_creator(
    RegularEmployee,
    name="RegularEmployee",
    exclude=["modified_at", "created_at"],
)


class UpdateRegularEmployee(UpdateEmployee):
    number_of_leaves: Optional[int]
    benefits: Optional[str]


ContractualEmployeeInSchema = pydantic_model_creator(
    ContractualEmployee, name="ContractualEmployeeIn", exclude_readonly=True
)
ContractualEmployeeOutSchema = pydantic_model_creator(
    ContractualEmployee,
    name="ContractualEmployee",
    exclude=["modified_at", "created_at"],
)


class UpdateContractualEmployee(UpdateEmployee):
    contract_end_date: Optional[int]
    projects: Optional[str]
