import os
from django.db import models
from django.core.files.base import ContentFile
import requests
from parler.models import TranslatableModel, TranslatedFields
from urllib.parse import urlparse


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
    url = models.URLField(max_length=1000)

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
    translation = TranslatedFields(product_url=models.URLField(max_length=1000))
    image_url = models.URLField(max_length=1000)
    image = models.ImageField(upload_to='product_images/', blank=True)

    def __str__(self):
        return f'{self.brand} {self.product_type} - Scraped from {self.website}'

    @staticmethod
    def get_image_upload_path(instance, filename):
        subfolder = None
        # determine the subfolder based on the website
        if instance.website.name == 'AM':
            subfolder = 'amazon'
        elif instance.website.name == 'JU':
            subfolder = 'jumia'
        elif instance.website.name == 'EH':
            subfolder = 'ehabgroup'
        elif instance.website.name == '2B':
            subfolder = 'twob'
        # construct the full upload path
        return os.path.join(subfolder, filename)

    def save(self, *args, **kwargs):
        if self.image_url and not self.image:
            # directly download the image content
            response = requests.get(self.image_url)
            if response.status_code == 200:
                # parse the URL to ignore query parameters
                parsed_url = urlparse(self.image_url)
                filename = os.path.basename(parsed_url.path)  # extract filename from the path, ignoring query parameters
                self.image.save(self.get_image_upload_path(self, filename), ContentFile(response.content), save=False)  # save image content to ImageField
        super().save(*args, **kwargs)
