from django.contrib import admin

# Register your models here.
from .models import Banner, Nav


# 轮播图
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'orders', 'is_show')
    actions = ['toggle_is_show']

    def toggle_is_show(self, request, queryset):
        for obj in queryset:
            obj.is_show = not obj.is_show
            obj.save()

    toggle_is_show.short_description = "Toggle is_show for selected banners"

admin.site.register(Banner, BannerAdmin)

# 导航菜单

class NavAdmin(admin.ModelAdmin):
    list_display=("title", "link", "is_show", "is_site", "position")

admin.site.register(Nav, NavAdmin)