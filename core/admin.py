from django.contrib import admin
from .models import Profile, Post, SiteAlert, Skill, UserProfile, Project


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'title', 'email', 'location')

    fieldsets = (
        ("Basic Info", {
            'fields': ('name', 'title', 'tagline', 'photo')
        }),
        ("Contact Details", {
            'fields': ('email', 'phone', 'location')
        }),
        ("Professional Details", {
            'fields': ('bio', 'resume')
        }),
        ("Social Links", {
            'fields': ('linkedin', 'github', 'twitter', 'website')
        }),
        ("Timestamps", {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'location', 'updated_at')
    list_filter = ('updated_at', 'created_at')
    search_fields = ('user__username', 'user__email', 'location', 'phone')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("User Link", {
            'fields': ('user',)
        }),
        ("Personal Information", {
            'fields': ('bio', 'profile_picture', 'phone', 'location')
        }),
        ("Social & Web Links", {
            'fields': ('linkedin', 'github', 'twitter', 'portfolio')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        # Prevent manual creation, only auto-create on user registration
        return False


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type', 'percentage')
    list_filter = ('skill_type',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(SiteAlert)
class SiteAlertAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_active', 'created_on')
    list_filter = ('is_active', 'created_on')
    search_fields = ('message',)
    readonly_fields = ('created_on',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'url')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)

