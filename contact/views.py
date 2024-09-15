from django.shortcuts import render

# Create your views here.
def contact(request):
    """ A view to return the contact page """

    template = 'contact/contact.html'

    return render(request, template)