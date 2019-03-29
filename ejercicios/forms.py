from django import forms

class ActorForm(forms.Form):

	actor = forms.CharField(label='actor')
