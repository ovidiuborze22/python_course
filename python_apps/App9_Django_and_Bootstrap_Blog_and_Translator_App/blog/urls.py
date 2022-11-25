from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
]