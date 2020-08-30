from django.contrib import admin
from .models import UserProfile


class ProfilesAdmin(admin.ModelAdmin):
    """
    Display and modify user profile in admin panel.
    """

    list_display = ("user", "is_client")

    readonly_fields = ("personal_key",)


admin.site.register(UserProfile, ProfilesAdmin)
