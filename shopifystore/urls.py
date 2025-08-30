from django.urls import path, include
from shopifystore import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("__reload__/", include("django_browser_reload.urls")),# just an example
]
