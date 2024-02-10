# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .forms import CaseSubTypeForm, CaseStageForm, CaseTypeForm
from .models import CaseSubType, CaseStage, CaseType

class CaseSubTypeView(View):
    template_name = 'case/list.html'

    def get(self, request, *args, **kwargs):
        case_subtype_list = CaseSubType.objects.filter(is_deleted=False)
        form = CaseSubTypeForm()
        return render(request, self.template_name, {"case_subtype_list": case_subtype_list,'form': form})

class CaseSubTypeCreateView(View):
    template_name = 'case/list.html'

    def get(self, request, *args, **kwargs):
        form = CaseSubTypeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CaseSubTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('case_subtype_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class CaseSubTypeUpdateView(View):
    template_name = 'act_law/list.html'

    def get(self, request, pk, *args, **kwargs):
        case_subtype = get_object_or_404(CaseSubType, pk=pk)
        form = CaseSubTypeForm(instance=case_subtype)
        return render(request, self.template_name, {'form': form, 'case_subtype': case_subtype})

    def post(self, request, pk, *args, **kwargs):
        case_subtype = get_object_or_404(CaseSubType, pk=pk)
        form = CaseSubTypeForm(request.POST, instance=case_subtype)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('case_subtype_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'case_subtype': case_subtype})

class CaseSubTypeDeleteView(View):
    template_name = 'act_law/list.html' 

    def get(self, request, pk, *args, **kwargs):
        case_subtype = get_object_or_404(CaseSubType, pk=pk)
        return render(request, self.template_name, {'case_subtype': case_subtype})

    def post(self, request, pk, *args, **kwargs):
        act_law = get_object_or_404(CaseSubType, pk=pk)
        act_law.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('case_subtype_list')




class CaseStageView(View):
    template_name = 'case/case_stage.html'

    def get(self, request, *args, **kwargs):
        case_stage_list = CaseStage.objects.filter(is_deleted=False)
        form = CaseStageForm()
        return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})

class CaseStageCreateView(View):
    template_name = 'case/case_stage.html'

    def get(self, request, *args, **kwargs):
        form = CaseStageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CaseStageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('case_stage_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class CaseStageUpdateView(View):
    template_name = 'case/case_stage.html'

    def get(self, request, pk, *args, **kwargs):
        case_stage = get_object_or_404(CaseStage, pk=pk)
        form = CaseStageForm(instance=case_stage)
        return render(request, self.template_name, {'form': form, 'case_stage': case_stage})

    def post(self, request, pk, *args, **kwargs):
        case_stage = get_object_or_404(CaseStage, pk=pk)
        form = CaseSubTypeForm(request.POST, instance=case_stage)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('case_stage_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'case_stage': case_stage})

class CaseStageDeleteView(View):
    template_name = 'case/case_stage.html' 

    def get(self, request, pk, *args, **kwargs):
        case_stage = get_object_or_404(CaseStage, pk=pk)
        return render(request, self.template_name, {'case_stage': case_stage})

    def post(self, request, pk, *args, **kwargs):
        case_stage = get_object_or_404(CaseStage, pk=pk)
        case_stage.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('case_stage_list')


class CaseTypeView(View):
    template_name = 'case/case_type.html'

    def get(self, request, *args, **kwargs):
        case_type_list = CaseType.objects.filter(is_deleted=False)
        form = CaseTypeForm()
        return render(request, self.template_name, {"case_type_list": case_type_list,'form': form})

class CaseTypeCreateView(View):
    template_name = 'case/case_type.html'

    def get(self, request, *args, **kwargs):
        form = CaseTypeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('case_type_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class CaseTypeUpdateView(View):
    template_name = 'case/case_type.html'

    def get(self, request, pk, *args, **kwargs):
        case_type = get_object_or_404(CaseType, pk=pk)
        form = CaseTypeForm(instance=case_type)
        return render(request, self.template_name, {'form': form, 'case_type': case_type})

    def post(self, request, pk, *args, **kwargs):
        case_type = get_object_or_404(CaseType, pk=pk)
        form = CaseTypeForm(request.POST, instance=case_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('case_type_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'case_type': case_type})

class CaseTypeDeleteView(View):
    template_name = 'case/case_type.html' 

    def get(self, request, pk, *args, **kwargs):
        case_type = get_object_or_404(CaseType, pk=pk)
        return render(request, self.template_name, {'case_type':case_type})

    def post(self, request, pk, *args, **kwargs):
        case_type = get_object_or_404(CaseType, pk=pk)
        case_type.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('case_type_list')
    
    
class CaseReportView(View):
    template_name = 'case/report.html'

    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)
    
class CaseReportDetailView(View):
    template_name = 'case/report_detail.html'

    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)
    
class ManageCaseReportView(View):
    template_name = 'case/manage_case_report.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class MailMilapKartaListView(View):
    template_name = 'case/mill_milap_karta_list.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class MailMilapKartaCreateView(View):
    template_name = 'case/mill_milap_karta_create.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)