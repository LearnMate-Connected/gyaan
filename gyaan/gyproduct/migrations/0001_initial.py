# Generated by Django 5.0.1 on 2024-03-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(choices=[('DS', 'Digital Product'), ('RS', 'Retail Product'), ('FS', 'Financial Service')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.URLField(blank=True, null=True)),
                ('custom_parameters', models.JSONField(blank=True, default=dict, null=True)),
                ('created_by_id', models.CharField(max_length=10)),
                ('updated_by_id', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
