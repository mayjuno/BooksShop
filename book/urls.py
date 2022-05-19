
from django.urls import path, include
from . import views
urlpatterns = [

    #path('info/', views.info,name='info'),
    path('', views.index,name='books_list'),
    path('<int:id>', views.show, name='book_detail')
]