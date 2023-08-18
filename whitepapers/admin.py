from django.contrib import admin
from whitepapers.models import Topic, WhitePapers

admin.site.register(Topic)
@admin.register(WhitePapers)
class WhitePapersAdminView(admin.ModelAdmin):
    list_display = ('title', 'topic','status' ,'created_at', 'published_at', 'count_of_downloads')
    list_filter = ('status', 'created_at', 'topic')
    sortable_by = ('status', 'updated_at')
    search_fields = ('title', 'topic__name')
    list_per_page = 10
    


