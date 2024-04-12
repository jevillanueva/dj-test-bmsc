"""
Create model country with city

Country: id, codigo, descripcion, is_active

City: id, id_country, codigo, descripcion, is_active
"""
from django.db import models

# Create your models here.
class Country(models.Model):
    """
    Country model

    Attributes:
    - codigo: str
    - descripcion: str
    - is_active: bool
    """
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
class City(models.Model):
    """
    City model

    Attributes:

    - id_country: Country
    - codigo: str
    - descripcion: str
    - is_active: bool
    """
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
