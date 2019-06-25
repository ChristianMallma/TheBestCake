from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Creando formulario para el registro
class UserCreationFormWithEmail(UserCreationForm):
    email=forms.EmailField(required=True, help_text="Requerido 254 caracteres como máximo y debe ser válido")

    #Extendemos el email
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    #Validando que el usuario sea único con su email
    def clean_email(self):
        email=self.cleaned_data.get("email") #rescatando los emails
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email ya existe, pruebe con otro.")
        return email
        