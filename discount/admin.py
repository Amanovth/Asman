from django.contrib import admin

from .models import Partners, PartnerCategory


@admin.register(PartnerCategory)
class PartnerCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    readonly_fields = ('qr', 'total_visits',)
