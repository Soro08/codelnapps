from django.db.models.signals import post_save
from clnapp.badge import user_has_badge, add_user_bage
from clnapp.models.constants import BADGE_COLLECTOR, CONDITION_COLLECTOR
from clnapp.models import Model3d


def user_has_collecter(sender, instance, created, update_fields=None, **kwargs):
    """
    Vérifier si l'utilisateur a plus de 5 model3d
    lui attribuler le badge Collector
    - compter le nombre de models
    - si le nbr model est >= 5
        - vérifier si l'utilisateur n'a pas de badge collector,
        lui attribuer le bage
        - sinon, passer
    - sinon passer
    """
    if created:
        nb = instance.author.model3d_set.count()
        if nb >= CONDITION_COLLECTOR and not user_has_badge(
            instance.author, BADGE_COLLECTOR
        ):
            add_user_bage(instance.author, BADGE_COLLECTOR)


post_save.connect(user_has_collecter, sender=Model3d)
