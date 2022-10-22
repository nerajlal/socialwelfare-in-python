# Generated by Django 4.0.1 on 2022-02-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orphanage_adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('marital', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='orphanage_donation',
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
            name='orphanage_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('talent', models.CharField(max_length=100)),
                ('disability', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
                ('bank', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='orphanage_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField()),
                ('pname', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('image', models.FileField(max_length=50, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='orphanage_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('disctrict', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='orphanage_sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('marital', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
