# Generated by Django 3.2 on 2021-04-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_alter_characters_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='description',
            field=models.CharField(max_length=3000),
        ),
    ]
