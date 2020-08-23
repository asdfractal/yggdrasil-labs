def verify_purchase(user_profile, order_model, product):
    """
    Verify user has purchased a product, return boolean.
    """
    user_orders = order_model.objects.filter(user_profile=user_profile)
    for order in user_orders:
        for item in order.lineitems.all():
            if item.product == product:
                return True
    return False
