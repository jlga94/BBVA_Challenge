from allauth.account.views import PasswordResetView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from . import forms
from project_name.apps.ubigeo.models import Country, State, City
from .models import UserProfile


class IndexView(TemplateView):
    template_name = 'themes/dashboard/test.html'

    @staticmethod
    def doubler(number):
        return number * 2

    def get(self, request, *args, **kwargs):
        st = "{0}\{1}".format(str(settings.STATIC_ROOT), str("tb_city.csv"))
        import csv
        with open(st) as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            for row in reader:
                city_id = row[0]
                city_country_id = row[1]
                city_state_id = row[2]
                city_name = str(row[3])
                city_latitude = row[4]
                city_longitude = row[5]
                city_status = row[6]

                _country = Country.objects.get(id=city_country_id)
                _state = State.objects.get(id=city_state_id)
                _city = City()
                _city.id = city_id
                _city.country = _country
                _city.state = _state
                _city.city = city_name.replace("`", "").strip()
                _city.latitude = city_latitude
                _city.longitude = city_longitude
                _city.status = city_status
                _city.save()
        f.close()
        print("Finished")
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'themes/pages/user/profile/user_profile.html'
    model = UserProfile
    form_class = forms.UserProfileForm
    context_object_name = "form_profile"

    def get_object(self, **kwargs):
        return UserProfile.objects.filter(uid=kwargs.get('uuid')).first()

    def get_success_url(self):
        kwargs = {'uuid': self.object.uuid}
        return reverse_lazy('user_app:profile', kwargs=kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     self.form_profile = self.get_form(form_class)
    #     return super().render_to_response(self.get_context_data())
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form_profile"] = self.form_profile
    #     return context


# class UserProfileView(TemplateView):
#     template_name = 'themes/pages/user/profile/user_profile.html'
#
#     def get(self, request, *args, **kwargs):
#         user_session = self.request.user
#         user = User.objects.get(email=user_session)
#         profile = UserProfile.objects.get(user=user)
#         initial = dict(first_name=user.first_name, last_name=user.last_name)
#         self.profile_form = forms.UserProfileForm(
#             instance=profile, initial=initial)
#         return super().render_to_response(self.get_context_data())
#
#     def post(self, request, *args, **kwargs):
#         user_session = self.request.user
#         user = User.objects.get(email=user_session)
#         profile = UserProfile.objects.get(user=user)
#         self.profile_form = forms.UserProfileForm(request.POST,instance=profile)
#         if self.profile_form.is_valid():
#             self.profile_form.save(user=user)
#         else:
#             self.profile_form = forms.UserProfileForm(instance=profile)
#
#         if form.is_valid():
#             return self.frm_valid(form)
#         else:
#             return self.frm_invalid(form)
#
#     def frm_valid(self, form):
#         with transaction.atomic():
#             self.object = form.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#     def frm_invalid(self, form):
#         self.form = form
#         return super().render_to_response(self.get_context_data())
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["profile_form"] = self.profile_form
#         return context


class UserCoinKasView(TemplateView):
    template_name = 'themes/pages/user/profile/user_coinkass.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserInvitedView(TemplateView):
    template_name = 'themes/pages/user/profile/user_invited.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserCodeCompanyView(TemplateView):
    template_name = 'themes/pages/user/profile/user_code_company.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserCompanyView(TemplateView):
    template_name = 'themes/pages/user/profile/user_company.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserCompanyTreeView(TemplateView):
    template_name = 'themes/pages/user/profile/user_company_tree.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserChangePasswordView(PasswordResetView):
    template_name = 'themes/pages/user/profile/user_change_password.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
