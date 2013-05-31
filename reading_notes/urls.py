from django.conf.urls import patterns, url

urlpatterns = patterns('reading_notes.views',
    url(r'^$', 'index'),
    url(r'^readings', 'readings'),
    url(r'^update$', 'update'),
    url(r'^detail/(?P<reading_id>\d+)$', 'detail'),
)

