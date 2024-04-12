"""
CRUD (Create, Read, Update, Delete, ver_detalle) for Country and City
"""
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Country, City
from .forms import CountryForm, CityForm

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

def city_index(request, country_id):
    """
    List all cities of an country
    """
    country = get_object_or_404(Country, pk=country_id)
    cities = City.objects.filter(id_country=country_id)
    return render(request, 'city/index.html', {'country': country,'cities': cities})

def city_new(request, country_id):
    """
    Create a new city
    """    
    country = get_object_or_404(Country, pk=country_id)
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.id_country = country
            city.save()
            return redirect("country:city_index", country_id=country.id)
    else:
        form = CityForm()
    return render(request, "city/new.html", {"form": form, "country": country})

def city_detail(request, country_id, city_id):
    country = get_object_or_404(Country, pk=country_id)
    city = get_object_or_404(City, pk=city_id)
    return render(request, "city/detail.html", {"country": country, "city": city})

def city_delete(request, country_id, city_id):
    if request.method == "DELETE":
        country = get_object_or_404(Country, pk=country_id)
        city = get_object_or_404(City, pk=city_id)
        city.delete()
    return redirect("country:city_index", country_id=country_id)