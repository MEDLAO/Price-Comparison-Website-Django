from django.db import models
from django.core.files.base import ContentFile
import requests
import pandas as pd
from parler.models import TranslatableModel, TranslatedFields


class Website(models.Model):
    WEBSITE_NAME = (
       ('AM', 'Amazon'),
       ('EH', 'Ehabgroup'),
       ('JU', 'Jumia'),
       ('2B', '2B'),
    )
    COUNTRY = (
       ('EG', 'Egypt'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, choices=WEBSITE_NAME)
    country = models.CharField(max_length=50, choices=COUNTRY)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.WEBSITE_NAME} {self.COUNTRY}'


class BaseProduct(TranslatableModel):
    PRODUCT_TYPE = (
        ('SW', 'Smart Watch'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    translations = TranslatedFields(
        description=models.TextField(),
        brand=models.CharField(max_length=50, blank=True),
        color=models.CharField(max_length=50, blank=True),
        currency=models.CharField(max_length=10),
    )
    product_type = models.CharField(max_length=50, choices=PRODUCT_TYPE, default='SW')
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ScrapedProduct(BaseProduct):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    product_url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return f'{self.brand} {self.product_type} - Scraped from {self.website}'

    def save(self, *args, **kwargs):
        if self.image_url and not self.image:
            # Directly download the image content
            response = requests.get(self.image_url)
            filename = self.image_url.split('/')[-1]  # Extract filename from URL
            self.image.save(filename, ContentFile(response.content), save=False)  # Save image content to ImageField
        super().save(*args, **kwargs)
