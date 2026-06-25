from django.urls import path
from . import views

urlpatterns = [

    path("", views.login_view, name="login"),

    path("logout/", views.logout_view, name="logout"),

path(
    "register/student/",
    views.student_signup,
    name="student_signup",
),

path(
    "register/teacher/",
    views.teacher_signup,
    name="teacher_signup",
),
]