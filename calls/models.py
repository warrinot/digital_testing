from django.db import models
import uuid
from django.core.validators import RegexValidator
from taggit.managers import TaggableManager


class Theme(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Call(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    timestamp_started = models.DateTimeField()
    timestamp_finished = models.DateTimeField()
    # формат не уточнен, поэтому регулярка под Российские номера без +
    phone_regex = RegexValidator(regex=r'^\d{11}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=11)
    is_finished = models.BooleanField()
    result = models.CharField(max_length=250)
    tags = TaggableManager()
    theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True)
    # seen_by ?

    @property
    def duration(self):
        delta = self.timestamp_finished - self.timestamp_started
        return delta.seconds

    def __str__(self):
        return f'Call {self.guid}'
