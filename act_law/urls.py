# urls.py
from django.urls import path
from .views import ActLawListView, ActLawCreateView, ActLawUpdateView, ActLawDeleteView

urlpatterns = [
    path('', ActLawListView.as_view(), name='actlaw_list'),
    path('create/', ActLawCreateView.as_view(), name='actlaw_create'),
    path('<int:pk>/update/', ActLawUpdateView.as_view(), name='actlaw_update'),
    path('<int:pk>/delete/', ActLawDeleteView.as_view(), name='actlaw_delete'),
]
