from django.contrib import admin
from apps.models import ChatGroup,Chat
# Register your models here.
@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','content','group','user')
