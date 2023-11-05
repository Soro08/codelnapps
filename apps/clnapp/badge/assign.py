from clnapp.models import Badge, UserBadge


def add_user_bage(user, badge_name):
    """
    assign a badge to a user
    """
    if not user_has_badge(user, badge_name):
        badge = Badge.objects.filter(name=badge_name).first()
        if badge:
            ub = UserBadge(badge=badge, user=user)
            ub.save()
        else:
            print("Badge Not found")


def user_has_badge(user, badge_name):
    """
    Check if the user already has a specific badge
    """
    if UserBadge.objects.filter(badge__name=badge_name, user=user).exists():
        return True
    else:
        return False
