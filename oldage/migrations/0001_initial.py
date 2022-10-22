# Generated by Django 4.0.1 on 2022-02-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oldage_donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('disctrict', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('amount', models.CharField(max_length=50)),
                ('receive', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oldage_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('account', models.IntegerField()),
                ('bank', models.IntegerField()),
                ('image', models.FileField(upload_to='files')),
            ],
        ),
    ]