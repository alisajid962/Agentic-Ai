from pydantic import BaseModel
from typing import List,Optional

class StudentModel(BaseModel):
    roll_no:str|int
    name:  str
    courses:List[str]

class StudentUpdateModel(BaseModel):
    roll_no:Optional[str]|None
    name:Optional[str]|None
    courses:Optional[List[str]]|None


