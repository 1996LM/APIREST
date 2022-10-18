
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#los ... quieren decir que puedo mandar cualquier cosa pero qeu es obligatorio mandarlo

class UserBase(BaseModel):
    email:EmailStr = Field(
        ...,
        example = 'lmiguel.hoyos@udea.edu.co'
    ) 

    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example = 'nombreUsuario10'
    )

class User(UserBase):
    id: int = Field(
        ...,
        example = '5'
    )
    
class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        ejemplo = 'contrasena'
    )