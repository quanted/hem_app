from django import forms

from hem_app.models import RunHistory, Chemical, Dose, RunParams, Product

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
	dose = Dose.objects.filter(runparams_id=1).distinct().values('chemical_id')
	chemical = forms.ModelChoiceField(queryset=Chemical.objects.filter(id__in=dose),
									  empty_label=None, to_field_name='cas')

	product = forms.ModelChoiceField(queryset=Product.objects.filter(id__in=RunParams.objects.values('product_id')),
									 empty_label=None)

	gender = forms.CharField(max_length=1, widget=forms.Select(choices=GENDER_CHOICES))
	min_age = forms.IntegerField(initial=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
	max_age = forms.IntegerField(initial=99, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = RunHistory
		fields = 'chemical', 'product', 'gender', 'min_age', 'max_age'
