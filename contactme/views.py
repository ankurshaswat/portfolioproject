from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse


def index(request):
    context={}
   # return HttpResponse("Hello, world. You're at the contactme index.")
    return render(request, 'contactme/index.html', {})
from django.http import HttpResponseRedirect

from .forms import MessageForm

def get_message(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('contactme/thanks.html'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MessageForm()

    return render(request, 'contactme/message.html', {'form': form})

def thanks(request):
    context={}
   # return HttpResponse("Hello, world. You're at the contactme index.")
    return render(request, 'contactme/thanks.html', {})
