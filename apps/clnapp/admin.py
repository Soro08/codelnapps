from django.contrib import admin
from clnapp.models import Badge, Model3d, UserBadge
# Register your models here.

admin.site.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")
    

admin.site.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Model3d)
class Model3dAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "nb_views", "created_at", "updated_at")
    date_hierarchy = ("created_at",)