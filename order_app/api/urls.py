from django.urls import path

from .views import (
    CompletedOrderCountView,
    OrderCountView,
    OrderViewSet,
)


order_list = OrderViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

order_detail = OrderViewSet.as_view(
    {
        "get": "retrieve",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("orders/", order_list, name="order-list"),
    path("orders/<int:pk>/", order_detail, name="order-detail"),
    path(
        "order-count/<int:business_user_id>/",
        OrderCountView.as_view(),
        name="order-count",
    ),
    path(
        "completed-order-count/<int:business_user_id>/",
        CompletedOrderCountView.as_view(),
        name="completed-order-count",
    ),
]