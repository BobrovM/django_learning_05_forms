from django import forms


class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=32)
    last_name = forms.CharField(label="Last Name", max_length=32)
    email = forms.EmailField(label="Email")
    review = forms.CharField(label="Your Review", max_length=100)
