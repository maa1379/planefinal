from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("airlines/", include("airlines.urls", namespace="airlines")),
    path("", include("passangers.urls", namespace="passengers")),
    path("hotels/", include("hotels.urls", namespace="hotel")),
    path("core/", include("core.urls", namespace="core")),
    path("job/", include("jobs.urls", namespace="job")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("pro/", include("profiles.urls", namespace="user_pro")),
    # path('api_doc/',include_docs_urls(title='7BLUSKY')),

]

if settings.DEBUG:
    # ADD ROOT MEDIA FILES
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
