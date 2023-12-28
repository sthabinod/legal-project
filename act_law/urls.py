from django.urls import path
from . import views

urlpatterns = [
    path("",views.ActLaw.as_view(),name="get_act_law")
]
