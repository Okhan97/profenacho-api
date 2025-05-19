# app/main.py
from fastapi import FastAPI, Header, HTTPException, Depends
from app.firebase import auth, db

app = FastAPI()

def verify_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/me")
def get_user(user=Depends(verify_token)):
    return {"uid": user["uid"], "email": user["email"]}

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World!"}

@app.get("/students")
def get_all_students(user=Depends(verify_token)):
    students_ref = db.collection("students")
    docs = students_ref.stream()
    students = []
    for doc in docs:
        user_data = doc.to_dict()
        user_data["id"] = doc.id
        students.append(user_data)
    return {"students": students}