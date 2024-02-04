# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .forms import ActLawForm, CourtTypeForm
from .models import ActLaw, CourtType

class ActLawListView(View):
    template_name = 'act_law/list.html'

    def get(self, request, *args, **kwargs):
        act_law_list = ActLaw.objects.filter(is_deleted=False)
        form = ActLawForm()
        return render(request, self.template_name, {"act_law_list": act_law_list,'form': form})

class ActLawCreateView(View):
    template_name = 'act_law/list.html'

    def get(self, request, *args, **kwargs):
        form = ActLawForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ActLawForm(request.POST)
        print("here")
        if form.is_valid():
            print("here")
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('actlaw_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class ActLawUpdateView(View):
    template_name = 'act_law/list.html'

    def get(self, request, pk, *args, **kwargs):
        act_law = get_object_or_404(ActLaw, pk=pk)
        form = ActLawForm(instance=act_law)
        return render(request, self.template_name, {'form': form, 'act_law': act_law})

    def post(self, request, pk, *args, **kwargs):
        act_law = get_object_or_404(ActLaw, pk=pk)
        form = ActLawForm(request.POST, instance=act_law)
        if form.is_valid():
            form.save()
            messages.success(request, "Object updated successfully.")
            return redirect('actlaw_list')
        else:
            messages.error(request, "Update form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'act_law': act_law})

class ActLawDeleteView(View):
    template_name = 'act_law/list.html' 

    def get(self, request, pk, *args, **kwargs):
        act_law = get_object_or_404(ActLaw, pk=pk)
        return render(request, self.template_name, {'act_law': act_law})

    def post(self, request, pk, *args, **kwargs):
        act_law = get_object_or_404(ActLaw, pk=pk)
        act_law.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('actlaw_list')


class CourtTypeListView(View):
    template_name = 'act_law/court_type.html'

    def get(self, request, *args, **kwargs):
        court_type_list = CourtType.objects.filter(is_deleted=False)
        form = CourtTypeForm()
        return render(request, self.template_name, {"court_type_list": court_type_list,'form': form})

class CourtTypeCreateView(View):
    template_name = 'act_law/court_type.html'

    def get(self, request, *args, **kwargs):
        form = CourtTypeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CourtTypeForm(request.POST)
        print("here")
        if form.is_valid():
            print("here")
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('court_type_list')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})
class CourtTypeUpdateView(View):
    template_name = 'act_law/court_type.html'

    def get(self, request, pk, *args, **kwargs):
        court_type = get_object_or_404(CourtType, pk=pk)
        form = CourtTypeForm(instance=court_type)
        return render(request, self.template_name, {'form': form, 'court_type':court_type})

    def post(self, request, *args, **kwargs):
        form = CourtTypeForm(request.POST)
        if form.is_valid():
            print("here.............")
            form.save()
            messages.success(request, "Object created successfully.")
            return redirect('court_type_list')
        else:
            print("hereeeeeeeeeeeeeeeeeee")
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form})

class CourtTypeDeleteView(View):
    template_name = 'act_law/court_type.html' 

    def get(self, request, pk, *args, **kwargs):
        court_type = get_object_or_404(CourtType, pk=pk)
        return render(request, self.template_name, {'court_type':court_type})

    def post(self, request, pk, *args, **kwargs):
        court_type = get_object_or_404(CourtType, pk=pk)
        court_type.delete()  
        messages.success(request, "Object deleted successfully.")
        return redirect('court_type_list')
