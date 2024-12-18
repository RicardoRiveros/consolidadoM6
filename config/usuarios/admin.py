'''from django.contrib import admin
from .models import Usuario

# Register your models here.
admin.site.register(Usuario)'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    # Puedes personalizar los campos visibles en el admin si es necesario
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets



