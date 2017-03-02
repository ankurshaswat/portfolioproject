from django.shortcuts import render
from django.utils import timezone
from .forms import MessageForm

def get_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.pub_date=timezone.now()
            message.save()
            return render(request, 'contactme/thanks.html', {})
    else:
        form = MessageForm()
    return render(request, 'contactme/message.html', {'form': form})


