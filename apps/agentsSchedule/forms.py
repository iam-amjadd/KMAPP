from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Agentshift, Shift

class AgentshiftForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset = User.objects.filter(is_staff=False),
        empty_label = "...",
        widget = forms.Select(attrs={'class': 'select2_single form-control'})
    )
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control has-feedback-left',
                'placeholder':'Date',
                'aria-describedby':'inputSuccess2Status3'
            }
        )
    )
    shifts = forms.ModelChoiceField(
        queryset = Shift.objects.all(),
        empty_label = "...",
        widget = forms.Select(attrs={'class': 'select2_single form-control'})
    )
    class Meta:
        model = Agentshift
        fields = ['user','date', 'shifts']