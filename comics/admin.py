from django.contrib import admin

from .models import Arc, Character, Creator, Team, Publisher, Series, Issue

admin.site.site_header = 'Tenma'
admin.site.site_title = 'Tenma'

admin.site.register(Arc)
admin.site.register(Character)
admin.site.register(Creator)
admin.site.register(Team)
admin.site.register(Publisher)
admin.site.register(Series)
admin.site.register(Issue)