from django.test import TestCase
from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from .services import ValidationService


# Create your tests here.
class ValidationServiceTests(SimpleTestCase):
    def test_rule1_with_ok_characters(self):
        ValidationService.validate_rule1("^[a-zA-Z\\s\\d]+$", "AA")

    def test_rule1_with_invalid_character(self):
        with self.assertRaises(ValidationError):
            ValidationService.validate_rule1("^[a-zA-Z\\s\\d]+$", "This is not valid Č\n text")

    def test_rule1_with_nok(self):
        with self.assertRaises(ValidationError):
            ValidationService.validate_rule1("aaAAbb", "ccc")

    def test_rule2_with_nok(self):
        with self.assertRaises(ValidationError):
            ValidationService.validate_rule2("aaAAbb")

    def test_rule2_with_nok1(self):
        ValidationService.validate_rule2("aaAAbb")

# TODO finish unit tests for other rules
