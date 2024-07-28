import pytest
from django.urls import reverse
from django.test import Client
from django.db.models import Max, Q
from .models import ScrapedProduct


