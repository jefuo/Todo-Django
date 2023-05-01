from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""タスクのデータスキーマを用意"""
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    
    """管理画面で上記のuser,titleなどを分かりやすく表示"""
    def __str__(self):
        return self.title
    
    """並び変えをする。日付や完了済みか、などでソート出来る"""
    class Meta:
        ordering = ["completed"]
        