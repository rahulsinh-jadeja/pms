# Generated by Django 2.2 on 2019-04-23 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='employee_firstname',
            new_name='firstname',
        ),
    ]