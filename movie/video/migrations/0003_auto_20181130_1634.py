# Generated by Django 2.1.2 on 2018-11-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_tvmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvmodel',
            name='url_list',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]