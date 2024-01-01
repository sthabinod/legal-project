# urls.py
from django.urls import path
from .views import DesignationDeleteView, DesignationView, DesignationCreateView, DesignationUpdateView

urlpatterns = [
    path('designation/', DesignationView.as_view(), name='designation_list'),
    path('designation/create/', DesignationCreateView.as_view(), name='designation_create'),
    path('designation/<int:pk>/update/', DesignationUpdateView.as_view(), name='designation_update'),
    path('designation/<int:pk>/delete/', DesignationDeleteView.as_view(), name='designation_delete'),
]
