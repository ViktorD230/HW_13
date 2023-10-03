from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr, validator


#validation for value phone
class PhoneNumberValidator:
    @classmethod
    def validate_phone_number(cls, phone: str) -> str:
        cleaned_phone_number = ''.join(filter(str.isdigit, phone))
        if len(cleaned_phone_number) <= 13:
            return cleaned_phone_number
        else:
            raise ValueError("Phone number must contain less than or exactly 13 digits")


#validation  input data contacts
class ContactModel(BaseModel):
    first_name: str = Field(max_length=25) 
    last_name: str = Field(max_length=25)
    email: EmailStr = Field(max_length=30)
    phone: str = Field(max_length=13)
    date_birthday: date

    @validator("phone")
    def validate_phone_number_length(cls, phone):
        return PhoneNumberValidator.validate_phone_number(phone)


#validation  output data contacts
class ContactResponse(ContactModel):
    id: int

    class Config:
        from_attributes = True

#validation  input data users
class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: EmailStr
    password: str = Field(min_length=6, max_length=10)

class UserDb(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime


    class Config:
        from_attributes = True


#validation  output data users
class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"

class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
