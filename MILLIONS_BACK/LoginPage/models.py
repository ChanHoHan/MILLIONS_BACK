from django.db import models

# Create your models here.
class Login(models.Model):
    user_id = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)