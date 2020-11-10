from django import forms
from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField,
    UserCreationForm,
    UserChangeForm,
)
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Подтверждение пароля", widget=forms.PasswordInput
    )

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email",)

    def clean_password2(self):
        password1 = self.clean_data.get("password1")
        password2 = self.clean_data.get("password1")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don`t match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "patronic_name",
            "address_shipment",
            "is_active",
            "is_admin",
        )

    def clean_password(self):
        return self.initial["password"]
