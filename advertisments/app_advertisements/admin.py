from django.contrib import admin
from .models import Advertisements
from django.db.models.query import QuerySet
# Register your models here.

#класс для костамизации модели
class AdvertisementsAdmin (admin.ModelAdmin):
    list_display = ['id','title','description','price','auction', 'created_at'] #столбцы для отображения в таблице
    list_filter = ['auction', 'created_at', 'price'] #столбцы по которым будет фильтрация
    actions = ['make_action_as_false', ] # методы для выбранных записей
    fieldsets = (
        ('Общие', {
            'fields': (
                'title','description'
            ),
        }),
        ('Финансы', {
            'fields': (
                'price', 'auction'
            ),
            'classes': ['collapse']
        }),
    )

    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset: QuerySet):
        queryset.update (auction = False)

    @admin.action(description='Убрать возможность торга')
    def make_action_as_true(self, request, queryset: QuerySet):
        queryset.update(auction=True)

admin.site.register(Advertisements, AdvertisementsAdmin)
