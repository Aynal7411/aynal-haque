from core.models import Skill


def get_grouped_top_skills(limit=3):
    """
    Return top skills grouped by skill type.
    """
    return {
        label: Skill.objects.filter(
            skill_type=key,
        ).order_by(
            "-percentage",
        )[:limit]
        for key, label in Skill.SKILL_TYPES
    }