from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import single_contact
from .forms import contact_form


def home(request):
    contacts = single_contact.objects.all()
    return render(request, 'contact_info_list.html', {"contacts":contacts})

def add_contact(request):
    if request.method == "POST":
        form  = contact_form(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('home')
    else:
        form = contact_form()
        return render(request, "add_contact.html", {"form": form})

    return render(request,'add_contact.html')

def update_contact(request):
    return render(request,'update_contact.html')

def delete_contact(request):
    return render(request,'delete_contact.html')

def others(request):
    return render(request,'others.html')