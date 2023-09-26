from snippets.models import Snippet
from rest_framework import serializers, status


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    firstName = serializers.CharField(max_length=20)
    lastName = serializers.CharField(max_length=20)

    # class SnippetSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Snippet
    #         fields = ['id', 'firstName', 'lastName', 'code']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # created_data = Snippet.objects.create(**validated_data)
        # print(created_data.id)
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.save()
        return instance


class VersionSerializer(serializers.Serializer):
    version = serializers.CharField()
