from django import forms
from .models import Profile, UserDocument


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
        )
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "نام",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "نام خانوادگی",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "ایمیل",
                }
            ),
        }


class UserDocumentForm(forms.ModelForm):
   class Meta:
       model=UserDocument
       fields=('title','image','description')