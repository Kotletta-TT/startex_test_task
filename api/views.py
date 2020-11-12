from core.models import CustomUser, Cart, Product
from rest_framework import viewsets, permissions, generics, mixins

from .serializers import CustomUserSerializer, CartSerializer, ProductSerializer
from .permissions import IsOwnerOrIsStaff


# class CustomUserList(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [IsOwnerOrIsStaff]


class CustomUserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrIsStaff]


class CartList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Создаем корзину если ее нет.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """
        Тут можно как добовлять пользователя при сохранении,
        так и проверять наличие уже существующей корзины у пользователя
        """
        serializer.save(user=self.request.user)


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwnerOrIsStaff]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
