# Generated by Django 4.0.5 on 2022-06-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_song_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='path',
            field=models.TextField(),
        ),
    ]