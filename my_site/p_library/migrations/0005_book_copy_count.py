# Generated by Django 3.0.7 on 2020-06-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200613_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(default=None, null=True),
        ),
    ]