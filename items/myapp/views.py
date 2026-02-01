from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'myapp/index.html',{'page_title':'lolaaa'})
def about(request): 
    context = {
        'page_title' : 'lolaaa',
        'members' : ['memeber1','memeber2','memeber3','memeber4','memeber5','memeber6','memeber7','memeber8','memeber9','memeber10']
    }
    return render(request,'myapp/about.html',context)

def child(request): 
    return render(request,'myapp/child.html')
 


def base(request): 
    return render(request,'myapp/base.html' ,{'page_title':'lili_base'})

def base1(request): 
    return render(request,'myapp/index.html', {'the_address':'current_address', 
                                               'the_package ': 'mypackage'})