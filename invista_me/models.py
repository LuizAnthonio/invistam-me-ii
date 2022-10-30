from datetime import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

'''
* investimento
* valor
* pago
* data

'''

class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)


objetos = models.Manager()

def somador(self):
    return sum([self.valor])

# Create your models here.
