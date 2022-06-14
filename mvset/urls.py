from django.contrib import admin
from django.urls import path , include 
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework import permissions
from api.views import UserViewSet , StudentViewset ,StudentGenericViewSet
router = routers.DefaultRouter()
router.register(r'StudentModelViewSet',StudentViewset)
router.register(r'StudentViewSet',UserViewSet,basename = 'user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rom/',include('api.urls')),
    path('', include(router.urls)),
     
]



schema_view = get_schema_view(
    openapi.Info(
        title="FOREX BACKEND API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    
 
)


urlpatterns += [
    path(
        "swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]