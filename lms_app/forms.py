from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import * 

class CategoryForm(forms.ModelForm):
    class Meta:
       model = Category
       fields = ['name']
       widgets = {
           'name' : forms.TextInput(attrs=({'class':'form-control'}))
        }






class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_photo',
            'author_photo',
            'pages',
            'price',
            'rental_price_per_day',
            'rental_period',
            'rental_total_price',
            'status',
            'category',
        ]
        widgets= {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'book_photo' : forms.FileInput(attrs={'class':'form-control'}),
            'author_photo' : forms.FileInput(attrs={'class':'form-control'}),
            'pages' : forms.NumberInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_per_day' : forms.NumberInput(attrs={'class':'form-control', 'id':'rentalperday'}),
            'rental_period' : forms.NumberInput(attrs={'class':'form-control', 'id':'rentalperiod'}),
            'rental_total_price' : forms.NumberInput(attrs={'class':'form-control', 'id':'rentaltotal'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
        }
