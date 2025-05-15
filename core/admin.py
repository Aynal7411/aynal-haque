from django.contrib import admin
from .models import Profile
from .models import Post
from .models import SiteAlert
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

from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type', 'percentage')
    list_filter = ('skill_type',)
    search_fields = ('name',)


admin.site.register(Post)


admin.site.register(SiteAlert)