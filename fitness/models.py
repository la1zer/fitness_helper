# fitness/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField("Вес (кг)", default=70)
    height = models.IntegerField("Рост (см)", default=170)
    age = models.IntegerField("Возраст", default=25)
    GENDER_CHOICES = [("M", "Мужской"), ("F", "Женский")]
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICES, default="M")
    activity_level = models.FloatField("Уровень активности", default=1.2)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return f"{self.user.username} - {self.weight} кг"


class Goal(models.Model):
    name = models.CharField("Цель", max_length=50)

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

    def __str__(self):
        return self.name


class FoodRecommendation(models.Model):
    name = models.CharField("Название блюда", max_length=100)
    description = models.TextField("Описание")
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, verbose_name="Цель")
    image = models.ImageField("Изображение", upload_to='food_images/', null=True, blank=True)

    class Meta:
        verbose_name = "Рекомендация по питанию"
        verbose_name_plural = "Рекомендации по питанию"

    def __str__(self):
        return f"{self.name} ({self.goal})"


class Exercise(models.Model):
    name = models.CharField("Название упражнения", max_length=100)
    description = models.TextField("Описание")
    intensity = models.CharField("Интенсивность", max_length=50)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, verbose_name="Цель")
    image = models.ImageField("Изображение", upload_to='exercise_images/', null=True, blank=True)

    class Meta:
        verbose_name = "Упражнение"
        verbose_name_plural = "Упражнения"

    def __str__(self):
        return f"{self.name} ({self.intensity})"


class CalculationResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    bmr = models.FloatField("BMR")
    tdee = models.FloatField("TDEE")
    protein = models.FloatField("Белки")
    fat = models.FloatField("Жиры")
    carbs = models.FloatField("Углеводы")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Результат расчёта"
        verbose_name_plural = "Результаты расчётов"
        ordering = ['-created_at']

    def __str__(self):
        return f"Расчет для {self.user.username}"


class FavoriteFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    food = models.ForeignKey(FoodRecommendation, on_delete=models.CASCADE, verbose_name="Блюдо")
    added_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Избранное блюдо"
        verbose_name_plural = "Избранные блюда"
        unique_together = ('user', 'food')  # один пользователь не может добавить одно блюдо дважды

    def __str__(self):
        return f"{self.user.username} - {self.food.name}"