from django.shortcuts import render,redirect

# Create your views here.
def getLoginPage(req):
    return render(req, 'portal/login.html')
