def increment_user_model_views(
    model3d,
):
    model3d.nb_views = model3d.nb_views + 1
    model3d.save()
