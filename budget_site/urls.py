from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'budget_site.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^budget/', include('budget.urls', namespace='budget')),
    url(r'^admin/', include(admin.site.urls)),
)
