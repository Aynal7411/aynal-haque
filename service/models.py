# core/models.py

from django.db import models
import uuid
from django.core.validators import RegexValidator

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Use Bootstrap icons, e.g., 'bi-code', 'bi-brush'")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


 
class ContactStatus(models.TextChoices):
    NEW = "new", "New"
    READ = "read", "Read"
    REPLIED = "replied", "Replied"
    CLOSED = "closed", "Closed"     

class ContactSource(models.TextChoices):
    WEBSITE = "website", "Website"
    LINKEDIN = "linkedin", "LinkedIn"
    FACEBOOK = "facebook", "Facebook"
    OTHER = "other", "Other"    

class ClientContact(models.Model):
    id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
)
    title = models.CharField(max_length=100,db_index=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True)
    phone = models.CharField(
    max_length=20,
    validators=[
        RegexValidator(
            regex=r'^\+?[\d\s\-]{7,20}$',
            message="Enter a valid phone number."
        )
    ],
    blank=True,
)
    message = models.TextField(
    max_length=3000,
)
    sent_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
    auto_now=True
)
    urgent = models.BooleanField(default=False)
    status = models.CharField(
    max_length=20,
    choices=ContactStatus.choices,
    default=ContactStatus.NEW,
    db_index=True,
)
    ip_address = models.GenericIPAddressField(
    blank=True,
    null=True
)
    read_at = models.DateTimeField(
    blank=True,
    null=True
)
    source = models.CharField(
    max_length=20,
    choices=ContactSource.choices,
    default=ContactSource.WEBSITE
)
    
    class Meta:
        ordering = ['-sent_at']
        verbose_name = "Client Contact"
        verbose_name_plural = "Client Contacts"

    def __str__(self):
        return f"{self.title} - {self.name}"

   

