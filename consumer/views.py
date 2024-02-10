# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import ConsumerForm, PermanentAddressForm, TemporaryAddressForm
from .models import Consumer

class ConsumerView(View):
    template_name = 'consumer/list.html'

    def get(self, request, *args, **kwargs):
        consumer_list = Consumer.objects.all()
        return render(request, self.template_name, {"consumer_list": consumer_list})

class ManageConsumerView(View):
    template_name = 'consumer/manage.html'
    def get(self, request, *args, **kwargs):
        form = ConsumerForm()
        permanent_form = PermanentAddressForm()
        temporary_form = TemporaryAddressForm()
        return render(request, self.template_name, {'form': form, 'permanent_form': permanent_form, 'temporary_form': temporary_form})

    def post(self, request, *args, **kwargs):
        consumer_form = ConsumerForm(request.POST)
        permanent_form = PermanentAddressForm(request.POST)
        temporary_form = TemporaryAddressForm(request.POST)

        if consumer_form.is_valid() and permanent_form.is_valid() and temporary_form.is_valid():
            print(request.POST)  # Print the POST data for debugging purposes

            consumer_instance = consumer_form.save()
            permanent_instance = permanent_form.save(commit=False)
            temporary_instance = temporary_form.save(commit=False)

            # Associate addresses with the consumer
            permanent_instance.consumer = consumer_instance
            temporary_instance.consumer = consumer_instance

            permanent_instance.save()
            temporary_instance.save()

            messages.success(request, "Consumer and addresses created successfully.")
            return redirect('consumer_list')  # Change 'consumer_list' to your actual URL name for the consumer list
        else:
            print(consumer_form.errors, permanent_form.errors, temporary_form.errors)
            messages.error(request, "Form submission failed. Please check the forms.")
            return render(request, self.template_name, {'form': consumer_form, 'permanent_form': permanent_form, 'temporary_form': temporary_form,'ce':consumer_form.errors,'te':permanent_form.errors,'pe': temporary_form.errors})
    
class ConsumerGroupView(View):
    template_name = 'consumer/list_group.html'

    def get(self, request, *args, **kwargs):
        consumer_group = Consumer.objects.all()
        return render(request, self.template_name, {"consumer_group": consumer_group})