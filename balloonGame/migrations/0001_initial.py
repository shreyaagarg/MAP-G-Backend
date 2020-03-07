# Generated by Django 2.2 on 2020-03-07 10:51

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='balloonGameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('clicks', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('amount', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('total', models.IntegerField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlogin.UserData')),
            ],
        ),
    ]
