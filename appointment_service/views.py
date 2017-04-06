from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms import ModelForm
from .models import Appointments, EventDate, TimeRange, SubmittedForms
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import generics
from .serializers import AppointmentsSerializer, EventDateSerializer, TimeRangeSerializer

# Create your views here.


class AppointmentListView(ListView):

    model = Appointments

    template_name = 'index.html'


class AppointmentDetailView(DetailView):

    model = Appointments

    template_name = 'appointment.html'


class NewAppointmentForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ['title', 'description']


class NewAppointmentCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'index.html'

    model = Appointments
    form_class = NewAppointmentForm
    template_name = 'new_appointment.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect('/')


class NewDateForm(ModelForm):
    class Meta:
        model = EventDate
        fields = ['date']
    appointment = forms.ModelChoiceField(queryset=Appointments.objects.all())

    def save(self, commit=True):
        instance = super().save(commit=False)
        appointment = self.cleaned_data['appointment']
        instance.appointment = Appointments.objects.get(pk=appointment.id)
        instance.save(commit)
        return instance


class NewTimeForm(ModelForm):
    class Meta:
        model = TimeRange
        fields = ['start_time', 'end_time']
    appointment = forms.ModelChoiceField(queryset=Appointments.objects.all())

    def save(self, commit=True):
        instance = super().save(commit=False)
        appointment = self.cleaned_data['appointment']
        instance.appointment = Appointments.objects.get(pk=appointment.id)
        instance.save(commit)
        return instance


class DateCreate(CreateView):

    model = EventDate
    form_class = NewDateForm
    template_name = 'new_date.html'

    def get_success_url(self):
            return reverse('home')


class TimeCreate(CreateView):

    model = TimeRange
    form_class = NewTimeForm
    template_name = 'new_time.html'

    def get_success_url(self):
            return reverse('home')


def submit_form(request):
    if request.method == 'POST':

        data = {'date': request.POST.get('date'),
                'time_range': request.POST.get('time_range'),
                'full_name': request.POST.get('full_name'),
                }

        email = request.POST.get('email')

        try:
            validate_email(email)
        except Exception:
            raise ValidationError('Invalid email', code='invalid')
        else:
            data['email'] = email

        form = SubmittedForms(**data)
        form.save()

    return HttpResponseRedirect(reverse('home'))


class SubmittedListView(ListView):

    model = SubmittedForms

    template_name = 'submitted.html'


# REST API
class AppointmentsList(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer


class AppointmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer


class EventDateList(generics.ListCreateAPIView):
    queryset = EventDate.objects.all()
    serializer_class = EventDateSerializer


class TimeRangeList(generics.ListCreateAPIView):
    queryset = TimeRange.objects.all()
    serializer_class = TimeRangeSerializer


