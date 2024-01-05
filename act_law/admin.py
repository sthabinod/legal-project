from django.contrib import admin
from .models import ActLaw, CourtType

class ActLawAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'status','is_deleted')  
    search_fields = ('name', 'code')  
    
class CourtTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','is_deleted')  
    search_fields = ('name', 'code')  

admin.site.register(ActLaw, ActLawAdmin)
admin.site.register(CourtType, CourtTypeAdmin)
