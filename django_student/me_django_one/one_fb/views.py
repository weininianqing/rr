from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
def withparm(r,year):
    return HttpResponse("This is withparm{}".format(year))



def do_man(r):
    return HttpResponse("这是一个子路由")

def pages(request,page_number):
    return HttpResponse("这是书的第{0}页".format(page_number))

def url_name(r,name):
    return HttpResponse("This is name{}".format(name))

def konw_name(r):
    return HttpResponse("This is url {}".format(reverse("askname")))

def v10(req):
    return HttpResponseRedirect('/v12_1')

def v11(req):
    return HttpResponseRedirect(reverse('v12_12'))

def v12(req):
    return HttpResponse("这是v12的")