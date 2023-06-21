from django.conf.urls import url
from post import views

urlpatterns = [
	url(r'^$', view=views.post_index_view, name='post_index_view'),
	url(r'^create/$', view=views.post_index_view, name='create_post_record'),
	url(r'^delete/(?P<id>\d+)/$', view=views.post_delete, name='delete_post_record'),
]
