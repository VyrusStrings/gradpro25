# Generated by Django 5.1.1 on 2025-03-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0007_announcement_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='club_images/'),
        ),
    ]
