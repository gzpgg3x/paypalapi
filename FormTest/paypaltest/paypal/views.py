from django.shortcuts import render
from django.http import HttpResponseRedirect
from paypal.forms import PayForm
import paypalrestsdk
import logging

def pay(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PayForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            cardtype = form.cleaned_data['cardtype']
            number = form.cleaned_data['number']
            expire_month = form.cleaned_data['expire_month']
            expire_year = form.cleaned_data['expire_year']
            cvv2 = form.cleaned_data['cvv2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # print cardtype


            logging.basicConfig(level=logging.INFO)

            paypalrestsdk.configure(
              mode="sandbox", # sandbox or live
              client_id="AeqEchB5ZiTwbWETXf4H5SK5GW22u4dr2L8uWAkMsbcUE9KECDJgjTlVGPcd",
              client_secret="EAFNlBD01ZxAmNT-Laks-PCU6zTeihRUQrwKq5w6KH4W_nACtMUP4wEuTjtC")

            payment = paypalrestsdk.Payment({
              "intent": "sale",
              "payer": {
                "payment_method": "credit_card",
                "funding_instruments": [{
                  "credit_card": {
                    "type": cardtype,
                    "number": number,
                    "expire_month": expire_month,
                    "expire_year": expire_year,
                    "cvv2": cvv2,
                    "first_name": first_name,
                    "last_name": last_name }}]},
              "transactions": [{
                "item_list": {
                  "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": "0.01",
                    "currency": "USD",
                    "quantity": 1 }]},
                "amount": {
                  "total": "0.01",
                  "currency": "USD" },
                "description": "This is the payment transaction description." }]})

            if payment.create():
              print("Payment created successfully")
            else:
              print(payment.error)


            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = PayForm() # An unbound form

    return render(request, 'pay.html', {
        'form': form,
    })