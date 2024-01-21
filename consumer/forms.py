import json
from django import forms
from .models import Consumer, PermanentAddress, TemporaryAddress
from nepali_datetime_field.forms import NepaliDateField, NepaliDateInput

def get_choices_from_json(json_file_path, key):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        return [(item, item) for item in data.get(key, [])]

class ConsumerForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    citizenship_issue_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    citizenship_issue_district = forms.ChoiceField(
        choices=get_choices_from_json('static/json/district.json','districts'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )

    class Meta:
        model = Consumer
        fields = '__all__'
# id_age
    def __init__(self, *args, **kwargs):
        super(ConsumerForm, self).__init__(*args, **kwargs)

        # Add the 'form-control' class to all fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['id'] = f'permanent_{field_name}'
            self.fields['age'].widget.attrs['readonly'] = True
            

class PermanentAddressForm(forms.ModelForm):
    state = forms.ChoiceField(
        choices=get_choices_from_json('static/json/states.json', 'states'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )
    
    district = forms.ChoiceField(
        choices=get_choices_from_json('static/json/district.json', 'districts'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )
    
    municipality = forms.ChoiceField(
        choices=get_choices_from_json('static/json/municipality.json', 'municipality'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )
    
    ward = forms.ChoiceField(
        choices=get_choices_from_json('static/json/ward.json', 'ward'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )

    class Meta:
        model = PermanentAddress
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(PermanentAddressForm, self).__init__(*args, **kwargs)
        self.fields['consumer'].required = False
            
            
class TemporaryAddressForm(forms.ModelForm):
    state = forms.ChoiceField(
        choices=get_choices_from_json('static/json/states.json', 'states'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )
    
    district = forms.ChoiceField(
        choices=get_choices_from_json('static/json/district.json', 'districts'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )
    
    municipality = forms.ChoiceField(
        choices=get_choices_from_json('static/json/municipality.json', 'municipality'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )
    
    ward = forms.ChoiceField(
        choices=get_choices_from_json('static/json/ward.json', 'ward'),
        widget=forms.Select(attrs={'class': 'select form-control'})
    )

    class Meta:
        model = TemporaryAddress
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(TemporaryAddressForm, self).__init__(*args, **kwargs)
        self.fields['consumer'].required = False