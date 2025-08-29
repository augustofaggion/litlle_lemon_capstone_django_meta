from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_create_menu_item(self):
        item = MenuItem.objects.create(title="Pizza", price=15.00, inventory=10)
        self.assertEqual(str(item), "Pizza : 15.00")