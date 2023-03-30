from django.contrib import admin
from .models import Query

# Register your models here.


class QueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')


admin.site.register(Query, QueryAdmin)
