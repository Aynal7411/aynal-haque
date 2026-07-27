
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
        verbose_name_plural = "Profile"

    def photo_preview(self):
        if self.photo:
            return format_html(
                '<img src="{}" width="80" height="80" style="border-radius:50%; object-fit:cover;" />',
                self.photo.url,
            )
        return "No Image"

    photo_preview.short_description = "Photo"
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        self.title = self.title.strip()
        if self.email:
            self.email = self.email.strip().lower()

        super().save(*args, **kwargs)

