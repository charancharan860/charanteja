from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UsForm(UserCreationForm):
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
        	"placeholder":"enter username"
        	}),
		}