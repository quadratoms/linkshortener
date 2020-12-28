from django import forms
from .models import Linkmodel


class LinkForm (forms. ModelForm ):
	class Meta :
		model = Linkmodel
		fields = [ 'inputlink' ]
	




