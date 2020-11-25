from django.db import models
from django.urls import reverse


class Check(models.Model):
    time = models.CharField(max_length=50, verbose_name="날짜")
    cafeteria = models.CharField(max_length=50, verbose_name="식당")
    menu = models.TextField(verbose_name="메뉴")

    def __str__(self):
        return self.cafeteria

    def get_absolute_url(self):
        return reverse('check_detail', args=[str(self.id)])

    class Meta:
        db_table = 'check'
        verbose_name = '식단등록'
        verbose_name_plural = '식단등록'
