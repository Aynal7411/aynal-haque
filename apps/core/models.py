from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from uuid import uuid4
from django.utils.html import format_html



class Skill(models.Model):
    SKILL_TYPES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('database', 'Database'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES, default='other')

    def __str__(self):
        return f"{self.name} - {self.get_skill_type_display()} ({self.percentage}%)"


class ProjectStatus(models.TextChoices):
    PLANNING = "planning", "Planning"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"
    MAINTENANCE = "maintenance", "Maintenance"
    ARCHIVED = "archived", "Archived"


class DifficultyLevel(models.TextChoices):
    BEGINNER = "beginner", "Beginner"
    INTERMEDIATE = "intermediate", "Intermediate"
    ADVANCED = "advanced", "Advanced"


class ProjectType(models.TextChoices):
    PERSONAL = "personal", "Personal"
    CLIENT = "client", "Client"
    OPEN_SOURCE = "open_source", "Open Source"


class ProjectRole(models.TextChoices):
    BACKEND = "backend", "Backend Developer"
    FRONTEND = "frontend", "Frontend Developer"
    FULLSTACK = "fullstack", "Full Stack Developer"
    ML = "ml", "Machine Learning Engineer"
    AI = "ai", "AI Engineer"


# =====================================================
# Technology
# =====================================================

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    icon = models.ImageField(
        upload_to="technology/icons/",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


# =====================================================
# Category
# =====================================================

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"

    def __str__(self):
        return self.name


# =====================================================
# Project
# =====================================================

class Project(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="projects",
    )

    technologies = models.ManyToManyField(
        Technology,
        related_name="projects",
        blank=True,
    )

    short_description = models.CharField(max_length=300)

    description = models.TextField()

    thumbnail = models.ImageField(
        upload_to="projects/thumbnails/"
    )

    github_url = models.URLField(blank=True)

    live_url = models.URLField(blank=True)

    documentation_url = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.COMPLETED,
    )

    difficulty = models.CharField(
        max_length=20,
        choices=DifficultyLevel.choices,
        default=DifficultyLevel.INTERMEDIATE,
    )

    project_type = models.CharField(
        max_length=20,
        choices=ProjectType.choices,
        default=ProjectType.PERSONAL,
    )

    role = models.CharField(
        max_length=20,
        choices=ProjectRole.choices,
        default=ProjectRole.BACKEND,
    )

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


# =====================================================
# Project Gallery
# =====================================================

class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="projects/gallery/"
    )

    alt_text = models.CharField(
        max_length=200,
        blank=True,
    )

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"{self.project.title} Image"


# =====================================================
# Project Features
# =====================================================

class ProjectFeature(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="features",
    )

    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Project Feature"
        verbose_name_plural = "Project Features"

    def __str__(self):
        return self.title

 