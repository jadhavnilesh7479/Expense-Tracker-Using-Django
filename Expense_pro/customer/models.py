from django.db import models


# Create your models here.
class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    comments = models.TextField()



    def __str__(self):
        return self.category