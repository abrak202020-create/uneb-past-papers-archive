from django.contrib import admin
from .models import PastPaper


@admin.register(PastPaper)
class PastPaperAdmin(admin.ModelAdmin):

    list_display = (
        "subject",
        "year",
        "paper",
        "uploaded_at",
    )

    search_fields = (
        "subject__name",
        "year",
    )

    list_filter = (
        "subject",
        "year",
    )