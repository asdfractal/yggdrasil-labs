def check_internet_explorer(request):
    """
    Check if the browser is internet explorer and return boolean.
    """
    head = request.META["HTTP_USER_AGENT"]
    if "Trident" in head:
        return True
    if "MSIE" in head:
        return True
    return False
