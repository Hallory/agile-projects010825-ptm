from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from projects.models import Tag
from projects.serializers import TagListSerializer
from rest_framework import status


class TagListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        all_tags = Tag.objects.all()
        list_tags = TagListSerializer(all_tags, many=True)
        return Response(list_tags.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        create_tag = TagListSerializer(data=request.data)
        if create_tag.is_valid():
            create_tag.save()
            return Response(create_tag.data, status=status.HTTP_201_CREATED)
        return Response(create_tag.errors, status=status.HTTP_400_BAD_REQUEST)