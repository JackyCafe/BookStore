"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app1 import views

app_name = 'app1'
urlpatterns = [
     path('index/',views.index,name = 'index'),
     path('books/',views.books,name = 'books'),
     path('books_add/', views.book_add, name='books_add'),
     path('chapter/<int:id>',views.delete,name = 'delete'),
     path('chapter_edit/<int:id>', views.chapter_edit, name='chapter_edit'),
     path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.chapter_detail  ,name = 'book_detail'),
     path('ch/<int:id>/<slug:chapter>/', views.ch_detail, name='ch_detail'),
     path('comment_add/<int:id>/',views.comment_add,name='comment_add'),
     path('comment_edit/<int:id>/<slug:comment>/', views.comment_edit, name='comment_edit'),
]
