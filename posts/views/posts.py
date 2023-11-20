from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import viewsets, status
from drf_yasg import openapi
from posts.models import BlogPost
from rest_framework.permissions import IsAuthenticated
from posts.serializers.model_serializers.posts import CreatePostSerializer, UpdatePostSerializer, ListPostsSerializer
from posts.serializers.validation_serializers.posts import CreatePostRequestValidationSerializer, \
    UpdatePostRequestValidationSerializer
from posts.utils.pagination import CustomPagination


class PostViewSet(viewsets.GenericViewSet):
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreatePostRequestValidationSerializer
    pagination_class = CustomPagination

    @swagger_auto_schema(
        responses={
            200: "Success"
        },
        tags=["Post"],
        operation_description="Create Post",
        operation_summary="Create Post",
        request_body=CreatePostRequestValidationSerializer()
    )
    def create(self, request):
        request_data = request.data
        serializer = CreatePostRequestValidationSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        login_user = request.user.id
        request_data['author'] = login_user
        serializer = CreatePostSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data="Success", status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            200: "Success"
        },
        tags=["Posts"],
        operation_description="Delete Post",
        operation_summary="Delete Post",
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                description="postId",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    def delete(self, request, pk):
        BlogPost.objects.filter(id=pk).update(is_deleted=True)

        return Response(data="Success", status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            200: "Success"
        },
        tags=["Post"],
        operation_description="Create Post",
        operation_summary="Create Post",
        request_body=UpdatePostRequestValidationSerializer(),
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                description="postId",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    def update(self, request, pk):
        try:
            post = BlogPost.objects.get(id=pk)
        except BlogPost.DoesNotExist:
            return Response(data="Invalid PostId ", status=status.HTTP_400_BAD_REQUEST)

        login_user = request.user.id
        request_data = request.data
        request_data['author'] = login_user
        serializer = UpdatePostSerializer(data=request_data, instance=post)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data="Success", status=status.HTTP_200_OK)

    def list(self, request):
        posts = self.queryset.filter(is_deleted=False, author_id=request.user.id)
        page = self.paginate_queryset(posts)
        serializer = ListPostsSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)
