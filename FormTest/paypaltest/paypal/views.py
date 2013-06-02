from django.shortcuts import render
from django.http import HttpResponseRedirect
from paypal.forms import PayForm

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

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = PayForm() # An unbound form

    return render(request, 'pay.html', {
        'form': form,
    })