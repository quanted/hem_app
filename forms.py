from django import forms

from hem_app.models import RunHistory, Category, Chemical, Dose

GENDER_CHOICES = (
	('B', 'Both'),
	('F', 'Female'),
	('M', 'Male')
)

PRODUCT_CHOICES = (
	('1', 'Products'),
	('0', 'Chemicals')
)

class RunForm(forms.ModelForm):
	class Meta:
		model = RunHistory
		fields = 'population_size', 'gender', 'min_age', 'max_age'


	population_size = forms.IntegerField(initial=5000, widget=forms.TextInput(attrs={'class': 'form-control'}))
	gender = forms.CharField(max_length=1, widget=forms.Select(choices=GENDER_CHOICES, initial='B')
	min_age = forms.IntegerField(initial=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
	max_age = forms.IntegerField(initial=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
