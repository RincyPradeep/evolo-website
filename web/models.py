from django.contrib.postgres.fields import ArrayField
from django.db import models


INTERESTS=(
    ("1","Marketing"),
    ("2","Sales"),
    ("3","Designing")
)

class Customer(models.Model):
    logo = models.ImageField(upload_to="customers/")

    def __str__(self):
        return str(self.id)


class Service(models.Model):
    image = models.FileField(upload_to="services/")
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title


class Feature(models.Model):
    image = models.FileField(upload_to="features/")
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=True)
    list_items = ArrayField(models.CharField(max_length=200), blank=True,null=True)

    def __str__(self):
        return self.title


class Pricing(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price_in_dollar = models.IntegerField()
    feature_list = ArrayField(models.CharField(max_length=200),blank=True,null=True)
    not_feature_list = ArrayField(models.CharField(max_length=200),blank=True,null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length = 128)
    email = models.EmailField()
    phone = models.BigIntegerField()
    interested_in = models.CharField(max_length = 128,choices=INTERESTS)
    user_agreement = models.BooleanField()

    def __str__(self):
        return self.full_name


class Video(models.Model):
    image = models.FileField(upload_to="video/")

    def __str__(self):
        return str(self.id)


class Team(models.Model):
    image = models.FileField(upload_to="team-members/")
    name = models.CharField(max_length = 128)
    designation = models.CharField(max_length = 128)

    def __str__(self):
        return self.name
