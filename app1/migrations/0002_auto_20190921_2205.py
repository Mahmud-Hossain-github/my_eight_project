# Generated by Django 2.2.5 on 2019-09-21 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact_group',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_name',
            new_name='name',
        ),
    ]
