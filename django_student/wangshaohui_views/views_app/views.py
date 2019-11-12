from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import  reverse
# Create your views here.
def v8_get(request):
    rst=""
    for k,v in request.GET.items():
        rst += k +"—>" +v
        rst += ","
    return HttpResponse("get为 {}".format(rst))


def v9_get(request):

    return render_to_response('day01.html')

def v9_post(request):
    rst=""
    for k,v in request.POST.items():
        rst += k +"—>" +v
        rst += ","
    return HttpResponse("post wei {}".format(rst))

def render_test(request):
    rsp = render(request,"render.html")
    return rsp


def render1_test(request):
    c = dict()
    c["name"] = "wangshaohui"
    rsp =render(request,"render1.html",context=c)
    return rsp


def render2_test(requst):
    from django.template import loader

    #得到模板
    t = loader.get_template("render2.html")

    r = t.render({"name":"sunjiajia"})

    return HttpResponse(r)