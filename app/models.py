from django.db import models

class Jarvis(models.Model):
    image = models.ImageField()
    name = models.CharField()
    title = models.CharField()
    link = models.CharField()
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Model(models.Model):
    name = models.CharField()
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField()
    email = models.EmailField()
    subject = models.CharField()
    text = models.TextField()

    def __str__(self):
        return self.name

