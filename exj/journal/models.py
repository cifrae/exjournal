from django.db import models

# Create your models here.

class NModel(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self) -> str:
        return f'{self.name}'

