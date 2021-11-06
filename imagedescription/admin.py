from django.contrib import admin
from .models import Images, Person, SendMail

# Register your models here.
admin.site.register(Images)
admin.site.register(Person)
admin.site.register(SendMail)
