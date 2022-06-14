from django.urls import path , include
from api.views import StudentViewset ,UserViewSet , StudentListMixinView , StudentGenericViewSet
from api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('snippets', views.StudentViewset,basename="snippets")


urlpatterns = [
    path('', include(router.urls)),
    path('viewset/',UserViewSet.as_view({'get': 'list'})),
    path('generic/',StudentGenericViewSet.as_view({'get': 'list'})),
    path('generic/<int:id>/',StudentGenericViewSet.as_view({'get': 'list'})),
    path('mixin/',StudentListMixinView.as_view()),
    path('mixin/<int:id>/',StudentListMixinView.as_view()),
    

   
]