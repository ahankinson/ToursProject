from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from goudimel.views.main import home
from goudimel.views.main import BookList
from goudimel.views.main import BookDetail
from goudimel.views.main import PieceList
from goudimel.views.main import PieceDetail
from goudimel.views.main import PhraseList
from goudimel.views.main import PhraseDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goudimel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^books/$', BookList.as_view(), name="books-list"),
    url(r'^book/(?P<pk>[0-9]+)/$', BookDetail.as_view(), name="book-detail"),

    url(r'^pieces/$', PieceList.as_view(), name="pieces-list"),
    url(r'^piece/(?P<pk>[0-9]+)/$', PieceDetail.as_view(), name="piece-detail"),

    url(r'^phrases/$', PhraseList.as_view(), name="phrases-list"),
    url(r'^phrase/(?P<pk>[0-9]+)/$', PhraseDetail.as_view(), name="phrase-detail"),

    url(r'^admin/', include(admin.site.urls)),
)