from .db import students, faculty

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
        return None
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
