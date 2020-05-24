from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account, Profile


class RegistrationForm(UserCreationForm):
    mobilenumber = forms.CharField(max_length=254, help_text='Required. Add a valid mobile number.')

    class Meta:
        model = Account
        fields = ('mobilenumber', 'username', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('mobilenumber', 'password')

    def clean(self):
        if self.is_valid():
            mobilenumber = self.cleaned_data['mobilenumber']
            password = self.cleaned_data['password']
            if not authenticate(mobilenumber=mobilenumber, password=password):
                raise forms.ValidationError("Invalid login")


class ProfileForm(forms.ModelForm):
    email = forms.EmailField()
    address1 = forms.CharField(max_length=100)
    address2 = forms.CharField(max_length=100)
    landmark = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    zip = forms.CharField(max_length=6)

    class Meta:
        model = Profile
        fields = ('email', 'address1', 'address2', 'landmark', 'city', 'state', 'zip')

# class AccountUpdateForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Account
# 		fields = ('email', 'username', )
#
# 	def clean_email(self):
# 		email = self.cleaned_data['email']
# 		try:
# 			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
# 		except Account.DoesNotExist:
# 			return email
# 		raise forms.ValidationError('Email "%s" is already in use.' % account)
#
# 	def clean_username(self):
# 		username = self.cleaned_data['username']
# 		try:
# 			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
# 		except Account.DoesNotExist:
# 			return username
# 		raise forms.ValidationError('Username "%s" is already in use.' % username)
