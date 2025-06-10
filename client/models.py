from django.db import models

TRADE_ROLE_CHOICES = [
    ('buyer', 'Buyer'),
    ('seller', 'Seller'),
    ('both', 'Both'),
]

class BusinessUser(models.Model):
    country = models.CharField(max_length=100)
    trade_role = models.CharField(max_length=10, choices=TRADE_ROLE_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # hashed later
    company_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    agree_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.email
