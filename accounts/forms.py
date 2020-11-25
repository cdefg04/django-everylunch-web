from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from accounts.models import myuser


class JoinForm(UserCreationForm):
    username = forms.CharField(label="아이디")
    password1 = forms.CharField(label="비밀번호")
    password2 = forms.CharField(label="비밀번호 확인")
    email = forms.EmailField(label="이메일")
    school = forms.CharField(label="학교")
    cafeteria = forms.CharField(label="식당")

    class Meta(UserCreationForm.Meta):
        model = myuser
        fields = ("username", "password1", "password2", "email", "school", "cafeteria")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "school", "cafeteria")


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })