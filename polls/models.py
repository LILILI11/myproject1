import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): #질문 내용, 생성날짜
    question_text =models.CharField(max_length=200) # 필드 문자열
    pub_date=models.DateTimeField('date published') #시간 타입

    def __str__(self): #Question.objects.all() 하면 어떤 오브젝트인지 구분이 안가니 이름이 나타나게 해줌
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #현재시간-하루 전날 시간 -> 어제

class Choice(models.Model): #선택지에 해당하는 질문, 투표수
    question=models.ForeignKey(Question, on_delete=models.CASCADE) #외래키-> Question 모델을 참조
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0) #숫자 타입

    def __str__(self):
        return self.choice_text