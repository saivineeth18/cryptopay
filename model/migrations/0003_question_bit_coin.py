# Generated by Django 3.2.3 on 2021-05-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_auto_20210531_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='bit_coin',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
