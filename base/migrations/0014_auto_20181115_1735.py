# Generated by Django 2.1.2 on 2018-11-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20181115_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
        migrations.AlterField(
            model_name='area',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]