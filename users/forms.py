
from django import forms
from captcha.fields import CaptchaField


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名",    max_length=128, widget=forms.TextInput(attrs={"placeholder":"输入手机号码"}))
    password = forms.CharField(label="密码",      max_length=256, widget=forms.TextInput(attrs={"placeholder":"输入密码"}))
    fuserid =  forms.CharField(label="上级会员名", max_length=128, widget=forms.TextInput(attrs={"placeholder":"上级会员编号"}))
    captcha = CaptchaField(label='验证码')


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名",    max_length=128, widget=forms.TextInput(attrs={"placeholder":"账号"}))
    password = forms.CharField(label="密码",      max_length=256, widget=forms.TextInput(attrs={"placeholder":"密码"}))
