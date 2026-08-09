from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List

class student(BaseModel):
    roll_no:str
    name:str
    courses:List[str]

class StudentUpdate(BaseModel):
    roll_no: str | None = None
    name: str | None = None
    courses: List[str] | None = None

app=FastAPI()

students={
    "1":{
        "roll_no":"sp24-bse-040",
        "name":"Ali Sajid",
        "courses":["Ai","Web","Math"]
    },
    "2":{
        "roll_no":"sp24-bse-041",
        "name":"Zain Shafeeq",
        "courses":["Dsa","App","Arts"]
    }
}

@app.get("/")
def view():
    return students

@app.post("/create_student")
def create_student(student:student):

    student_id=str(len(students)+1)

    students[student_id]=student.model_dump()

    return {
        "status":"201",
        "Created":students[student_id]
    }

@app.delete("/delete_student/{student_id}")
def delete_student(student_id:str):
    if student_id not in students.keys():
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    
    deleted_student = students.pop(student_id)
    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }

@app.patch("/update_student/{student_id}")
def update_student(student_id: str, student: StudentUpdate):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student_data = student.model_dump(exclude_unset=True)
    print(student_data)

    students[student_id].update(student_data)

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }