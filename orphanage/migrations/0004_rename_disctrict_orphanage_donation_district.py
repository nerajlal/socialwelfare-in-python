# Generated by Django 4.0 on 2022-02-27 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0003_orphanage_donation_society'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orphanage_donation',
            old_name='disctrict',
            new_name='district',
        ),
    ]
