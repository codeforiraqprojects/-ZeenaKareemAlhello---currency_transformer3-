# Generated by Django 2.0 on 2020-01-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_dec_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.TextField()),
            ],
        ),
    ]