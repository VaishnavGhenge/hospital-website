from django import forms
from site_.models import contact_us, hospital_details, doctor_details

class Contact_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = "__all__"

class Hospital_form(forms.ModelForm):
    class Meta:
        model = hospital_details
        fields = "__all__"

class Doctor_form(forms.ModelForm):
    class Meta:
        model = doctor_details
        fields = "__all__"