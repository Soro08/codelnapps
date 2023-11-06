from django.contrib.auth.models import (
    User,
)
from django.db import models


class Model3d(models.Model):
    """Model definition for Model3d."""

    title = models.CharField(max_length=200)
    description = models.TextField(
        null=True,
        blank=True,
    )
    file = models.FileField(upload_to="model/")
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    nb_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Model3d."""

        verbose_name = "Model3d"
        verbose_name_plural = "Model3ds"
        ordering = ["-created_at"]

    def __str__(self):
        """Unicode representation of Model3d."""
        return self.title
