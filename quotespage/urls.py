from django.conf.urls import url
from django.views.generic import TemplateView
from quotespage import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<pagenum>\d+)/$', views.index, name='pages'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^submit/success/$', TemplateView.as_view(template_name="quotespage/success.html"), name='success'),
    url(r'^about/$', TemplateView.as_view(template_name="quotespage/about.html"), name='about'),
	url(r'^search/$', views.search, name='search'),
	url(r'^speakers/$', views.speaker_list, name='speaker-list'),
	url(r'^speaker/(?P<speaker>[-,%.\w]+)/$', views.speaker_archive, name='speaker'),
	url(r'^speaker/(?P<speaker>[-,%.\w]+)/(?P<pagenum>\d+)/$', views.speaker_archive, name='speaker-pages'),
	url(r'^random/$', views.random_quote, name='random'),
	url(r'^random/(?P<year>\d{4})/$', views.random_quote, name='random-byyear'),
	url(r'^byvotes/$', views.top_voted, name='byvotes'),
	url(r'^byvotes/(?P<pagenum>\d+)/$', views.top_voted, name='byvotes-pages'),
	url(r'^quote/(?P<quoteid>\d+)/$', views.permalink, name='permalink'),
	url(r'^api/vote/$', views.vote, name='vote'),
	url(r'^api/random/$', views.json_random_quote, name='api-random'),
	url(r'^api/genkey/$', views.generate_api_key, name='genkey'),
	url(r'^api/submit/$', views.remote_submit, name='remote-submit'),
]
