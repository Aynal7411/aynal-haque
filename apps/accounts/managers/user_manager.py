from django.contrib.auth.base_user import BaseUserManager
from django.utils.text import slugify


class UserManager(BaseUserManager):
    """
    Custom manager for User model.
    """

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user.
        """

        if not email:
            raise ValueError("Email address is required.")

        email = self.normalize_email(email)
        extra_fields.setdefault("username", self._generate_username(email))

        user = self.model(
            email=email,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            email,
            password,
            **extra_fields,
        )

    def _generate_username(self, email):
        """
        Generate a unique username when registration only supplies an email.
        """
        base_username = slugify(email.split("@", 1)[0]) or "user"
        base_username = base_username[:140]
        username = base_username
        counter = 1

        while self.model.objects.filter(username=username).exists():
            suffix = f"-{counter}"
            username = f"{base_username[:150 - len(suffix)]}{suffix}"
            counter += 1

        return username
