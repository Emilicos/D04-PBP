# Generated by Django 4.1.2 on 2022-12-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymous', models.BooleanField()),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
    ]
