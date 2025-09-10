from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Member, Author

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=Member
    list_display=('email','first_name', 'last_name', 'is_active')
    list_filter=('is_staff', 'is_active')

    fieldsets=(
        (None,{'fields':('email', 'password')}),
        ('Personal Info',{'fields':('first_name','last_name', 'address', 'phone_number')}),
        ('Permissions',{'fields':('is_staff', 'is_active','is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates',{'fields':('last_login', 'date_joined')})

    )

    search_fields=('email',)
    ordering=('email',)

admin.site.register(Member,CustomUserAdmin)
admin.site.register(Author)
