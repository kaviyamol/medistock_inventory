from django.db import models
from datetime import date

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()

    def is_expired(self):
        return self.expiry_date < date.today()

    def __str__(self):
        return self.name
