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

    theme = ThemeSerializer()
    duration = serializers.ReadOnlyField()
    tags = TagSerializerField()

    class Meta:
        model = Call
        fields = '__all__'
