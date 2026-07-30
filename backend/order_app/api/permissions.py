from profile_app.models import UserProfile


def is_customer_user(user):
    """Check if the user has a customer profile."""
    return hasattr(user, "profile") and user.profile.type == UserProfile.CUSTOMER


def is_business_user(user):
    """Check if the user has a business profile."""
    return hasattr(user, "profile") and user.profile.type == UserProfile.BUSINESS


def is_order_customer(user, order):
    """Check if the user is the customer of the order."""
    return order.customer_user == user


def is_order_business(user, order):
    """Check if the user is the business owner of the order."""
    return order.business_user == user


def can_see_order(user, order):
    """Check if the user is involved in the order."""
    return is_order_customer(user, order) or is_order_business(user, order)