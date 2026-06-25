from django.urls import path
from .views import choose_account

# Import the REAL signup views
from users.views import student_signup, teacher_signup

urlpatterns = [

    path(
        "register/",
        choose_account,
        name="choose_account",
    ),

    path(
        "register/student/",
        student_signup,
        name="student_signup",
    ),

    path(
        "register/teacher/",
        teacher_signup,
        name="teacher_signup",
    ),

]