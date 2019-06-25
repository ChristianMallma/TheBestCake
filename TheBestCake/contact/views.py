from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form=ContactForm()#crear plantilla vacía
    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)#rellenamos plantilla con los campos
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            
            #Enviamos correo y redireccionamos
            email=EmailMessage(
                "Pastelería Best Cake: Nuevo mensaje de contacto",#asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),#cuerpo
                "no-contestar@inbox.mailtrap.io",#email_origen
                ["christianmichelmallma@gmail.com"],#email_destino
                reply_to=[email]
            )
            try:
                email.send()
                #todo anda bien, redireccionamos a OK
                return redirect(reverse('contact')+'?ok')
            except:
                #algo no anda bien, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail')
            
    return render(request,"contact/contact.html",{'form':contact_form})