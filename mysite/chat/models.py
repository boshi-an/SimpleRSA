from django.db import models

# Create your models here.

def Message(models.Model):

    UserFrom = models.ForeignKey(User)