# Generated by Django 3.2.13 on 2022-08-25 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_myuser_nat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user_permissions',
        ),
    ]