# Generated by Django 4.0.1 on 2022-02-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
