# fitness/admin.py

from django.contrib import admin
from .models import UserProfile, Goal, FoodRecommendation, Exercise, CalculationResult, FavoriteFood


class FavoriteFoodInline(admin.TabularInline):
    model = FavoriteFood
    extra = 1
    readonly_fields = ('added_at',)
    can_delete = True


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
    verbose_name = "Цель"
    verbose_name_plural = "Цели"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'age', 'gender', 'activity_level')
    list_filter = ('gender',)
    raw_id_fields = ('user',)
    readonly_fields = ('user',)
    inlines = [FavoriteFoodInline]
    search_fields = ('user__username',)
    date_hierarchy = 'user__date_joined'
    list_display_links = ('user',)
    verbose_name = "Профиль пользователя"
    verbose_name_plural = "Профили пользователей"


@admin.register(FoodRecommendation)
class FoodRecommendationAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'has_image')
    list_filter = ('goal',)
    search_fields = ('name',)
    list_display_links = ('name',)
    fieldsets = (
        ("Основная информация", {
            'fields': ('name', 'description', 'goal')
        }),
        ("Медиа", {
            'fields': ('image',)
        }),
    )
    verbose_name = "Рекомендация по питанию"
    verbose_name_plural = "Рекомендации по питанию"

    @admin.display(description='Есть ли изображение')
    def has_image(self, obj):
        return bool(obj.image)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'intensity', 'goal', 'has_image')
    list_filter = ('goal',)
    search_fields = ('name',)
    list_display_links = ('name',)
    verbose_name = "Упражнение"
    verbose_name_plural = "Упражнения"

    @admin.display(description='Есть ли изображение')
    def has_image(self, obj):
        return bool(obj.image)


@admin.register(CalculationResult)
class CalculationResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'bmr', 'tdee', 'protein', 'fat', 'carbs', 'created_at')
    list_filter = ('user',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    search_fields = ('user__username',)
    list_display_links = ('user',)
    ordering = ['-created_at']
    verbose_name = "Результат расчёта"
    verbose_name_plural = "Результаты расчётов"


@admin.register(FavoriteFood)
class FavoriteFoodAdmin(admin.ModelAdmin):
    list_display = ('profile', 'food', 'added_at')
    list_filter = ('profile',)
    date_hierarchy = 'added_at'
    raw_id_fields = ('profile', 'food')
    search_fields = ('profile__user__username', 'food__name')
    readonly_fields = ('added_at',)
    verbose_name = "Избранное блюдо"
    verbose_name_plural = "Избранные блюда"