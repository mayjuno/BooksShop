from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
def info(request):
    name = 'Dr Kyaw Myo Swe'
    degree = ['B.C.Sc','ME(IT)','Ph.D(IT)']
    age = 43
    jobs = ['Software Enginner', 'Administrator of ADE education center']
    thumbnailURL = 'https://avatars.githubusercontent.com/u/46017986?s=400&u=ff164e30e905af652e9aba799fa7975f53e3a423&v=4'
    context = {
        "name" : name,
        "degree" : degree,
        "age" : age,
        "jobs" : jobs,
        "thumbnailURL" : thumbnailURL
    }
    return render(request,'book/info.html',context)
    #return HttpResponse('Hello Django')

bookData = open('/home/ade/Django_Project/Bitfumes/BooksShop/books.json').read()
data = json.loads(bookData)


def index(request):
    
    context = {
        'books' : data,
    }
    return render(request,'book/index.html',context)


def show(request, id):
    singleBook = list()
    for book in data:
        if book['id'] == id:
            singleBook = book
    context = {
        'book' : singleBook,
    }
    return render(request,'book/show.html',context)