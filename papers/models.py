from django.db import models
from subjects.models import Subject


class PastPaper(models.Model):

    PAPER_CHOICES = [
        ("Paper 1", "Paper 1"),
        ("Paper 2", "Paper 2"),
        ("Paper 3", "Paper 3"),
        ("Practical", "Practical"),
    ]

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    year = models.PositiveIntegerField()

    paper = models.CharField(
        max_length=20,
        choices=PAPER_CHOICES
    )

    pdf = models.FileField(
        upload_to="past_papers/"
    )

    description = models.TextField(blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject.name} - {self.year} - {self.paper}"