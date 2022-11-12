from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import datetime


# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=5000, blank=False, verbose_name=_("Event Name"))
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name=_("User"))
    timest = models.DateTimeField(default=datetime.now, blank=True, verbose_name=_("Posted date"))
    images = models.CharField(max_length=5000, blank=False, verbose_name=_("Event media"))
    models.
