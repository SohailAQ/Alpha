# Generated by Django 3.2.7 on 2021-09-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
