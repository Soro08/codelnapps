from clnapp.models import Badge, UserBadge


def add_user_bage(user, badge_name):
    """
    Ajouter un badge à un utilisateur
    """
    badge = Badge.objects.filter(name=badge_name).first()
    if badge:
        ub = UserBadge(badge=badge, user=user)
        ub.save()
    else:
        print("Badge Not found")


def user_has_badge(user, badge_name):
    """
    Vérifier si l'utilisateur à déjà un badge donné
    """
    if UserBadge.objects.filter(badge__name=badge_name, user=user).exists():
        return True
    else:
        return False
