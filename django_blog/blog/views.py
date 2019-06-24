from django.shortcuts import render

posts = [
    {
        'author':'Tabish',
        'title':'First Post',
        'content':'First Post Content',
        'date_posted':'June 23, 2019'
    },
    {
        'author':'Mehvish',
        'title':'Mehvish Post',
        'content':'Mehvishs Content',
        'date_posted':'June 28, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
