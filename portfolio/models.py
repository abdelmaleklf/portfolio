from django.db import models


class Info(models.Model):
    birthday = models.DateField(blank=False)
    phone = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False, max_length=254)
    degree = models.CharField(blank=False, max_length=50)
    city = models.CharField(blank=False, max_length=50)
    website = models.URLField(blank=False, max_length=200)


class Social(models.Model):
    github = models.URLField(blank=False, max_length=200)
    linkedin = models.URLField(blank=False, max_length=200)


class Testimonial(models.Model):
    image = models.ImageField(upload_to='static/img/')
    name = models.CharField(blank=False, max_length=50)
    comment = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(blank=False, max_length=50)
    url = models.URLField(blank=True, max_length=200)
    image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.name








