from django import forms

from hem_app.models.runhistory import RunHistory, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import TabHolder, Tab

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><


class popgenForm(forms.Form):
    population_field = forms.IntegerField(min_value=0,
                                          initial='1000000',
                                          label='Population Size',
                                          error_messages={'min_value': 'Negative number is not allowed'},
                                          widget=forms.NumberInput(attrs={'onchange': "populationsync(value);"}))

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><
# Unable to user modelForm because we need to filter data and
# we are using Radio buttons, we need to define min and max value

class HemForm(forms.ModelForm):
    """ Form for Model run """

    class Meta:
        model = RunHistory
        fields = ('categories', 'products', 'population_size')

