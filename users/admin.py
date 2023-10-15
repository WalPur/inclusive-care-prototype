from django.contrib import admin

from users.models import ContactData, CustomUser

admin.site.register(ContactData)
admin.site.register(CustomUser)
