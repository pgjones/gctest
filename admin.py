from django.contrib import admin
from gctest.models import App, Build, Developer, News

admin.site.register(App)
admin.site.register(Build)
admin.site.register(Developer)
admin.site.register(News)
