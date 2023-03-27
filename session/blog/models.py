from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='블로그 제목을 작성해주세요')
    author = models.CharField(max_length=10,default="")
    StudentID = models.CharField(max_length=8,default="", help_text="학번을 입력해주세요(예시:20181020)")
    email = models.EmailField(max_length=128, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
   
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]