from django.contrib import admin
from .models import Subscriber
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    list_filter = ('subscribed_at')
    list_editable = ('email')

admin.site.register(Subscriber)