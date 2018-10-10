from django.contrib import admin

from .models import NewUser, Resource

admin.site.register(NewUser)
admin.site.register(Resource)
