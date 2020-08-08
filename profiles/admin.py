from django.contrib import admin
from .models import UserProfile


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ("user", "is_client")


admin.site.register(UserProfile, ProfilesAdmin)