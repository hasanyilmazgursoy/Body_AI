# Generated by Django 5.1.2 on 2024-10-24 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spor_AI', '0004_rename_boyuzunlugu_sporcu_boy_uzunlugu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sporcu',
            old_name='boy_uzunlugu',
            new_name='boyUzunlugu',
        ),
        migrations.RenameField(
            model_name='sporcu',
            old_name='kac_aylik',
            new_name='kacAylik',
        ),
    ]
