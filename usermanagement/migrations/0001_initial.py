# Generated by Django 5.1.3 on 2024-12-02 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_first_name', models.CharField(max_length=255)),
                ('customer_middle_initial', models.CharField(max_length=255)),
                ('customer_last_name', models.CharField(max_length=255)),
                ('customer_birth_date', models.DateField()),
                ('customer_location', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
