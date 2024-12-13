
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
 


@api_view()
def post_list(request):
    return Response("ok")

@api_view()
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)