from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class UserSignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')



    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2' )

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
