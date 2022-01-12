# Generated by Django 2.2.11 on 2021-04-22 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=200, verbose_name='نام استان ')),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'استان',
            },
        ),
    ]
