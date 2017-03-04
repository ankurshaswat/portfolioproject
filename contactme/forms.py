from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
	class Meta:
		model=Message
		fields=('messager_name','message_text','messager_email')
