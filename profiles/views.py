from django.shortcuts import render, get_object_or_404


from .models import UserProfile


def profile(request, profile_id):
    """
    Display the users profile.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user, id=profile_id)

    context = {
        "profile": user_profile,
    }

    return render(request, "dashboard.html", context)
