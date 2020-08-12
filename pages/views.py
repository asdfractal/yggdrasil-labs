from django.shortcuts import render


def index(request):
    """
    Renders the index view.
    """
    return render(request, "pages/index.html")
