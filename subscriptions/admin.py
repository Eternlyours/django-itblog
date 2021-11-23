from django.contrib import admin

from subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subscription, SubscriptionAdmin)
