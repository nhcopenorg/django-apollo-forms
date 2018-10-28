from django.views.generic import ListView
from assets import models
from fobi.contrib.plugins.form_handlers.db_store.models import SavedFormDataEntry
from django.contrib.messages.views import SuccessMessageMixin


class HomePageView(SuccessMessageMixin, ListView):
    model = models.Asset
    template_name = 'home.html'
    template_base = "base_public.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        # if self.request.method == 'POST':
        #    form = AuthenticationForm(data=self.request.POST)
        #    if form.is_valid(self):
        #        user = form.get_user(self)
        #        auth_login(self.request, user)
        if self.request.user.is_authenticated:
            self.template_base = "base_private.html"
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['base_template'] = self.template_base
        return context


class DataPageView(ListView):
    model = SavedFormDataEntry
    template_name = 'data.html'
