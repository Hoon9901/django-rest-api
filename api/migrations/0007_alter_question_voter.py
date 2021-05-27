# Generated by Django 3.2.3 on 2021-05-24 11:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20210524_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='voter',
            field=models.ManyToManyField(related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
