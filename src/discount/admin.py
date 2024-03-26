from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Partner, PartnerCategory


@admin.register(PartnerCategory)
class PartnerCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Partner)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'get_html_img', 'id')
    list_display_links = ('title',)
    readonly_fields = ('qr', 'total_visits', 'date_joined')

    fieldsets = (
        (None,
         {'fields': (
             'is_active', 'cost_of_visit', 'cat', 'title', 'description',
             'img', 'total_visits', 'date_joined', 'qr'
         )}),
        ('Скидки',
         {'fields': (
             'd_standard', 'd_bronze',
             'd_silver', 'd_gold', 'd_vip'
         )}),
        ('Посещения',
         {'fields': (
             'v_standard', 'v_bronze',
             'v_silver', 'v_gold', 'v_vip'
         )}),
    )

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width='130'>")
        return None

    get_html_img.short_description = 'Изображение'
