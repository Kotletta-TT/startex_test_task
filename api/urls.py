from django.urls import include, path
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register(r'users', views.CustomUserViewSet)
# router.register(r'carts', views.CartList)
# router.register(r'cart/<int:pk>', views.CartDetail)
# router.register(r'products', views.ProductViewSet)

urlpatterns = [
    # path('users/', views.CustomUserList.as_view()),
    path('user/<int:pk>/', views.CustomUserDetail.as_view()),
    path('carts/', views.CartList.as_view()),
    path('cart/<int:pk>/', views.CartDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
]
