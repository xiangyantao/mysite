# Generated by Django 2.2.1 on 2019-05-24 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='chioce_text',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='qustion_text',
            new_name='question_text',
        ),
    ]
