from django.conf.urls import url
from locaties import views

urlpatterns = [
    url(r'^$', views.index, name='locations'),
    url(r'nieuw', views.LocationCreateView.as_view(), name='new_location'),
    url(r'^(?P<pk>[0-9]+)/edit', views.UpdateLocation.as_view(), name='edit_location'),
    url(r'^(?P<pk>[0-9]+)/delete', views.DeleteLocation.as_view(), name='delete_location'),
    url(r'^(?P<pk>[0-9]+)', views.DetailLocation.as_view(),  name='detail_location')
]