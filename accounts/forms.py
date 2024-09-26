from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CostomUser,EditProfile

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class CostomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CostomUser
        fields = UserCreationForm.Meta.fields + ('email','age',)

class CostomUserChangeForm(UserChangeForm):
    class Meta:
        model = CostomUser
        fields = UserChangeForm.Meta.fields

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = EditProfile
        fields = ['about','photo','age']

class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CostomUser
        fields = ['old_password','new_password1','new_password2']

class PasswordResetForm(PasswordResetForm):
    class Meta:
        model = CostomUser
        fields = ['email']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = CostomUser
        fields = ['new_password1','new_password2']
