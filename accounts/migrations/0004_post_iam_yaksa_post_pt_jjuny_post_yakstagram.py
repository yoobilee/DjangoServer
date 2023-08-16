# Generated by Django 3.2.20 on 2023-08-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230809_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_iam_yaksa',
            fields=[
                ('post_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('caption', models.TextField(max_length=10000)),
                ('comments_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('media_type', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('owner_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'post_iam_yaksa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post_pt_jjuny',
            fields=[
                ('post_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('caption', models.TextField(max_length=10000)),
                ('comments_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('media_type', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('owner_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'post_pt__jjuny',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post_yakstagram',
            fields=[
                ('post_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('caption', models.TextField(max_length=10000)),
                ('comments_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('media_type', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('owner_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'post_yakstagram',
                'managed': False,
            },
        ),
    ]