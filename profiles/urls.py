from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from profiles.views import (
    UserCreateView,
    UserGetNavigationView,
    UserSetNavigationView,
    UserGetLEDView,
    UserSetLEDView,
)

urlpatterns = [
    path('', UserCreateView.as_view(), name="create"),
    path('navigation/get/', UserGetNavigationView.as_view(), name="get-navigation"),
    path('navigation/set/', UserSetNavigationView.as_view(), name="set-navigation"),
    path('led/get/', UserGetLEDView.as_view(), name="get-led"),
    path('led/set/', UserSetLEDView.as_view(), name="set-led"),
]
