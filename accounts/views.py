from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect

from userena.utils import (signin_redirect, get_profile_model, get_user_model,
                           get_user_profile)
from userena import settings as userena_settings
import logging
# Create your views here.

class ProfileListView(ListView):
    """ Lists all profiles """
    context_object_name='profile_list'
    page=1
    paginate_by=50
    template_name='userena/profile_list.html'
    extra_context=None

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProfileListView, self).get_context_data(**kwargs)
        try:
            page = int(self.request.GET.get('page', None))
        except (TypeError, ValueError):
            page = self.page

        if userena_settings.USERENA_DISABLE_PROFILE_LIST \
           and not self.request.user.is_staff:
            raise Http404

        if not self.extra_context: self.extra_context = dict()

        context['page'] = page
        context['paginate_by'] = self.paginate_by
        context['extra_context'] = self.extra_context

        return context

    def get_queryset(self):

        logging.error(get_user_profile(self.request.user).__dict__)
        profile_model = get_profile_model()
        logging.error(profile_model.__dict__)
        logging.error(profile_model.objects.all())
        logging.error(profile_model.__doc__)
##        logging.error(self.__dict__)
##        logging.error(self.request.__dict__)
        queryset = profile_model.objects.get_visible_profiles(self.request.user).select_related()
        return queryset



class ProviderListView(ListView):
    """ Lists all profiles """
    context_object_name='profile_list'
    page=1
    paginate_by=50
    template_name='userena/providers_list.html'
    extra_context=None

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProviderListView, self).get_context_data(**kwargs)
        try:
            page = int(self.request.GET.get('page', None))
        except (TypeError, ValueError):
            page = self.page

        if userena_settings.USERENA_DISABLE_PROFILE_LIST \
           and not self.request.user.is_staff:
            raise Http404

        if not self.extra_context: self.extra_context = dict()

        context['page'] = page
        context['paginate_by'] = self.paginate_by
        context['extra_context'] = self.extra_context

        return context

    def get_queryset(self):

        filter_kwargs = {'usertype': 'chef'}
        profile_model = get_profile_model()

        logging.error('all')
        logging.error(profile_model.objects.all())
##        logging.error(self.__dict__)
##        logging.error(self.request.__dict__)
        ##queryset = profile_model.objects.get_visible_profiles(self.request.user).select_related()
        queryset = profile_model.objects.get_visible_profiles().filter(**filter_kwargs)

        logging.error('cook  - queryset')
        logging.error(queryset)
        return queryset
