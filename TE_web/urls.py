from django.conf.urls import patterns, include, url
from django.contrib import admin
import te_blog.urls
from te_blog import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TE_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(te_blog.urls)),
    url(r'^acc_login/$',views.acc_login),
    url(r'^login/$',views.Login),
    url(r'logout/$',views.Logout),
)
