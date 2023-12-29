from django.db import models


class Post(models.Model):
    title =models.CharField(max_length=255)
    body =models.TextField()

    def __str__(self):
        return "{}".format(self.title)
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name