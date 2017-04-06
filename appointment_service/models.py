from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Appointments(models.Model):

    class Meta(object):
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        ordering = ['datetime']

    title = models.CharField(
        max_length=256,
        verbose_name="Title"
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description"
    )

    datetime = models.DateTimeField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}".format(self.title)


class EventDate(models.Model):

    class Meta(object):
        verbose_name = "Date of event"
        verbose_name_plural = "Dates of event"

    date = models.DateField()

    appointment = models.ForeignKey(
        Appointments,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}".format(self.date)


class TimeRange(models.Model):

    class Meta(object):
        verbose_name = "Time range "
        verbose_name_plural = "Time ranges"

    start_time = models.TimeField()

    end_time = models.TimeField()

    appointment = models.ForeignKey(
        Appointments,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}-{}".format(self.start_time, self.end_time)


class SubmittedForms(models.Model):

    class Meta(object):
        verbose_name = "Submitted form "
        verbose_name_plural = "Submitted forms"

    date = models.CharField(
        max_length=256,
        verbose_name="Date"
    )

    time_range = models.CharField(
        max_length=256,
        verbose_name="Time range"
    )

    full_name = models.CharField(
        max_length=256,
        verbose_name="Full name"
    )

    email = models.EmailField(
        max_length=254
    )

    def __str__(self):
        return "{}".format(self.full_name)
