from django.shortcuts import render,redirect
from .db import students
from .services import checkUser
# Create your views here.
def getLoginPage(req):
    try:
        user_session=req.session.get("user")
        role_session=req.session.get("role")
        if user_session and role_session:
            if role_session=="faculty":
                return redirect("FacultyDashboard")
            elif role_session=="student":
                return redirect("StudentDashboard")
        if req.method=="POST":
            reqMethod=req.POST
            email=reqMethod.get("email")
            password=reqMethod.get("password")
            user=checkUser(email)
            if user and user.get("password")==password:
                req.session["user"]=user["email"]
                req.session["role"]=user["role"]
                if user["role"]=="faculty":
                    return redirect("FacultyDashboard")
                elif user["role"]=="student":
                    return redirect("StudentDashboard")
            else:
                return render(req,"portal/login.html",{"error":"Invalid Credentials"})
        return render(req,"portal/login.html")
    except Exception as e:
        print(f"Error while checking:{e}")
        return render(req,"portal/login.html",{"error":"Error Occured while Login"})

def FacultyDashboard(req):
    return render(req,"portal/faculty.html")

def StudentDashboard(req):
    return render(req,"portal/student.html")
            
def logout(req):
    try:
        req.session.flush()
        return redirect('loginPage')
    except Exception as e:
        print(f"Error occurred while logging out: {e}")
        return redirect('login')
