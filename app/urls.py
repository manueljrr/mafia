from django.conf.urls import include, url

from .views import MemberListView, BossListView, MemberDetailView, MemberCreateView

urlpatterns = [
    url(r'^lista-completa/$', MemberListView.as_view(),
        name='member-list'),
    url(r'^lista-jefes/$', BossListView.as_view(),
        name='boss-list'),
    url(r'^miembro/nuevo/$', MemberCreateView.as_view(),
        name='member-new'),
    url(r'^miembro/(?P<pk>[0-9]+)/$', MemberDetailView.as_view(),
        name='member-view'),
]
