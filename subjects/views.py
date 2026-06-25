from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from users.decorators import role_required


# ==========================================
# List All Subjects
# ==========================================

@role_required("ADMIN", "TEACHER")
def subject_list(request):

    subjects = Subject.objects.all().order_by("name")

    return render(
        request,
        "subjects/subject_list.html",
        {
            "subjects": subjects
        }
    )


# ==========================================
# Add Subject
# ==========================================

@role_required("ADMIN")
def add_subject(request):

    if request.method == "POST":

        Subject.objects.create(
            name=request.POST["name"],
            code=request.POST["code"],
            level=request.POST["level"],
            description=request.POST["description"],
        )

        return redirect("subject_list")

    return render(
        request,
        "subjects/add_subject.html"
    )


# ==========================================
# Edit Subject
# ==========================================

@role_required("ADMIN")
def edit_subject(request, id):

    subject = get_object_or_404(
        Subject,
        id=id
    )

    if request.method == "POST":

        subject.name = request.POST["name"]
        subject.code = request.POST["code"]
        subject.level = request.POST["level"]
        subject.description = request.POST["description"]

        subject.save()

        return redirect("subject_list")

    return render(
        request,
        "subjects/edit_subject.html",
        {
            "subject": subject
        }
    )


# ==========================================
# Delete Subject
# ==========================================

@role_required("ADMIN")
def delete_subject(request, id):

    subject = get_object_or_404(
        Subject,
        id=id
    )

    if request.method == "POST":

        subject.delete()

        return redirect("subject_list")

    return render(
        request,
        "subjects/delete_subject.html",
        {
            "subject": subject
        }
    )