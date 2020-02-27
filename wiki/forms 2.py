from django import forms
from wiki.models import Page


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    model = Page

# class FriendlyForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)