# Generated by Django 3.0.2 on 2020-02-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitenode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitenode',
            name='attribute',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='sitenode',
            name='siteName',
            field=models.CharField(max_length=30),
        ),
    ]