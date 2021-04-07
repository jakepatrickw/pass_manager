from django.db import models

class UsernamePasswordService(models.Model):
    service = models.CharField(max_length=30)
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

