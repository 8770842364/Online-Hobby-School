# Generated by Django 3.1.6 on 2023-11-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admission',
            fields=[
                ('admission', models.AutoField(primary_key=True, serialize=False)),
                ('batchid', models.IntegerField()),
                ('emailid', models.CharField(max_length=40)),
                ('admissiondate', models.DateField()),
            ],
        ),
    ]