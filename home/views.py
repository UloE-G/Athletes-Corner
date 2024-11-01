from django.shortcuts import render
from django.contrib import messages

from .models import Newsletter
from .forms import NewsletterForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    if request.method == "POST":
        print("Recived post request")
        letter_form = NewsletterForm(data=request.POST)
        if letter_form.is_valid():
            print("Valid request")
            letter_form.save()
            messages.success(request,
                             'Thank you :) Please check email for \
                             an exclusive welcome discount!!!')
        else:
            messages.error(request,
                           'Request failed, please make sure \
                           email was typed in correctly')

    letter_form = NewsletterForm()
    letter = Newsletter

    context = {
        'letter': letter,
        'letter_form': letter_form
    }

    return render(request, 'home/index.html', context)
