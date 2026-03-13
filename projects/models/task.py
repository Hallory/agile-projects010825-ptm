from django.core.validators import MinLengthValidator
from django.db import models

from projects.models.project import Project
from projects.models.teg import Teg


class Task(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("canceled", "Canceled"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    title = models.CharField(unique=True, max_length=100, validators=[MinLengthValidator(10)], null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="new")
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    tags = models.ManyToManyField("Tag", blank=True, related_name="tasks")
    due_date = models.DateTimeField(null=True, blank=True)

