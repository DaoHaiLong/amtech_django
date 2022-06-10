from django.contrib import admin

from .models import Quote, Quote_Items

# # Register your models here.
admin.site.register(Quote)
admin.site.register(Quote_Items)