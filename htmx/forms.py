from django import forms

from .models import Game


# class GameAddForm(forms.ModelForm):
#     class Meta:
#         model = Game
#         index = ['name']
#         fields = ['name', 'description', 'price']
#         widgets = {
#             'name': forms.CharField(widget=forms.TextInput(attrs={
#                 'class': 'clrtxt', 'placeholder': 'Name'
#             })),
#             'description': forms.CharField(widget=forms.TextInput(attrs={
#                 'class': 'clrtxt', 'placeholder': 'Description'
#             })),
#             'price': forms.FloatField(widget=forms.TextInput(attrs={
#                 'class': 'clrtxt', 'placeholder': 'Price'
#             }))
#         }

class GameAddForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "clrtxt", "placeholder": "Name"}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "clrtxt", "placeholder": "Description"}))
    price = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "clrtxt", "placeholder": "Price"}))

    class Meta:
        model = Game
        fields = ['name', 'description', 'price']


class GameEditForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput())
    description = forms.CharField(required=False, widget=forms.TextInput())
    price = forms.CharField(required=False, widget=forms.TextInput())

    class Meta:
        model = Game
        fields = ['name', 'description', 'price']


