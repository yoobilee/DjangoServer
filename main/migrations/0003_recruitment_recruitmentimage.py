# Generated by Django 3.2.20 on 2023-08-19 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20230817_2326'),
        ('main', '0002_rename_content_yourmodel_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('period', models.CharField(max_length=100)),
                ('marketing_content', models.TextField()),
                ('media_channels', models.TextField()),
                ('subtitle', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('content_1', models.TextField()),
                ('sub_content_1', models.TextField()),
                ('content_2', models.TextField()),
                ('sub_content_2', models.TextField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user_adv')),
            ],
            options={
                'db_table': 'Recruitment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RecruitmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recruitment_images/')),
                ('is_profile', models.BooleanField(default=False)),
                ('recruitment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.recruitment')),
            ],
            options={
                'db_table': 'RecruitmentImage',
                'managed': True,
            },
        ),
    ]
