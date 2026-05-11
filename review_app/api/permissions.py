from profile_app.models import UserProfile


def is_customer_user(user):
    """Check if the user has a customer profile."""
    return hasattr(user, "profile") and user.profile.type == UserProfile.CUSTOMER


def is_review_owner(user, review):
    """Check if the user created the review."""
    return review.reviewer == user