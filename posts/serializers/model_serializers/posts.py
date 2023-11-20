from rest_framework import serializers
from posts.models import BlogPost, User


class CreatePostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    author = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.all())

    class Meta:
        model = BlogPost
        fields = "__all__"


class UpdatePostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    author = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.all())

    class Meta:
        model = BlogPost
        fields = "__all__"


class ListPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = "__all__"
