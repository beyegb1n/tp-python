from django.contrib import admin
from .models import Album
from django.utils.html import format_html

@admin.register(Album)
class AlbumAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'price', 'stock', 'cover_image_preview')
    list_filter = ('release_date',)
    search_fields = ('title',)

    def cover_image_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.cover_image.url)
        return "pas d'image"
    
    cover_image_preview.short_description = 'Pochette'
