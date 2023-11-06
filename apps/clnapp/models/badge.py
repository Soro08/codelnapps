from django.contrib.auth.models import User
from django.db import models


class Badge(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="badge/")

    class Meta:
        """Meta definition for Badge."""

        verbose_name = "Badge"
        verbose_name_plural = "Badges"
        ordering = ["id"]

    def __str__(self):
        """Unicode representation of Badge."""
        return self.name


class UserBadge(models.Model):
    """Model definition for UserBadge."""

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    badge = models.ForeignKey(Badge, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    ordering = ["id"]

    class Meta:
        """Meta definition for User Badge."""

        unique_together = ("user", "badge")
        verbose_name = "User Badge"
        verbose_name_plural = "Users Badges"

    def __str__(self):
        """Unicode representation of UserBadge."""
        return f"{self.user.username} : {self.badge.name}"
