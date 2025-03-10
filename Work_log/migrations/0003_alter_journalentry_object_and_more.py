# Generated by Django 5.0.7 on 2024-07-23 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_log', '0002_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Work_log.object'),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='structure',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journalentryhistory',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Work_log.object'),
        ),
        migrations.AlterField(
            model_name='journalentryhistory',
            name='structure',
            field=models.TextField(blank=True, null=True),
        ),
    ]
