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

    def test_get_product_list(self):
        Product.objects.create(name='Product 1', description='Description 1')
        Product.objects.create(name='Product 2', description='Description 2')

        response = self.client.get('/resource/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_get_product_detail(self):
        product = Product.objects.create(name='Test Product', description='Test Description')
        response = self.client.get(f'/resource/{product.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product')


    def test_update_product(self):
        product = Product.objects.create(name='Old Name', description='Old Description')
        data = {'name': 'New Name', 'description': 'New Description'}
        response = self.client.put(f'/resource/{product.id}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().name, 'New Name')

    def test_delete_product(self):
        product = Product.objects.create(name='Product to Delete', description='Description to Delete')
        response = self.client.delete(f'/resource/{product.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
