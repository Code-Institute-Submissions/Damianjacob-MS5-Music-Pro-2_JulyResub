from django.contrib import admin
from .models import UserQuestion, OwnerAnswer

@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    ordering = ('date', )
    list_display = (
        'date',
        'user',
        'product',
        'has_answer',
    )


@admin.register(OwnerAnswer)
class OwnerAnswerAdmin(admin.ModelAdmin):
    pass

