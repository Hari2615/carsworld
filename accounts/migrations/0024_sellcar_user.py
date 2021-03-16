# Generated by Django 3.1.7 on 2021-03-11 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_remove_sellcar_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellcar',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]