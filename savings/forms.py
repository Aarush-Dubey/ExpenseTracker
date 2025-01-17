
from django import forms
from .models import SavingGoal

class SavingGoalForm(forms.ModelForm):
    class Meta:
        model = SavingGoal
        fields = ['name', 'target_amount', 'amount_saved', 'target_date', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter goal name'}),
            'target_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter target amount'}),
            'amount_saved': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount saved'}),
            'target_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
        }

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter deposit amount'}))
