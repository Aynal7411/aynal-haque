from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from uuid import uuid4

def profile_photo_upload_path(instance, filename):
    extension = Path(filename).suffix.lower()
    return f"profile/photos/{uuid4().hex}{extension}"


def resume_upload_path(instance, filename):
    extension = Path(filename).suffix.lower()
    return f"profile/resumes/{uuid4().hex}{extension}"


class Profile(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
    )

    title = models.CharField(
        max_length=150,
    )

    tagline = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    bio = models.TextField()

    photo = models.ImageField(
        upload_to=profile_photo_upload_path,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
        default="",
        null= True,
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        default="",
        null= True,
    )

    location = models.CharField(
        max_length=150,
        blank=True,
        default="",
        null= True,
    )

    resume = models.FileField(
        upload_to=resume_upload_path,
        blank=True,
        null=True,
    )

    linkedin = models.URLField(
        blank=True,
        default="",
        null= True,
    )

    github = models.URLField(
        blank=True,
        default="",
        null= True,
    )

    twitter = models.URLField(
        blank=True,
        default="",
        null= True,
    )

    website = models.URLField(
        blank=True,
        default="",
        null= True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        self.title = self.title.strip()
        if self.email:
            self.email = self.email.strip().lower()

        super().save(*args, **kwargs)


class UserProfile(models.Model):
    """Extended user profile for authenticated users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True, help_text="Tell us about yourself")
    profile_picture = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name_plural = "User Profiles"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create UserProfile when a User is created"""
    if created:
        UserProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Automatically save UserProfile when User is saved"""
    try:
        instance.profile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)


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



            
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title      
    



 