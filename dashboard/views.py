from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from users.decorators import role_required

from subjects.models import Subject
from papers.models import PastPaper
from downloads.models import Download


# ==========================================
# ADMIN & TEACHER DASHBOARD
# ==========================================

@login_required
@role_required("ADMIN", "TEACHER")
def dashboard(request):

    # Statistics
    subjects = Subject.objects.count()
    papers = PastPaper.objects.count()
    downloads = Download.objects.count()
    users = User.objects.count()

    # Papers by Level
    ple = PastPaper.objects.filter(subject__level="PLE").count()
    uce = PastPaper.objects.filter(subject__level="UCE").count()
    uace = PastPaper.objects.filter(subject__level="UACE").count()

    # Recent Papers
    recent_papers = (
        PastPaper.objects
        .select_related("subject")
        .order_by("-id")[:5]
    )

    # Recent Downloads
    recent_downloads = (
        Download.objects
        .select_related(
            "paper",
            "paper__subject",
            "user"
        )
        .order_by("-downloaded_at")[:5]
    )

    context = {

        "subjects": subjects,
        "papers": papers,
        "downloads": downloads,
        "users": users,

        "ple": ple,
        "uce": uce,
        "uace": uace,

        "recent_papers": recent_papers,
        "recent_downloads": recent_downloads,

        # Logged in user
        "role": request.user.userprofile.role,
        "user": request.user,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )