# Generated by Django 3.2 on 2022-06-29 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['updated', 'created']},
        ),
    ]
