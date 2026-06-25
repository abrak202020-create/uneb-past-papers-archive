from django.db import models
from django.contrib.auth.models import User
from papers.models import PastPaper


class Download(models.Model):

    paper = models.ForeignKey(
        PastPaper,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paper.subject} {self.paper.year} {self.paper.paper}"