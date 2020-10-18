# Generated by Django 3.1.1 on 2020-09-03 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('usn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phoneno', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('age', models.CharField(default='', max_length=50)),
            ],
        ),
    ]