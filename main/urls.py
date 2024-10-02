from django.urls import path

from .views import CarListCreateAPIView, CarDetailAPIView, BrandListCreateAPIView, BrandDetailAPIView


urlpatterns = [
    path("car/", CarListCreateAPIView.as_view()),
    path("car/<int:pk>", CarDetailAPIView.as_view()),

    path("brand/", BrandListCreateAPIView.as_view()),
    path("brand/<int:pk>", BrandDetailAPIView.as_view())
]
