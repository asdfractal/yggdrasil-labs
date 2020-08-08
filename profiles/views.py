from django.shortcuts import render, get_object_or_404


from .models import UserProfile


def profile(request):
    """
    Display the users profile.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        "profile": user_profile,
    }

    return render(request, "dashboard.html", context)
