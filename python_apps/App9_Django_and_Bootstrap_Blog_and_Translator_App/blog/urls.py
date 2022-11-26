from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('about/', views.AboutView.as_view(), name='about_view')
]