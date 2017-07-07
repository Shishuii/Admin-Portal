from django import forms
from .models import Assessment
from .choices import *

class Assessment_Form(forms.ModelForm):
    Profile=forms.ChoiceField(choices = PROFILE_CHOICES, label="Profile", initial='', widget=forms.Select(), required=True)
    Primary_category=forms.ChoiceField(choices = CATEGORY_CHOICES, label="Primary_category", initial='', widget=forms.Select(), required=True)
    class Meta:
        model = Assessment
        fields = ["Profile","Primary_category","assessment_name"]
