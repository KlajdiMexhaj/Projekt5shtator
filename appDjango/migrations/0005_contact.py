# Generated by Django 4.2.5 on 2023-09-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0004_item_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=60, null=True)),
                ('contact_mbiemri', models.CharField(blank=True, max_length=60, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_mesazh', models.TextField(blank=True, max_length=9000, null=True)),
            ],
        ),
    ]