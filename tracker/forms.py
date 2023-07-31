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

class ExpenseForm(forms.Form):
    expense_form_title = forms.CharField()
    expense_form_category = forms.CharField()
    expense_form_deductible = forms.BooleanField(initial=False)
    expense_form_date = forms.DateField()
    expense_form_amount = forms.DecimalField()
    expense_form_comment = forms.CharField(empty_value=' ')