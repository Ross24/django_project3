from django.urls import path
from .views import (
    PostListView,
    #PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from. import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<slug:pk_slug>/', views.post_detail, name='post-detail'),
    #path('post/<slug:the_slug>/', views.post_detail, name='post-detail'),
    
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   # path('comment/<int:pk>/delete/', views.DeleteCommentView, name='comment-delete'),
    path('about/', views.about, name='blog-about'),
    path('comments/<int:pk>/delete_own/', views.delete_own_comment, name='delete_own_comment'),

    #path('abc/',TemplateView.as_view(template_name='blog/index.html'), name="facebook")
]