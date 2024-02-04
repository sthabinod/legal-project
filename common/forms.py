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
            if field_name == 'name':
                field.label = 'नाम'
                field.widget.attrs['placeholder'] = 'नाम प्रविष्ट गर्नुहोस्'
            if field_name == 'notes':
                field.label = 'नोटहरू'
                field.widget.attrs['placeholder'] = 'नोटहरू प्रविष्ट गर्नुहोस्'
            if field_name == 'status':
                field.label = 'स्थिति'

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

            if field_name == 'name':
                field.label = 'नाम'
                field.widget.attrs['placeholder'] = 'नाम प्रविष्ट गर्नुहोस्'
            if field_name == 'notes':
                field.label = 'नोटहरू'
                field.widget.attrs['placeholder'] = 'नोटहरू प्रविष्ट गर्नुहोस्'
            if field_name == 'status':
                field.label = 'स्थिति'
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

            if field_name == 'name':
                field.label = 'नाम'
                field.widget.attrs['placeholder'] = 'नाम प्रविष्ट गर्नुहोस्'    
            if field_name == 'start_date':
                field.label = 'नोटहरू'
                field.widget.attrs['placeholder'] = 'नोटहरू प्रविष्ट गर्नुहोस्'
            if field_name == 'end_date':
                field.label = 'सुरु मिति'
                field.widget.attrs['placeholder'] = 'सुरु मिति प्रविष्ट गर्नुहोस्'
            if field_name == 'notes':
                field.label = 'अन्तिम मिति'
                field.widget.attrs['placeholder'] = 'अन्तिम मिति प्रविष्ट गर्नुहोस्'
            if field_name == 'status':
                field.label = 'स्थिति'
        
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
            
            if field_name == 'name':
                field.label = 'नाम'
                field.widget.attrs['placeholder'] = 'नाम प्रविष्ट गर्नुहोस्'
          
            if field_name == 'status':
                field.label = 'स्थिति'

        

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
            if field_name == 'ward_no':
                field.label = 'वडा नं'
                field.widget.attrs['placeholder'] = 'वडा नं प्रविष्ट गर्नुहोस्'
            if field_name == 'ward_name':
                field.label = 'वडा कार्यलयको नाम'
                field.widget.attrs['placeholder'] = 'वडा कार्यलयको नाम प्रविष्ट गर्नुहोस्'
            if field_name == 'status':
                field.label = 'स्थिति'


