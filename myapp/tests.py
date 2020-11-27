from django.test import TestCase
from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from .services import ValidationService


# Create your tests here.
class ValidationServiceTests(SimpleTestCase):
    def test_rule1_with_ok_characters(self):
        ValidationService.validate_rule1("aaAAbb", "AA")

    def test_rule1_with_nok(self):
        with self.assertRaises(ValidationError):
            ValidationService.validate_rule1("aaAAbb", "ccc")
