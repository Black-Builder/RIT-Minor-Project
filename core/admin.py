from django.contrib import admin
from .models import Feedback, Timetable, Newsupdate, Contact, Importantlink

# Register your models here.

admin.site.register(Feedback)
admin.site.register(Timetable)
admin.site.register(Newsupdate)
admin.site.register(Contact)
admin.site.register(Importantlink)
