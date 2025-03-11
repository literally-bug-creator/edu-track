from fastapi import Form
from dataclasses import dataclass
from schemas.common.forms import BaseForm, convert_dc_to_pd
from pydantic import EmailStr


class Register(BaseForm):
    username: EmailStr
    password: str
    first_name: str
    middle_name: str
    last_name: str


@dataclass
class _RegisterDC:
    username: EmailStr = Form(...)
    password: str = Form(...)
    first_name: str = Form(...)
    middle_name: str = Form(...)
    last_name: str = Form(...)


register = convert_dc_to_pd(_RegisterDC, Register)


class Login(BaseForm):
    username: EmailStr
    password: str


@dataclass
class _LoginDC:
    username: EmailStr = Form(...)
    password: str = Form(...)


login = convert_dc_to_pd(_LoginDC, Login)
