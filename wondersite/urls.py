from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),


    url(r'^contents/$', 'blog.views.contents', name='contents'),
    url(r'^post/(\d+)/$', 'blog.views.single_post', name='post'),
    url(r'^post/(\d+)/fav/$', 'blog.views.favourite', name='mark-fav'),
    url(r'^post/(\d+)/unfav/$', 'blog.views.unfavourite', name='mark-unfav'),
    url(r'^category/(\w+)/$', 'blog.views.category', name='category'),


    url(r'^new-post/$', 'blog.views.new_post', name='new_post'),
    url(r'^feedback/$', 'blog.views.feedback', name='feedback'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),



    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
