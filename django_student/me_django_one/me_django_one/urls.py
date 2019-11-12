from django.conf.urls import include, url
from django.contrib import admin
from one_fb import views as av
from one_fb import url1

urlpatterns = [
    # Examples:
    # url(r'^$', 'me_django_one.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^withparm/[0-9]{4}',av.withparm),

    #转到url1里面去，在主路由student后面加上子路由url1
    url(r'^student/',include(url1)),
    url(r'^book/(?:page-(?P<page_number>\d+)/)?$',av.pages),
    url(r'^yourname/$',av.url_name,{"name":"sunjia"}),
    url(r'^konwname/',av.konw_name,name="askname"),
    url(r'^v10_1/',av.v10),
    url(r'^v11_1/',av.v11),
    url(r'^v12_1/',av.v12,name="v12_12"),


]
