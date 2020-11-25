from django.db import models
from django.urls import reverse

from accounts.models import myuser


class Evaluate(models.Model):
    time = models.CharField(max_length=50, verbose_name="날짜")
    cafeteria = models.CharField(max_length=50, verbose_name="식당")
    menu = models.CharField(max_length=50, verbose_name="메뉴")
    contents = models.TextField(verbose_name="내용")

    def __str__(self):
        return self.cafeteria

    def get_absolute_url(self):
        return reverse('evaluate_detail', args=[str(self.id)])

    class Meta:
        db_table = 'evaluate'
        verbose_name = '의견 및 평가 제출'
        verbose_name_plural = '의견 및 평가 제출'
