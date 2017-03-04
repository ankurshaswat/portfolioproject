from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.forms import ModelForm

# Create your models here.
class Message(models.Model):
    messager_name=models.CharField(max_length=30,default="What's Your name")
    messager_email=models.CharField(max_length=50,default='Email comes here')
    message_text = models.CharField(max_length=400,default='Hello')
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.messager_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


