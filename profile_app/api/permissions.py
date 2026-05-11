def is_profile_owner(user, profile):
    """Check if the current user owns the profile."""
    return profile.user == user