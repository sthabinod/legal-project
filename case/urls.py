# urls.py
from django.urls import path
from .views import CaseSubTypeDeleteView, CaseSubTypeView, CaseSubTypeCreateView, CaseSubTypeUpdateView,CaseStageCreateView,CaseStageUpdateView,CaseStageDeleteView, CaseStageView

urlpatterns = [
    path('case_subtype', CaseSubTypeView.as_view(), name='case_subtype_list'),
    path('case_subtype/create/', CaseSubTypeCreateView.as_view(), name='case_subtype_create'),
    path('case_subtype/<int:pk>/update/', CaseSubTypeUpdateView.as_view(), name='case_subtype_update'),
    path('case_subtype/<int:pk>/delete/', CaseSubTypeDeleteView.as_view(), name='case_subtype_delete'),
    path('case_stage', CaseStageView.as_view(), name='case_stage_list'),
    path('case_stage/create/', CaseStageCreateView.as_view(), name='case_stage_create'),
    path('case_stage/<int:pk>/update/', CaseStageUpdateView.as_view(), name='case_stage_update'),
    path('case_stage/<int:pk>/delete/', CaseStageDeleteView.as_view(), name='case_stage_delete'),
]
