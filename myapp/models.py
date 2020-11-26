from django.db import models
from django.contrib.auth.models import User


class Audio(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    file_name = models.CharField(max_length=255)
    CREATED = 'CR'
    COMPLETED = 'CO'
    STATUS_CHOICES = [
        (CREATED, 'Created'),
        (COMPLETED, 'Completed'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=CREATED,
        db_index=True
    )
    content = models.BinaryField()
    created_at = models.DateTimeField
    updated_at = models.DateTimeField

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Transcription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    charset = models.ForeignKey
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    text = models.TextField(null=False)


class Charset(models.Model):
    name = models.CharField(max_length=128)
    allowed_characters = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Configuration(models.Model):
    name = models.CharField(max_length=128)
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=1024)

    def __str__(self):
        return self.name
