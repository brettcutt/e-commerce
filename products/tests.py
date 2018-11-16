from django.test import TestCase
from .models import Product
# Create your tests here.


class ProductsTests(TestCase):
    """
    Here we'll define the test that we'll
    run against out product models
    """

    def test_str(self):
        test_name = Product(name='A product', description='A description')
        self.assertEqual(str(test_name), 'A product\nA description')
