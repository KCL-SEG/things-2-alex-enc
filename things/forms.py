"""Forms of the project."""

# Create your forms here.
# the project includes a nearly empty file called things/forms.py.
# In this file, define a form called ThingForm, that contains the fields name, description, and quantity, but not created_at.
#
# The form must accept valid inputs for Thing and reject invalid input for Thing.
#
# The description field must be displayed as a Textarea. The quantity field must be displayed as NumberInput.
from django import forms
from .models import Thing

class ThingForm(forms.Form):
        name = forms.CharField(label="Name")
        description = forms.CharField(widget=forms.Textarea,label="Description")
        quantity = forms.CharField(widget=forms.NumberInput, label="Quantity")
