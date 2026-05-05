# User Profile Management System

## Overview

This Django application now includes a comprehensive user profile management system that allows users to register, login, manage their profiles, and securely manage their accounts.

## Features

### 1. **User Registration**
- Enhanced registration form with email validation
- Password strength requirements:
  - Minimum 8 characters
  - Must contain letters and numbers
  - Real-time validation feedback
- Email uniqueness verification
- Automatic UserProfile creation on registration

**URL:** `/register/`

### 2. **User Login**
- Simple and secure login system
- Session management
- Protection against invalid credentials
- Failed login attempt tracking (via django-axes)

**URL:** `/login/`

### 3. **User Profile View**
- Display comprehensive user information:
  - Profile picture
  - First and last name
  - Email address
  - Phone number
  - Location
  - Bio/about section
  - Social media links (LinkedIn, GitHub, Twitter)
  - Portfolio/Website link
- Display membership date and last update timestamp
- Quick links to edit profile, change password, and delete account

**URL:** `/profile/`
**Access:** Login required

### 4. **Profile Edit**
- Update personal information:
  - First name and last name
  - Email address
  - Phone number
  - Location
  - Bio
  - Profile picture upload
- Add/update social media links:
  - LinkedIn profile
  - GitHub profile
  - Twitter profile
  - Portfolio website
- Form validation for URLs
- Image upload with size validation

**URL:** `/profile/edit/`
**Access:** Login required

### 5. **Password Management**
- Change password securely:
  - Verify current password before allowing change
  - Strong password validation for new password
  - Confirmation password matching
  - Session update after password change (prevents logout)
- Password requirements displayed
- Security guidelines provided

**URL:** `/profile/change-password/`
**Access:** Login required

### 6. **Account Deletion**
- Permanent account deletion with confirmation
- Clear warning about consequences
- One-click confirmation to proceed
- Automatic logout after deletion
- Irreversible action

**URL:** `/profile/delete/`
**Access:** Login required

### 7. **User Logout**
- Secure session termination
- Confirmation message
- Redirect to home page

**URL:** `/logout/`

## Database Models

### UserProfile Model
Extends Django's built-in User model with additional fields:

```python
class UserProfile(models.Model):
    user = OneToOneField(User)
    bio = TextField()
    profile_picture = ImageField()
    phone = CharField()
    location = CharField()
    linkedin = URLField()
    github = URLField()
    twitter = URLField()
    portfolio = URLField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
```

**Key Features:**
- Automatically created when a new User is registered (via Django signals)
- One-to-one relationship with Django User model
- Fields are optional (except user relationship) for flexibility

## URL Routes

| URL | View | Required Auth | Description |
|-----|------|---------------|-------------|
| `/register/` | register_view | No | User registration |
| `/login/` | login_view | No | User login |
| `/logout/` | logout_view | Yes | User logout |
| `/profile/` | profile_view | Yes | View user profile |
| `/profile/edit/` | profile_edit | Yes | Edit user profile |
| `/profile/change-password/` | password_change_view | Yes | Change password |
| `/profile/delete/` | profile_delete_confirm | Yes | Delete account |

## Navigation

The navbar has been updated with a user dropdown menu when logged in:

```
User Avatar/Username (dropdown)
├── My Profile
├── Edit Profile
├── Change Password
└── Logout
```

When not logged in:
```
├── Login
└── Register
```

## Forms

### UserRegistrationForm
Enhanced registration form with:
- Username field with validation
- Email field with uniqueness check
- Password field with strength requirements
- Password confirmation field
- Help text for all fields

### UserProfileForm
For editing user profile with:
- First name, last name, email fields
- Bio textarea
- Profile picture file upload
- Phone, location, social media URL fields
- Auto-save user details to Django User model

### UserPasswordChangeForm
For password changes with:
- Old password verification
- New password strength validation
- Password confirmation matching
- Error messages for each field

## Security Features

