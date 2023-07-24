from django import forms
from . import models

##
# Add Bootstrap Class
##
class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control form-control-lg'
            })

class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control form-control-lg'
            })
            
class BudgetForm(forms.Form):
    budget_amount = forms.IntegerField()
    budget_periodic = forms.IntegerField(max_value=2)