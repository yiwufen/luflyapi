from django.contrib import admin

# Register your models here.
from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'orders', 'is_show')

admin.site.register(Banner, BannerAdmin)