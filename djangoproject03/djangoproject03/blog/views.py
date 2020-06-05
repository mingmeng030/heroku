from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects 
    #model로 부터 전달받은 object list: query set
    #기능들을 표시해 주는 방법 : method
    #query set을 활용하게 해주는 것이 method

    #블로그의 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator=Paginator(blog_list,3)
    #request 된 페이지가 무엇인지 알아내고
    page=request.GET.get('page')
    #request 된 페이지를 얻어온 뒤 return 해준다.
    #posts 안에는 request된 page가 담김
    posts=paginator.get_page(page)

    return render(request, 'home.html', {'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

#new.html 을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

#입력받은 내용을 db에 넣어주는 함수
def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    #.save : 쿼리셋 메시지 중 하나로 blog에 넣은 모든 객체 db에 저장하는 메소드
    blog.save() 
    #blog.id는 int형인데 url은 항상 문자열이므로 str로 형 변환
    #redirect(url) : 위의 모든 함수를 수행 후에 url로 넘겨라
    return redirect('/blog/'+str(blog.id))


    #redirect와 render의 차이점
    #redirect : 상위 모든 코드 수행 후에 redirect 내의 인자 url이 띄워짐(외부 url도 상관 없음)
    #render : 파이썬 함수 내에서 생성한 내용을 html 상에서 data를 담아 처리하고 싶을 때 사용

def blogpost(request):
    #1.입력된 내용을 처리하는 기능 ->POST
    if request.method=='POST':
        #POST방식으로 들어온 data를 form이라는 변수에 담기
        form=BlogPost(request.POST)
        #form이 잘 입력됐는지 검사하는 과정
        if form.is_valid():
            #model객체를 반환하되 저장하지 않고 가져오기, post는 blog형 객체
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')

    #2.빈 페이지를 띄워주는 기능 ->GET
    else:
        #form에 빈 객체 BlogPost 담기
        form=BlogPost()
        return render(request, 'new.html',{'form':form})


