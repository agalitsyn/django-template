from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from app.components.main.views import index


admin.autodiscover()
admin.site.site_header = _('Site Administration')

handler404 = 'app.components.main.views.page_not_found'
handler500 = 'app.components.main.views.server_error'


urlpatterns = [
    path('admin/', admin.site.urls),

    # Text and xml static files:
    path('robots.txt', TemplateView.as_view(
        template_name='txt/robots.txt',
        content_type='text/plain',
    )),
    path('humans.txt', TemplateView.as_view(
        template_name='txt/humans.txt',
        content_type='text/plain',
    )),

    path('', index, name='index'),
    # or
    # path('', include(('app.components.main.urls', 'main'), namespace='main')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path('__debug__/', include(debug_toolbar.urls)),  # noqa: DJ05
    ] + urlpatterns + static(
        # Serving media files in development only:
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
