from django.contrib import admin
from .models import Listing, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listings')
    list_per_page = 25
    list_filter = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Listing)
