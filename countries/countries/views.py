"""Index view for the countries app."""

from django.shortcuts import redirect


def index(request):
    return redirect("country:country_index")