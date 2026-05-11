from profile_app.models import UserProfile


def is_business_user(user):
    """Check if the user has a business profile."""
    return hasattr(user, "profile") and user.profile.type == UserProfile.BUSINESS


def is_offer_owner(user, offer):
    """Check if the user owns the offer."""
    return offer.user == user