import uuid

from django.db import models


class TimeTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("タイトル", max_length=100)
    description = models.TextField("詳細情報", blank=True, null=True)
    is_published = models.BooleanField("タイムテーブルの公開", default=False)

    def __str__(self):
        return self.title
