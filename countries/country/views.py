"""
CRUD (Create, Read, Update, Delete, ver_detalle) for Country and City
"""
from django.shortcuts import render, get_object_or_404, redirect
from .models import Country, City
from .forms import CountryForm

def country_index(request):
    """
    List all countries
    """
    countries = Country.objects.all()
    return render(request, 'country/index.html', {'countries': countries})


def country_new(request):
    """
    Create a new country
    """    
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save()
            return redirect("country:country_detail", country_id=country.id)
    else:
        form = CountryForm()
    return render(request, "country/new.html", {"form": form})

def country_detail(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    return render(request, "country/detail.html", {"country": country})

def country_delete(request, country_id):
    if request.method == "DELETE":
        country = get_object_or_404(Country, pk=country_id)
        country.delete()
    return redirect("country:country_index")

def country_edit(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            country = form.save()
            return redirect("country:country_detail", country_id=country.id)
    else:
        form = CountryForm(instance=country)
    return render(request, "country/edit.html", {"form": form, "country": country})