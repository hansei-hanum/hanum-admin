# Generated by Django 5.1.1 on 2024-09-24 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_articlecomments_articlereactions_articles_userblocks_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArticleReactions',
        ),
    ]
