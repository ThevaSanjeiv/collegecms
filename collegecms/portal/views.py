from django.shortcuts import render,redirect
from .db import students
from .services import CheckUser
# Create your views here.
def getLoginPage(req):
    try:
        user.req.session.get("user")
        if user:
            return redirect(homePage)
        if (req.method=="POST"):
            reqMethod=req.POST
            email=reqMethod.get("email")
            password=reqMethod.get("password")
            if (CheckUser(email)):
                user=students.find_one({"email":email})


    return render(req, 'portal/login.html')
