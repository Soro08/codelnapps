from django.db.models.signals import (
    post_save,
)

from clnapp.models import (
    Model3d,
)
from clnapp.badge import (
    user_has_badge,
    add_user_bage,
)
from clnapp.models.constants import (
    CONDITION_STAR,
    BADGE_STAR,
)


def assign_badge_star(sender, instance, created, update_fields=None, **kwargs):
    if update_fields and "nb_views" in update_fields:
        # refresh from database
        instance.refresh_from_db()
        if instance.nb_views >= CONDITION_STAR and not user_has_badge(
            instance.author,
            BADGE_STAR,
        ):
            add_user_bage(
                instance.author,
                BADGE_STAR,
            )


post_save.connect(
    assign_badge_star,
    sender=Model3d,
)
