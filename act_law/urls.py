# urls.py
from django.urls import path
from .views import ActLawListView, ActLawCreateView, ActLawUpdateView, ActLawDeleteView

urlpatterns = [
    path('actlaw/', ActLawListView.as_view(), name='actlaw_list'),
    path('actlaw/create/', ActLawCreateView.as_view(), name='actlaw_create'),
    path('actlaw/<int:pk>/update/', ActLawUpdateView.as_view(), name='actlaw_update'),
    path('actlaw/<int:pk>/delete/', ActLawDeleteView.as_view(), name='actlaw_delete'),
]
