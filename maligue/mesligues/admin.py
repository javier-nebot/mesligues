from django.contrib import admin

from .models import Participant, Ligue, Match


admin.site.register(Participant)
admin.site.register(Ligue)
admin.site.register(Match)
