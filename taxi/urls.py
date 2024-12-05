from django.urls import path

from .views import (
    index,
    ManufacturerView,
    CarListView, CarDetailView,
    DriverListView,
    DriverDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers", ManufacturerView.as_view(), name="manufacturers"),
    path("cars/", CarListView.as_view(), name="cars"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver-detail"),
]

app_name = "taxi"
