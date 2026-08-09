from fastapi import APIRouter,HTTPException
from config.student_data import students
from models.student_model import StudentModel,StudentUpdateModel

student_router=APIRouter(
    prefix="/student",
    tags=["Student_Router"]
)



@student_router.get("/")
def view():
    return  students

@student_router.post("/create_student")
def create_student(student_data:StudentModel):

    student_id=str(len(students)+1)
    students[student_id]=student_data.model_dump()

    return{
        "status":"201",
        "Created":students[student_id]
    }

@student_router.patch("/edit_student/{student_id}")
def edit_student(student_id:str,update_data:StudentUpdateModel):
    if student_id in students:
        updated_data=update_data.model_dump(exclude_unset=True)
        print(updated_data)
        students[student_id].update(updated_data)
        return   {
            "status":"200",
            "message":students[student_id]
        }
    else:
        return HTTPException(status_code=404,)
        


       

        

@student_router.delete("/delete_student/{student_id}")
def delete_student(student_id:str):
    if student_id in students:
        del students[student_id]
        return {
            "status":"200",
            "message":"Student deleted",
            "data":students[student_id]
        }
    else:
        raise HTTPException(
            status_code=404
        )

    