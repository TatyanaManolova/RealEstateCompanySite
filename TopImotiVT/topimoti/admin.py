
from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 15  # Show 5 empty image slots (up to 15)
    fields = ['image']  # Only show image field


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'area', 'rooms', 'year_built')
    inlines = [PropertyImageInline]  # Allows image upload in Property admin page


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image')

