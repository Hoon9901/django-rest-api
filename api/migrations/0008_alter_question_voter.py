# Generated by Django 3.2.3 on 2021-05-24 11:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_alter_question_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='voter',
            field=models.ManyToManyField(blank=True, null=True, related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
