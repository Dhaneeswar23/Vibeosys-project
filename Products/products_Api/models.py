from django.db import models

# Create your models here.
from django.db import models

class Products(models.Model):
    PRODUCT_CATEGORIES = [
        ('finished', 'Finished'),
        ('semi-finished', 'Semi-Finished'),
        ('raw', 'Raw'),
    ]

    UNIT_MEASURES = [
        ('mtr', 'Meter'),
        ('mm', 'Millimeter'),
        ('ltr', 'Liter'),
        ('ml', 'Milliliter'),
        ('cm', 'Centimeter'),
        ('mg', 'Milligram'),
        ('gm', 'Gram'),
        ('unit', 'Unit'),
        ('pack', 'Pack'),
    ]
    #primary key field is autoincrement field
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=15, choices=PRODUCT_CATEGORIES)
    description = models.CharField(max_length=250, blank=True, null=True)
    product_image = models.URLField(max_length=500, blank=True, null=True)
    
    #stock keeping unit to mannaually set unique id
    sku = models.CharField(max_length=100, unique=True)
    unit_of_measure = models.CharField(max_length=5, choices=UNIT_MEASURES)
    lead_time = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.product_id} {self.category}"
    
