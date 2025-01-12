from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=255) 
    releaseYear = models.IntegerField()
    GENRE_CHOICES = [
            ('action' , '액션'),
            ('romance' , '로맨스'),
            ('comedy' , '코미디'),
            ('horror' , '공포'),
            ('sci-fi' , 'SF'),
            ('ani','애니메이션'),
            ('criticism','사회비판')
        ]
    genre = models.CharField(
        max_length= 50,
        choices = GENRE_CHOICES,
        default='action',
    )
    rating = models.FloatField()
    producer = models.CharField(max_length=255) 
    actors = models.TextField()
    runningTime  = models.TextField()
    review = models.TextField()


