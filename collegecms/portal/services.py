from .db import students, faculty,admin

def checkUser(email):
    try:
        user = students.find_one({"email": email})
        if user:
            user["role"] = "student"
            return user
        user = faculty.find_one({"email": email})
        if user:
            user["role"] = "faculty"
            return user
        user=admin.find_one({"email":email})
        if user:
            user["role"]=="admin"
            return user
        return None
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
