from django.contrib import admin

# Register your models here.
from .models import Audio
from .models import Charset
from .models import Configuration
from .models import Transcription

admin.site.register(Audio)
admin.site.register(Charset)
admin.site.register(Configuration)
admin.site.register(Transcription)