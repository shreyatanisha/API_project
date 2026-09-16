# #from fastapi importing the fastapi module
# from fastapi import FastAPI

# # we are creating an instance of the object so we can access this laterin the code
# app = FastAPI() 

# #here we are using the get method for getting the information or to show the output in the browser
# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

from fastapi import FastAPI

from app.schemas import User

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Voting eligibility API is running"}


@app.post("/check-vote")
def check_vote(user: User):
    if user.age >= 18:
        return {
            "name": user.name,
            "age": user.age,
            "eligible": True,
            "message": "You are eligible to vote"
        }

    return {
        "name": user.name,
        "age": user.age,
        "eligible": False,
        "message": "You are not eligible to vote"
    }

