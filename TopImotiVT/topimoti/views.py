from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from TopImotiVT.topimoti.models import Property


def get_properties():
    return Property.objects.all()


def get_rent_properties():
    return Property.objects.filter(property_type='rent')


def get_sale_properties():
    return Property.objects.filter(property_type='sale')


def get_property(pk):
    return Property.objects.filter(pk=pk).get()


def home(request):
    properties = get_properties()
    context = {
        'properties': properties
    }
    return render(request, 'home.html', context)


def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = "Ново съобщение от контактната форма"
        body = f"Име: {name}\nEmail: {email}\n\nСъобщение:\n{message}"

        try:
            send_mail(
                subject,
                body,
                email,
                ["topimotivt@abv.bg"],
                fail_silently=False,
            )
            messages.success(request, "Съобщението беше изпратено успешно.")

        except Exception as e:
            messages.error(request, "Грешка при изпращане на съобщението.")

        return redirect("send_email")

    return render(request, "contact.html")


def see_sale_properties(request):
    sale_properties = get_sale_properties()
    context = {
        'sale_properties': sale_properties
    }

    return render(request, 'sale.html', context)


def see_rent_properties(request):
    rent_properties = get_rent_properties()
    context = {
        'rent_properties': rent_properties
    }

    return render(request, 'rent.html', context)


def property_details(request, pk):

    property = get_property(pk)

    context = {
        'property': property,
    }

    return render(request, 'property-details.html', context)







