# Generated by Django 4.2.6 on 2023-10-08 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-id']},
        ),
    ]
