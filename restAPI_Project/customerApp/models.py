from django.db import models

class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=100)
    product = models.CharField(max_length=100)

    def __str__(self):
        return self.name
