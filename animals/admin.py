from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Animal, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ('animal', 'position')

    def get_model_perms(self, request):
        return {}


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['image', 'preview', 'position']
    readonly_fields = ['preview']

    def preview(self, obj):
        image_height = 200
        return format_html(f'<img src="{obj.image.url}" height={image_height} />')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['kind', 'breed', 'name']