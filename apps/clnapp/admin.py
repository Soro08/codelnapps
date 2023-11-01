from django.contrib import admin
from clnapp.models import Badge, Model3d, UserBadge
# Register your models here.


class BadgeAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")
    


class UserBadgeAdmin(admin.ModelAdmin):
    pass


class Model3dAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "nb_views", "created_at", "updated_at")


admin.site.register(Badge, BadgeAdmin)
admin.site.register(UserBadge, UserBadgeAdmin)
admin.site.register(Model3d, Model3dAdmin)