from django.db.models.signals import (
    post_save,
)
from django.contrib.auth.models import User
from django.utils import (
    timezone,
)
from clnapp.badge import (
    user_has_badge,
    add_user_bage,
)
from clnapp.models.constants import (
    CONDITION_PIONNEER,
    BADGE_PIONNEER,
)


def user_has_badge_star(sender, instance, created, update_fields=None, **kwargs):
    if update_fields and "last_login" in update_fields:
        one_year_ago = timezone.now() - timezone.timedelta(days=CONDITION_PIONNEER)
        if instance.date_joined >= one_year_ago and not user_has_badge(
            instance,
            BADGE_PIONNEER,
        ):
            add_user_bage(
                instance,
                BADGE_PIONNEER,
            )


post_save.connect(
    user_has_badge_star,
    sender=User,
)
