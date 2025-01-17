from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'total_expenses', 'total_saving')
    search_fields = ('username', 'email')

admin.site.site_title = "Expense Tracker Admin"
admin.site.site_header = "Expense Tracker Admin"
admin.site.index_title = "Welcome to Expense Tracker"

admin.site.register(UserProfile, UserProfileAdmin)
