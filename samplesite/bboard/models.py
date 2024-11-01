from django.db import models
from django.db.models import PROTECT


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата публикации")
    rubric = models.ForeignKey("Rubric", null=True, on_delete=PROTECT, verbose_name="Рубрика")

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявление"
        ordering = ["-published"]


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]
