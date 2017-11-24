from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^Tango-In-Hyderabad/$', views.TangoHyderabadPage.as_view(), name='Tango-In-Hyderabad'),
    url(r'^Tango-In-Auroville-Pondicherry/$', views.TangoAurovillePage.as_view(), name='Tango-In-Auroville-Pondicherry'),
    url(r'^Tango-In-Chennai/$', views.TangoChennaiPage.as_view(), name='Tango-In-Chennai'),
    url(r'^Tango-In-Delhi/$', views.TangoNewDelhiPage.as_view(), name='Tango-In-Delhi'),
    url(r'^Tango-In-Bangalore/$', views.TangoBangalorePage.as_view(), name='Tango-In-Bangalore'),
    url(r'^Tango-Essentials/$', views.TangoEssentials.as_view(), name='Tango-Essentials'),
    url(r'^Tango-Radio/$', views.TangoRadio.as_view(), name='Tango-Radio'),
    url(r'^sitemap_location/$', views.TangoSitemap.as_view(), name='sitemap_location'),
    url(r'^Tango-In-Mumbai/$', views.TangoMumbai.as_view(), name='Tango-In-Mumbai'),
    url(r'^Tango-Events/$', views.EventsPage.as_view(), name='Tango-Events'),
    url(r'^Tango-In-Pune/$', views.TangoPunePage.as_view(), name='Tango-In-Pune'),
    url(r'^Tango-In-Bangalore-El-Cabeceo/$', views.TangoElCabeceoPage.as_view(), name='Tango-In-Bangalore-El-Cabeceo'),
    url(r'^Tango-In-Mumbai-BTangoConscious/$', views.TangoMumbaiBTangoConscious.as_view(), name='Tango-In-Mumbai-BTangoConscious'),
    url(r'^Past-Events/$', views.PastEventsPage.as_view(), name='Past-Events'),
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
