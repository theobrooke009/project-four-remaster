from django.urls import path 
from .views import CommentDetailView, GameListView, GameDetailView, CommentListView, GameLikeView

urlpatterns = [
    path('', GameListView.as_view()),
    path('<int:pk>/', GameDetailView.as_view()),
    path('<int:game_pk>/comments/', CommentListView.as_view()),
    path('<int:game_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view()),
    path('<int:game_pk>/like/', GameLikeView.as_view())
]