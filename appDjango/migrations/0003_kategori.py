# Generated by Django 4.2.5 on 2023-09-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0002_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_name', models.CharField(blank=True, max_length=60, null=True)),
                ('kategori_image', models.ImageField(blank=True, null=True, upload_to='kategori/')),
            ],
        ),
    ]
