# Generated by Django 5.0.1 on 2024-03-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_working',
            field=models.BooleanField(default=True),
        ),
    ]
