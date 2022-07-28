from django.test import TestCase
from myapp.models import Restaurant, Menu


class RestaurantTestCase(TestCase):
    def setUp(self):
        restaurant = Restaurant.objects.create(name="RestaurantTestName1")
        Menu.objects.create(menu="MenyMenuForMonday", price=10.5, day=0, restaurant=restaurant)

    def test_animals_can_speak(self):
        menu = Menu.objects.get(menu="MenyMenuForMonday")
        self.assertEqual(menu.__str__(), 'RestaurantTestName1 | Monday MENU')
