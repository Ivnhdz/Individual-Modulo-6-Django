from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Formulario(models.Model):
    cuerpo = models.TextField(max_length=250)
    fecha = models.DateTimeField(default= timezone.now)