from django.forms import ModelForm
from django import forms
from django.forms.widgets import EmailInput,Select,TextInput,NumberInput
from web.models import Contact
from web.models import INTERESTS

EMPTY_INTERESTS = (("","Interested in"),) + INTERESTS

class ContactForm(ModelForm):
    interested_in = forms.ChoiceField(choices = EMPTY_INTERESTS)

    class Meta:
        model = Contact
        fields = "__all__"
        widgets={
            "email":EmailInput(attrs={"placeholder":"Email"}),
            "full_name":TextInput(attrs={"placeholder":"Full name"}),
            "phone":NumberInput(attrs={"placeholder":"Phone"})
        }