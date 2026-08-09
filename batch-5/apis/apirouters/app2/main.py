from fastapi import FastAPI
from routers.student import student_router
from Middleware_student.response_time_middle import response_time_middleware

app=FastAPI()
app.add_middleware(response_time_middleware)
app.include_router(student_router)



