"""apollo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Examples:
    # url(r'^$', quick_start.views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('pages.urls')),
    #path('accounts', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('assets/', include('assets.urls')),
    path('assets/', include('django.contrib.auth.urls')),

    # apolloforms
    path('forms/', include('apolloforms.urls')),
    # charts
    path('charts/', include('charts.urls')),

    # DB Store plugin URLs
    url(r'^fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),
    # , namespace='fobi'
    # View URLs
    url(r'^view/', include('fobi.urls.view')),
    # , namespace='fobi'
    # Edit URLs
    url(r'^edit/', include('fobi.urls.edit')),
]
