# Generated by Django 4.2.4 on 2023-08-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20230817_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('words', models.CharField(max_length=100)),
                ('weights', models.DecimalField(decimal_places=10, max_digits=15, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'keyword',
                'managed': False,
            },
        ),
    ]