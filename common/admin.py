from django.contrib import admin
from .models import Designation

class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','is_deleted')  
    search_fields = ('name',)  

admin.site.register(Designation, DesignationAdmin)