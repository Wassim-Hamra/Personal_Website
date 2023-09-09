from django.db import models


# Create your models here.

class Visitor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
