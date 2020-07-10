# Generated by Django 3.0.7 on 2020-07-10 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='debeter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='p_library.Friend'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='full_name',
            field=models.CharField(default=0, max_length=25, null=True),
        ),
    ]
