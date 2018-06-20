from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from profiles.views import (
    UserCreateView,
)

urlpatterns = {
    url(r'^$', UserCreateView.as_view(), name="create"),
    }

urlpatterns = format_suffix_patterns(urlpatterns)