1. **Login Protection**
   - `@login_required` decorators on protected views
   - Automatic redirect to login page for unauthenticated users
   - After login, redirects to profile (not home)

2. **Password Security**
   - Minimum 8 characters
   - Must contain letters and numbers
   - Old password verification before change
   - Session update after password change (prevents logout)

3. **Form Validation**
   - Server-side validation on all forms
   - Email uniqueness check
   - URL format validation for social links
   - File size validation for image upload

4. **Account Protection**
   - Confirmation required for account deletion
   - Clear warnings about irreversible actions
   - Automatic logout after deletion

5. **Failed Login Attempts**
   - Tracked via django-axes
   - User locked out after 5 failed attempts
   - 1-hour cooloff period
   - Custom lockout template

## Static Assets

- Profile pictures stored in `/media/user_profiles/`
- Uploaded resumes in `/media/resumes/`

## Admin Management

UserProfile models can be managed through Django admin:
- List all user profiles with filters
- Search by username, email, location, or phone
- Edit individual profiles
- View creation and update timestamps
- Manual creation disabled (only auto-create on registration)

## Usage Examples

### For Users

1. **Register a new account:**
   - Click "Register" in navbar
   - Fill in username, email, and strong password
   - Click "Register"
   - Auto-redirected to profile after login

2. **Login:**
   - Click "Login" in navbar
   - Enter username and password
   - Click "Login"
   - Redirected to profile

3. **Edit profile:**
   - Click user dropdown → "Edit Profile"
   - Update any fields
   - Upload profile picture (optional)
   - Save changes

4. **Change password:**
   - Click user dropdown → "Change Password"
   - Enter current password
   - Enter new password twice
   - Save changes

5. **Delete account:**
   - Click user dropdown → (no direct link, must go via profile settings)
   - Or navigate to `/profile/delete/`
   - Read warnings carefully
   - Click "Delete Permanently"

### For Developers

To check if a user is logged in in templates:
```django
{% if user.is_authenticated %}
  <p>Welcome, {{ user.username }}!</p>
  <a href="{% url 'profile' %}">View Profile</a>
{% else %}
  <a href="{% url 'login' %}">Login</a>
{% endif %}
```

To access user profile data in views:
```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    user_profile = request.user.profile
    return render(request, 'template.html', {'profile': user_profile})
```

## Deployment Considerations

1. **Media Files:** Ensure `/media/` directory is properly configured in production
2. **Static Files:** Run `python manage.py collectstatic` before deploying
3. **File Uploads:** Configure max upload size in web server (nginx/Apache)
4. **Email Validation:** Optional - could add email confirmation in future
5. **Password Reset:** Consider adding forgot password functionality in future
6. **HTTPS:** Always use HTTPS in production for login/password pages

## Future Enhancements

- [ ] Email verification on registration
- [ ] Password reset via email
- [ ] Social login (Google, GitHub, etc.)
- [ ] Two-factor authentication (2FA)
- [ ] Profile visibility settings (public/private)
- [ ] User activity log
- [ ] Account preferences and notifications
- [ ] Profile badges and achievements
- [ ] User search and discovery

## Error Handling

All forms include comprehensive error handling:
- Form validation errors displayed per field
- User-friendly error messages
- Suggestions for fixing common errors
- No sensitive information exposed in errors

## Testing

To test the profile system:

```bash
# Create a test user
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('testuser', 'test@example.com', 'TestPass123')

# Test login
# Visit /login/ and enter credentials

# Test profile view
# Visit /profile/ after logging in

# Test profile edit
# Visit /profile/edit/ and update information

# Test password change
# Visit /profile/change-password/

# Test account deletion
# Visit /profile/delete/ (careful!)
```

## Support

For issues or questions about the profile system:
1. Check Django documentation: https://docs.djangoproject.com/
2. Review the models in `core/models.py`
3. Check the views in `core/views.py`
4. Review form validation in `core/forms.py`

---

**Last Updated:** May 5, 2026
**Status:** Production Ready
