from django.shortcuts import render
from django.template import loader
from django.views.decorators.debug import sensitive_variables
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Account
import sqlite3

# Create your views here.

@login_required
@sensitive_variables('sender', 'receiver')
@transaction.atomic
def transfer(request, sender, receiver, amount):
	acc1 = Account.objects.get(iban=sender)
	acc2 = Account.objects.get(iban=receiver)

	if amount > 0 and acc1 != acc2 and acc1.owner == str(request.user):
		if amount < acc1.balance:
			acc1.balance -= amount
			acc2.balance += amount

	acc1.save()
	acc2.save()


@login_required
def homePageView(request):
	if request.method == 'POST':
		sender = request.POST.get('from')
		receiver = request.POST.get('to')
		amount = int(request.POST.get('amount'))
		transfer(request, sender, receiver, amount)

	accountz = Account.objects.all()
	accounts = []
	for account in accountz:
		print(account.balance)
		if account.owner == str(request.user):
			accounts.append(account)
		else:
			account.balance = '?'
			accounts.append(account)
	context = {'accounts': accounts}
	return render(request, 'pages/index.html', context)


