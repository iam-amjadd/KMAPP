from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Agentprofile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class AgentProfileEditForm(forms.ModelForm):
    CSS_class = "form-control col-md-7 col-xs-12"
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": CSS_class
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": CSS_class
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": CSS_class
            }
        )
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control has-feedback-left",
                "placeholder": "Date of birth",
                "aria-describedby": "inputSuccess2Status3",
            }
        )
    )
    gender = forms.ChoiceField(
        choices=Agentprofile.gender_choices,
        widget=forms.RadioSelect(
            attrs={
                "class": "btn-group",
            }
        ),
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": CSS_class
            }
        )
    )
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "3"
            }
        )
    )
    job_position = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": CSS_class
            }
        )
    )
    department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": CSS_class
            }
        )
    )
    employment_start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control has-feedback-left",
                "placeholder": "Date of birth",
                "aria-describedby": "inputSuccess2Status3",
            }
        )
    )
    supervisor = forms.CharField(
        widget=forms.TextInput(
            attrs={
            "class": CSS_class
            }
        )
    )
    salary = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
            "class": CSS_class
            }
        )
    )
    skills = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "tags form-control",
                "name": "skills"
            }
        )
    )
    education = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "3"
            }
        )
    )
    experience = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "3"
            }
        )
    )
    emergency_contact_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": CSS_class
            }
        )
    )
    emergency_contact_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": CSS_class
            }
        )
    )

    class Meta:
        model = Agentprofile
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.user:
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["email"].initial = self.instance.user.email

    def save(self, commit=True):
        agent_profile = super().save(commit=False)
        if agent_profile.user:
            agent_profile.user.first_name = self.cleaned_data["first_name"]
            agent_profile.user.last_name = self.cleaned_data["last_name"]
            agent_profile.user.email = self.cleaned_data["email"]
            agent_profile.user.save()
        if commit:
            agent_profile.save()
        return agent_profile
