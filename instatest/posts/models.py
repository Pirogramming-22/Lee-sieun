from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)  
    content = models.TextField()  
    like = models.IntegerField(default=0)  
    photo = models.ImageField(upload_to='images/', blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)  # User 대신 문자열로 변경
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} on {self.post.title}'
