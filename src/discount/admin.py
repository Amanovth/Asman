from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Partner, PartnerCategory, Status

admin.site.register(Status)


@admin.register(PartnerCategory)
class PartnerCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Partner)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'get_html_img', 'id')
    list_display_links = ('title',)
    readonly_fields = ('qr', 'total_visits',)

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width='130'>")
        return None

    get_html_img.short_description = 'Изображение'
