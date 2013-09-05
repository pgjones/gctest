from rest_framework import serializers

from gctest.models import App, Build

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('name', 'released')

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ('version', 'app', 'current')
