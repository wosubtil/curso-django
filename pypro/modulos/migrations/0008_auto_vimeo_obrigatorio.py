# Generated by Django 3.1.3 on 2020-11-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0007_aula_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(max_length=32),
        ),
    ]
