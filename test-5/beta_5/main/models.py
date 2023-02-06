from django.db import models

# Create your models here.
class Number(models.Model):
    number = models.IntegerField(max_length=10000000)
def __str__(self):
        return self.number