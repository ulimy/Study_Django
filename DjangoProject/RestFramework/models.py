from django.db import models

# Create your models here.
from django.db import models
# User는 django에서 제공하는 일반적인 사용자에 대한 모델
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    subtitle = models.CharField(max_length=144, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # 문자열 반환
    def __str__(self):
        return '[ {} ] {}'.format(self.user.username, self.title)
