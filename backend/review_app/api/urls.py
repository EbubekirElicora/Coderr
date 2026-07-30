from django.urls import path

from .views import ReviewViewSet


review_list = ReviewViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

review_detail = ReviewViewSet.as_view(
    {
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("reviews/", review_list, name="review-list"),
    path("reviews/<int:pk>/", review_detail, name="review-detail"),
]