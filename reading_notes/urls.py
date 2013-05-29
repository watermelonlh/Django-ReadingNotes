from django.conf.urls import patterns, url

urlpatterns = patterns('reading_notes.views',
    url(r'^$', 'index'),
    url(r'^readings', 'readings'),
)

