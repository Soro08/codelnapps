from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from clnapp.badge import add_user_bage
from clnapp.models import UserBadge
from clnapp.models.constants import CONDITION_PIONNEER, BADGE_PIONNEER


class Command(BaseCommand):
    help = "A description of the command"

    def handle(self, *args, **options):
        one_year_ago = timezone.now() - timedelta(days=CONDITION_PIONNEER)
        self.stdout.write("My sample command just ran.")

        users_without_pioneer_badge = User.objects.filter(
            date_joined__lt=one_year_ago
        ).exclude(
            id__in=UserBadge.objects.filter(badge__name="pionnier").values("user")
        )

        for user in users_without_pioneer_badge:
            add_user_bage(user, BADGE_PIONNEER)
