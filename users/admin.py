from django.contrib import admin

from users.models import ContactData, CustomUser

admin.site.register(ContactData)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email"]
