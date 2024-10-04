from django.urls import path
from . import views

urlpatterns = [
    path("kiosk/", views.kiosk, name="kiosk"),
    path("kiosk/<str:url>", views.kiosk_detailes, name="kiosk_detailes"),
    path("souls/", views.souls, name="souls"),
    path("souls/<str:url>", views.souls_detailes, name="souls_detailes"),
    path("fact/", views.fact, name="fact"),
    path("fact/<str:url>", views.fact_detailes, name="fact_detailes"),
    path("microscope/", views.microscope, name="microscope"),
    path("microscope/<str:url>", views.microscope_detailes, name="microscope_detailes"),

]
