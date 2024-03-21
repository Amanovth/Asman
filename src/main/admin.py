from django.contrib import admin
from .models import (
    Stories,
    StoryVideos,
    Wallets,
    AsmanRate
)


class StoryVideosInline(admin.StackedInline):
    model = StoryVideos
    extra = 0


@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")
    list_display_links = list_display
    inlines = (StoryVideosInline,)


@admin.register(Wallets)
class WalletsAdmin(admin.ModelAdmin):
    list_display = ('asman', 'usdt')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AsmanRate)
class AsmanRateAdmin(admin.ModelAdmin):
    list_display = ('rate', )

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
