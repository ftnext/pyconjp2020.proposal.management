from django.db import models


class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    slug = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TimeTableRow(models.Model):
    id = models.AutoField(primary_key=True)
    table_id = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    start_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class TimeTableColumn(models.Model):
    id = models.AutoField(primary_key=True)
    table_id = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Talk(models.Model):
    id = models.AutoField(primary_key=True)
    speaker_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    talk_language = models.CharField(max_length=100, null=True, blank=True)
    slide_language = models.CharField(max_length=100, null=True, blank=True)
    target_audience = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TimeTableItem(models.Model):
    id = models.AutoField(primary_key=True)
    row_id = models.ForeignKey(TimeTableRow, on_delete=models.CASCADE)
    column_id = models.ForeignKey(TimeTableColumn, on_delete=models.CASCADE)
    talk_id = models.ForeignKey(Talk, on_delete=models.CASCADE)
    is_empty = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
