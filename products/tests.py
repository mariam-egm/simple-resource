from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

class ProductAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_product(self):
        data = {'name': 'Test Product', 'description': 'This is a test product.'}
        response = self.client.post('/resource/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')
