"""cloudbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
#from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from . views import *
#import cloudbank.views, cloudbank.apilist

#admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing),
    path('api/v1/createnewwallet/', createnewwallet),
    path('api/v1/checkwallet/', checkwallet),
    path('login', login),
    path('logout', logout),

    # url(r'^admin/', admin.site.urls),
    # url(r'^$', cloudbank.views.landing),
    # url(r'^login', cloudbank.views.login),
    # url(r'^logout', cloudbank.views.logout),
    # url(r'^transactions', cloudbank.views.ws),
    #
    #
    # #REST API
    # url(r'^api/v1/checkwallet/', cloudbank.views.checkwallet),
    # url(r'^api/v1/sendcloudcoin', cloudbank.views.sendcloudcoin),
    # url(r'^api/v1/createnewwallet/', cloudbank.views.createnewwallet),
    # url(r'^api/v1/alltransactions/', cloudbank.apilist.alltransactions),
    # url(r'^api/v1/gettransaction/(?P<tid>\w+)/$', cloudbank.apilist.gettransaction,  name='gettransaction'),
    # url(r'^api/v1/getwalletfrompkey/(?P<pkey>\w+)/$', cloudbank.apilist.getwalletfrompkey, name='getwalletfrompkey'),
    # url(r'^api/v1/getpublickeyfromprikey/(?P<private_key>\w+)/$', cloudbank.apilist.getpublickeyfromprikey, name='getpublickeyfromprikey'),
    # url(r'^api/v1/getbalancefromwallet/(?P<wallet>\w+)/$', cloudbank.apilist.getbalancefromwallet, name='getbalancefromwallet'),
    # url(r'^api/v1/getwalletdetails/(?P<wallet>\w+)/$', cloudbank.apilist.getwalletdetails, name='getwalletdetails'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



"""cloudbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#-*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
import cloudbank.views, cloudbank.apilist
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', cloudbank.views.landing),
    url(r'^login', cloudbank.views.login),
    url(r'^logout', cloudbank.views.logout),
    url(r'^transactions', cloudbank.views.ws),


    #REST API
    url(r'^api/v1/checkwallet/', cloudbank.views.checkwallet),
    url(r'^api/v1/sendcloudcoin', cloudbank.views.sendcloudcoin),
    url(r'^api/v1/createnewwallet/', cloudbank.views.createnewwallet),
    url(r'^api/v1/alltransactions/', cloudbank.apilist.alltransactions),
    url(r'^api/v1/gettransaction/(?P<tid>\w+)/$', cloudbank.apilist.gettransaction,  name='gettransaction'),
    url(r'^api/v1/getwalletfrompkey/(?P<pkey>\w+)/$', cloudbank.apilist.getwalletfrompkey, name='getwalletfrompkey'),
    url(r'^api/v1/getpublickeyfromprikey/(?P<private_key>\w+)/$', cloudbank.apilist.getpublickeyfromprikey, name='getpublickeyfromprikey'),
    url(r'^api/v1/getbalancefromwallet/(?P<wallet>\w+)/$', cloudbank.apilist.getbalancefromwallet, name='getbalancefromwallet'),
    url(r'^api/v1/getwalletdetails/(?P<wallet>\w+)/$', cloudbank.apilist.getwalletdetails, name='getwalletdetails'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib import admin
from django.urls import path
from django.conf import settings
#from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
#import cloudbank.views, cloudbank.apilist
from core import views
#import cloudbank.views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name="landing"),
    path("test", views.test, name="test"),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', cloudbank.views.landing),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
url(r'^login', cloudbank.views.login),
url(r'^logout', cloudbank.views.logout),
url(r'^transactions', cloudbank.views.ws),

#REST API
url(r'^api/v1/checkwallet/', cloudbank.views.checkwallet),
url(r'^api/v1/sendcloudcoin', cloudbank.views.sendcloudcoin),
url(r'^api/v1/createnewwallet/', cloudbank.views.createnewwallet),
url(r'^api/v1/alltransactions/', cloudbank.apilist.alltransactions),
url(r'^api/v1/gettransaction/(?P<tid>\w+)/$', cloudbank.apilist.gettransaction,  name='gettransaction'),
url(r'^api/v1/getwalletfrompkey/(?P<pkey>\w+)/$', cloudbank.apilist.getwalletfrompkey, name='getwalletfrompkey'),
url(r'^api/v1/getpublickeyfromprikey/(?P<private_key>\w+)/$', cloudbank.apilist.getpublickeyfromprikey, name='getpublickeyfromprikey'),
url(r'^api/v1/getbalancefromwallet/(?P<wallet>\w+)/$', cloudbank.apilist.getbalancefromwallet, name='getbalancefromwallet'),
url(r'^api/v1/getwalletdetails/(?P<wallet>\w+)/$', cloudbank.apilist.getwalletdetails, name='getwalletdetails'),
"""
