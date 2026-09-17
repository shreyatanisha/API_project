

from typing import Optional
from fastapi import FastAPI,Path

app = FastAPI()

#new dictionary to store the data
students = {
    1: {
        "name": "John",
        "age":20,
        "class":"12th grade",
    }
}

@app.get("/")
def index():
    return {"name": "First data"}

@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(None,description="The ID of the Student you want to view",gt=0,lt=3) ):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int, name: Optional[str]=None,test:int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return{"Data":"Not Found"}

