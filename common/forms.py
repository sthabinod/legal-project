# forms.py
from django import forms
from .models import Designation

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
