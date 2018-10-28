from django.urls import path
from . import views
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from fobi.views import (
    add_form_element_entry,
    add_form_handler_entry,
    add_form_wizard_form_entry,
    add_form_wizard_handler_entry,
    create_form_entry,
    create_form_wizard_entry,
    dashboard,
    delete_form_element_entry,
    delete_form_entry,
    delete_form_handler_entry,
    delete_form_wizard_entry,
    delete_form_wizard_form_entry,
    delete_form_wizard_handler_entry,
    edit_form_element_entry,
    edit_form_entry,
    edit_form_handler_entry,
    edit_form_wizard_entry,
    edit_form_wizard_handler_entry,
    export_form_entry,
    export_form_wizard_entry,
    form_importer,
    form_wizards_dashboard,
    import_form_entry,
    import_form_wizard_entry
)

# from fobi.contrib.plugins.form_handlers.db_store.views import view_saved_form_data_entries

urlpatterns = [
    path('submitted/', views.FormSubmitedListView.as_view(), name='apollo_forms_submitted'),
    path('assigned/', views.FormAssignedListView.as_view(), name='apollo_forms_assigned'),
    # url(r'^$',views.FormulariosListView.as_view(), name='data'),
    # path('formsaved', views.DataPageFormView.as_view(), name='data_form'),
    # dashboard to create form
    url(_(r'^dashboard/'), views.apollo_dashboard, name='apollo_dashboard'),
    #url(_(r'^$'), view=views.apollo_dashboard, name='fobi.dashboard'),
    # hack to redirect from create form fobi to application apollo dashboard
    # come edit/ from fobi edit
    # url(_(r'^'), views.apollo_dashboard, name='apollo_dashboard'),
    # View form entry
    url(_(r'^(?P<form_entry_id>\d+)/$'),
        views.view_saved_form_data_entries),

    # rewriting context rules for view form
    url(_(r'^(?P<form_entry_slug>[\w_\-]+)/$'),
        views.apollo_view_form,
        name='apollo_view_form'),

    # create form
    url(_(r'^create'),
        views.apollo_create_form_entry,
        name='apollo_create_form_entry'),

    # import form
    url(_(r'^import'),
        views.apollo_import_form_entry,
        name='apollo_import_form_entry'),

    # edit form
    url(_(r'^edit/(?P<form_entry_id>\d+)/$'),
        views.apollo_edit_form_entry,
        name='apollo_edit_form_entry'),

    url(_(r'^forms/edit/(?P<form_entry_id>\d+)/$'),
        views.apollo_edit_form_entry,
        name='fobi.edit_form_entry'),

]
