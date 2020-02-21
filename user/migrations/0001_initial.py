# Generated by Django 3.0.2 on 2020-01-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logup_time', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('email', models.CharField(max_length=30, verbose_name='邮箱')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('login_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '用户',
                'db_table': 'user',
            },
        ),
    ]
