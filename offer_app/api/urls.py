from django.urls import path

from .views import OfferDetailView, OfferViewSet


offer_list = OfferViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

offer_detail = OfferViewSet.as_view(
    {
        "get": "retrieve",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("offers/", offer_list, name="offer-list"),
    path("offers/<int:pk>/", offer_detail, name="offer-detail"),
    path("offerdetails/<int:pk>/", OfferDetailView.as_view(), name="offerdetail"),
]