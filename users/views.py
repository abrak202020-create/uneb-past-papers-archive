from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import UserProfile


# ==========================================
# LOGIN
# ==========================================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Create a profile automatically if one doesn't exist
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    "role": "ADMIN" if user.is_superuser else "STUDENT"
                }
            )

            login(request, user)

            if profile.role == "ADMIN":
                return redirect("dashboard")

            elif profile.role == "TEACHER":
                return redirect("dashboard")

            elif profile.role == "STUDENT":
                return redirect("paper_list")

            else:
                messages.error(
                    request,
                    "Your account has no valid role assigned."
                )
                logout(request)
                return redirect("login")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "login.html")


# ==========================================
# LOGOUT
# ==========================================

def logout_view(request):

    logout(request)

    return redirect("login")

# ==========================================
# STUDENT SIGN UP
# ==========================================

def student_signup(request):

    if request.method == "POST":

        form = StudentSignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.save()

            profile = user.userprofile
            profile.role = "STUDENT"
            profile.school = form.cleaned_data["school"]
            profile.save()

            messages.success(
                request,
                "Student account created successfully. Please login."
            )

            return redirect("login")

    else:

        form = StudentSignUpForm()

        print(form)
        print(type(form))

    return render(

        request,

        "accounts/student_signup.html",

        {

            "form": form,

        }

    )


# ==========================================
# TEACHER SIGN UP
# ==========================================

def teacher_signup(request):

    if request.method == "POST":

        form = TeacherSignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.save()

            profile = user.userprofile
            profile.role = "TEACHER"
            profile.school = form.cleaned_data["school"]
            profile.teaching_subject = form.cleaned_data["teaching_subject"]
            profile.save()

            messages.success(
                request,
                "Teacher account created successfully. Please login."
            )

            return redirect("login")

    else:

        form = TeacherSignUpForm()

    return render(

        request,

        "accounts/teacher_signup.html",

        {

            "form": form,

        }

    )