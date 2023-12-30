# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .forms import ActLawForm
from .models import ActLaw

class ActLawListView(View):
    template_name = 'act_law/list.html'

    def get(self, request, *args, **kwargs):
        act_law_list = ActLaw.objects.all()
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
            messages.error(request, "Form submission failed. Please check the form.")
            return render(request, self.template_name, {'form': form, 'act_law': act_law})

class ActLawDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        act_law = get_object_or_404(ActLaw, pk=pk)
        act_law.delete()
        messages.success(request, "Object deleted successfully.")
        return redirect('actlaw_list')
