# Generated by Django 3.0.5 on 2021-05-19 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_auto_20210518_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
