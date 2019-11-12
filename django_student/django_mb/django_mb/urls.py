from django.conf.urls import include, url
from django.contrib import admin
from mb_view import views as av
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_mb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^one/',av.one),
    url(r'^two/',av.two),
    url(r'^three',av.three),
    #url(r'^four',av.four),
    #url()
]
