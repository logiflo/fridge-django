# Generated by Django 3.1 on 2020-08-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
