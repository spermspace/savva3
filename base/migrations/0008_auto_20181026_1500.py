# Generated by Django 2.1.2 on 2018-10-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20181026_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='areas',
            field=models.ManyToManyField(null=True, to='base.Area'),
        ),
        migrations.AlterField(
            model_name='url',
            name='many_tag',
            field=models.ManyToManyField(null=True, to='base.Tag'),
        ),
    ]
