from django.contrib.auth.models import User
from django.db import models


class Badge(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="badge/")

    class Meta:
        """Meta definition for Model3d."""

        verbose_name = "Model3d"
        verbose_name_plural = "Model3ds"

    def __str__(self):
        """Unicode representation of Model3d."""
        return self.name


class UserBadge(models.Model):
    """Model definition for UserBadge."""

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    badge = models.ForeignKey(Badge, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for User Badge."""

        verbose_name = "User Badge"
        verbose_name_plural = "Users Badges"

    def __str__(self):
        """Unicode representation of UserBadge."""
        return f"{self.user.username} : {self.badge.name}"
