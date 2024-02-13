from django.contrib import admin
from authentication.models import User, Role


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'deposit']
    readonly_fields = ('id',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list