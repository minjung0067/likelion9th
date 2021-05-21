"""myProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp.views import main, detail, create_page, create, update_page, update, delete, create_comment, delete_comment

from django.conf import settings
from django.conf.urls.static import static
# 위 부분은 장고 미디어 파일을 사용하기 위해 꼭 추가해줘야함 !!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('detail/<int:id>/', detail, name="detail"),
    path('create_page/', create_page, name="create_page"),
    path('create/', create, name="create"),
    path('update_page/<int:id>/', update_page, name="update_page"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('detail/<int:id>/comments/create/', create_comment, name="create_comment"),
    path('detail/<int:id>/comments/delete/<int:comment_id>', delete_comment, name="delete_comment"),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

