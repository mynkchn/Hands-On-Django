from django.contrib import admin
from .models import *

# Register your models here.
class EmpAdmin(admin.ModelAdmin) :
    list_display=('name','address','working')
    search_fields=('name',)
    list_filter=('course',)
admin.site.register(Emp,EmpAdmin)

class TestiApp(admin.ModelAdmin) :
    list_display=('name',)

admin.site.register(Testimonial,TestiApp)
