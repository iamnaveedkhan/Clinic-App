# Generated by Django 4.2.2 on 2023-06-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='description',
            field=models.CharField(default='no value', max_length=100),
        ),
        migrations.AddField(
            model_name='msg',
            name='symptoms',
            field=models.CharField(default='no', max_length=100),
        ),
        migrations.AddField(
            model_name='msg',
            name='weight',
            field=models.FloatField(default='no'),
        ),
    ]