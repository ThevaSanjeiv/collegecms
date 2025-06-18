from .db import students
def CheckUser(email):
    try:
        user=students.find_one({"email":email})
        return True if user else False
    except Exception as e:
        print(f"Error while checking {e}")
