from django import forms

from hem_app.models.runhistory import RunHistory, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import TabHolder, Tab


class ProductForm(forms.ModelForm):
    """ Form for Model run """

    class Meta:
        model = RunHistory
        fields = ('categories', 'products',)


class ChemicalForm(forms.ModelForm):
    model = RunHistory
    fields = ('categories', 'chemical')

