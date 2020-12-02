from django.core.exceptions import ValidationError
import re


class ValidationService(object):

    @staticmethod
    def validate_rule1(allowed_characters, text):
        """All characters should belong to a given character set (allowed_characters)
        :param allowed_characters: list of all characters that are valid in text. E.G. aAbBcC!.
        :param text: to validate
        :return:
        """
        if text == "":
            raise ValidationError('Text is empty')
        invalid_string = re.sub(allowed_characters, "", text)
        if invalid_string != "":
            raise ValidationError(
                'Invalid characters: %(value)s',
                params={'value': invalid_string},
            )

    @staticmethod
    def validate_rule2(text):
        """Capital letters are allowed only as a first word letter or if the word is entirely uppercase.
        :param text: to validate
        :return:
        """
        if text == "":
            raise ValidationError('Text is empty')
        x = re.search("\\b[a-z]+[A-Z]+[a-z]+\\b", text)
        if x is not None:
            raise ValidationError(
                'Invalid character at position: %(value)s',
                params={'value': str(x.start())},
            )

    @staticmethod
    def validate_rule3(text):
        """There can be only zero or one space between two consecutive non-blank characters.
        :param text: to validate
        :return:
        """
        if text == "":
            raise ValidationError('Text is empty')
        x = re.search("\\b\\s{2,}\\b", text)
        if x is not None:
            raise ValidationError(
                'Invalid character at position: %(value)s',
                params={'value': str(x.start())},
            )

    @staticmethod
    def validate_rule4(text):
        """
        Characters ?.! should be end of text or followed by one space and an uppercase character.
        :param text: to validate
        :return:
        """
        # TODO implement rule 4
        pass

    @staticmethod
    def validate_rule5(text):
        """
        Characters ,;: should be end of text or followed by one space.
        :param text:
        :return:
        """
        # TODO implement rule 5
        pass
