from django.shortcuts import render
from django.http import HttpResponseRedirect
from paypal.forms import PayForm

def pay(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PayForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            print subject

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = PayForm() # An unbound form

    return render(request, 'pay.html', {
        'form': form,
    })