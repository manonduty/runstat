"""root URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from django.views.generic import TemplateView

from runstat.views import group_members, member, AboutPage, statistic, test

urlpatterns = [
    url(r'^tocms/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='runstat/runners.html')),
    url(r'^$', group_members, name='group_members'),
    url(r'^member/(?P<pk>\d+)/$', member, name='member'),
    url(r'^about/$', AboutPage.as_view(), name='about'),
    url(r'^statistic/$', statistic, name='statistic'),
    url(r'^test/$', test, name='test'),
]
