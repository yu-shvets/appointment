from django.contrib import admin
from .models import Appointments, EventDate, TimeRange, SubmittedForms

# Register your models here.
admin.site.register(Appointments)
admin.site.register(EventDate)
admin.site.register(TimeRange)
admin.site.register(SubmittedForms)
