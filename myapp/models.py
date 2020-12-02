from django.db import models
from django.contrib.auth.models import User


class CreatedUpdateAtModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True
    )

    class Meta:
        abstract = True


class Audio(CreatedUpdateAtModel):
    CREATED = 'CR'
    COMPLETED = 'CO'
    STATUS_CHOICES = [
        (CREATED, 'Created'),
        (COMPLETED, 'Completed'),
    ]

    name = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    file_name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=CREATED,
        db_index=True
    )
    content = models.BinaryField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Charset(models.Model):
    name = models.CharField(max_length=128)
    allowed_characters = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Transcription(CreatedUpdateAtModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, db_index=True)
    charset = models.ForeignKey(Charset, on_delete=models.PROTECT, db_index=True)
    text = models.TextField(null=False)


class Configuration(models.Model):
    name = models.CharField(max_length=128)
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=1024)

    def __str__(self):
        return self.name
