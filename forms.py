from django import forms
from hem_app.models.runhistory import RunHistory


class HemForm(forms.ModelForm):

    class Meta:
        model = RunHistory
        fields = ('products', 'population_size', 'gender', 'categories')

