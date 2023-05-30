from django.urls import path
from rest_framework import routers
from trucksapp import views

router = routers.SimpleRouter()
router.register(r'cargo', views.CargoViewSet)
router.register(r'car', views.CarViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('load/', views.load, name='load'),
]


