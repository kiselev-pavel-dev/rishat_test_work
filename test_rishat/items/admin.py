from django.contrib import admin

from .models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "description", "price", "currency")
    search_fields = ("name",)
    empty_value_display = "-пусто-"


class OrderAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "product")
    empty_value_display = "-пусто-"


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
