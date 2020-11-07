from django.urls import path
from .views import (
     about, PostListView,
     PostDetailView, PostCreateView,
     PostUpdateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home' ),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail' ),
    path('detail/<int:pk>/update/', PostUpdateView.as_view(), name='update' ),
    path('new/', PostCreateView.as_view(), name='create' ),
    path('about/', about, name='about' ),
]