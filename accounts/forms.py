from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'address')
    error_class = forms.ValidationError

    first_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
             'class': 'form-control mx-auto',
            'placeholder': 'Ismingizni kiriting',
        }
        ))

    last_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control mx-auto',
            'placeholder': 'Familiyangizni kiriting',
        })
        )
    username = forms.CharField(
        label= None,
        max_length = 100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mx-auto',
            'placeholder': 'Username kiriting',

        })
    )

    birthday = forms.IntegerField(
        label='Yoshingizni kiriting:',
        widget=forms.NumberInput(attrs={
            'class': 'form-control mx-auto',
            'placeholder': 'Yoshingizni kiriting',
        }))
    address = forms.CharField(
        max_length=100,
        required=False,

        widget=forms.TextInput(attrs={
            'class': 'form-control mx-auto',
            'placeholder': 'Manzilingizni kiriting',
        }
        ))

    email = forms.EmailField(
        # label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control mx-auto',
            'placeholder': 'Email kiriting'
        })
    )
    password1 = forms.CharField(
        # label="Parol",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mx-auto',
            'placeholder': 'Parol kiriting'
        })
    )
    password2 = forms.CharField(
        # label="Parolni tasdiqlash",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mx-auto',
            'placeholder': 'Parolni tasdiqlang'
        })
    )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'address')
    error_class = forms.ValidationError



class UserForm(forms.Form):
    model = CustomUser
    username = forms.CharField(
        label="Foydalanuvchi nomi",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Bootstrap uchun
            'placeholder': 'Username kiriting',
            'style': 'width=75%',
        })
    )


    # email = forms.EmailField(
    #     label="Email",
    #     widget=forms.EmailInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Email kiriting'
    #     })
    # )

    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parol kiriting'
        })
    )

    # agree = forms.BooleanField(
    #     label="Shartlarga rozimisiz?",
    #     required=True,
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input'
    #     })
    # )
