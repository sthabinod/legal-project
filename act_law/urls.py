# urls.py
from django.urls import path
from .views import ActLawListView, ActLawCreateView, ActLawUpdateView, ActLawDeleteView, CourtTypeCreateView, CourtTypeDeleteView, CourtTypeListView, CourtTypeUpdateView

urlpatterns = [
    path('', ActLawListView.as_view(), name='actlaw_list'),
    path('create/', ActLawCreateView.as_view(), name='actlaw_create'),
    path('<int:pk>/update/', ActLawUpdateView.as_view(), name='actlaw_update'),
    path('<int:pk>/delete/', ActLawDeleteView.as_view(), name='actlaw_delete'),
    path('court_type', CourtTypeListView.as_view(), name='court_type_list'),
    path('court_type/create/', CourtTypeCreateView.as_view(), name='court_type_create'),
    path('court_type/<int:pk>/update/', CourtTypeUpdateView.as_view(), name='court_type_update'),
    path('court_type/<int:pk>/delete/', CourtTypeDeleteView.as_view(), name='court_type_delete'),
]
