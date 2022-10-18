# Generated by Django 3.2.15 on 2022-10-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_contact', models.CharField(max_length=100)),
                ('employee_address', models.CharField(max_length=500)),
            ],
        ),
    ]
