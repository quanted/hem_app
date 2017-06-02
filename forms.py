from django import forms

from hem_app.models import RunHistory, Category, Chemical, Dose, RunParams

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

	chemical = forms.ModelChoiceField(queryset=Chemical.objects.filter(id__in=Dose.objects.values('chemical_id')),
									  empty_label=None, to_field_name='cas')
	categories = forms.ModelChoiceField(queryset=Category.objects.filter(id__in=RunParams.objects.values('category_id')),
									  empty_label=None)
	population_size = forms.IntegerField(initial=5000, widget=forms.TextInput(attrs={'class': 'form-control'}))
	gender = forms.CharField(max_length=1, widget=forms.Select(choices=GENDER_CHOICES))
	min_age = forms.IntegerField(initial=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
	max_age = forms.IntegerField(initial=5, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = RunHistory
		fields = 'chemical', 'categories', 'population_size', 'gender', 'min_age', 'max_age'
