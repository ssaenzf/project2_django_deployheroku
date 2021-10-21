"""bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from authentication import views as authentication_views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', authentication_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', authentication_views.signup, name='signup'),
    url(r'^account_activation_sent/$', authentication_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        authentication_views.activate, name='activate'),
    path('orders/', include('orders.urls')),
    path('catalog/', include('catalog.urls')),
    path('authentication/', include('authentication.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
