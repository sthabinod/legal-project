from django.contrib import admin
from .models import Designation,JudgeCommittee, DocumentType, FiscalYear, OfficeWard

class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','is_deleted')  
    search_fields = ('name',)  


class JudgeCommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','is_deleted')  
    search_fields = ('name',)
      
      
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','is_deleted')  
    search_fields = ('name',)

class OfficeWardAdmin(admin.ModelAdmin):
    list_display = ('ward_no','ward_name', 'status','is_deleted')  
    search_fields = ('name',)

class FiscalYearAdmin(admin.ModelAdmin):
    list_display = ('name','start_date','end_date','status','is_deleted')  
    search_fields = ('name',)  

admin.site.register(JudgeCommittee, JudgeCommitteeAdmin)
admin.site.register(DocumentType,DocumentTypeAdmin)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(FiscalYear,FiscalYearAdmin)
admin.site.register(OfficeWard,OfficeWardAdmin)