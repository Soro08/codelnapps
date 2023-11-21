from django.db.models import F


def increment_user_model_views(
    model3d,
):
    model3d.nb_views = F("nb_views") + 1
    model3d.save(update_fields=["nb_views"])
