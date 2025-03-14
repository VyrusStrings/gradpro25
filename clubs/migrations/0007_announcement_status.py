# Generated by Django 5.1.1 on 2025-03-10 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_remove_clubactivity_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
