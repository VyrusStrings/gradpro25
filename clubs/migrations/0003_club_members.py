# Generated by Django 5.1.3 on 2025-02-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_club_leader'),
        ('users', '0002_user_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='clubs', to='users.clubmember'),
        ),
    ]
