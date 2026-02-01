from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request): 
    
    context = { 
        'page_title':'Welcome to Our Store' ,
        'user_name':'Guest' ,
        'user_authenticated': False ,
        'products': [
        { 'name': 'Laptop' , 'price': 9999} ,
        { 'name': 'Mouse' , 'price': 299} ,
        { 'name': 'Keyboard' , 'price': 799}]}
    # the httpresponse is included in render 
    # so it will load the template , rendering with context and
    # return httpresponse 
    return render(request,'myapp/index.html',context)

def about(request): 
    html = """
    <html>
        <head>
        <title>about us</title>
        </head>
        <body>
        <h1>about us</h1>
        <p>we are learnign django</p>
        </body>
    </html>
    """
    return HttpResponse(html)
def article_det(request ,id): 
    return HttpResponse(f"<h1>article #{id}</h1>")
def category(request , slug): 
    return HttpResponse(f"<h1>category #{slug}</h1>")

def profile(request,username): 
    return HttpResponse(f"<h1>current profile is : #{username}</h1>")
