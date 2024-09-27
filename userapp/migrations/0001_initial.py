# Generated by Django 5.1.1 on 2024-09-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('name', models.CharField(max_length=5)),
                ('profile', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
