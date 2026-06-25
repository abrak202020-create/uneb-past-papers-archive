from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required

from users.decorators import role_required

from .models import Download
from papers.models import PastPaper


# ==========================================
# DOWNLOAD PAPER
# ADMIN • TEACHER • STUDENT
# ==========================================

@login_required
@role_required("ADMIN", "TEACHER", "STUDENT")
def download_paper(request, id):

    paper = get_object_or_404(
        PastPaper,
        id=id
    )

    Download.objects.create(

        paper=paper,
        user=request.user

    )

    return redirect(
        paper.pdf.url
    )


# ==========================================
# DOWNLOAD HISTORY
# ==========================================

@login_required
@role_required("ADMIN", "TEACHER", "STUDENT")
def download_list(request):

    role = request.user.userprofile.role

    if role == "ADMIN":

        downloads = Download.objects.select_related(

            "paper",
            "paper__subject",
            "user"

        ).order_by("-downloaded_at")

    else:

        downloads = Download.objects.select_related(

            "paper",
            "paper__subject",
            "user"

        ).filter(

            user=request.user

        ).order_by("-downloaded_at")

    return render(

        request,

        "downloads/download_list.html",

        {

            "downloads": downloads,
            "role": role,

        }

    )