from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .services import ValidationService

# Register your models here.
from .models import Audio
from .models import Charset
from .models import Configuration
from .models import Transcription


class MyTranscriptionAdminForm(ModelForm):
    def clean_text(self):
        # validate text with validation service
        text = self.data['text']
        # retrieve charset
        charset = Charset.objects.filter(id=self.data['charset']).first()
        # run validations
        ValidationService.validate_rule1(charset.allowed_characters, text)
        ValidationService.validate_rule2(text)
        ValidationService.validate_rule3(text)
        ValidationService.validate_rule4(text)
        ValidationService.validate_rule5(text)
        return self.cleaned_data["text"]

    def clean(self):
        cleaned_data = super().clean()
        audio = cleaned_data.get("audio")
        # retrieve configuration parameter N
        configuration = Configuration.objects.filter(key='n').first()
        n = int(configuration.value)
        # check how many transcription object is already present for given audio sample
        trans_count = Transcription.objects.filter(audio=audio).count()
        if trans_count > n:
            raise ValidationError(
                'Cant add more than N=%(value)s transcriptions',
                params={'value': str(n)},
            )


class TranscriptionAdmin(admin.ModelAdmin):
    form = MyTranscriptionAdminForm


admin.site.register(Audio)
admin.site.register(Charset)
admin.site.register(Configuration)
admin.site.register(Transcription, TranscriptionAdmin)
