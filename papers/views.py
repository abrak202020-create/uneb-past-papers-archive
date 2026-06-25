from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import PastPaper
from subjects.models import Subject
from downloads.models import Download

from django.contrib.auth.decorators import login_required
from users.decorators import role_required


# ==========================================
# PAPER LIST
# Admin, Teacher and Student
# ==========================================

@login_required
@role_required("ADMIN", "TEACHER", "STUDENT")
def paper_list(request):

    papers = PastPaper.objects.all().order_by("-uploaded_at")
    subjects = Subject.objects.all()

    search = request.GET.get("search")
    subject = request.GET.get("subject")
    level = request.GET.get("level")
    year = request.GET.get("year")

    if search:
        papers = papers.filter(
            Q(subject__name__icontains=search) |
            Q(paper__icontains=search)
        )

    if subject:
        papers = papers.filter(subject_id=subject)

    if level:
        papers = papers.filter(subject__level=level)

    if year:
        papers = papers.filter(year=year)

    return render(
        request,
        "papers/paper_list.html",
        {
            "papers": papers,
            "subjects": subjects,
            "search": search,
            "role": request.user.userprofile.role,
        }
    )


# ==========================================
# ADD PAPER
# Admin & Teacher
# ==========================================

@login_required
@role_required("ADMIN", "TEACHER")
def add_paper(request):

    subjects = Subject.objects.all()

    if request.method == "POST":

        subject = Subject.objects.get(
            id=request.POST["subject"]
        )

        PastPaper.objects.create(

            subject=subject,
            year=request.POST["year"],
            paper=request.POST["paper"],
            pdf=request.FILES["pdf"],
            description=request.POST["description"]

        )

        return redirect("paper_list")

    return render(
        request,
        "papers/add_paper.html",
        {
            "subjects": subjects
        }
    )


# ==========================================
# EDIT PAPER
# Admin & Teacher
# ==========================================

@login_required
@role_required("ADMIN", "TEACHER")
def edit_paper(request, id):

    paper = get_object_or_404(
        PastPaper,
        id=id
    )

    subjects = Subject.objects.all()

    if request.method == "POST":

        paper.subject = Subject.objects.get(
            id=request.POST["subject"]
        )

        paper.year = request.POST["year"]
        paper.paper = request.POST["paper"]
        paper.description = request.POST["description"]

        if "pdf" in request.FILES:
            paper.pdf = request.FILES["pdf"]

        paper.save()

        return redirect("paper_list")

    return render(
        request,
        "papers/edit_paper.html",
        {
            "paper": paper,
            "subjects": subjects,
        }
    )


# ==========================================
# DELETE PAPER
# ADMIN ONLY
# ==========================================

@login_required
@role_required("ADMIN")
def delete_paper(request, id):

    paper = get_object_or_404(
        PastPaper,
        id=id
    )

    if request.method == "POST":

        paper.delete()

        return redirect("paper_list")

    return render(
        request,
        "papers/delete_paper.html",
        {
            "paper": paper
        }
    )


# ==========================================
# PUBLIC HOME PAGE
# ==========================================

def home(request):

    context = {

        "subjects": Subject.objects.count(),
        "papers": PastPaper.objects.count(),
        "downloads": Download.objects.count(),

        "latest_papers":
        PastPaper.objects.order_by("-uploaded_at")[:3],

    }

    return render(
        request,
        "home.html",
        context
    )


# ==========================================
# PUBLIC SEARCH
# ==========================================

def public_search(request):

    search = request.GET.get("search", "")
    level = request.GET.get("level")

    papers = PastPaper.objects.all()

    if search:

        papers = papers.filter(

            Q(subject__name__icontains=search) |
            Q(paper__icontains=search)

        )

        if search.isdigit():

            papers = papers | PastPaper.objects.filter(
                year=int(search)
            )

        papers = papers.distinct()

    if level:
        papers = papers.filter(
            subject__level=level
        )

    return render(
        request,
        "papers/public_search.html",
        {
            "papers": papers,
            "search": search,
            "level": level,
        }
    )