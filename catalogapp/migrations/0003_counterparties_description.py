# Generated by Django 3.2.9 on 2021-11-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0002_counterparties'),
    ]

    operations = [
        migrations.AddField(
            model_name='counterparties',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='Краткое описание'),
        ),
    ]
