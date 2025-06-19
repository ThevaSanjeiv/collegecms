from  django.urls import path
from . import views

urlpatterns = [
    path("",views.getLoginPage,name="login"),
    path("StudentDashboard",views.StudentDashboard,name="StudentDashboard"),
    path("FacultyDashboard",views.FacultyDashboard,name="FacultyDashboard"),
    path("logout",views.logout,name="logout"),
    path("AdminDashboard",views.AdminDashboard,name="AdminDashboard")
]