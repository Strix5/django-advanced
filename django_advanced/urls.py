"""
URL configuration for django_advanced project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('permis.urls', namespace='permis')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('movies/', include('movies.urls', namespace='movies')),
    path('htmx/', include('htmx.urls', namespace='htmx1'))
)
