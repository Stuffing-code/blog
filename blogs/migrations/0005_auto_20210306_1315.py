# Generated by Django 3.1.7 on 2021-03-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20210306_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='TitlePost',
        ),
    ]
