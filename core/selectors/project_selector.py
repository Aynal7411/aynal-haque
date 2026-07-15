from core.models import Project


def get_featured_projects(limit=3):
    """
    Return projects for the home page.
    """
    return Project.objects.all()[:limit]