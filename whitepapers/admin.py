from django.contrib import admin
from whitepapers.models import Topic, WhitePapers, DownloadLog

admin.site.register(Topic)
@admin.register(WhitePapers)
class WhitePapersAdminView(admin.ModelAdmin):
    list_display = ('id','title', 'topic','status' ,'created_at', 'published_at', 'count_of_downloads')
    list_filter = ('status', 'created_at', 'topic')
    sortable_by = ('status', 'published_at')
    search_fields = ('title', 'topic__name')
    list_per_page = 10
@admin.register(DownloadLog)
class DownloadLog(admin.ModelAdmin):
    list_display = ('id','user', 'whitepaper','download_date')
    list_filter = ('download_date', 'whitepaper')
    sortable_by = ('download_date', 'whitepaper')
    search_fields = ('user__name', 'whitepaper__title')
    list_per_page = 10