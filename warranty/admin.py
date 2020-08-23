from django.contrib import admin
from .models import Note, Item, ItemLog
# Register your models here.

admin.site.register(Note)
admin.site.register(Item)
admin.site.register(ItemLog)