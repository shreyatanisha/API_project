from typing import Optional
from fastapi import FastAPI,Path

from schemas1 import Student, UpdateStudent, Patient

app = FastAPI()

#new dictionary to store the data
students = {
    1: {
        "name": "John",
        "age":20,
        "year":"12th"
    }
}
@app.get("/")
def index():
    return {"name": "First data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the Student you want to view", gt=0, lt=3)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return{"Data":"Not Found"} 
 
@app.post("/create-student/{student_id}")
def create_student(student_id: int,student: Student):
    if student_id in students:
        return{"Error" : "student exist"}
    students[student_id] = student
    return students[student_id]

@app.post("/create-patient/{patient_id}")
def create_patient(patient_id: int, patient: Patient):
    if patient_id in students:
        return{"Error" : "patient exist"}
    students[patient_id] = patient
    return students[patient_id]

@app.put("/update-student/{student_id}")
def update_student(student_id:int, student: UpdateStudent):
    if student_id not in students:
        return{"Error":"stuednt does not exist"}

    # students[student_id] = student
    # return students[student_id] 
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
            students[student_id].age = student.age

    if student.year != None:
            students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
          return{"Error":"Student does not exist"}
    del students[student_id]
    return{"Message": "student deleted successfully"}


    
     