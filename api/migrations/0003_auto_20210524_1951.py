# Generated by Django 3.2.3 on 2021-05-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210524_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='subject',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
