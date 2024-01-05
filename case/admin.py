from django.contrib import admin
from .models import CaseSubType, CaseStage, CaseType

class CaseTypeAdmin(admin.ModelAdmin):
    list_display = ('name',  'status','is_deleted')  
    search_fields = ('name', 'type') 
    
class CaseStageAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','is_deleted')  
    search_fields = ('name', 'type')   

class CaseStageAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','is_deleted')  
    search_fields = ('name', 'type')   

admin.site.register(CaseType, CaseTypeAdmin)

admin.site.register(CaseSubType, CaseStageAdmin)

admin.site.register(CaseStage, CaseStageAdmin)