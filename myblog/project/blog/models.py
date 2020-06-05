from django.db import models

class Blog(models.Model):
    #model 내의 문자로 된 data를 title 변수로 정의, 길이 최대 200
    #CharField는 짧은 문자열을 나타냄
    title=models.CharField(max_length=200)
    #model 내의 시간 data를 pub_data로 처리
    pub_date=models.DateTimeField('date published')
    #model 내의 textfield 형식을 통해 body 변수를 처리
    body=models.TextField()

    #model.뭐뭐뭐Field()

    #블로그 post 제목이 뜨도록 하고 싶을 때
    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]


    
