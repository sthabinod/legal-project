# urls.py
from django.urls import path
from .views import (
    CaseSubTypeDeleteView,
    CaseSubTypeView,
    CaseSubTypeCreateView,
    CaseSubTypeUpdateView,
    CaseStageCreateView,
    CaseStageUpdateView,
    CaseStageDeleteView,
    CaseStageView,
    CaseTypeCreateView,
    CaseTypeDeleteView,
    CaseTypeUpdateView,
    CaseTypeView,
    CaseReportView,
    CaseReportDetailView,
    ManageCaseReportView
)

urlpatterns = [
    path('case_subtype/', CaseSubTypeView.as_view(), name='case_subtype_list'),
    path('case_subtype/create/', CaseSubTypeCreateView.as_view(), name='case_subtype_create'),
    path('case_subtype/<int:pk>/update/', CaseSubTypeUpdateView.as_view(), name='case_subtype_update'),
    path('case_subtype/<int:pk>/delete/', CaseSubTypeDeleteView.as_view(), name='case_subtype_delete'),
    path('case_stage/', CaseStageView.as_view(), name='case_stage_list'),
    path('case_stage/create/', CaseStageCreateView.as_view(), name='case_stage_create'),
    path('case_stage/<int:pk>/update/', CaseStageUpdateView.as_view(), name='case_stage_update'),
    path('case_stage/<int:pk>/delete/', CaseStageDeleteView.as_view(), name='case_stage_delete'),
    path('case_type/', CaseTypeView.as_view(), name='case_type_list'),
    path('case_type/create/', CaseTypeCreateView.as_view(), name='case_type_create'),
    path('case_type/<int:pk>/update/', CaseTypeUpdateView.as_view(), name='case_type_update'),
    path('case_type/<int:pk>/delete/', CaseTypeDeleteView.as_view(), name='case_type_delete'),
    path('case_report/', CaseReportView.as_view(), name='case_report_list'),
    path('case_report_detail/', CaseReportDetailView.as_view(), name='case_report_detail'),
    path('manage_case_report/', ManageCaseReportView.as_view(), name='manage_case_report'),
]
