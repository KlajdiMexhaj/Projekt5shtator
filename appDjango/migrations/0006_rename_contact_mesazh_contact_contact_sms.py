# Generated by Django 4.2.5 on 2023-09-14 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact_mesazh',
            new_name='contact_sms',
        ),
    ]