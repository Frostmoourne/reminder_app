# Generated by Django 3.1.7 on 2021-04-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('reminder_time', models.DateTimeField(verbose_name='Время напоминания')),
                ('is_active', models.BooleanField(default=False, verbose_name='Статус напоминания')),
            ],
        ),
    ]
