from rest_framework import permissions


class IsOwnerOrIsStaff(permissions.BasePermission):
    """
    Данное разрешение необходимо для корзины.
    Класс-разрешение, дает доступ к запрошенному объекту:
    1. Создателю объекта
    2. Персоналу магазина(менеджерам, админам)
    """

    def has_object_permission(self, request, view, obj):
        # Данный if должен быть первым.
        if request.user.is_staff:
            return True
        # Когда приходит запрос по пользователю проверка происходит тут
        if hasattr(obj, 'email'):
            return obj.email == request.user.email
        # Когда приходит запрос по корзине запрос происходит тут
        if hasattr(obj, 'user'):
            return obj.user == request.user
