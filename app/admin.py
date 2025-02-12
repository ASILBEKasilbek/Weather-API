from django.contrib import admin
from .models import Subscriber
# Register your models here.
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','city','created_at','updated_at')
    search_fields = ('email','city')
    list_filter = ('city',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at','updated_at')
    fieldsets = (
        (None, {
            'fields': ('email','city')
        }),
        ('Date Information',{
            'fields': ('created_at','updated_at'),
            'classes': ('collapse',)
        })
    )
    add_fieldsets = (
        (None, {
            'fields': ('email','city')
        }),
    )
    ordering = ('-created_at',)
    actions = ['send_email']
    
    def send_email(self,request,queryset):
        for subscriber in queryset:
            SendWeatherEmailsCronJob().do()
        self.message_user(request,'Emails sent successfully')
    send_email.short_description = 'Send weather emails'
    
    def has_add_permission(self,request):
        return False