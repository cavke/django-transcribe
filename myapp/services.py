from django.core.exceptions import ValidationError


class ValidationService(object):

    @staticmethod
    def validate_rule1(allowed_characters, text):
        """All characters should belong to a given character set (allowed_characters)
        :param allowed_characters: list of all characters that are valid in text. E.G. aAbBcC!.
        :param text: to validate
        :return:
        """
        print('rule1:' + text)
        if text == "":
            raise ValidationError('Text is empty')
        for c in text:
            if c not in allowed_characters:
                raise ValidationError(
                    'Character not allowed',
                    params={'value': c},
                )


    @staticmethod
    def validate_rule2(text):
        """Capital letters are allowed only as a first word letter or if the word is entirely uppercase.
        :param text: to validate
        :return:
        """
        if text == "":
            raise ValidationError('Text is empty')

    @staticmethod
    def validate_rule3(text):
        """There can be only zero or one space between two consecutive non-blank characters.
        :param text: to validate
        :return:
        """
        if text == "":
            raise ValidationError('Text is empty')

    @staticmethod
    def validate_rule4(text):
        """
        Characters ?.! should be end of text or followed by one space and an uppercase character.
        :param text: to validate
        :return:
        """
        pass

    @staticmethod
    def validate_rule5(text):
        """
        Characters ,;: should be end of text or followed by one space.
        :param text:
        :return:
        """
        pass
