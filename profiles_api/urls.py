from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router=DefaultRouter()
#hello-viewset/ is not needed as in hello-view/ because the url are created by default using default router
#base_name will be used to retreive urls in router
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('',include(router.urls))
]