# Generated by Django 2.2.10 on 2021-02-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0005_auto_20210221_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystocks',
            name='kforeverholdyn',
            field=models.BooleanField(default=False),
        ),
    ]
