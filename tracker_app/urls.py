from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracker_app.views import (
    CompanyViewSet,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
    DeviceListCreateView,
    DeviceRetrieveUpdateDestroyView,
    AssignedDeviceListCreateView,
    AssignedDeviceRetrieveUpdateDestroyView,
)

router = DefaultRouter()
router.register(r"company", CompanyViewSet, basename="company")

urlpatterns = [
    path("", include(router.urls)),
    path("company/<int:company_id>/employees/", EmployeeListCreateView.as_view()),
    path(
        "company/<int:company_id>/employees/<int:emp_id>/",
        EmployeeRetrieveUpdateDestroyView.as_view(),
    ),
    path("company/<int:company_id>/devices/", DeviceListCreateView.as_view()),
    path(
        "company/<int:company_id>/devices/<int:device_id>/",
        DeviceRetrieveUpdateDestroyView.as_view(),
    ),
    path(
        "company/<int:company_id>/assigned-devices/",
        AssignedDeviceListCreateView.as_view(),
    ),
    path(
        "company/<int:company_id>/assigned-devices/<int:device_id>/",
        AssignedDeviceRetrieveUpdateDestroyView.as_view(),
    ),
]
