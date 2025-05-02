from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_email', views.send_email, name='send_email'),

    path('sale', views.see_sale_properties, name='sale'),
    path('rent', views.see_rent_properties, name='rent'),

    path('properties/', include([
        path('details/<int:pk>/', views.property_details, name='property_details'),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)