from django.contrib import admin
from .models import report,Suggestion,Faculty
# Register your models here.

admin.site.site_header = "CampusShield Admin"
admin.site.site_title = "CampusShield Portal"
admin.site.index_title = "Welcome to CampusShield Admin Panel"

admin.site.register(report)
admin.site.register(Suggestion)
admin.site.register(Faculty)


