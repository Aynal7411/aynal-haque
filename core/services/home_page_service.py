from django.utils import timezone

from core.selectors.profile_selector import get_primary_profile
from core.selectors.project_selector import get_featured_projects
from core.selectors.skill_selector import get_grouped_top_skills


def build_home_page_context():
    """
    Build the complete presentation context for the home page.
    """
    return {
        "profile": get_primary_profile(),
        "grouped_skills": get_grouped_top_skills(limit=3),
        "projects": get_featured_projects(limit=3),
        "year": timezone.now().year,
    }