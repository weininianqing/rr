from django.conf.urls import include,url
from . import views as tv
urlpatterns = [
    # Examples:
    # url(r'^$', 'me_django_one.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

  url(r'wangshaohui/',tv.do_man),
]