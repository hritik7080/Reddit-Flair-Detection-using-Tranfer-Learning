from django.conf.urls import url
from .views import FileView

urlpatterns = [
    url(r'^automated_testing/$', FileView.as_view(), name='file-upload'),
]