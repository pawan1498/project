# Generated by Django 3.0.3 on 2020-02-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_id', models.CharField(max_length=45, unique=True)),
                ('name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('permission_id', models.PositiveIntegerField(max_length=5)),
            ],
        ),
    ]
