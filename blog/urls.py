from django.urls import path
from .views import home, about, PostListView,PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='home' ),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail' ),
    path('new/', PostCreateView.as_view(), name='create' ),
    path('about/', about, name='about' ),
]