# Generated by Django 5.0.6 on 2024-06-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='costomuser',
            name='about',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='costomuser',
            name='photo',
            field=models.ImageField(default='null', upload_to='photo/profile/%Y/%m/%d/'),
        ),
    ]
