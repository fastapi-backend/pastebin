from pydantic import BaseModel


class UserData(BaseModel):
    data: str