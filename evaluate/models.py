from django.db import models

from accounts.models import myuser


class Evaluate(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey(myuser, on_delete=models.CASCADE, verbose_name="작성자")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'evaluate'
        verbose_name = '의견 및 평가 제출'
        verbose_name_plural = '의견 및 평가 제출'
