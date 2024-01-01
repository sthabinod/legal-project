from django.contrib import admin
from .models import CaseSubType, CaseStage

class CaseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status','is_deleted')  
    search_fields = ('name', 'type') 
    
class CaseStageAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','is_deleted')  
    search_fields = ('name', 'type')   

admin.site.register(CaseSubType, CaseTypeAdmin)

admin.site.register(CaseStage, CaseStageAdmin)