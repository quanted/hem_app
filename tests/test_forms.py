from django.test import TestCase
from hem_app.forms import HemForm


class RunFormTest(TestCase):
    '''Main form test'''
    def test_blank_form(self):
        hem = HemForm()
        self.assertFalse(hem.is_valid())
