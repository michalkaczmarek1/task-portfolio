from django.urls import path
from .views import homepage, about_me, contact

urlpatterns = [
    path("", homepage),
    path("me/", about_me),
    path("contact/", contact),
]
