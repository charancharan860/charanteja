from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from App.models import HandiCrafts

class RegForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"
		}))
	class Meta:
		model=User
		fields=['username']
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter username",
			}),
		}

class CraftsForm(forms.ModelForm):
	class Meta:
		model=HandiCrafts
		fields=["category_type","quantity","price","im"]
		widgets = {
		"category_type":forms.Select(attrs= {
			"class":"form-control",
			}),
		"quantity":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Quantity",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Price",
			}),
		}