from django.contrib import admin
from .models import StudentDetails


class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','mobile','email','password']


admin.site.register(StudentDetails,StudentAdmin)
