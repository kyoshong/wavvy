from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = timezone.now)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments') # 관계 설정
    comment_date = models.DateTimeField(default = timezone.now) # 댓글 날짜
    comment_body = models.CharField(max_length=200) # 댓글 내용
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 유저 관계설정
    
    def __str__(self):
        return self.comment_body
        
    class Meta:
        ordering=['id'] # 정렬기준
    