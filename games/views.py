from rest_framework.exceptions import NotFound
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Games, Comment
from .serializers import CommentSerializer, GameSerializer

class GameListView(ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class GameDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentListView(APIView):
    '''List view for /game/gameId/comments CREATE comments'''

    permission_classes = (IsAuthenticated, )
    def post(self, request, game_pk):
        
        request.data['game'] = game_pk
        request.data['owner'] = request.user.id
        created_comment = CommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors)
    

class CommentDetailView(APIView):
    '''REMOVE A COMMENT VIEW'''
    permission_classes = (IsAuthenticated, )

    def delete(self, _request, **kwargs):
        comment_pk = kwargs['comment_pk']
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            comment_to_delete.delete()        
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return NotFound()

class GameLikeView(APIView):
    '''adds likes to games'''

    permission_classes = (IsAuthenticated, )
    def post(self, request, game_pk):
        try:
            game_to_like = Games.objects.get(pk=game_pk)
        except Games.DoesNotExist:
            raise NotFound()
        
        if request.user in game_to_like.liked_by.all():
            game_to_like.liked_by.remove(request.user.id)
        else:
            game_to_like.liked_by.add(request.user.id)
        
        serialized_game = GameSerializer(game_to_like)

        return Response(serialized_game.data, status=status.HTTP_202_ACCEPTED)

