# Generated by Django 4.2 on 2023-04-30 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_register_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
