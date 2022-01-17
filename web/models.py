from django.db import models


class Customer(models.Model):
    logo = models.ImageField(upload_to="customers/")

    def __str__(self):
        return str(self.id)