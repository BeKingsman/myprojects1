from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('details/', views.details, name='details'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.Home.as_view(), name='home'),
]