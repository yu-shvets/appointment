"""appointment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required
from appointment_service.views import AppointmentListView, AppointmentDetailView, NewAppointmentCreate, DateCreate, \
    TimeCreate, submit_form, SubmittedListView, AppointmentsList, AppointmentsDetail, EventDateList, TimeRangeList

urlpatterns = [

    # User Related urls
    url(r'^users/login/$', login, {'authentication_form': AuthenticationForm}, name='login'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
        name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),
    url(r'^users/profile/$', login_required(TemplateView.as_view(
        template_name='registration/profile.html')), name='profile'),

    url(r'^$', AppointmentListView.as_view(), name='home'),

    url(r'^appointment/(?P<pk>\d+)/info/$', AppointmentDetailView.as_view(), name='appointment'),

    url(r'^new_appointment/$', NewAppointmentCreate.as_view(), name='new_appointment'),

    url(r'^new_date/$', DateCreate.as_view(), name='new_date'),

    url(r'^new_time/$', TimeCreate.as_view(), name='new_time'),

    url(r'^submit_form/$', submit_form, name='submit_form'),

    url(r'^submitted_appointments/$', login_required(SubmittedListView.as_view()), name='submitted'),

    # REST API urls
    url(r'^api/appointments/$', AppointmentsList.as_view()),
    url(r'^api/appointments/(?P<pk>[0-9]+)/$', AppointmentsDetail.as_view()),
    url(r'^api/appointments/dates/$', EventDateList.as_view()),
    url(r'^api/appointments/time/$', TimeRangeList.as_view()),


    url(r'^admin/', admin.site.urls),
]
