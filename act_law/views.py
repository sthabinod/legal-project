from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

from .models import ActLaw  

class ActLawView(View):
    template_name = 'act_law/fetch.html'

    def get(self, request, *args, **kwargs):
        act_law = ActLaw.objects.all()[:1]
        print(act_law)
        return render(request, self.template_name,{"data":act_law})

    # def post(self, request, *args, **kwargs):
    #     # Handle POST request logic here
    #     # For example, create a new object based on the form data
    #     data = request.POST.get('your_form_field')  
    #     ActLaw.objects.create(your_field=data)
    #     messages.success(request, "Object created successfully.")
    #     return redirect('actlaw')  

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     instance = get_object_or_404(ActLaw, pk=pk)
    #     instance.delete()
    #     messages.success(request, "Object deleted successfully.")
    #     return redirect('actlaw')

    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     instance = get_object_or_404(ActLaw, pk=pk)
    #     data = request.POST.get('your_form_field')
    #     instance.your_field = data
    #     instance.save()
    #     messages.success(request, "Object updated successfully.")
    #     return redirect('actlaw')
