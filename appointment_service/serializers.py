from rest_framework import serializers
from .models import Appointments, EventDate, TimeRange


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ('id', 'title', 'description', 'user')


class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = ('id', 'date', 'appointment')


class TimeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeRange
        fields = ('id', 'start_time', 'end_time', 'appointment')
