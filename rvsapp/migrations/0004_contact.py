# Generated by Django 3.2.4 on 2021-07-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rvsapp', '0003_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('query', models.TextField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]