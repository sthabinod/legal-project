# forms.py
from django import forms
from .models import ActLaw, CourtType

class ActLawForm(forms.ModelForm):
    class Meta:
        model = ActLaw
        fields = ['name', 'code', 'notes', 'status']

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
            if field_name == 'code':
                field.label = 'कोड'
                field.widget.attrs['placeholder'] = 'कोड प्रविष्ट गर्नुहोस्'
            if field_name == 'notes':
                field.label = 'नोटहरू'
                field.widget.attrs['placeholder'] = 'नोटहरू प्रविष्ट गर्नुहोस्'
            if field_name == 'status':
                field.label = 'स्थिति'
class CourtTypeForm(forms.ModelForm):
    class Meta:
        model = CourtType
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
