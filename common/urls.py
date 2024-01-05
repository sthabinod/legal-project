# urls.py
from django.urls import path
from .views import DesignationDeleteView, DesignationView, DesignationCreateView, DesignationUpdateView, JudgeCommitteeView, JudgeCommitteeCreateView, JudgeCommitteeUpdateView, JudgeCommitteeDeleteView, DocumentTypeView, DocumentTypeCreateView, DocumentTypeDeleteView, DocumentTypeUpdateView, FiscalYearView, FiscalYearCreateView, FiscalYearDeleteView,FiscalYearUpdateView, OfficeWardView, OfficeWardCreateView, OfficeWardUpdateView, OfficeWardDeleteView

urlpatterns = [
    path('designation/', DesignationView.as_view(), name='designation_list'),
    path('designation/create/', DesignationCreateView.as_view(), name='designation_create'),
    path('designation/<int:pk>/update/', DesignationUpdateView.as_view(), name='designation_update'),
    path('designation/<int:pk>/delete/', DesignationDeleteView.as_view(), name='designation_delete'),
    path('judge_committee/', JudgeCommitteeView.as_view(), name='judge_committee_list'),
    path('judge_committee/create/', JudgeCommitteeCreateView.as_view(), name='judge_committee_create'),
    path('judge_committee/<int:pk>/update/', JudgeCommitteeUpdateView.as_view(), name='judge_committee_update'),
    path('judge_committee/<int:pk>/delete/', JudgeCommitteeDeleteView.as_view(), name='judge_committee_delete'),
    path('document_type/', DocumentTypeView.as_view(), name='document_type_list'),
    path('document_type/create/', DocumentTypeCreateView.as_view(), name='document_type_create'),
    path('document_type/<int:pk>/update/', DocumentTypeUpdateView.as_view(), name='document_type_update'),
    path('document_type/<int:pk>/delete/', DocumentTypeDeleteView.as_view(), name='document_type_delete'),
    path('fiscal_year/', FiscalYearView.as_view(), name='fiscal_year_list'),
    path('fiscal_year/create/', FiscalYearCreateView.as_view(), name='fiscal_year_create'),
    path('fiscal_year/<int:pk>/update/', FiscalYearUpdateView.as_view(), name='fiscal_year_update'),
    path('fiscal_year/<int:pk>/delete/', FiscalYearDeleteView.as_view(), name='fiscal_year_delete'),
    path('office_ward/', OfficeWardView.as_view(), name='office_ward_list'),
    path('office_ward/create/', OfficeWardCreateView.as_view(), name='office_ward_create'),
    path('office_ward/<int:pk>/update/', OfficeWardUpdateView.as_view(), name='office_ward_update'),
    path('office_ward/<int:pk>/delete/', OfficeWardDeleteView.as_view(), name='office_ward_delete'),   
]
