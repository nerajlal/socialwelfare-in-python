# Generated by Django 4.0 on 2022-02-27 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oldage', '0003_oldage_donation_society'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oldage_donation',
            old_name='disctrict',
            new_name='district',
        ),
    ]