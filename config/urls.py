from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from apps.accounts.views import router as accounts_router

from django.conf import settings
from django.conf.urls.static import static

api = NinjaAPI()

api.add_router("/accounts/", accounts_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
