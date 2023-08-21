from django.contrib import admin
from users.models import Country , Users
# Register your models here.
@admin.register(Users)
class UserDownload(admin.ModelAdmin):
    list_display = ('name', 'company', 'position', 'phone', 'country')
    search_fields = ('name', 'company', 'position', 'phone', 'country')

admin.site.register(Country)