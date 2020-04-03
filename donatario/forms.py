from django import forms
from donatario.models import Grantee

class GranteeForm(forms.ModelForm):
    class Meta:
        model = Grantee
        exclude = ['data', 'atendido']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'