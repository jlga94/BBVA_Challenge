from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.models import SpacePlans
from project_name.apps.core.utils.ClearaFileInputOne import CustomClearableFileInput
from project_name.apps.core import constants as core_constants
from project_name.apps.ubigeo.models import Country, State, City
from .models import (
    User, UserProfile
)


class UserCreationAdminForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserCreationAdminForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email', 'required': True,
             'class': 'form-control'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password',
             'required': True, 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Repeat Password',
             'required': True, 'class': 'form-control'})
        if self.instance.id:
            self.fields['email'].widget.attrs.update({'readonly': True})
            self.fields['password1'].required = False
            self.fields['password2'].required = False

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = _("Passwords don't match")
            self.add_error('password1', msg)
            self.add_error('password2', msg)
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeAdminForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label=_("Password"), help_text=_(
        "Raw passwords are not stored, so there is no way to see "
        "this user's password, but you can change the password "
        "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.HiddenInput(), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email', 'required': True,
             'class': 'form-control'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password', 'class': 'form-control',
             'onfocus': "if(this.getAttribute('type')==='text') "
                        "this.setAttribute('type','password'); "
                        "this.setAttribute('value','')"
             })
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Repeat Password', 'class': 'form-control',
             'onfocus': "if(this.getAttribute('type')==='text')"
                        " this.setAttribute('type','password'); "
                        "this.setAttribute('value','')"
             })
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'First Name', 'class': 'form-control'})
        self.fields['team'].widget.attrs.update(
            {'placeholder': 'Team', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Last Name', 'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update(
            {'placeholder': 'is active', 'class': 'styled'})
        self.fields['is_admin'].widget.attrs.update(
            {'placeholder': 'is admin', 'class': 'styled'})

        if self.instance.id:
            self.fields['email'].widget.attrs.update({'readonly': True})
            self.fields['password1'].required = False
            self.fields['password2'].required = False

    class Meta:
        model = User
        fields = "__all__"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 or password2:
            if password1 != password2:
                msg = _("Passwords don't match")
                self.add_error('password1', msg)
                self.add_error('password2', msg)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    gender_choice = core_constants.SELECT_DEFAULT \
                    + core_constants.TYPE_GENDER_OPTIONS
    first_name = forms.CharField(label='First Name', widget=forms.TextInput)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput, required=False)
    # gender_type = forms.ChoiceField(label="Gender", widget=forms.Select)
    # logo_profile = forms.FileField(widget=CustomClearableFileInput, required=False)
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        empty_label=core_constants.NAME_SELECT_DEFAULT,
        required=False
    )
    state = forms.ModelChoiceField(
        queryset=State.objects.none(),
        empty_label=core_constants.NAME_SELECT_DEFAULT,
        required=False
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.none(),
        empty_label=core_constants.NAME_SELECT_DEFAULT,
        required=False
    )
    space_plan = forms.ModelChoiceField(
        queryset=SpacePlans.objects.all(),
        empty_label=core_constants.NAME_SELECT_DEFAULT
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Last Name'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Address'})
        self.fields['gender_type'].widget.attrs.update(
            {'placeholder': 'Gender Type'})
        self.fields['home_phone'].widget.attrs.update(
            {'placeholder': 'Home phone'})
        self.fields['mobile_phone'].widget.attrs.update(
            {'placeholder': 'Mobile phone'})
        self.fields['logo_profile'].widget.attrs.update(
            {'placeholder': 'image', 'class': 'file-styled'})
        self.fields['country'].widget.attrs.update(
            {'placeholder': 'country'})
        self.fields['state'].widget.attrs.update(
            {'placeholder': 'state'})
        self.fields['city'].widget.attrs.update(
            {'placeholder': 'state'})
        self.fields['space_plan'].widget.attrs.update(
            {'placeholder': 'space_plan'})

    class Meta:
        model = UserProfile
        fields = ["address", "gender_type", "home_phone",
                  "mobile_phone", "logo_profile", "country",
                  "state", "city", "space_plan"]

    def save(self, user=None, *args, **kwargs):
        profile = super().save(*args, **kwargs)
        if user:
            profile.user = user
        profile.save()
        return profile
