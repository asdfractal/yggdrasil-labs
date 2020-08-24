def check_internet_explorer(request):
    head = request.META["HTTP_USER_AGENT"]
    if "Trident" in head:
        return True
    if "MSIE" in head:
        return True
    return False
