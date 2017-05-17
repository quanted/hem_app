from django import forms

from hem_app.models.runhistory import RunHistory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RunForm(forms.ModelForm):


	class Meta:
		model = RunHistory
		fields = 'population_size',
		widgets = {'chemical'}
