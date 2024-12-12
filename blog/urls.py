from django.urls import path, include
from blog import views


urlpatterns = [
    path('post/', views.post_list_view, name='post-list'),
    path('api/v1/', include('blog.api.v1.urls')),
]

