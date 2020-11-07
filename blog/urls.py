from django.urls import path
from .views import home, about, PostListView,PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='home' ),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail' ),
    path('about/', about, name='about' ),
]