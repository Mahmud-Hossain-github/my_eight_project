# Generated by Django 2.2.5 on 2019-09-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0003_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('about', models.TextField()),
            ],
        ),
    ]
