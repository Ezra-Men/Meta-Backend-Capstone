from django.test import TestCase
from restaurant.models import MenuItem
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
 def test_get_item(self):
  item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
  self.assertEqual(item, "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(name='Menu 1', description='Test menu 1')
        self.menu2 = Menu.objects.create(name='Menu 2', description='Test menu 2')

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
