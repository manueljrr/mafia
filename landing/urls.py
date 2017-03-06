from django.conf.urls import url

from .views import IndexView, MemberView

urlpatterns = [
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),
    url(
        r'^miembros/$',
        MemberView.as_view(),
        name='member_info'
    ),
]
