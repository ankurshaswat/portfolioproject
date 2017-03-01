from django import forms

class MessageForm(forms.Form):
    messager_name = forms.CharField(label='Your name', max_length=100)
