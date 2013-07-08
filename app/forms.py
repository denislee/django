from django.forms import ModelForm 

from app.models import App

class AppForm(ModelForm):
	class Meta:
		model = App 
		exclude = ('points', 'moderator', 'voters')