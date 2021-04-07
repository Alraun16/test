from rest_framework import serializers
from .models import New

class NewSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=30)
    title = serializers.CharField(max_length=120)
    content = serializers.CharField()
    publicationDate = serializers.DateField()

    def create(self, validated_data):
        return New.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.publicationDate = validated_data.get('publicationDate', instance.publicationDate)

        instance.save()
        return instance