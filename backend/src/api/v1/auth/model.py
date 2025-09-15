from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class AuthUser(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=7)


class TokenResponse(BaseModel):
    message: str
    access_token: str
    token_type: str = "bearer"


class UserData(BaseModel):
    email: EmailStr
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = Field(None, gt=0 , lt=100, description="Age must be between 0 to 100")
    contact: Optional[str] = None
    city: Optional[str] = None
    pincode: Optional[str] = None
    state: Optional[str] = None
    house_detail: Optional[str] = None


class UserRead(UserData):
    id: int
    

    




