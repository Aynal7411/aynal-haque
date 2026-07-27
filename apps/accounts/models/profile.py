from django.db import models

from apps.common.models import BaseModel


class Profile(BaseModel):

    ROLE_CHOICES = (

        ("admin", "Admin"),

        ("recruiter", "Recruiter"),

        ("client", "Client"),

        ("developer", "Developer"),

        ("student", "Student"),

    )
    """
    User professional profile information.
    """

    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="profile",
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="developer"
    )


    avatar = models.ImageField(
        upload_to="profiles/avatar/",
        blank=True,
        null=True,
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    location = models.CharField(
        max_length=100,
        blank=True,
    )

    website = models.URLField(
        blank=True,
    )

    github = models.URLField(
        blank=True,
    )

    linkedin = models.URLField(
        blank=True,
    )

    twitter = models.URLField(
        blank=True,
    )

    class Meta:
        db_table = "profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.email} Profile"