from django.contrib import admin

# Register your models here.
from football.models import FootballField, Config, ImageForFootballField


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ("title", "key", "value")


class ImageInline(admin.TabularInline):
    fk_name = "football_field"
    model = ImageForFootballField


@admin.register(FootballField)
class FootballFieldAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    inlines = (ImageInline, )
