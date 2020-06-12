# Generated by Django 3.0.6 on 2020-06-11 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]