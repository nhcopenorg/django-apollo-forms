import logging
from django.views.generic import ListView
from fobi.contrib.plugins.form_handlers.db_store.models import SavedFormDataEntry

from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from fobi.base import (
    get_form_handler_plugin_widget,
    get_form_wizard_handler_plugin_widget,
)

from . import UID
from nine import versions

from django.shortcuts import redirect
from assets import models
from fobi.views import dashboard, view_form_entry, create_form_entry, import_form_entry, edit_form_entry

if versions.DJANGO_GTE_1_10:
    from django.shortcuts import render
else:
    from django.shortcuts import render_to_response

if versions.DJANGO_GTE_1_10:
    from django.shortcuts import render
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse
    from django.shortcuts import render_to_response

logger = logging.getLogger(__name__)


# @login_required
class FormSubmitedListView(ListView):
    # queryset = models.Asset.objects.all()
    model = SavedFormDataEntry
    # assets = models.Asset
    # assets.users.objects.filter(users='id')
    template_name = 'forms/forms_submitted.html'
    context_object_name = 'entries'
    queryset = SavedFormDataEntry.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)

    """
    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['assets'] = models.Asset.objects.all()
        return super(FormSubmitedListView, self).get_context_data(**kwargs)
        # context = super(FormulariosListView, self).get_context_data(**kwargs)
        # context['entries'] = self.model
        # context = {'asset': self.assets}
        # return context
    """


class FormAssignedListView(ListView):
    # model = models.FormEntry
    model = models.Asset
    template_name = 'forms/forms_assigned.html'
    context_object_name = 'asset'
    queryset = models.Asset.objects.all()

    def get_queryset(self):
        return self.queryset.filter(users__exact=self.request.user)


# *****************************************************************************
# *************************** Form handler views ******************************
# *****************************************************************************

# entries_permissions = [
#    'db_store.add_savedformdataentry',
#    'db_store.change_savedformdataentry',
#    'db_store.delete_savedformdataentry',
# ]

# Create your views here.
# @permissions_required(satisfy=SATISFY_ANY, perms=entries_permissions)
@login_required
def view_saved_form_data_entries(
        request, form_entry_id=None, theme=None,
        template_name='apolloforms/view_form_apollo_entries.html'):
    """View saved form data entries.

    :param django.http.HttpRequest request:
    :param int form_entry_id: Form ID.
    :param fobi.base.BaseTheme theme: Subclass of ``fobi.base.BaseTheme``.
    :param string template_name:
    :return django.http.HttpResponse:
    """
    entries = SavedFormDataEntry._default_manager \
        .select_related('form_entry') \
        .filter(form_entry__user__pk=request.user.pk)

    # jsanchez improve: getting the user_id from db_store_savedformdataentry

    if form_entry_id:
        entries = entries.filter(form_entry__id=form_entry_id)

    context = {'entries': entries, 'form_entry_id': form_entry_id}

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    widget = get_form_handler_plugin_widget(
        UID, request=request, as_instance=True, theme=theme
    )

    if widget and widget.view_saved_form_data_entries_template_name:
        template_name = widget.view_saved_form_data_entries_template_name

    if versions.DJANGO_GTE_1_10:
        return render(request, template_name, context)
    else:
        return render_to_response(
            template_name, context, context_instance=RequestContext(request)
        )


def apollo_dashboard(request, theme=None, template_name='forms/dashboard.html'):
    return dashboard(request, theme, template_name)


# *******************
# Forms
# *******************

def apollo_view_form(request, form_entry_slug, theme=None, template_name='forms/view_form.html'):
    resolver = view_form_entry(request, form_entry_slug, theme, template_name)
    if request.method == 'POST':
        if 'submitted' in str(resolver.url):
            return redirect(
                # reverse('fobi.form_entry_submitted', args=[form_entry.slug])
                reverse('apollo_forms_submitted')
            )
    return resolver


def apollo_create_form_entry(request, theme=None, template_name='forms/create_form_entry.html'):
    resolver = create_form_entry(request, theme, template_name)
    if request.method == 'POST':
        if not resolver.url is None:
            form_entry_pk = resolver.url.split('/')[4]
            return redirect('apollo_edit_form_entry', form_entry_id=form_entry_pk)
    return resolver


def apollo_import_form_entry(request, template_name='forms/import_form_entry.html'):
    resolver = import_form_entry(request, template_name)
    return resolver


def apollo_edit_form_entry(request, form_entry_id, theme=None, template_name='forms/edit_form_entry.html'):
    resolver = edit_form_entry(request, form_entry_id, theme, template_name)
    # if request.method == 'POST':
    # if 'submitted' in str(resolver.url):
    # return redirect(
    #    'fobi.edit_form_entry', form_entry_id=form_entry.pk
    # )
    return resolver
