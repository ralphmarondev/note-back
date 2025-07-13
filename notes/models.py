from django.db import models


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    caption = models.CharField(max_length=200, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
