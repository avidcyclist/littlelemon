from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a menu item
        item = Menu.objects.create(title="Eggplant", price=3, inventory=10)

        # Check the string representation directly on the created item
        self.assertEqual(str(item), "Eggplant : 3")
