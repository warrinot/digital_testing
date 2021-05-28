from rest_framework import serializers
from calls.models import Call, Theme


class TagSerializerField(serializers.ListField):

    def to_representation(self, data):
        return data.values_list('name', flat=True)


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = ['name']


class CallSerializer(serializers.ModelSerializer):

    theme = ThemeSerializer(read_only=True)
    duration = serializers.ReadOnlyField()
    tags = TagSerializerField(read_only=True)

    class Meta:
        model = Call
        fields = '__all__'
