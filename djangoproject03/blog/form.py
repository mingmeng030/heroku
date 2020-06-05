from django import forms
from .models import Blog

#모델을 기반으로 한 입력 공간
class BlogPost(forms.ModelForm):
    class Meta:
        #Blog 모델을 기반으로한 입력 공간을 만들거고
        model= Blog
        #그 중 title과 body를 입력 받을 수 있게 할거야

#임의의 입력 공간 만든 예시
#class BlogPost(forms.Form):
#email=forms.EmailField()
#files=forms.FileField()
#url=forms.URLField()