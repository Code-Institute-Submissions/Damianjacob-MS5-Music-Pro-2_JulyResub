from django.contrib import admin
from .models import UserQuestion, OwnerReply

@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    ordering = ('date', )
    list_display = (
        'date',
        'user',
        'product',
        'has_answer',
    )


@admin.register(OwnerReply)
class OwnerReplyAdmin(admin.ModelAdmin):
    pass

