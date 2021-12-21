from django.db import models
from Acquisition import Implicit

# Create your models here.


class Account(models.Model):
	owner = models.TextField()
	iban = models.TextField()
	balance = models.IntegerField()


class BankingDetails(Implicit):
	SWIFT = models.TextField()
	IBAN = models.TextField()
	Advisor = models.TextField()