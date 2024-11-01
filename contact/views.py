from django.shortcuts import render
from django.contrib import messages

from .models import Return
from .forms import ReturnForm


# Create your views here.
def contact(request):
    """ A view to return the contact page """

    if request.method == "POST":
        print("Recived post request")
        return_form = ReturnForm(data=request.POST)
        if return_form.is_valid():
            print("Valid request")
            return_form.save()
            messages.success(request, "Message received! We will \
                             contact you in the coming days.")
        else:
            messages.error(request, 'Message failed, please look over form')

    return_form = ReturnForm()
    returns = Return

    template = 'contact/contact.html'
    context = {
        'returns': returns,
        "return_form": return_form
    }

    return render(request, template, context)
