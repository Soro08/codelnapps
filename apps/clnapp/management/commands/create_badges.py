from django.core.management.base import BaseCommand, CommandError
from clnapp.models import Badge
from clnapp.models.constants import BADGE_COLLECTOR, BADGE_START, BADGE_PIONNEER


class Command(BaseCommand):
    help = "Create default badges"

    def handle(self, *args, **options):
        badges = [
            {"name": BADGE_COLLECTOR, "logo": "badge/collector.png"},
            {"name": BADGE_PIONNEER, "logo": "badge/pionner.png"},
            {"name": BADGE_START, "logo": "badge/star.png"},
        ]
        for badge in badges:
            Badge.objects.get_or_create(
                name=badge.get("name"),
                defaults={
                    "logo": badge.get("logo"),
                },
            )

        self.stdout.write(self.style.SUCCESS("Successfully created badges "))
