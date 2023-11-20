from rest_framework import serializers


class CreatePostRequestValidationSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)

    class Meta:
        fields = "__all__"


class UpdatePostRequestValidationSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)

    class Meta:
        fields = "__all__"