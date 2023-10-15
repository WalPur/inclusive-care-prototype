from django.contrib import admin

from care.models import (
    Article,
    CenterRating,
    Event,
    EventRegistration,
    ReabilatationCenter,
    Tag,
)

admin.site.register(ReabilatationCenter)
admin.site.register(CenterRating)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(EventRegistration)
