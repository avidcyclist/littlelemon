from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title="Dish1", price=10, inventory=20)
        Menu.objects.create(title="Dish2", price=15, inventory=25)
        Menu.objects.create(title="Dish3", price=12, inventory=18)

    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        url = reverse('menu-list-create')  # Assuming this is the URL for your Menu list view
        response = client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
