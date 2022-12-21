from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User

list_atr = ['OpenDate', 'CityGroup', 'P1',
            'P2', 'P6', 'P7', 'P11', 'P17',
            'P21', 'P22', 'P28']

class NewUserForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super(NewUserForm, self).__init__(*args, **kargs)
        del self.fields['password2']

    username = forms.CharField(min_length=4, max_length=25)

    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')

    password1 = forms.CharField(label='Password', min_length=4, max_length=25,
                    widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')


class PredictTableForm(forms.Form):
    def __init__(self, atr_dict: dict = None, *args, **kwargs):
        super(PredictTableForm, self).__init__(*args, **kwargs)
        if atr_dict:
            for atr in atr_dict:
                self.fields[atr].initial = atr_dict[atr]

    OpenDate = forms.FloatField(label='Open Date', min_value=0, max_value=1, initial=0.11)
    CityGroup = forms.IntegerField(label='City Group', min_value=0, max_value=1, initial=1)
    P1 = forms.FloatField(min_value=0, max_value=1, initial=0.27)
    P2 = forms.FloatField(min_value=0, max_value=1, initial=0.56)
    P6 = forms.FloatField(min_value=0, max_value=1, initial=0.09)
    P7 = forms.FloatField(min_value=0, max_value=1, initial=0.87)
    P11 = forms.FloatField(min_value=0, max_value=1, initial=0.71)
    P17 = forms.FloatField(min_value=0, max_value=1, initial=0.18)
    P21 = forms.FloatField(min_value=0, max_value=1, initial=0.88)
    P22 = forms.FloatField(min_value=0, max_value=1, initial=0.67)
    P28 = forms.FloatField(min_value=0, max_value=1, initial=0.19)

class ProfileForm(UserChangeForm):
    def __init__(self, default_username: str = None, default_email: str = None, *args, **kwargs):

        super(ProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password']

        if default_username:
            self.fields['new_username'].initial = default_username
        if default_email:
            self.fields['new_email'].initial = default_email

    new_username = forms.CharField(min_length=4, max_length=25)

    new_email = forms.EmailField(max_length=64)

    class Meta:
        model = User
        fields = ('new_username', 'new_email')

