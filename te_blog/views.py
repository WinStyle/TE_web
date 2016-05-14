from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
import models
from django.contrib import comments
from django.contrib.contenttypes.models import ContentType
# Create your views here.
def index(request):
    if request.user.is_anonymous():
        return  render_to_response('login.html')
    else:
        print request.user.id
        te_user_id=request.user.id
        te_user= models.TE_user.objects.get(user_id=te_user_id)
        print te_user.signature

        blog_list = models.TE_BLOG.objects.all()
        return render_to_response('index.html', {'blog_list':blog_list,
                                                    'user':request.user,
                                                    })




def blog_detail(request, blog_id):
    blog = models.TE_BLOG.objects.get(id=blog_id)
    return render_to_response('bbs_detail.html', {'blog_obj':blog,
                                                      'user':request.user,
                                                  })

def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user= auth.authenticate(username=username,password=password)
    errlog='Erro username or password'
    if user is None:
        return render_to_response('login.html',{'err_log':errlog})
    else:
        auth.login(request,user)
        return HttpResponseRedirect('/')

def Login(request):
    return render_to_response('login.html')

def Logout(request):

    auth.logout(request)
    return HttpResponseRedirect('/')