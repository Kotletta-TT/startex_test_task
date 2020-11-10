from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Cart, CustomUser, Product


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'patronic_name', 'is_staff',)
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronic_name', 'address_shipment')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    ordering = ('email',)
    search_fields = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.unregister(Group)