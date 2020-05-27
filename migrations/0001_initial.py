# Generated by Django 3.0.3 on 2020-03-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=150)),
                ('mobile', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
