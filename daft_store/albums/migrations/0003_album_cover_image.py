# Generated by Django 5.1.4 on 2025-01-09 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_album_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_image',
            field=models.ImageField(default='default.jpg', upload_to='album_covers/'),
            preserve_default=False,
        ),
    ]
