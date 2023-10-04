from pydantic import Field, BaseModel


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)  # between 0 -> 5
    complete: bool

    # class Config:
    #     json_schema_extra = {
    #         'example': {
    #             'title': 'A new book',
    #             'description': ' a new description of a book',
    #             'priority': 5,
    #             'complete': False
    #         }
    #     }

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number: str


class UsersVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)
class Token(BaseModel):
    access_token: str
    token_type: str