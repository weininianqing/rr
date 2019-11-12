from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request,"one.html")


def two(request):
    ct = dict()
    ct["name"] = "大辉"
    ct["name1"] = "小家子"
    ct["name2"] = "goujia"

    return render(request,"two.html",context=ct)

def three(request):
    ct = dict()
    ct["score"]=[77,88,66,99,100]
    return render(request,"three.html",context=ct)