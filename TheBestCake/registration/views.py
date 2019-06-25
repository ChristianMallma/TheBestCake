from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreationFormWithEmail
from django import forms

# Creando vistas
class SignUpView(CreateView):
    form_class=UserCreationFormWithEmail #usando esta plantilla en la vista de creación
    template_name="registration/signup.html" #renderizando en este template

    def get_success_url(self):
        return reverse_lazy("login")+"?register" #después de registrar se irá aquí

    #Recuperando el formulario y modificandolo en tiempo real
    def get_form(self, form_class=None):
        form=super(SignUpView,self).get_form()

        form.fields["username"].widget=forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Nombre de usuario"})
        form.fields["email"].widget=forms.EmailInput(attrs={"class":"form-control mb-2","placeholder":"Correo electrónico"})
        form.fields["password1"].widget=forms.PasswordInput(attrs={"class":"form-control mb-2","placeholder":"Ingrese Contraseña"})
        form.fields["password2"].widget=forms.PasswordInput(attrs={"class":"form-control mb-2","placeholder":"Confirmar contraseña"})

        return form