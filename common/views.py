# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .forms import DesignationForm
from .models import Designation

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
