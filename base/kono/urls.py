from django.urls import path
from kono.views import index

app_name = "kono"

urlpatterns = [
    path("", index, name="index"),
]
