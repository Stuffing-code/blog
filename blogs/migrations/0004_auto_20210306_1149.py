# Generated by Django 3.1.7 on 2021-03-06 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogpost_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitlePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.titlepost'),
        ),
    ]
