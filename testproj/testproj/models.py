from django.db import models

class user_reg(models.Model):
    firstname =models.CharField(max_length=35)
    lastname =models.CharField(max_length=35)

