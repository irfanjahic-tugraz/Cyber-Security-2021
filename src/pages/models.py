from django.db import models

# Create your models here.

class Account(models.Model):
	owner = models.TextField()
	iban = models.TextField()
	balance = models.IntegerField()

