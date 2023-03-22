from django import forms
from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']


"""class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=32)
    last_name = forms.CharField(label="Last Name", max_length=32)
    email = forms.EmailField(label="Email")
    review = forms.CharField(label="Your Review", max_length=500, widget=forms.Textarea(
        attrs={'class': 'myform', 'rows': '6', 'cols': '64'})) """
