from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') # ondelete -> 계정 삭제 시 다 삭제
    subject = models.CharField(max_length=200)  # 질문 제목
    content = models.TextField()                # 질문 내용
    create_date = models.DateTimeField(auto_now_add=True)        # 작성 일시

    def __str__(self):
        return self.subject
