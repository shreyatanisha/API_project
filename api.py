# from fastapi import FastAPI 

# from schemas import User

# app = FastAPI()

# @app.get("/")
# def func():
#     return {"message": "hello world"}

# @app.post("/check-vote")
# def check_vote(user: User):
#     if user.age >=18:
#         return{
#             "name" : user.name,
#             "age": user.age,
#             "eligible":True,
#             "msg": "You are eligible to vote"
#         }

from fastapi import FastAPI

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
def get_student(student_id: int):
    return students.get(student_id)
