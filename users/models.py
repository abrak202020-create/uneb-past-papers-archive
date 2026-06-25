from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = (

        ("ADMIN", "Administrator"),
        ("TEACHER", "Teacher"),
        ("STUDENT", "Student"),

    )

    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE

    )

    role = models.CharField(

        max_length=20,

        choices=ROLE_CHOICES,

        default="STUDENT"

    )

    school = models.CharField(

        max_length=200,

        blank=True

    )

    teaching_subject = models.CharField(

        max_length=100,

        blank=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    def __str__(self):

        return f"{self.user.username} ({self.role})"