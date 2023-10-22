from django.contrib import admin
 # user: nowell pass:nowell12345


# register the new database:
from .models import Category, Item

admin.site.register(Category)
admin.site.register(Item)
# Register your models here.
