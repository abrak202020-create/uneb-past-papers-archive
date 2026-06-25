from django.db import models

class Subject(models.Model):
    LEVEL_CHOICES = [
        ('PLE', 'PLE'),
        ('UCE', 'UCE'),
        ('UACE', 'UACE'),
    ]

    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name