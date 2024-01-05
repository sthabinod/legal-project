# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .forms import DesignationForm, JudgeCommitteeForm, DocumentTypeForm, FiscalYearForm, OfficeWardForm
from .models import Designation, JudgeCommittee, DocumentType, FiscalYear, OfficeWard

class DesignationView(View):
    template_name = 'common/designation/list.html'

    def get(self, request, *args, **kwargs):
        designation_list = Designation.objects.filter(is_deleted=False)
        form = DesignationForm()
        return render(request, self.template_name, {"designation_list": designation_list,'form': form})

class DesignationCreateView(View):
    template_name = 'common/designation/list.html'

    def get(self, request, *args, **kwargs):
        form = DesignationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('designation_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class DesignationUpdateView(View):
    template_name = 'common/designation/list.html'

    def get(self, request, pk, *args, **kwargs):
        designation = get_object_or_404(Designation, pk=pk)
        form = DesignationForm(instance=designation)
        return render(request, self.template_name, {'form': form, 'designation': designation})

    def post(self, request, pk, *args, **kwargs):
        designation = get_object_or_404(Designation, pk=pk)
        form = DesignationForm(request.POST, instance=designation)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('designation_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'designation': designation})

class DesignationDeleteView(View):
    template_name = 'common/designation/list.html' 

    def get(self, request, pk, *args, **kwargs):
        designation = get_object_or_404(Designation, pk=pk)
        return render(request, self.template_name, {'designation':designation})

    def post(self, request, pk, *args, **kwargs):
        act_law = get_object_or_404(Designation, pk=pk)
        act_law.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('designation_list')

class JudgeCommitteeView(View):
    template_name = 'common/judge_committee/list.html'

    def get(self, request, *args, **kwargs):
        judge_committee_list = JudgeCommittee.objects.filter(is_deleted=False)
        form = JudgeCommitteeForm()
        return render(request, self.template_name, {"judge_committee_list": judge_committee_list,'form': form})

class JudgeCommitteeCreateView(View):
    template_name = 'common/judge_committee/list.html'

    def get(self, request, *args, **kwargs):
        form = JudgeCommitteeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = JudgeCommitteeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('judge_committee_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class JudgeCommitteeUpdateView(View):
    template_name = 'common/judge_committee/list.html'

    def get(self, request, pk, *args, **kwargs):
        judge_committee = get_object_or_404(JudgeCommittee, pk=pk)
        form = JudgeCommitteeForm(instance=judge_committee)
        return render(request, self.template_name, {'form': form, 'judge_committee': judge_committee})

    def post(self, request, pk, *args, **kwargs):
        judge_committee = get_object_or_404(JudgeCommittee, pk=pk)
        form = JudgeCommitteeForm(request.POST, instance=judge_committee)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('judge_committee_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'judge_committee': judge_committee})

class JudgeCommitteeDeleteView(View):
    template_name = 'common/judge_committee/list.html' 

    def get(self, request, pk, *args, **kwargs):
        judge_committee = get_object_or_404(JudgeCommittee, pk=pk)
        return render(request, self.template_name, {'judge_committee':judge_committee})

    def post(self, request, pk, *args, **kwargs):
        judge_committee = get_object_or_404(JudgeCommittee, pk=pk)
        judge_committee.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('judge_committee_list')

class DocumentTypeView(View):
    template_name = 'common/document_type/list.html'

    def get(self, request, *args, **kwargs):
        document_type_list = DocumentType.objects.filter(is_deleted=False)
        form = DocumentTypeForm()
        return render(request, self.template_name, {"document_type_list": document_type_list,'form': form})

class DocumentTypeCreateView(View):
    template_name = 'common/document_type/list.html'

    def get(self, request, *args, **kwargs):
        form = DocumentType()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = DocumentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('document_type_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class DocumentTypeUpdateView(View):
    template_name = 'common/document_type/list.html'

    def get(self, request, pk, *args, **kwargs):
        document_type = get_object_or_404(Designation, pk=pk)
        form = DocumentTypeForm(instance=document_type)
        return render(request, self.template_name, {'form': form, 'document_type': document_type})

    def post(self, request, pk, *args, **kwargs):
        document_type = get_object_or_404(DocumentType, pk=pk)
        form = DocumentTypeForm(request.POST, instance=document_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('document_type_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'document_type': document_type})

class DocumentTypeDeleteView(View):
    template_name = 'common/document_type/list.html' 

    def get(self, request, pk, *args, **kwargs):
        document_type = get_object_or_404(DocumentType, pk=pk)
        return render(request, self.template_name, {'document_type':document_type})

    def post(self, request, pk, *args, **kwargs):
        document_type = get_object_or_404(DocumentType, pk=pk)
        document_type.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('document_type_list')

class FiscalYearView(View):
    template_name = 'common/fiscal_year/list.html'

    def get(self, request, *args, **kwargs):
        fiscal_year_list = FiscalYear.objects.filter(is_deleted=False)
        form = FiscalYearForm()
        print(fiscal_year_list)
        return render(request, self.template_name, {"fiscal_year_list": fiscal_year_list,'form': form})

class FiscalYearCreateView(View):
    template_name = 'common/fiscal_year/list.html'

    def get(self, request, *args, **kwargs):
        form = FiscalYearForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FiscalYearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('fiscal_year_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class FiscalYearUpdateView(View):
    template_name = 'common/fiscal_year/list.html'

    def get(self, request, pk, *args, **kwargs):
        fiscal_year = get_object_or_404(FiscalYear, pk=pk)
        form = FiscalYearForm(instance=fiscal_year)
        return render(request, self.template_name, {'form': form, 'fiscal_year': fiscal_year})

    def post(self, request, pk, *args, **kwargs):
        fiscal_year = get_object_or_404(FiscalYear, pk=pk)
        form = FiscalYearForm(request.POST, instance=fiscal_year)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('fiscal_year_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'fiscal_year': fiscal_year})

class FiscalYearDeleteView(View):
    template_name = 'common/fiscal_year/list.html' 

    def get(self, request, pk, *args, **kwargs):
        fiscal_year = get_object_or_404(FiscalYear, pk=pk)
        return render(request, self.template_name, {'fiscal_year':fiscal_year})

    def post(self, request, pk, *args, **kwargs):
        fiscal_year = get_object_or_404(FiscalYear, pk=pk)
        fiscal_year.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('fiscal_year_list')

class OfficeWardView(View):
    template_name = 'common/office_ward/list.html'

    def get(self, request, *args, **kwargs):
        office_ward_list = OfficeWard.objects.filter(is_deleted=False)
        form = OfficeWardForm()
        return render(request, self.template_name, {"office_ward_list": office_ward_list,'form': form})

class OfficeWardCreateView(View):
    template_name = 'common/office_ward/list.html'

    def get(self, request, *args, **kwargs):
        form = OfficeWardForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = OfficeWardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('office_ward_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class OfficeWardUpdateView(View):
    template_name = 'common/office_ward/list.html'

    def get(self, request, pk, *args, **kwargs):
        office_ward = get_object_or_404(OfficeWard, pk=pk)
        form = OfficeWardForm(instance=office_ward)
        return render(request, self.template_name, {'form': form, 'office_ward': office_ward})

    def post(self, request, pk, *args, **kwargs):
        office_ward = get_object_or_404(OfficeWard, pk=pk)
        form = OfficeWardForm(request.POST, instance=office_ward)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('office_ward_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'office_ward': office_ward})

class OfficeWardDeleteView(View):
    template_name = 'common/office_ward/list.html' 

    def get(self, request, pk, *args, **kwargs):
        office_ward = get_object_or_404(OfficeWardForm, pk=pk)
        return render(request, self.template_name, {'office_ward':office_ward})

    def post(self, request, pk, *args, **kwargs):
        fiscal_year = get_object_or_404(OfficeWard, pk=pk)
        fiscal_year.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('office_ward_list')