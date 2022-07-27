from django.contrib import admin
from django.urls import path, include
from rules import views
from django.conf import settings
from django.conf.urls.static import static
# from django.core.urlresolvers import reverse
# from .fields import MarkdownFormField
# from .widgets import MarkdownWidget
# from .utils import editor_js_initialization

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('points/', include('points.urls')),
    path('competitons/', include('competitions.urls')),
    path('method/', include('method.urls')),
    path('users/', include('users.urls')),
    path('rules/', include('rules.urls')),
    path('ranking/', include('hof.urls')),
    path('shop/', include('shop.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)