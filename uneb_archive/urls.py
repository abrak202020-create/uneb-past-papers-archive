from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import the home view
from papers.views import home

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("login/", include("users.urls")),
    path("", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("subjects/", include("subjects.urls")),
    path("papers/", include("papers.urls")),
    path("downloads/", include("downloads.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)