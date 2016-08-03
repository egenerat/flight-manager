from django.conf.urls.defaults import *
#from django.contrib.auth.forms import AuthenticationForm

#handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
   # (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/guestbook/', }),
    (r'^fm/', include('fm.urls')),

    #(r'^accounts/login/$', 'django.contrib.auth.views.login',
    #    {'authentication_form': AuthenticationForm,
    #    'template_name': 'guestbook/login.html',}),
    #(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
# url(r'^admin/', include(admin.site.urls)),
)
