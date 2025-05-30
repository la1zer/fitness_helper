# fitness/admin.py

from django.contrib import admin
from .models import UserProfile, Goal, FoodRecommendation, Exercise, CalculationResult, FavoriteFood


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'age', 'gender')
    raw_id_fields = ('user',)
    readonly_fields = ('user',)
    list_filter = ('gender',)
    search_fields = ('user__username',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(FoodRecommendation)
class FoodRecommendationAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'has_image')
    list_filter = ('goal',)
    search_fields = ('name',)
    list_display_links = ('name',)

    @admin.display(description='Есть ли изображение')
    def has_image(self, obj):
        return bool(obj.image)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'intensity', 'goal')
    list_filter = ('goal',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(CalculationResult)
class CalculationResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'bmr', 'tdee', 'protein', 'created_at')
    list_filter = ('user',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    search_fields = ('user__username',)



@admin.register(FavoriteFood)
class FavoriteFoodAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'added_at')
    list_filter = ('user',)
    date_hierarchy = 'added_at'
    raw_id_fields = ('user', 'food')
    search_fields = ('user__username', 'food__name')
    readonly_fields = ('added_at',)
    verbose_name = "Избранное блюдо"
    verbose_name_plural = "Избранные блюда"