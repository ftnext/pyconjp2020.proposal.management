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


class TimeTableRow(models.Model):
    table = models.ForeignKey(
        TimeTable,
        on_delete=models.CASCADE,
        related_name="rows",
        verbose_name="タイムテーブル",
    )
    start_at = models.TimeField("開始時刻")
    duration = models.DurationField("持続時間")

    def __str__(self):
        return f"{self.table} {self.start_at}"


class TimeTableColumn(models.Model):
    table = models.ForeignKey(
        TimeTable,
        on_delete=models.CASCADE,
        related_name="columns",
        verbose_name="タイムテーブルID",
    )
    name = models.CharField("列名", max_length=20)

    def __str__(self):
        return f"{self.table} {self.name}"


class Talk(models.Model):
    ACCEPTED = "AC"
    WAITLIST = "WL"
    REJECTED = "RJ"
    DECLINED = "DC"
    UNKNOWN = "UK"
    STATUS_CHOICES = [
        (ACCEPTED, "Accepted"),
        (WAITLIST, "Waitlist"),
        (REJECTED, "Rejected"),
        (DECLINED, "Declined"),
        (UNKNOWN, "Unknown"),
    ]
    TALK_LANGUAGE_CHOICES = [
        ("日(JA)", "日本語(Japanese)"),
        ("英(EN)", "英語(English)"),
    ]
    SLIDE_LANGUAGE_CHOICES = TALK_LANGUAGE_CHOICES + [
        ("日英(Both)", "日英両方(JA & EN)")
    ]
    BEGINNER = "BG"
    INTERMIDIATE = "IM"
    ADVANCED = "AV"
    ALL = "AL"
    AUDIENCE_CHOICES = [
        (BEGINNER, "Beginner"),
        (INTERMIDIATE, "Intermidiate"),
        (ADVANCED, "Advanced"),
        (ALL, "All"),
    ]

    table = models.ForeignKey(
        TimeTable,
        on_delete=models.CASCADE,
        related_name="talks",
        verbose_name="所属タイムテーブル",
        blank=True,
        null=True,
    )
    speaker_name = models.CharField("発表者氏名", max_length=100)
    title = models.CharField("タイトル", max_length=200)
    status = models.CharField(
        "ステータス", max_length=2, choices=STATUS_CHOICES, default=UNKNOWN
    )
    tag = models.CharField("タグ", max_length=100)
    talk_language = models.CharField(
        "発表言語", max_length=5, choices=TALK_LANGUAGE_CHOICES
    )
    slide_language = models.CharField(
        "スライドの言語", max_length=8, choices=SLIDE_LANGUAGE_CHOICES
    )
    target_audiences = models.CharField(
        "想定する対象者層", max_length=2, choices=AUDIENCE_CHOICES
    )

    def __str__(self):
        return self.title
