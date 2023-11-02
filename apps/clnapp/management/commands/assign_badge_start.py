from django.core.management.base import BaseCommand, CommandError
from django.db.models import Subquery, OuterRef

from clnapp.badge import add_user_bage
from clnapp.models import Model3d, UserBadge
from clnapp.models.constants import CONDITION_START, BADGE_START


class Command(BaseCommand):
    help = "A description of the command"

    def handle(self, *args, **options):
        users_with_star_badge = UserBadge.objects.filter(
            badge__name=BADGE_START, user=OuterRef("author")
        ).values("user")

        model3ds = Model3d.objects.annotate(
            has_star_badge=Subquery(users_with_star_badge)
        ).filter(nb_views__gte=CONDITION_START, has_star_badge=None)

        for m3d in model3ds:
            add_user_bage(m3d.author, BADGE_START)
