from django.db import models

# Product Model
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    quality     = models.TextField(default="This awesome product")

# Mobile Model
class Mobile(models.Model):
    brand = models.TextField()
    model = models.TextField()

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    query = models.TextField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return self.name