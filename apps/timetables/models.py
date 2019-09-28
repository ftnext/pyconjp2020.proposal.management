import uuid

from django.db import models
from django.utils import timezone


class TimeTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("タイトル", max_length=100)
    description = models.TextField("詳細情報", blank=True, null=True)
    is_published = models.BooleanField("タイムテーブルの公開", default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class TimeTableColumn(models.Model):
    table_id = models.ForeignKey(
        TimeTable,
        on_delete=models.CASCADE,
        related_name="columns",
        verbose_name="タイムテーブルID",
    )
    name = models.CharField("列名", max_length=20)

    def __str__(self):
        return f"{self.table_id} {self.name}"
