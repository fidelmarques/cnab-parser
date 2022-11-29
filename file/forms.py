from django import forms

from .models import File


class formularioFile(forms.ModelForm):
    class Meta:
        model = File
        fields = {"file"}

    # file = forms.FileInput()
    # nome = forms.CharField()
    # numero = forms.IntegerField()
