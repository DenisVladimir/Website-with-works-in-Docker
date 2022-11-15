# Generated by Django 2.2.16 on 2021-08-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210817_1441'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='username_is_not_me',
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, username__iexact='me'), name='username_is_not_me'),
        ),
    ]
