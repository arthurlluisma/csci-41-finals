# Generated by Django 5.1.3 on 2024-12-02 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='manager_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='website.agent'),
        ),
    ]
