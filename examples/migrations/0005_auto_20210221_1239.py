# Generated by Django 2.2.10 on 2021-02-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0004_auto_20210220_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystocks',
            name='kforeverholdyn',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
