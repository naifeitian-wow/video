# Generated by Django 2.1.2 on 2018-12-01 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20181130_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartoonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('pic', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=30, null=True)),
                ('director', models.CharField(max_length=30)),
                ('zhuyan', models.CharField(max_length=50)),
                ('story', models.TextField()),
                ('url', models.CharField(max_length=300)),
                ('url_lists', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cartoons', to='video.Category')),
            ],
            options={
                'verbose_name_plural': '动漫',
                'db_table': 'cartoon',
                'ordering': ('time',),
            },
        ),
    ]
