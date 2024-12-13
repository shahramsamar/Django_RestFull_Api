
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
 


@api_view(['GET','POST'])
def post_list(request):
    # Handle GET request
    if request.method == 'GET':
        # Retrieve all active posts
        posts = Post.objects.filter(status=True)
        # Serialize the queryset of posts
        serializer = PostSerializer(posts, many=True)
        # Return serialized data as response
        return Response(serializer.data)
    
    # Handle POST request
    elif request.method == 'POST':
        # return Response("ok")
        # return Response(request.data)

        # Create a serializer instance with the request data
        serializer = PostSerializer(data=request.data)
        # Validate the serializer data
 
        if serializer.is_valid():
        #     # Save the new post
            serializer.save()
        #     # Return the serialized data of the new post
            return Response(serializer.data)
        else:
            # Return serializer errors if data is invalid
            return Response(serializer.errors)



@api_view()
def post_detail(request, id):
 
    # Get the post object or return a 404 error if not found
    post = get_object_or_404(Post, pk=id, status=True)
    
    # Serialize the post object
    serializer = PostSerializer(post)
    
    # Return the serialized data as a response
    return Response(serializer.data)
