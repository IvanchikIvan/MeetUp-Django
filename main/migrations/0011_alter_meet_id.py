# Generated by Django 5.0.2 on 2024-04-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_meet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='id',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]
