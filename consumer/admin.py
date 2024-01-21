from django.contrib import admin
from .models import Consumer

@admin.register(Consumer)
class AdminConsumer(admin.ModelAdmin):
    list_display = ('full_name',  'birth_date','age','gender','email_address','mobile_number','citizenship_no','citizenship_issue_district','citizenship_issue_date','grandfather_name','father_name')  
    search_fields = ('full_name', 'email_address', 'phone_number') 