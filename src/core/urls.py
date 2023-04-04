from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # Template views
    path("", TemplateView.as_view(template_name="home.html")),
    path("<int:pk>/", TemplateView.as_view(template_name="business-view.html")),
    path(
        "create/<str:name>/",
        TemplateView.as_view(template_name="business-create.html"),
        {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY},
    ),
    # API views
    path("api/businesses/", include("apps.businesses.urls")),
    # Admin portal
    path("admin/", admin.site.urls),
]
