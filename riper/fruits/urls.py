from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'index/$',views.IndexView.as_view(), name='index'),
	url(r'search_results/$', views.search_bar, name='search'),
	url(r'(?P<pk>[0-9]+)/$', views.FruitDetail.as_view(), name='detail')



]