# Generated by Django 2.2 on 2019-04-23 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20190423_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='employee_birth_date',
            new_name='birthdate',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_branch',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_designation',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_joining_date',
            new_name='joiningdate',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_lastname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_leaves',
            new_name='leaves',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_photo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_salary',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='employee_username',
            new_name='username',
        ),
    ]