from django.contrib import admin
from .models import Todo


@admin.action(description="선택된 todo의 완료 상태를 변경합니다")
def change_done(model_admin, request, queryset):
    for i in queryset:
        if i.done == True:
            i.done = False
            i.save()
        else:
            i.done = True
            i.save()


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    actions = (change_done,)

    list_display = (
        "title",
        "user",
        "deadline",
        "time_left",
        "done",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "title",
        "deadline",
        "done",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "user__username",
    )
