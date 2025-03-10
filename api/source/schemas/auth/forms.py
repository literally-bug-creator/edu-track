from fastapi import Form
from dataclasses import dataclass
from schemas.common.forms import BaseForm, convert_dc_to_pd
from schemas.auth.common import BaseUser


class Register(BaseForm, BaseUser):
    password: str


@dataclass
class _RegisterDC:
    email: str = Form(...)
    password: str = Form(...)
    first_name: str = Form(...)
    middle_name: str = Form(...)
    last_name: str = Form(...)


register = convert_dc_to_pd(_RegisterDC, Register)


class Login(BaseForm):
    email: str
    password: str


@dataclass
class _LoginDC:
    email: str = Form(...)
    password: str = Form(...)


login = convert_dc_to_pd(_LoginDC, Login)
