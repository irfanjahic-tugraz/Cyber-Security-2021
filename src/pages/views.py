from django.shortcuts import render
from django.template import loader
from django.views.decorators.debug import sensitive_variables
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Account
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@transaction.atomic
@csrf_exempt
def transfer(request, sender, receiver, amount):
	acc1 = Account.objects.get(iban=sender)
	acc2 = Account.objects.get(iban=receiver)

	if amount > 0 and acc1 != acc2:
		if amount < acc1.balance:
			acc1.balance -= amount
			acc2.balance += amount

	acc1.save()
	acc2.save()

@csrf_exempt
def homePageView(request):
	if request.method == 'POST':
		sender = request.POST.get('from')
		receiver = request.POST.get('to')
		amount = int(request.POST.get('amount'))
		transfer(request, sender, receiver, amount)

	accounts = Account.objects.all()
	context = {'accounts': accounts}
	return render(request, 'pages/index.html', context)


