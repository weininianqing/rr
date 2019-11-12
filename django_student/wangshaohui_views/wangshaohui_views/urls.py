from django.conf.urls import include, url
from django.contrib import admin
from views_app import views as v
urlpatterns = [
    # Examples:
    # url(r'^$', 'wangshaohui_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'v8',v.v8_get),
    url(r'v9_get',v.v9_get),
    url(r'v9_post',v.v9_post),
    url(r'render_test',v.render_test),
    url(r'render1_test',v.render1_test),
    url(r'render2_test',v.render2_test),
]
