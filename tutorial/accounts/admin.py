from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'city',
        'phone',
        'user_info',
    ]

    def user_info(self, obj):
        return obj.desc

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-city', 'user')
        return queryset




admin.site.register(UserProfile, UserProfileAdmin)

# # Changing the django admin page - changed it in the template 
# admin.site.site_header = 'Administration'


