from django.db import models


class ReminderModel(models.Model):
    name = models.CharField(verbose_name='Заголовок', max_length=256, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True, blank=True)
    reminder_time = models.DateTimeField(verbose_name='Время напоминания', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Статус напоминания', default=True, blank=True)

    def __str__(self):
        return self.name
