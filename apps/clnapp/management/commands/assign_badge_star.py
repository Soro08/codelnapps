from django.core.management.base import (
    BaseCommand,
)
from django.db.models import (
    Subquery,
    OuterRef,
)

from clnapp.badge import (
    add_user_bage,
)
from clnapp.models import (
    Model3d,
    UserBadge,
)
from clnapp.models.constants import (
    CONDITION_STAR,
    BADGE_STAR,
)


class Command(BaseCommand):
    help = "This command awards the star badge to all users whose 3d models has been viewed more than 1000 times."

    def handle(self, *args, **options):
        pass
        # users_with_star_badge = UserBadge.objects.filter(
        #     badge__name=BADGE_STAR,
        #     user=OuterRef("author"),
        # ).values("user")

        # model3ds = Model3d.objects.annotate(has_star_badge=Subquery(users_with_star_badge)).filter(
        #     nb_views__gte=CONDITION_STAR,
        #     has_star_badge=None,
        # )

        # for m3d in model3ds:
        #     add_user_bage(
        #         m3d.author,
        #         BADGE_STAR,
        #     )

        # self.stdout.write(self.style.SUCCESS("badge distribués."))
