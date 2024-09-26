from django.urls import path
from .views import (HomeView,
                    PostNewView,
                    PostDetailView,
                    PostUpdateView,
                    PostDeleteView,
                    AboutUsView,
                    CategoryView,
                    edit_comment,
                    delete_comment,)

urlpatterns =[
    path('',HomeView.as_view(),name='home'),
    path('post/new',PostNewView.as_view(),name='newpost'),
    path('post/<int:pk>',PostDetailView.as_view(),name='detail'),
    path('post/update/<int:pk>',PostUpdateView.as_view(),name='updatepost'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name='deletepost'),
    path('edit/comment/<int:pk>/',edit_comment, name='edit_comment'),
    path('delete/comment/<int:pk>/',delete_comment, name='delete_comment'),
    path('aboutus/',AboutUsView.as_view(),name='aboutus'),
    path('category/<str:category>/',CategoryView.as_view(),name='category')
]