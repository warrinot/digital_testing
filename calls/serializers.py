from rest_framework import serializers
from calls.models import Call, Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['name']


class CallSerializer(serializers.ModelSerializer):
    theme = ThemeSerializer()
    duration = serializers.ReadOnlyField()

    class Meta:
        model = Call
        fields = '__all__'
