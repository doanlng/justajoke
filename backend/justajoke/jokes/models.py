from django.db import models

# Create your models here.
class joke (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    punchline = models.CharField(max_length=400)
    date_submitted= models.DateTimeField(default=None)
    verified = models.BooleanField(default=False)

