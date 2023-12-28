from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

# from .models import YourModel  # Replace YourModel with the actual model you are working with

class ActLaw(View):
    template_name = 'act_law/fetch.html'  # Replace 'your_template.html' with your actual template file

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     # Handle POST request logic here
    #     # For example, create a new object based on the form data
    #     data = request.POST.get('your_form_field')  # Replace 'your_form_field' with the actual form field name
    #     YourModel.objects.create(your_field=data)
    #     messages.success(request, "Object created successfully.")
    #     return redirect('actlaw')  # Replace 'actlaw' with the actual URL name or path to redirect to

    # def delete(self, request, *args, **kwargs):
    #     # Handle DELETE request logic here
    #     # For example, delete an object based on the URL parameter
    #     pk = kwargs.get('pk')
    #     instance = get_object_or_404(YourModel, pk=pk)
    #     instance.delete()
    #     messages.success(request, "Object deleted successfully.")
    #     return redirect('actlaw')

    # def put(self, request, *args, **kwargs):
    #     # Handle PUT request logic here
    #     # For example, update an object based on the URL parameter and form data
    #     pk = kwargs.get('pk')
    #     instance = get_object_or_404(YourModel, pk=pk)
    #     data = request.POST.get('your_form_field')  # Replace 'your_form_field' with the actual form field name
    #     instance.your_field = data
    #     instance.save()
    #     messages.success(request, "Object updated successfully.")
    #     return redirect('actlaw')

    # def dispatch(self, request, *args, **kwargs):
    #     # Custom dispatch method to route requests based on HTTP method
    #     if request.method.lower() in self.http_method_names:
    #         handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
    #     else:
    #         handler = self.http_method_not_allowed
    #     return handler(request, *args, **kwargs)
