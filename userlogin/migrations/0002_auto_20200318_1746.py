# Generated by Django 2.2 on 2020-03-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='gender',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userdata',
            name='openID',
            field=models.CharField(default='000', max_length=100),
        ),
    ]
