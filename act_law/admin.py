from django.contrib import admin
from .models import ActLaw

class ActLawAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'status','is_deleted')  
    search_fields = ('name', 'code')  

admin.site.register(ActLaw, ActLawAdmin)