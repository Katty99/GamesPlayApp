from django import forms

from GamesPlayApp.account.models import Profile


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['email_address', 'age', 'password']


class EditProfile(ProfileForm):
    class Meta:
        model = Profile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
