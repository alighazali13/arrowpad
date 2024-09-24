from django.urls import path
from . import views

urlpatterns = [
    path("kiosk/", views.kiosk, name="kiosk"),
    path("kiosk/<str:meta_title>", views.kiosk_detailes, name="kiosk_detailes"),

]
