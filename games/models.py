from django.db import models

# Create your models here.

class Games(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=400)
    price = models.FloatField()
    platform = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, default='Action')
    full_game = models.CharField(max_length=50)
    game_info = models.CharField(max_length=5000)
    size = models.FloatField()
    release_date = models.DateField()
    developer = models.CharField(max_length=50)
    rating = models.CharField(max_length=300, blank=True)
    is_official = models.BooleanField(default=True)
    liked_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='liked_games',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'
        
class Comment(models.Model):
    text=models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    games = models.ForeignKey(
        Games,
        related_name='comments',
        on_delete=models.CASCADE
    )

    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='comments_made',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.games} - {self.created_at}'