from django.db import models

# Create your models here.


class Brand(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title
    

class Color(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title
    

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=150)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self) -> str:
        return self.brand.title