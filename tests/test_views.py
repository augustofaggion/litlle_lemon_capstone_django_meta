from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Burger", price=10.00, inventory=20)
        self.item2 = Menu.objects.create(title="Pasta", price=12.50, inventory=15)

    def test_getall(self):
        response = self.client.get("/restaurant/menu-items/")  # your Menu API endpoint
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)