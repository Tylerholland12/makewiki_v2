from django.forms import ModelForm
from .models import Page


class PageForm(ModelForm):
    """ Render and process a form based on the Page model. """
    model = Page
