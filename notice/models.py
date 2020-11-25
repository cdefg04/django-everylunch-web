from django.db import models
from django.urls import reverse

from accounts.models import myuser


class Notice(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey(myuser, on_delete=models.CASCADE, verbose_name="작성자")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice_detail', args=[str(self.id)])

    class Meta:
        db_table = 'notice'
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'
