# Generated by Django 4.2.3 on 2023-07-18 19:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_complete_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userpayment",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user id",
            ),
        ),
    ]