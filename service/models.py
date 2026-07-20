# core/models.py

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Use Bootstrap icons, e.g., 'bi-code', 'bi-brush'")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

        
class ClientContact(models.Model):
    STATUS_CHOICES = [
    ("new", "New"),
    ("read", "Read"),
    ("replied", "Replied"),
    ("closed", "Closed"),
]
    SOURCE_CHOICES = [
    ("website", "Website"),
    ("linkedin", "LinkedIn"),
    ("facebook", "Facebook"),
    ("other", "Other"),
]
    
    title = models.CharField(max_length=100,db_index=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True)
    phone = models.CharField(
    max_length=20,
    blank=True,
    null=True
)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
    auto_now=True
)
    urgent = models.BooleanField(default=False)
    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="new"
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
    choices=SOURCE_CHOICES,
    default="website"
)
    
    class Meta:
        ordering = ['-sent_at']
        verbose_name = "Client Contact"
        verbose_name_plural = "Client Contacts"

    def __str__(self):
        return f"{self.title} - {self.name}"

   

