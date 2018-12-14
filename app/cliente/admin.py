from django.contrib import admin
from .models import Ciudad, Comuna, Cliente

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Cliente)