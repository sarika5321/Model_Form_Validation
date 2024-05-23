from django import forms
from app.models import *
import re

class credForm(forms.ModelForm):
    class Meta:
        model = credential
        fields = '__all__'
        
    def clran_pno(self):
        pno = self.cleaned_data.get('pno')
        if re.match(r"(?:\+91 ?)?[6-9]\d{9}",pno):
            return pno
        return None
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.match(r"[A-Za-z]+\.?\w*\@[a-zA-Z]+\.[a-zA-Z]{2,3}", email):
            return email
        return None