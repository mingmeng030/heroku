from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name='home'),
    #path converter를 이용해 url 자동 생성
    path('blog/<int:blog_id>',blog.views.detail, name='detail'),
    path('blog/new/', blog.views.new, name='new'),
    #path를 추가한다고 해서 html을 무조건 띄워야 하는 것은 아님
    #path('어떤 url이 들어오면',(어디에 있는)어떤 함수를 실행시켜라)
    #즉, 아래는 blog/create url이 들어오면 blogapp.view에 있는 create 를 실행시켜라
    path('blog/create',blog.views.create, name='create'),
    path('portfolio/',portfolio.views.portfolio,name='portfolio'),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
