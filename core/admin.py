from django.contrib import admin
from .models import Profile,  Skill, UserProfile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
        "photo_preview",
        "updated_at",
    )

    readonly_fields = (
        "photo_preview",
        "created_at",
        "updated_at",
    )


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



from .models import (
    Technology,
    ProjectCategory,
    Project,
    ProjectImage,
    ProjectFeature,
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "featured",
        "project_type",
        "created_at",
    )

    list_filter = (
        "status",
        "featured",
        "project_type",
        "difficulty",
        "category",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "technologies",
    )

    inlines = [
        ProjectFeatureInline,
        ProjectImageInline,
    ]


admin.site.register(ProjectCategory)
admin.site.register(Technology)
