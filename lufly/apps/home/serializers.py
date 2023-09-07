from rest_framework import serializers
from .models import Banner, Nav


class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ["image_url", "link"]

class NavModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ["title","link","is_site"]