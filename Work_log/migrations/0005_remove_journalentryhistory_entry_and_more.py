# Generated by Django 5.1 on 2024-10-16 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work_log', '0004_remove_profile_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalentryhistory',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='journalentryhistory',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='journalentryhistory',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='journalentryhistory',
            name='object',
        ),
        migrations.DeleteModel(
            name='JournalEntry',
        ),
        migrations.DeleteModel(
            name='JournalEntryHistory',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
    ]
