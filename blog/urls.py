from django.urls import path
from .views import home, about, PostListView

urlpatterns = [
    # path('', home, name='home' ),
    path('', PostListView.as_view(), name='home' ),
    path('about/', about, name='about' ),
]