from django.contrib.auth import password_validation
from django import forms
from .models import Comment, User
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# User = get_user_model()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class UserCreateForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
    