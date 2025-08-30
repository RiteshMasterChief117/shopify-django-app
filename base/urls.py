from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shopify/', include('myshopifyapp.urls')),  # <-- your app urls
    path('shopifytailwind/', include('shopifystore.urls')),  # <-- your app urls
]
