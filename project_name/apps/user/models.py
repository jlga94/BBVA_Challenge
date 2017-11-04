from random import randint

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, AbstractUser)
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.mail import send_mail
from django.db import models
from django.utils import six
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core import constants as core_constants
from project_name.apps.core.manager import UserManager
from project_name.apps.core.models import Team, SpacePlans
from project_name.apps.ubigeo.models import Country, State, City
from project_name.apps.core.utils.fields import BaseModel2
from project_name.apps.core.utils.upload_folder import upload_user_profile

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class CustomUser(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
    )
    first_name = models.CharField(max_length=40, blank=True,
                                  null=True, unique=False)
    last_name = models.CharField(max_length=40, blank=True,
                                 null=True, unique=False)
    display_name = models.CharField(_('display name'), max_length=14,
                                    blank=True, null=True, unique=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_invited = models.BooleanField(default=False)
    team = models.ManyToManyField(
        Team, verbose_name=_('teams'), blank=True, related_name='team'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        full_name = '{0:s} {1:s}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    @property
    def name(self):
        if self.first_name:
            return self.first_name
        elif self.display_name:
            return self.display_name
        return 'You'

    def guess_display_name(self):
        if self.display_name:
            return
        if self.first_name and self.last_name:
            dn = "%s %s" % (self.first_name, self.last_name[0])
        elif self.first_name:
            dn = self.first_name
        else:
            dn = 'You'
        self.display_name = dn.strip()

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def get_profile(self):
        profile = UserProfile.objects.select_related('user').get(pk=self)
        return profile

    def get_teams(self):
        return self.team.filter(is_deleted=False)

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        abstract = True


class User(CustomUser):
    class Meta(CustomUser.Meta):
        swappable = AUTH_USER_MODEL
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'auth_user'


class UserCompany(BaseModel2):
    user = models.ForeignKey(
        User, verbose_name='user',
        related_name="%(app_label)s_%(class)s_user",
        on_delete=models.SET_NULL, blank=True, null=True)
    document_choice = core_constants.SELECT_DEFAULT \
                      + core_constants.TRIBUTE_PERSON_OPTIONS
    document_type = models.CharField(
        max_length=10, null=True, blank=True, choices=document_choice)
    document_number = models.CharField(max_length=20, null=True, blank=True)
    trade_name = models.CharField(_(' trade_name'), max_length=255, null=True, blank=True)
    contributor_type = models.CharField(_('contributor_type'), max_length=80, null=True, blank=True)
    status_contributor = models.CharField(_('status_contributor'), max_length=80, null=True, blank=True)
    condition = models.CharField(_('condition'), max_length=80, null=True, blank=True)
    address_fiscal = models.CharField(_('address_fiscal'), max_length=255, null=True, blank=True)
    affiliate_ple = models.CharField(_('affiliate_ple'), max_length=255, null=True, blank=True)
    padrones = models.CharField(_('padrones'), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("User Company")
        verbose_name_plural = _("Users Company")
        unique_together = ['user', 'document_type', 'document_number']

    def __str__(self):
        return force_text(self.trade_name)


class UserProfile(BaseModel2):
    profile_choice = core_constants.SELECT_DEFAULT \
                     + core_constants.TYPE_IDENTITY_DOCUMENT_OPTIONS
    gender_choice = core_constants.SELECT_DEFAULT \
                    + core_constants.TYPE_GENDER_OPTIONS
    user = models.OneToOneField(
        User, primary_key=True, verbose_name='user',
        related_name="%(app_label)s_%(class)s_user")
    address = models.CharField(max_length=200, blank=True, null=True)
    gender_type = models.CharField(
        max_length=10, null=True, blank=True, choices=gender_choice)
    home_phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)
    logo_profile = models.ImageField(
        upload_to=upload_user_profile, blank=True, null=True)
    country = models.ForeignKey(
        Country, verbose_name='country',
        related_name="%(app_label)s_%(class)s_country",
        on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(
        State, verbose_name='state',
        related_name="%(app_label)s_%(class)s_state",
        on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(
        City, verbose_name='city',
        related_name="%(app_label)s_%(class)s_city",
        on_delete=models.SET_NULL, blank=True, null=True)
    space_plan = models.ForeignKey(
        SpacePlans, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_space_plan")

    def __str__(self):
        return force_text(self.user.email)

    def get_full_name(self):
        return "{0}{1}".format(self.user.first_name, self.user.last_name)

    @property
    def get_user_email(self):
        return self.user.email

    def get_logo_profile_url(self):
        if self.logo_profile:
            return self.logo_profile.url
        else:
            return static('themes/img/default/default-user-male.jpg')

    def thumb(self):
        if self.logo_profile:
            return format_html(u'<img src="{0:s}" width=60 height=60 />'
                               .format(self.logo_profile.url))
        else:
            img = static('assets/img/uncompressed/default_profile.png')
            return format_html(
                u'<img src="{0:s}" width=60 height=60 />'.format(img))

    thumb.short_description = _('Thumbnail')
    thumb.allow_tags = True

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        db_table = 'user_profile'


# class UserInvitationCode(BaseModel2):
#     user = models.ForeignKey(
#         User, verbose_name='user', related_name="%(app_label)s_%(class)s_user")
#     email = models.EmailField(verbose_name='email address', max_length=255)
#     code_invitation = models.CharField(max_length=255, null=True, blank=True)
#     accept_invitation = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name = _("User Code Invitation")
#         verbose_name_plural = _("User Code Invitations")
#         unique_together = ['user', 'email', 'code_invitation']
#
#     def __str__(self):
#         return force_text(self.user.email)


# class UserGuest(BaseModel2):
#     role_choice = core_constants.SELECT_DEFAULT \
#                   + core_constants.TYPE_ROLE_OPTIONS
#     user = models.ForeignKey(
#         User, verbose_name='user', related_name="%(app_label)s_%(class)s_user")
#     email = models.EmailField(
#         verbose_name='email address', max_length=255)
#     is_valid = models.BooleanField(default=False)
#     role_type = models.CharField(
#         max_length=30, null=True, blank=True,
#         choices=role_choice, default=core_constants.ROLE_ONE_STRING)
#     company = models.ManyToManyField(UserCompany)
#
#     class Meta:
#         verbose_name = _("User Guest")
#         verbose_name_plural = _("Users Guest")
#         unique_together = ['user', 'email', 'role_type']
#
#     def __str__(self):
#         return force_text(self.user.email)
