# forms.py
from django import forms
from .models import Designation, JudgeCommittee, DocumentType, FiscalYear, OfficeWard

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['name', 'notes', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'id_' + field_name
            field.label_from_instance = lambda obj: obj.label_tag(attrs={'for': 'id_' + field_name})
            field.widget.attrs['placeholder'] = f"Enter {field.label.lower()}"

        self.fields['status'].widget.attrs['class'] = 'select'
        self.fields['status'].widget.attrs['placeholder'] = 'Select status'

class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['name', 'notes', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'id_' + field_name
            field.label_from_instance = lambda obj: obj.label_tag(attrs={'for': 'id_' + field_name})
            field.widget.attrs['placeholder'] = f"Enter {field.label.lower()}"

        self.fields['status'].widget.attrs['class'] = 'select'
        self.fields['status'].widget.attrs['placeholder'] = 'Select status'
        
class FiscalYearForm(forms.ModelForm):
    class Meta:
        model = FiscalYear
        fields = ['name', 'start_date', 'end_date', 'notes', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'id_' + field_name
            field.label_from_instance = lambda obj: obj.label_tag(attrs={'for': 'id_' + field_name})
            field.widget.attrs['placeholder'] = f"Enter {field.label.lower()}"

        self.fields['status'].widget.attrs['class'] = 'select'
        self.fields['status'].widget.attrs['placeholder'] = 'Select status'
        
class JudgeCommitteeForm(forms.ModelForm):
    class Meta:
        model = JudgeCommittee
        fields = ['name', 'image', 'designation', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'id_' + field_name
            field.widget.attrs['placeholder'] = f"Enter {field.label.lower()}"

        if 'designation' in self.fields:
            designation_field = self.fields['designation']
            if hasattr(designation_field, 'queryset'):
                designation_field.widget.attrs['class'] = 'select'
                designation_field.widget.attrs['placeholder'] = 'Select designation'
                designation_field.label_from_instance = lambda obj: obj.name  # Adjust based on your Designation model

        if 'status' in self.fields:
            status_field = self.fields['status']
            if hasattr(status_field, 'queryset'):
                status_field.widget.attrs['class'] = 'select'
                status_field.widget.attrs['placeholder'] = 'Select status'
                status_field.label_from_instance = lambda obj: obj.name  

class OfficeWardForm(forms.ModelForm):
    class Meta:
        model = OfficeWard
        fields = ['ward_no', 'ward_name', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'id_' + field_name
            field.label_from_instance = lambda obj: obj.label_tag(attrs={'for': 'id_' + field_name})
            field.widget.attrs['placeholder'] = f"Enter {field.label.lower()}"

        self.fields['status'].widget.attrs['class'] = 'select'
        self.fields['status'].widget.attrs['placeholder'] = 'Select status'

